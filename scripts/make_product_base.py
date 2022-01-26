from load_save import save, load, file_path
from recipe import Recipe


def bool_scan(code) -> bool:
    """
    returns bool if something is in code base
    """
    if code not in product:
        return False
    else:
        return True


def get_product(code):
    """
    returns product from its code
    """
    try:
        return product[code]
    except KeyError:
        return None


def add_to_storage(category, amount):
    """
    przyjmuje kategorie i ilosc
    pobiera, updatuje i zapisuje storage
    """
    storage = load(file_path.storage) # loaduje storage
    storage[category] = storage.get(category, 0) + amount # updatuje storage
    save(storage, file_path.storage) # savuje storage


def subtract_from_storage(category, amount):
    add_to_storage(category, -amount)


def sub_storage(recipe):
    storage = recipe.subtract_ingredients(get_storage())
    save(storage, file_path.storage)


def get_storage():
    return load(file_path.storage)


# Zwraca listę przepisów które można wykonać ze składników w magazynie
def get_doable_recipes():
    storage = load(file_path.storage)
    result = list()
    for recipe in get_recipes():
        if recipe.is_doable(storage):
            result.append(recipe)
    return result


product = load(file_path.products)
# storage = load(file_path.storage)
# recipes = load(file_path.recipes)

# s

def get_recipes() -> list:
    recipes_list = load(file_path.recipes)

    # Zamień dane wczystane z recipes.json na
    # liste klasy Recipe
    for i, rec in enumerate(recipes_list):
        ingredients = zip(rec["ingredients"], rec["ingredients_amount"])
        text = "\n".join(rec["steps"])
        recipes_list[i] = Recipe(rec["id"], rec["name"], dict(ingredients), text)

    return recipes_list
