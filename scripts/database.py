from load_save import load, file_path
from recipe import Recipe
import json


def get_storage():
    with open("/home/polamarysia/What2bite/data/storage_dict.json", "r") as file_handle:
        return json.load(file_handle)


# Zwraca listę przepisów wczytaną z recipes_path
def get_recipes() -> list:
    recipes_list = load(file_path.recipes)

    # Zamień dane wczystane z recipes.json na
    # liste klasy Recipe
    for i, rec in enumerate(recipes_list):
        ingredients = zip(rec["ingredients"], rec["ingredients_amount"])
        text = "\n".join(rec["steps"])
        recipes_list[i] = Recipe(rec["id"], rec["name"], dict(ingredients), text)

    return recipes_list


# Zwraca listę przepisów które można wykonać ze składników w magazynie
def get_doable_recipes(storage):
    result = list()
    for recipe in get_recipes():
        if recipe.is_doable(storage):
            result.append(recipe)
    return result


if __name__ == "__main__":
    storage = load(file_path.storage)

    for recipe in get_recipes():
        print(recipe)
    print("=" * 20)
    print("Możliwe do zrobienia:")

    for recipe in get_doable_recipes(storage):
        print(recipe)
