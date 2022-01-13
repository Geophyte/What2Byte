from load_save import load, file_path
from recipe import Recipe


# def get_storage():
#     storage = open(storage_path, "r").read().split("\n")
#     storage.remove(storage[-1])
#     storage = {product.split(" ")[0]: int(product.split(" ")[1]) for product in storage}
#     return storage


# def update_storage(storage):
#     with open(storage_path, "w") as f:
#         for product, amount in storage.items():
#             f.write(f"{product} {amount}\n")
#         f.close()


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


# def get_codes():
#     codes = get_codes_text().split("\n")
#     codes.remove(codes[-1])
#     codes = {code.split(" ")[1]: (code.split(" ")[2], int(code.split(" ")[3])) for code in codes}
#     return codes


# def get_codes_text():
#     codes = open(codes_path, "r").read()
#     return codes


# def add_code(code, category, amount):
#     codes = get_codes_text()
#     id = len(codes.split("\n"))
#     new_code = f"{id} {code} {category} {amount}\n"
#     codes += new_code
#     with open(codes_path, "w") as f:
#         f.write(codes)
#         f.close()


# def get_product(code):
#     return get_codes().get(code, "code not found")


# def scan_code(code):
#     category = get_product(code)
#     if category == "code not found":
#         category = get_code_info_from_input()
#         add_code(code, category[0], category[1])
#     storage = get_storage()
#     storage[category[0]] = category[1] + storage.get(category[0], 0)
#     update_storage(storage)
#     print(f"{category[1]} of {category[0]} added to storage.")


# def get_code_info_from_input():
#     category = input("What is this product? ")
#     amount = int(input("How much of it is in this product? "))
#     return category, amount

if __name__ == "__main__":
    storage = load(file_path.storage)

    for recipe in get_recipes():
        print(recipe)
    print("=" * 20)
    print("Możliwe do zrobienia:")

    for recipe in get_doable_recipes(storage):
        print(recipe)
