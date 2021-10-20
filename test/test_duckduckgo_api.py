import pytest
import requests

url = "https://api.duckduckgo.com/?q=presidents of the united states&format=json"
resp = requests.get(url)
rsp_data = resp.json()

# list of links related to presidents (dictionaries)
related_topics = rsp_data["RelatedTopics"]

# string containing info about the presidents
info = ""
for topic in related_topics:
    info += topic["Text"]


@pytest.mark.parametrize("president", [
    "Washington",
    "Adams",
    "Jefferson",
    "Madison",
    "Monroe",
    "Jackson",
    "Van Buren",
    "Harrison",
    "Tyler",
    "Polk",
    "Taylor",
    "Fillmore",
    "Pierce",
    "Buchanan",
    "Lincoln",
    "Johnson",
    "Garfield",
    "Arthur",
    "Cleveland",
    "Harrison",
    "McKinley",
    "Roosevelt",
    "Taft",
    "Wilson",
    "Harding",
    "Coolidge",
    "Hoover",
    "Truman",
    "Eisenhower",
    "Kennedy",
    "Nixon",
    "Ford",
    "Carter",
    "Reagan",
    "Bush",
    "Clinton",
    "Obama",
    "Trump",
    "Biden",
])
def test_duckduckgo_api_passes_with_real_presidents(president):
    assert president in info


@pytest.mark.xfail
def test_duckduckgo_api_fails_with_fake_president():
    assert "Dumpty" in info
