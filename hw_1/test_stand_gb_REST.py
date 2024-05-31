from conftest import data
import requests


def test_step1(login, test_text1):
    headers = {"X-Auth-Token": login}
    res = requests.get(data["address"] + "api/posts", params={"owner": "notMe"}, headers=headers)
    list_res = [i["title"] for i in res.json()["data"]]
    print(list_res)
    assert test_text1 in list_res


def test_step2(login, test_text2):
    headers = {"X-Auth-Token": login}
    res = requests.post(data["address"] + "api/posts",
                        params={"title": "test3",
                                "description": "some test data",
                                "content": "some new content"},
                        headers=headers)
    assert test_text2 in res.json()["description"]
