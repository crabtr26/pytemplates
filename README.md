```

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
A basic template which includes proper package structure, imports, and a working `setup.py`.
Includes flake8, pylint, isort, and pytest settings with configurations compatible with
the black autoformatter. Pylint settings are based on the Google style standards for python
and adapted for black compatibility. Package metadata and dependency information is stored
in the pyproject.toml.

## Setup
Using `virtualenv`:
```
git clone https://github.com/crabtr26/pytemplates.git
cd pytemplates
virtualenv venv
source venv/bin/activate
pip install .
```

## Usage
From the CLI:
```
pytemplates --hello {user}
pytemplates --goodbye {user}
pytemplates --test
```

From a `.py` file:
```python
import mypackage
mypackage.greet(user="Jacob")
mypackage.wish_farewell(user="Jacob")
mypackage.__version__
```

## Development Setup
Using `virtualenv`:
```
git clone https://github.com/crabtr26/pytemplates.git
cd pytemplates
virtualenv venv
source venv/bin/activate
pip install -e .[dev]
```

## Testing
To run the tests locally using the development environment:
```
cd pytemplates
pytest
```

## Documentation
To build and view the documentation locally using the development environment:
```
cd pytemplates/docs
make html
google-chrome build/html/index.html
```
