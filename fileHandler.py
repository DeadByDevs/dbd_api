import json
import random


def getFileData(filePath):
    with open(filePath) as dataFile:
        return json.load(dataFile)


def getRandomChapter(filePath):
    data = getFileData(filePath)
    return random.choice(data)


def getRandomMap(filePath):
    data = getFileData(filePath)
    return random.choice(data)


def getDataByRole(filePath, characterRole):
    data = getFileData(filePath)
    filteredData = [item for item in data if item["node"]["role"] == characterRole]
    return random.choice(filteredData)


# def randomElementFile(filePath, characterType="survivor"):
#     data = getDataByType(filePath, characterType)
#     return data[random.randint(0, len(data) - 1)]  # return random element


# def randomMultipleElementsFile(filePath, numberOfElements=4, characterType="survivor"):
#     data = getDataByType(filePath, characterType)
#     return random.sample(data, numberOfElements)  # return random element
