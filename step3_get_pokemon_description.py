from bs4 import BeautifulSoup
import requests

from utils import dumpJSONToFile, readJSONDataFromFile

INPUT_FILE = "all_pokemon_stage_2.json"
OUTPUT_FILE = "all_pokemon_stage_3.json"

def extractDescriptionForPokemon(pokemonId, pokemonObj):
    url = "https://www.pokemon.com/us/pokedex/" + pokemonId
    response = requests.get(url, timeout = 5)
    content = BeautifulSoup(response.content, "html.parser")
    descriptionDoms = content.find('div', attrs={"class": "version-descriptions"}).find_all('p')
    descriptionArray = []

    for descriptionDom in descriptionDoms:
        descriptionArray.append(descriptionDom.getText())

    pokemonObj['descriptions'] = descriptionArray


def getDescriptionForAllPokemon():
    indexed_pokemon_dictionary = readJSONDataFromFile(INPUT_FILE)
    listOfAllPokemonIds = list(indexed_pokemon_dictionary.keys())

    countDescriptionAdded = 0
    for pokemonId in listOfAllPokemonIds:
        pokemonObj = indexed_pokemon_dictionary[pokemonId]
        if 'descriptions' not in pokemonObj:
            print(pokemonId, pokemonObj['name'])
            extractDescriptionForPokemon(pokemonId, pokemonObj)
            countDescriptionAdded += 1
            if countDescriptionAdded % 10 == 0:
                print('dumpJSON!!!')
                dumpJSONToFile("all_pokemon_stage_3.json", indexed_pokemon_dictionary)

    
    print('\ndone!')
    return indexed_pokemon_dictionary

# get extract pokemon from https://pokemondb.net/pokedex/all and put in dictionary
pokemonDictionary = getDescriptionForAllPokemon()
# convert dictionary of pokemon to all_pokemon.json
dumpJSONToFile(OUTPUT_FILE, pokemonDictionary)