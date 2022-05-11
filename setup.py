from setuptools import setup

with open("src/mypackage/__version__.py", "r", encoding="UTF-8") as f:
    text = f.read()
    __version__ = text.split('"')[1]
    print("VERSION")
    print(text)

setup(version=__version__)
