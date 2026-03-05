import json
from calculator import add


def test_cases_from_json():

    with open("test_cases.json") as f:
        test_cases = json.load(f)

    for case in test_cases:
        a, b = case["input"]
        expected = case["expected"]

        assert add(a, b) == expected