import pytest

def test_url_shorten(test_app):
    response = test_app.get("/shorten?url=https://www.formula1.com")
    assert response.json() == "http://localhost:8000/4lEkWTr"
    assert response.status_code == 200


def test_training_backslash_url(test_app):
    response = test_app.get("/shorten?url=https://www.formula1.com/")
    assert response.json() == "http://localhost:8000/4lEkWTr"
    assert response.status_code == 200


def test_invalid_shortened_url(test_app):
    response = test_app.get("/abcd")
    assert response.json() == {"detail": "Provided link does not exist."}
    assert response.status_code == 404


def test_stored_url(test_app):
    response = test_app.get("/shorten?url=https://www.formula1.com")
    with open("artifacts/urls.txt", "r") as urlfile:
        contents = urlfile.read()
    
    assert contents.rstrip("\n") == "https://www.formula1.com 4lEkWTr"