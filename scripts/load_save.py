from pathlib import Path
from enum import Enum
import json
from typing import Any


# Zwraca ścieżkę bezwzględną do pliku
def _get_abs_path(rel_path: str):
    return Path(__file__).parent / rel_path


class file_path(Enum):
    products = _get_abs_path("../data/products.json")
    categories = _get_abs_path("../data/categories_list.json")
    storage = _get_abs_path("../data/storage_dict.json")
    recipes = _get_abs_path("../data/recipes.json")


def load(f_path: file_path) -> Any:
    # Otwiera podany plik .json. Jeśli podany plik nie istnieje zwraca
    # pusty słownik i tworzy podany plik
    with open(f_path.value, encoding="utf-8", mode="r") as file:
        try:
            data = json.load(file)
        except FileNotFoundError:
            print("Nie znaleziono bazy danych, tworzenie pustych baz")
            data = dict()
            save(data)
        return data


def save(data: Any, f_path: file_path) -> None:
    # zapisuje podane dane do pliku .json
    with open(f_path.value, encoding="utf-8", mode="w") as file:
        json.dump(data, file, indent=4)


if __name__ == "__main__":
    # wczytywanie pliku:
    data = load(file_path.products)

    # zapisywanie pliku:
    save(data, file_path.products)
