import pytest, requests
import yaml


with open("config.yaml") as f:
    data = yaml.safe_load(f)


@pytest.fixture()
def good_word():
    return "Привет"


@pytest.fixture()
def bad_word():
    return "Првет"


@pytest.fixture()
def login():
    res1 = requests.post(data["address"] + "gateway/login",
                         data={"username": data["username"], "password": data["password"]})
    return res1.json()["token"]


@pytest.fixture()
def test_text1():
    return "test"


@pytest.fixture()
def test_text2():
    return "some test data"
