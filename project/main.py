import classes


def get_storage():
    storage = open("storage.txt", "r").read().split("\n")
    storage.remove(storage[-1])
    storage = {product.split(" ")[0]: int(product.split(" ")[1]) for product in storage}
    return storage


def update_storage(storage):
    with open("storage.txt", "w") as f:
        for product, amount in storage.items():
            f.write(f"{product} {amount}\n")
        f.close()


def get_recipe(rec):
    id_name = rec[0].split(" ")
    id = int(id_name[0])
    id_name.remove(id_name[0])
    name = " ".join(id_name)

    ingredients = rec[2].split("/")
    ingredients = {product.split(" ")[0]: int(product.split(" ")[1]) for product in ingredients}

    text = rec[4]

    recipe = classes.Recipe(id, name, ingredients, text)
    return recipe


def get_recipes():
    recipes = open("recipes.txt", "r").read().split("\n")
    recipes_list = []
    rec = []
    for line in recipes:
        if len(rec) < 5:
            rec.append(line)
        else:
            recipes_list.append(get_recipe(rec))
            rec.clear()
    return recipes_list


def get_doable_recipes():
    storage = get_storage()
    return list(rec for rec in get_recipes() if rec.is_doable(storage))


def get_codes():
    codes = get_codes_text().split("\n")
    codes.remove(codes[-1])
    codes = {code.split(" ")[1]: (code.split(" ")[2], int(code.split(" ")[3])) for code in codes}
    return codes


def get_codes_text():
    codes = open("codes.txt", "r").read()
    return codes


def add_code(code, category, amount):
    codes = get_codes_text()
    id = len(codes.split("\n"))
    new_code = f"{id} {code} {category} {amount}\n"
    codes += new_code
    with open("codes.txt", "w") as f:
        f.write(codes)
        f.close()


def get_product(code):
    return get_codes().get(code, "code not found")


def scan_code(code):
    category = get_product(code)
    if category == "code not found":
        category = get_code_info_from_input()
        add_code(code, category[0], category[1])
    storage = get_storage()
    storage[category[0]] = category[1] + storage.get(category[0], 0)
    update_storage(storage)
    print(f"{category[1]} of {category[0]} added to storage.")


def get_code_info_from_input():
    category = input("What is this product? ")
    amount = int(input("How much of it is in this product? "))
    return category, amount


def main():
    while True:
        print("what do u want to do? ")
        print("1: scan")
        print("2: show available recipes")
        print("3: show all recipes")
        print("4: show storage")
        choice = input()
        if choice == "1":
            scan_code(input("scan code... : "))
        elif choice == "2":
            recipes = get_doable_recipes()
            if recipes:
                for rec in recipes:
                    print(rec)
                    print()
                rec_choice = input("Which recipe do you want to make? (q = none)? ")
                if rec_choice.isdigit():
                    recipe = recipes[int(rec_choice) - 1]
                    print(f"You make {recipe.name()}")
                    update_storage(recipe.subtract_ingredients(get_storage()))
            else:
                print("No recipes available")
        elif choice == "3":
            recipes = get_recipes()
            for rec in recipes:
                print(rec)
                print()
            rec_choice = input("Which recipe do you want to check? (q = none)? ")
            if rec_choice.isdigit():
                recipe = recipes[int(rec_choice) - 1]
                lacking = recipe.check(get_storage())
                if lacking:
                    print("Lacking ingredients: ")
                    print(lacking)
                else:
                    print("This recipe is available")
        elif choice == "4":
            print(get_storage())
        print("\n"*3)


if __name__ == "__main__":
    main()

