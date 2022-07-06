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

A basic microservices template which includes three services: an API built using fastapi, a plotly dashboard, and a reverse-proxy built using traefik. The docker-compose.yml can be used to build and deploy the API and the dashboard behind the traefik reverse-proxy, exposing both services through a secure HTTPS endpoint. The services can be deployed on a single host machine or a docker swarm cluster, and the docker-compose.override.yml can be used to override the default, multi-worker, production configuration during local development.

## Services
The source code for the two services deployed in this template are located in the *fastapi* and *plotly_dash* branches respectively. Public demos are also available:

**Fastapi Demo -** https://api.pytemplates.gallery/

**Fastapi Demo Documentation -** https://api.pytemplates.gallery/docs

**Plotly Dashboard Demo -** https://pytemplates.gallery/

## Images

Public docker images are also available from the repository crabtr26/pytemplates.

Fastapi:

```bash
docker pull crabtr26/pytemplates:fastapi
```

Plotly Dashboard:

```bash
docker pull crabtr26/pytemplates:plotly_dash
```

## Development Setup

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
