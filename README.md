# Recurse Center: Tic-tac-toe
Welcome to the docs for my tic-tac-toe program 🤓

# Introduction
This program allows two players to play tic-tac-toe on the command line.

# To-do
* Add intro announcement explaining rules and how user input maps to cells
* Optimise checking for a win. It currently loops over every possible winning sequence, which is inefficient as many are mutually exclusive.
* Utilise [coverage.py](https://coverage.readthedocs.io/en/7.1.0/) to improve tests
* Add fixtures that return instantiated classes for class unit tests to reduce repetition 
* Consider whether `@dataclass` decorator could reduce boilerplate (particularly getters and setters) without reducing usability

# Local development
This section tells you how to...
* create and activate a virtual environment to run the code in
* install dependencies into this environment
* run the tests
* use the formatter
* play the game

The below commands make a couple of assumptions:
1. You have navigated to the root of the project in the CLI  
2. You are using a version of Python compatible with Python 3.10.8.

## Create and activate virtual environment
Create:
```console
python -m venv ./.venv
```
Activate:
```console
source .venv/bin/activate
```

## Install dependencies

```console
python -m pip install -r requirements.txt
```
## Run tests
```console
python -m pytest
```
## Format files
```console
black .
```

## Play the game
```console
python -m src.entry_point
```