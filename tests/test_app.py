import subprocess


def test_app():
    greeting = subprocess.run(["greet", "Jacob"], capture_output=True, text=True)
    assert "Hello Jacob!" in greeting.stdout
