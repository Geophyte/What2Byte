# from pathlib import Path
# import json

# # ingredients - lista krotek (ingredients, ingredients_amount)
recipes_list = []
# recipes_dict_name = Path(file).parent / "../data/recipes_dict.json"


def add_recipe(name: str, ingredients: list, steps: list, recipes_list: list):
    id = len(recipes_list)
    dict = {}
    dict["id"] = id
    dict["name"] = name
    ingredients1 = []
    ingredients_amount = []
    ingredients_units = []
    for ingredient, amount in ingredients:
        ingredients1.append(ingredient)
        ingredients_amount.append(amount)
        ingredients_units.append("x")
    dict["ingredients"] = ingredients1
    dict["ingredients_amount"] = ingredients_amount
    dict["ingredients_units"] = ingredients_units
    dict["steps"] = steps
    return recipes_list.append(dict)


if __name__ == "__main__":
    add_recipe(
        "spagethi",
        (("masło", 50), ("makaron", 500)),
        ("Zmielić", "Zważyć", "Umyć", "Obrać"),
        recipes_list,
    )
    print(recipes_list)
