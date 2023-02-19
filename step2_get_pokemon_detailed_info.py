from bs4 import BeautifulSoup
import requests

from utils import dumpJSONToFile, readJSONDataFromFile

INPUT_FILE = "all_pokemon_stage_1.json"
OUTPUT_FILE = "all_pokemon_stage_2.json"

def getPokemonTypes(typeRow):
    typeTags = typeRow.find_all('a')
    types = []
    for typeTag in typeTags:
        types.append(typeTag.getText())

    return types

def extractDataFromPokedexDataSection(pokedexDataSection, pokemonObject):
    vitalsRows = pokedexDataSection.find('table', attrs={"class": "vitals-table"}).find_all('td')
    pokemonObject["type"] = getPokemonTypes(vitalsRows[1])
    pokemonObject["species"] = vitalsRows[2].getText()
    pokemonObject["height"] = vitalsRows[3].getText()
    pokemonObject["weight"] = vitalsRows[4].getText()

def extractDataFromTrainingSection(trainingSection, pokemonObject):
    vitalsRows = trainingSection.find('table', attrs={"class": "vitals-table"}).find_all('td')
    pokemonObject["catchRate"] = vitalsRows[1].getText()
    pokemonObject["baseExperience"] = vitalsRows[3].getText()
    pokemonObject["growthRate"] = vitalsRows[4].getText()

def extractDataFromBaseStatsSection(baseStatsSection, pokemonObject):
    vitalsRows = baseStatsSection.find('table', attrs={"class": "vitals-table"}).find_all('tr')
    pokemonObject["hp"] = vitalsRows[0].find('td').getText()
    pokemonObject["attack"] = vitalsRows[1].find('td').getText()
    pokemonObject["defense"] = vitalsRows[2].find('td').getText()
    pokemonObject["specialAttack"] = vitalsRows[3].find('td').getText()
    pokemonObject["specialDefense"] = vitalsRows[4].find('td').getText()
    pokemonObject["speed"] = vitalsRows[5].find('td').getText()
    pokemonObject["total"] = vitalsRows[6].find('td').getText()

def extractBasicEvolutionData(page, pokemonObject):
    evolutions = []
    evolutionInfocardSections = page.find_all('div', attrs={"class": "infocard-list-evo"})
    
    for section in evolutionInfocardSections:
        evolutionInfocard = section.find_all('div', attrs={"class": "infocard"})
        
        for card in evolutionInfocard:
            evolutions.append(card.find('small').getText())
    
    pokemonObject['evolutions'] = evolutions

def extractNamesInOtherLanguages(page, pokemonObject):
    languageTranslations = []
    otherLanguagesSection = page.find(id="main").find_all('div', attrs={"class": "grid-row"})[6]
    value = otherLanguagesSection.prettify()
    vitalsRows = otherLanguagesSection.find('table', attrs={"class": "vitals-table"}).find_all('tr')

    for vital in vitalsRows:
        languageTuple = [
            vital.find('th').getText(),
            vital.find('td').getText()
        ]
        languageTranslations.append(languageTuple)
    
    pokemonObject['namesInOtherLanguages'] = languageTranslations

def scrapeForDetailedPokemonInfo(id, pokemonObject):
    print("- - - - - - - -", id, "- - -- - -- - -- - -- --  ")
    url = "https://pokemondb.net/pokedex/" + id
    response = requests.get(url, timeout = 5)
    content = BeautifulSoup(response.content, "html.parser")

    idtoSearch = f"tab-basic-{id}"

    topInfoPannels = content.find(id=idtoSearch).find_all('div', attrs={"class": "grid-row"})
    pokemonObject["imageUrl"] = content.find(id=idtoSearch).find('img')["src"]

    extractDataFromPokedexDataSection(topInfoPannels[0], pokemonObject)
    extractDataFromTrainingSection(topInfoPannels[1], pokemonObject)
    extractDataFromBaseStatsSection(topInfoPannels[2], pokemonObject)
    extractBasicEvolutionData(content, pokemonObject)
    # extractNamesInOtherLanguages(content, pokemonObject)

    pokemonObject["description"] = "" # get from other website
    return pokemonObject

def getDetailedInformationAboutAllPokemon(): 
    indexed_pokemon_dictionary = readJSONDataFromFile(INPUT_FILE)
    listOfAllPokemonIds = list(indexed_pokemon_dictionary.keys())

    for id in listOfAllPokemonIds:
        pokemon = scrapeForDetailedPokemonInfo(id, indexed_pokemon_dictionary[id])
        indexed_pokemon_dictionary[id] = pokemon
        print(id, indexed_pokemon_dictionary[id]['name'], 'extracted.')

    print('\ndone!')
    return indexed_pokemon_dictionary

# get extract pokemon from https://pokemondb.net/pokedex/all and put in dictionary
pokemonDictionary = getDetailedInformationAboutAllPokemon()
# convert dictionary of pokemon to all_pokemon.json
dumpJSONToFile(OUTPUT_FILE, pokemonDictionary)