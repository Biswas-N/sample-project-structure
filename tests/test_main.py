import pytest
import json
from flask import Flask

from main import APP


@pytest.fixture(scope="module")
def client():
    return APP.test_client


def test_index_route(client):
    res = client().get("/")
    data = json.loads(res.data)

    assert res.status_code == 200
    assert data["success"] == True
    assert data["message"] == "Main index route"
