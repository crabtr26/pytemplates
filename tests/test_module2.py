from mypackage.subpackage.module2 import wish_farewell


def test_module2():
    goodbye = wish_farewell(user="Jacob")
    assert goodbye == "Goodbye Jacob!"
