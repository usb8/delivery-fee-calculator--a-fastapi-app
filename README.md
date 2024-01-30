# Delivery Fee Calculator (Python-based backend)

- FastAPI run with Swagger UI at: http://localhost:8000/docs
- All of the features in the specification have been completed.
- It should be noted that:
  - Env is skipped because it is not mentioned in the specification.
  - There is only one branch because this is a basic app.

[[_TOC_]]

# Versions

- Python: v3.8.10

# Backend development

## Install backend dependencies

```shell
$ python -m pip install virtualenv
$ python -m virtualenv .venv
$ source .venv/bin/activate
$ pip install poetry==1.3.1
$ poetry install
```

## Run backend (in venv)

```shell
$ python ./app.py
```

## Run test (in venv)

```shell
$ python -m unittest tests.<test-name> # Run one test
$ python -m unittest tests/* # Run all test
```
- Handle error quickly: "ModuleNotFoundError: No module named 'tests/__pycache__'"
  - Delete __pycache__

## Prettier / format code (in venv)

```shell
$ black .
```