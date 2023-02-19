import json

def dumpJSONToFile(filename, jsonData):
    """ write given JSON data to a file with the given file name
    filename should be appended with '.json'
    """
    with open(filename, 'w') as outfile:
        json.dump(jsonData, outfile)

def readJSONDataFromFile(filename):
    with open(filename, 'r') as json_data:
        return json.load(json_data)