# Delivery Fee Calculator (Python-based backend)

- All of the features in the specification have been completed.
- It should be noted that:
  - Env is skipped because it is not mentioned in the specification.
  - There is only one branch because this is a basic app.

[[_TOC_]]

# Versions

- Version: v3.8.10

# Backend development

## Install backend dependencies

```shell
$ source .venv/bin/activate
$ pip install poetry==1.3.1
$ poetry install
```

## Run backend

```shell
$ python ./app.py # Run app
$ black . # Prettier / format code
$ python -m unittest tests.<test-name> # Run one test
$ python -m unittest tests/* # Run all test
```
