from pytemplates.core.module2 import wish_farewell


def test_wish_farewell():
    goodbye = wish_farewell(user="Jacob")
    assert goodbye == "Goodbye Jacob!"
