```bash

   ___        _____                         _         _
  / _ \ _   _/__   \ ___  _ __ ___   _ __  | |  __ _ | |_  ___  ___
 / /_)/| | | | / /\// _ \| '_ ` _ \ | '_ \ | | / _` || __|/ _ \/ __|
/ ___/ | |_| |/ /  |  __/| | | | | || |_) || || (_| || |_|  __/\__ \
\/      \__, |\/    \___||_| |_| |_|| .__/ |_| \__,_| \__|\___||___/
        |___/                       |_|

```
<!-- source - https://patorjk.com/software/taag/#p=display&h=1&f=Ogre&t=PyTemplates -->

[![License](https://img.shields.io/badge/License-Creative%20Commons%20Zero%20v1.0-informational?style=flat)](./LICENSE)
[![Documentation: Sphinx](https://img.shields.io/badge/Documentation-Sphinx-08476D?style=flat)](https://www.sphinx-doc.org/en/master/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-151515?style=flat)](https://github.com/psf/black)
[![codecov](https://codecov.io/gh/crabtr26/pytemplates/branch/main/graph/badge.svg?token=RRYTJVFDG3)](https://codecov.io/gh/crabtr26/pytemplates)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/crabtr26/pytemplates/main.svg)](https://results.pre-commit.ci/latest/github/crabtr26/pytemplates/main)
<!-- [![Imports: isort](https://img.shields.io/badge/%20imports-isort-EE8236?style=flat)](https://pycqa.github.io/isort/) -->

## Description

A basic template which includes proper package structure with a functioning package installation.
The package is built using poetry; metadata and dependency information is stored in the pyproject.toml.
This template includes flake8, pylint, isort, and pytest settings with configurations compatible with
the black autoformatter. Pylint settings are based on the Google style standards for python
and adapted for black compatibility.  Testing is automated using github workflows, codecov.io,
and pre-commit.ci. Application deployment is managed using multi-staged docker builds for fast develop/deploy
cycles.

This template includes two services: an API built using fastapi and a reverse-proxy built using traefik. The
docker-compose.yml can be used to build and deploy both services on a single machine or on a docker swarm cluster.
The docker-compose.override.yml is used to override the production configuration during local development.

## Basic Setup

Using `poetry`:

```bash
git clone https://github.com/crabtr26/pytemplates.git
cd pytemplates
poetry install --no-dev
poetry shell
uvicorn pytemplates.app:app
```

## Development Setup

Using `poetry`:

```bash
git clone https://github.com/crabtr26/pytemplates.git
cd pytemplates
poetry install
poetry shell
uvicorn pytemplates.app:app
```

Using `Docker`:

```bash
git clone https://github.com/crabtr26/pytemplates.git
cd pytemplates
docker build . -t api
docker run --rm -p 8000:80 api
```

Using `Docker Compose`:

```bash
git clone https://github.com/crabtr26/pytemplates.git
cd pytemplates
docker compose up
```

## Production Setup
On a single server using `Docker Compose`:

```bash
git clone https://github.com/crabtr26/pytemplates.git
cd pytemplates
docker compose -f docker-compose.yml up
```

On a single server or a cluster using `Docker Swarm`:

```bash
git clone https://github.com/crabtr26/pytemplates.git
cd pytemplates
docker stack deploy -c docker-compose.yml pytemplates
```

## Testing

To run the unit tests locally using the development environment:

```bash
cd pytemplates
poetry run pytest
```

To run performance tests locally using the development environment,
run the app from one terminal:

```bash
cd pytemplates
poetry shell
uvicorn pytemplates.app:app
```

Then run locust from another terminal:

```bash
cd pytemplates
poetry shell
locust -f tests/test_performance.py
```

## Documentation

To build and view the documentation locally using the development environment:

```bash
cd pytemplates/docs
make html
google-chrome build/html/index.html
```
