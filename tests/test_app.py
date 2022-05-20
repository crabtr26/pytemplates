from fastapi import __version__ as fastapi_version
from fastapi.testclient import TestClient

from pytemplates import __version__ as pytemplates_version
from pytemplates.app import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == "Hello PyTemplates User!"


def test_hello():
    response = client.get("/hello?user=jacob")
    assert response.status_code == 200
    assert response.json() == "Hello jacob!"


def test_goodbye():
    response = client.get("/goodbye?user=jacob")
    assert response.status_code == 200
    assert response.json() == "Goodbye jacob!"


def test_test():
    response = client.get("/test")
    assert response.status_code == 200
    message = [
        "Hello PyTemplates User! PyTemplates has been installed successfully!",
        f"pytemplates=={pytemplates_version}",
        f"fastapi=={fastapi_version}",
        "Goodbye PyTemplates User!",
        "Thank you for using PyTemplates!",
    ]
    assert response.json() == message
