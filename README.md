# deadbydayapi

## required library :

python-dotenv
fastapi
uvicorn

## how to set up the environment :

- create api-env

  - python3 -m venv api-env

- activate virtual env:

  - source api-env/bin/activate

- install in env

  - pip install "uvicorn[standard]"

- add packages to requirements.txt
  - pip freeze > requirements.txt

## how to run the app :

- activate virtual env if not already in it:
  - source api-env/bin/activate
- run app using uvicorn:
  - uvicorn main:app --reload
