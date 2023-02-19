from bs4 import BeautifulSoup

from utils import dumpJSONToFile, readJSONDataFromFile

INPUT_FILE = "all_pokemon_stage_3.json"
OUTPUT_FILE = "all_pokemon_stage_4.json"

def convertWeightToKilograms(pokemon):
    weight = pokemon['weight'].replace("\u00A0","")
    pokemon['weightKg'] = weight.split('kg')[0]
    del pokemon['weight']

def convertHeightToMeters(pokemon):
    height = pokemon['height'].replace("\u00A0","")
    pokemon['heightM'] = height.split('m')[0]
    del pokemon['height']

def removeExtraDataForCatchRate(pokemon):
    catchRate = pokemon['catchRate'].replace("\n","")
    pokemon['catchRate'] = catchRate.split(' (')[0]
    
def removeExtraCharactersFromSpeciesField(pokemon):
    species = pokemon['species'].replace("\u00e9","")
    pokemon['species'] = species

def convertEvolutionArrayToArrayOfIds(pokemon):
    evolutions = pokemon['evolutions']
    cleanedEvolutions = []
    for evolution in evolutions:
        cleanedEvolutions.append(int(evolution.split('#')[1]))

    pokemon['evolutions'] = cleanedEvolutions

def cleanDescriptionsText(pokemon):
    del pokemon['description']
    cleanedDescriptions = []
    descriptions = pokemon['descriptions']
    for description in descriptions:
        description = description.replace("\n","").strip()
        cleanedDescriptions.append(description)

    pokemon['descriptions'] = cleanedDescriptions

def renameTotalToBaseStatTotal(pokemon):
    total = pokemon['total']
    del pokemon['total']
    pokemon['baseStatTotal'] = total

def convertAllApplicableFieldsToNumbers(pokemon):
    keyValuesToConvertToInt = [
        'catchRate',
        'baseExperience',
        'hp',
        'attack',
        'defense',
        'specialAttack',
        'specialDefense',
        'speed',
    ]

    keyValuesToConvertToFloat = [
        'weightKg',
        'heightM'
    ]

    for key in keyValuesToConvertToInt:
        convertedInt = int(pokemon[key])
        pokemon[key] = convertedInt

    for key in keyValuesToConvertToFloat:
        convertedFloat = float(pokemon[key])
        pokemon[key] = convertedFloat
    


def cleanPokemonData(pokemon):
    convertWeightToKilograms(pokemon)
    convertHeightToMeters(pokemon)
    removeExtraDataForCatchRate(pokemon)
    removeExtraCharactersFromSpeciesField(pokemon)
    convertEvolutionArrayToArrayOfIds(pokemon)
    cleanDescriptionsText(pokemon)
    renameTotalToBaseStatTotal(pokemon)
    convertAllApplicableFieldsToNumbers(pokemon)

def cleanAllPokemonData():
    indexed_pokemon_dictionary = readJSONDataFromFile(INPUT_FILE)
    listOfAllPokemonIds = list(indexed_pokemon_dictionary.keys())
    
    for pokemonId in listOfAllPokemonIds:
        cleanPokemonData(indexed_pokemon_dictionary[pokemonId])
        print(f'{pokemonId} {indexed_pokemon_dictionary[pokemonId]["name"]} cleaned.')

    print('\ndone!')
    return indexed_pokemon_dictionary

# get extract pokemon from https://pokemondb.net/pokedex/all and put in dictionary
pokemonDictionary = cleanAllPokemonData()
# convert dictionary of pokemon to all_pokemon.json
dumpJSONToFile(OUTPUT_FILE, pokemonDictionary)