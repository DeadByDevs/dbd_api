from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

import fileHandler

app = FastAPI()

@app.get("/")
async def read_root():
    return {"DBD api": "OK"}

@app.get("/map")
async def read_map():
    return fileHandler.getRandomMap('./assets/maps.json')

@app.get("/perk/{characterType}/set")
# get a set of perks for a killer or a survivor
async def read_perks(characterType):
    if characterType == 'survivor':
        return fileHandler.randomMultipleElementsFile('./assets/perks.json', 4, characterType)
    elif characterType == 'killer':
        return fileHandler.randomMultipleElementsFile('./assets/perks.json', 4, characterType)
    else:
        return "Error : Invalid character type"

@app.get("/perk/{characterType}/single")
# get a single perk for a killer or a survivor
async def read_perk(characterType):
    if characterType == 'survivor':
        return fileHandler.randomElementFile('./assets/perks.json', characterType)
    elif characterType == 'killer':
        return fileHandler.randomElementFile('./assets/perks.json', characterType)
    else:
        return "Error : Invalid character type"