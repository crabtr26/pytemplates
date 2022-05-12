<!-- [![Build and Test](https://github.com/snowflakedb/snowflake-connector-python/actions/workflows/build_test.yml/badge.svg)](https://github.com/snowflakedb/snowflake-connector-python/actions/workflows/build_test.yml)
[![codecov](https://codecov.io/gh/snowflakedb/snowflake-connector-python/branch/main/graph/badge.svg?token=MVKSNtnLr0)](https://codecov.io/gh/snowflakedb/snowflake-connector-python)
[![PyPi](https://img.shields.io/pypi/v/snowflake-connector-python.svg)](https://pypi.python.org/pypi/snowflake-connector-python/) -->
<!-- [![License](https://img.shields.io/badge/license-MIT-green)](./LICENSE) [![Codestyle Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black) -->

<!-- ![NPM License](https://img.shields.io/npm/l/:packageName) -->
# Python Templates
<!-- Templates for developing, testing, packaging, and deploying python applications. -->

[![License](https://img.shields.io/badge/License-Creative%20Commons%20Zero%20v1.0-informational?style=flat)](./LICENSE)
[![codecov](https://codecov.io/gh/crabtr26/python_templates/branch/main/graph/badge.svg?token=RRYTJVFDG3)](https://codecov.io/gh/crabtr26/python_templates)
[![Code style: black](https://img.shields.io/badge/code%20style-black-151515?style=flat)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-EE8236?style=flat)](https://pycqa.github.io/isort/)
[![Documentation: Sphinx](https://img.shields.io/badge/Documentation-Sphinx-08476D?style=flat)](https://www.sphinx-doc.org/en/master/)


## Description
A basic template which includes proper package structure, imports, and a working setup.py.
Includes flake8, pylint, isort, and pytest settings with configurations compatible with
the black autoformatter. Pylint settings are based on the Google style standards for python.
Package metadata and dependency information is stored in pyproject.toml.

## Setup
Using `virtualenv`:
```
git clone https://github.com/crabtr26/python_templates.git
cd python_templates
virtualenv venv
source venv/bin/activate
pip install .
```

## Usage
```
greet {User}
```

## Development Setup
Using `virtualenv`:
```
git clone https://github.com/crabtr26/python_templates.git
cd python_templates
virtualenv venv
source venv/bin/activate
pip install -e .[dev]
```

## Testing
To run the tests locally using the development environment:
```
cd python_templates
pytest
```

## Documentation
To build and view the documentation locally using the development environment:
```
cd docs
make html
google-chrome build/html/index.html
```
