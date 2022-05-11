import argparse

import pandas as pd

from mypackage.my_module import greet


def main():
    parser = argparse.ArgumentParser(description="Greet the user.")
    parser.add_argument("name", type=str, help="The name of the user.")
    args = vars(parser.parse_args())
    greeting = greet(args["name"])
    message = f"{greeting} Your python package has been installed successfully!"
    info = f"Pandas version: {pd.__version__}"
    print(message, info)


if __name__ == "__main__":
    main()
