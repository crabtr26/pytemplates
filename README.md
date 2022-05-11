# python_templates
Templates for developing, testing, packaging, and deploying python applications.

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
To run the tests locally:
```
cd python_templates
pytest
```

## Documentation
To build and view the documentation locally:
```
cd docs
make html
google-chrome build/html/index.html
```
