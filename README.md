# API Tests Swagger Store

## How to start

Use python 3.11 +
Create virtual environment:
```
python -m venv venv
```
### Activate virtual environment for Windows

cmd.exe:
```
venv\Scripts\activate.bat
```
PowerShell:
```
venv\Scripts\Activate.ps1
```
## There are two ways to use:
### 1. For run tests - Install requirements with pip

```
pip install -r requirements.txt
```
### 2. For Develop tests - Install requirements with Poetry

2.1 install poetry from web: https://python-poetry.org/

2.2 then for install requirements use command:

```
poetry install
```

and add pre-commit
```
pre-commit install
pre-commit autoupdate
```

## Run all tests

```
pytest
```

## For information:
Some requests require an authorization token. Use header like
```
"Authorization": "Bearer {token}"
```
