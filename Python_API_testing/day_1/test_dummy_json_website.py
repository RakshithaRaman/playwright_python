import requests
import pytest
import json

HEADERS = {
   "Content-Type": "application/json"
}

def test_get_users():
    res = requests.get("https://dummyjson.com/users",headers=HEADERS)
    print(res.json())
    assert res.status_code == 200, "Wrong status"
    assert res.headers["Content-Type"] == "application/json; charset=utf-8", "Wrong content type"
    assert res.elapsed.total_seconds() < 2, "Too slow"
    data = res.json()
    print(data)
