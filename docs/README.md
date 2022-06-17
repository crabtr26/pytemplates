# Modifying Documentation

## Build

To build and view the documentation locally using the development environment, follow the steps below:

```bash
cd pytemplates/docs
make html
google-chrome build/html/index.html
```

## Update

To generate documentation for a new project, or to update the documentation after code changes, follow the steps below:

1. `mkdir docs`
2. `cd docs`
3. `sphinx-quickstart`
   - `Separate source and build directories (y/n) [n]: y`
4. Edit `docs/source/conf.py`
   - Add: `sys.path.insert(0, os.path.abspath('../../src'))`
   - Edit: `extensions = ['sphinx.ext.napoleon', 'sphinx.ext.autodoc']`
   - Edit: `html_theme = 'sphinx_rtd_theme'`
5. Edit `docs/source/index.rst`
   - Add: `modules`
6. `sphinx-apidoc -o source/ ../src/`
7. `make html`
8. `google-chrome build/html/index.html`
