import subprocess

import pandas as pd

import mypackage


def test_app():
    hello = subprocess.run(
        ["pytemplates", "--hello", "Jacob"], capture_output=True, text=True, check=True
    )
    assert hello.stdout == "Hello Jacob!\n"
    goodbye = subprocess.run(
        ["pytemplates", "--goodbye", "Jacob"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert goodbye.stdout == "Goodbye Jacob!\n"
    test = subprocess.run(
        ["pytemplates", "--test"], capture_output=True, text=True, check=True
    )
    assert (
        "Hello PyTemplates User! PyTemplates has been installed successfully!"
        in test.stdout
    )
    assert "Goodbye PyTemplates User! Thank you for using PyTemplates!" in test.stdout
    assert f"mypackage=={mypackage.__version__}" in test.stdout
    assert f"pandas=={pd.__version__}" in test.stdout
