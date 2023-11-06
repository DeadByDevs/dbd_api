import json
import random


def getFileData(filePath):
    with open(filePath) as dataFile:
        return json.load(dataFile)


def getRandomChapter(filePath):
    data = getFileData(filePath)
    return data[random.randint(0, len(data) - 1)]  # return random element


def getRandomMap(filePath):
    data = getFileData(filePath)
    return data[random.randint(0, len(data) - 1)]  # return random element


# def getDataByType(filePath, characterType):
#     data = getFileData(filePath)
#     filteredData = []
#     for item in data:
#         if item["type"] == characterType:
#             filteredData.append(item)
#     return filteredData


# def randomElementFile(filePath, characterType="survivor"):
#     data = getDataByType(filePath, characterType)
#     return data[random.randint(0, len(data) - 1)]  # return random element


# def randomMultipleElementsFile(filePath, numberOfElements=4, characterType="survivor"):
#     data = getDataByType(filePath, characterType)
#     return random.sample(data, numberOfElements)  # return random element
