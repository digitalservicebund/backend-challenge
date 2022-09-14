## Install

- clone repository
- move to project dir: `cd ./dsb-backend-challenge/app`
- depending on OS make sure you're using the Python 3.10 (recommended to use [pyenv](https://github.com/pyenv/pyenv)) 
- install or upgrade `pip` to latest version

`python3 -m pip install --user --upgrade pip`

- install virtual environment

`python3 -m pip install --user virtualenv`

- create virtual environment for project

`python3 -m venv .env`

- activate the virtual environment

`source .env/bin/activate`

- install [Poetry packet manager](https://python-poetry.org/)

`pip install poetry` 

## Lint
Activate virtual environment `source .env/bin/activate`.

Uses `mypy` to check type hints and `flake8` to check code style and existence of docstrings. 

```commandline
make lint
```
## Test
Activate virtual environment `source .env/bin/activate`.

Run with: 

```commandline
make test
```
## Run
Activate virtual environment `source .env/bin/activate`.

Run in development mode:

```commandline
make run
```
