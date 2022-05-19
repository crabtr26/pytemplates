from mypackage.subpackage.module1 import greet


def test_module1():
    hello = greet(user="Jacob")
    assert hello == "Hello Jacob!"
