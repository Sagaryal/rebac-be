# REBAC Backend

## Getting started

The easiest way to get started to use poetry.

[Install poetry](https://python-poetry.org/docs/cli/)


### Poetry
```
poetry shell
poetry install
poetry run start
```

### PIP

If you are using pip you will need to generate dependencies and install them

```
poetry export -f requirements.txt --without-hashes > requirements.txt
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn rebac_be.main:app --reload
```

## Environment varibles

.env file contains necessary env variables. Please modify it if you want to test from your own account.

## Sample Screenshots

![alt text](image.png)
![alt text](image-1.png)