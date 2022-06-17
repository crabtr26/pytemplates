from dash.testing.application_runners import import_app


def test_hello(dash_duo):
    app = import_app(app_file="pytemplates.main")
    dash_duo.start_server(app)

    assert dash_duo.find_element("#result").text == ""
    dash_duo.multiple_click("#hello-btn", 1)
    assert dash_duo.find_element("#result").text == "Please provide a username."

    dash_duo.find_element("#hello-user").send_keys("Tester")
    dash_duo.multiple_click("#hello-btn", 1)
    assert dash_duo.find_element("#result").text == "Hello Tester!"

    assert dash_duo.get_logs() == []


def test_goodbye(dash_duo):
    app = import_app(app_file="pytemplates.main")
    dash_duo.start_server(app)

    assert dash_duo.find_element("#result").text == ""
    dash_duo.multiple_click("#goodbye-btn", 1)
    assert dash_duo.find_element("#result").text == "Please provide a username."

    dash_duo.find_element("#goodbye-user").send_keys("Tester")
    dash_duo.multiple_click("#goodbye-btn", 1)
    assert dash_duo.find_element("#result").text == "Goodbye Tester!"

    assert dash_duo.get_logs() == []


def test_whoami(dash_duo):
    app = import_app(app_file="pytemplates.main")
    dash_duo.start_server(app)

    assert dash_duo.find_element("#result").text == ""
    dash_duo.multiple_click("#whoami-btn", 1)
    assert dash_duo.find_element("#result").text != ""

    assert dash_duo.get_logs() == []
