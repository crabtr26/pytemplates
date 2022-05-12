import argparse

import pandas as pd

from mypackage import __version__
from mypackage.module1 import greet
from mypackage.module2 import wish_farewell


def main():
    """Start the PyTemplates application.

    Takes the name of a user as input and returns a greeting. The greeting
    includes a note which verifies that pandas has been imported succesfully
    based on your package dependencies.

    """
    parser = argparse.ArgumentParser(description="A python application template.")
    parser.add_argument("--hello", type=str, metavar="STRING", help="Greet the user!")
    parser.add_argument(
        "--goodbye", type=str, metavar="STRING", help="Wish the user farewell!"
    )
    parser.add_argument(
        "--test", action="store_true", help="Test the PyTemplates application."
    )
    args = vars(parser.parse_args())

    if args["hello"]:
        hello = greet(user=args["hello"])
        print(hello)

    if args["goodbye"]:
        goodbye = wish_farewell(user=args["goodbye"])
        print(goodbye)

    if args["test"]:
        hello = greet(user="PyTemplates User")
        message = f"{hello} PyTemplates has been installed successfully!"
        mypackage_info = f"mypackage=={__version__}"
        pandas_info = f"pandas=={pd.__version__}"
        print(message, mypackage_info, pandas_info)
        goodbye = wish_farewell(user="PyTemplates User")
        print(goodbye, "Thank you for using PyTemplates!")
