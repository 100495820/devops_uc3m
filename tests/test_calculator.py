import json
import os
from calculator import add

def test_cases_from_json():
    # Obtener la carpeta del test
    test_dir = os.path.dirname(__file__)
    # Subir un nivel para llegar a la raíz y abrir test_cases.json
    file_path = os.path.join(test_dir, "..", "test_cases.json")

    with open(file_path) as f:
        test_cases = json.load(f)

    for case in test_cases:
        a, b = case["input"]
        expected = case["expected"]

        assert add(a, b) == expected