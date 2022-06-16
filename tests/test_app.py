import subprocess

import typer

import pytemplates


def test_app():
    hello = subprocess.run(
        ["pytemplates", "hello", "Jacob"], capture_output=True, text=True, check=True
    )
    assert hello.stdout == "Hello Jacob!\n"
    goodbye = subprocess.run(
        ["pytemplates", "goodbye", "Jacob"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert goodbye.stdout == "Goodbye Jacob!\n"
    test = subprocess.run(
        ["pytemplates", "whoami"], capture_output=True, text=True, check=True
    )
    assert "Socket stuff" in test.stdout
