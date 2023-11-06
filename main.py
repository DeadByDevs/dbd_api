from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
import subprocess

# import fileHandler

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# cron // schedule task
download_assets = "cd dbd_assets && cargo build && cargo run"
copy_assets = "cp -r ./dbd_assets/assets/* ./assets/"


def call_dbd_assets():
    try:
        print("Downloading DBD assets...", datetime.now())
        subprocess.run(download_assets, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print("Error while downloading DBD assets", e.output)
    try:
        print("Copying DBD assets...", datetime.now())
        subprocess.run(copy_assets, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print("Error while copying DBD assets", e.output)


@app.on_event("startup")
async def startup_event():
    scheduler = BackgroundScheduler()
    scheduler.add_job(call_dbd_assets, "interval", minutes=1)
    scheduler.start()


# routes
@app.get("/")
async def read_root():
    return {"DBD api": "OK"}


@app.get("/healthcheck")
async def healthcheck():
    return {"status": "ok"}


# @app.get("/map")
# async def read_map():
#     return fileHandler.getRandomMap("./assets/maps.json")


# @app.get("/perk/{characterType}/set")
# # get a set of perks for a killer or a survivor
# async def read_perks(characterType):
#     if characterType == "survivor":
#         return fileHandler.randomMultipleElementsFile(
#             "./assets/perks.json", 4, characterType
#         )
#     elif characterType == "killer":
#         return fileHandler.randomMultipleElementsFile(
#             "./assets/perks.json", 4, characterType
#         )
#     else:
#         return "Error : Invalid character type"


# @app.get("/perk/{characterType}/single")
# # get a single perk for a killer or a survivor
# async def read_perk(characterType):
#     if characterType == "survivor":
#         return fileHandler.randomMultipleElementsFile(
#             "./assets/perks.json", 1, characterType
#         )
#     elif characterType == "killer":
#         return fileHandler.randomMultipleElementsFile(
#             "./assets/perks.json", 1, characterType
#         )
#     else:
#         return "Error : Invalid character type"
