from pathlib import Path
import json


barcode_base_name = Path(__file__).parent / "../data/barcode_base.json"
categories_list_name = Path(__file__).parent / "../data/categories_list.json"
storage_dict_name = Path(__file__).parent / "../data/storage_dict.json"
recipes_dict_name = Path(__file__).parent / "../data/recipes.json"


def load():
    try:  # tries to open files if failes saves blanc dict and list to create blank database file
        product = json.load(open(barcode_base_name))
        categories = json.load(open(categories_list_name))
        storage = json.load(open(storage_dict_name))
        recipes = json.load(open(recipes_dict_name))
    except FileNotFoundError:
        print("Nie znaleziono bazy danych, tworzenie pustych baz")
        product = {}
        categories = []
        storage = {}
        recipes = {}
        save(product, categories, storage, recipes)
    return product, categories, storage, recipes


def save(product, categories, storage, recipes) -> None:
    """
    This will save new list and dict to their files
    """
    dict_file = open(barcode_base_name, "w")
    json.dump(product, dict_file)  # dups product dict into file product_base.py
    dict_file.close()

    categories_file = open(categories_list_name, "w")
    json.dump(categories, categories_file)  # dups types list into file product_base.py
    categories_file.close()

    storage_file = open(storage_dict_name, "w")
    json.dump(storage, storage_file)  # dups types list into file product_base.py
    storage_file.close()

    recipes_file = open(recipes_dict_name, "w")
    json.dump(recipes, recipes_file)  # dups types list into file product_base.py
    storage_file.close()
