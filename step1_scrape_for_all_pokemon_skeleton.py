from bs4 import BeautifulSoup
import requests

from utils import dumpJSONToFile

OUTPUT_FILE = "all_pokemon_stage_1.json"

def getDictionaryOfAllPokemonFromPokemonDB(): 
    """ get a basic dictionary of all pokemon from pokemondb/all
    dictionary will have the following structure
    {
        [id-of-pokemon-n]: {
            [id]: string,
            [tinyImageURL]: string,
            [name]: string,
        },
        ...
    }
    """
    url = "https://pokemondb.net/pokedex/all"
    response = requests.get(url, timeout = 5)
    content = BeautifulSoup(response.content, "html.parser")
    allPokemonRows = content.find(id="pokedex").find_next('tbody').find_all('tr')

    indexedPokemon = {}

    index = 0
    for pokemonRow in allPokemonRows:
        pokemon = convertPokedexRowToPokemon(allPokemonRows[index])
        indexedPokemon[pokemon['id']] = pokemon
        print(pokemon['id'], pokemon['name'], 'consumed.')
        index = index + 1

    print('\ndone!')
    return indexedPokemon

def convertPokedexRowToPokemon(row):
    """extract basic pokemon information from pokemondb/all row
    the row should be retireved from https://pokemondb.net/pokedex/all
    info retrieved from the row is tinyImageURL, id, and name
    """
    pokemonDict = {}
    columns = row.find_all('td');

    pokemonDict['tinyImageURL'] = row.find('img')['src']
    pokemonDict['id'] = int(columns[0].select(".infocard-cell-data")[0].getText())
    pokemonDict['name'] = columns[1].find('a').getText()

    return pokemonDict

# get extract pokemon from https://pokemondb.net/pokedex/all and put in dictionary
pokemonDictionary = getDictionaryOfAllPokemonFromPokemonDB()
# convert dictionary of pokemon to all_pokemon.json
dumpJSONToFile(OUTPUT_FILE, pokemonDictionary)