from mypackage.my_module import greet


def test_module():
    greeting = greet(name="Jacob")
    assert greeting == "Hello Jacob!"
