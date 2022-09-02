import pytest
import api
import app
import flask


def test_app():
    response = app.test_client().get('/')
    assert response.json.get("name") == "Алиса", "Имя получено неверно"