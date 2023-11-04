# dbd_api

## how to set up the environment:

- create env:
  python3 -m venv env

- activate virtual env:
  source env/bin/activate

- install requirements:
  pip install -r requirements.txt

- activate virtual env if not already in it:
  source env/bin/activate

## how to run the app:

- uvicorn main:app --reload

## submodules:

- git submodule update --init --recursive
  then use git submodule update instead of git pull
