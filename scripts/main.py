import database


def main():
    while True:
        print("what do u want to do? ")
        print("1: scan")
        print("2: show available recipes")
        print("3: show all recipes")
        print("4: show storage")
        choice = input()
        if choice == "1":
            database.scan_code(input("scan code... : "))
        elif choice == "2":
            recipes = database.get_doable_recipes()
            if recipes:
                for rec in recipes:
                    print(rec)
                    print()
                rec_choice = input("Which recipe do you want to make? (q = none)? ")
                if rec_choice.isdigit():
                    recipe = recipes[int(rec_choice) - 1]
                    print(f"You make {recipe.name()}")
                    database.update_storage(recipe.subtract_ingredients(database.get_storage()))
            else:
                print("No recipes available")
        elif choice == "3":
            recipes = database.get_recipes()
            for rec in recipes:
                print(rec)
                print()
            rec_choice = input("Which recipe do you want to check? (q = none)? ")
            if rec_choice.isdigit():
                recipe = recipes[int(rec_choice) - 1]
                lacking = recipe.check(database.get_storage())
                if lacking:
                    print("Lacking ingredients: ")
                    print(lacking)
                else:
                    print("This recipe is available")
        elif choice == "4":
            print(database.get_storage())
        print("\n"*3)


if __name__ == "__main__":
    main()
