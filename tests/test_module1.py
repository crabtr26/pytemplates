from pytemplates.core.module1 import greet


def test_module1():
    hello = greet(user="Jacob")
    assert hello == "Hello Jacob!"
