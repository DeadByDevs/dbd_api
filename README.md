# deadbydayapi

## required library :

python-dotenv, fastapi, uvicorn

## how to set up the environment :

- create api-env

  - python3 -m venv api-env

- activate virtual env:

  - source api-env/bin/activate

- install in env
  - pip install fastapi && pip install "uvicorn[standard]"

## how to run the app :

- activate virtual env if not already in it:
  - source bot-env/bin/activate
- run app using uvicorn:
  - uvicorn main:app --reload
