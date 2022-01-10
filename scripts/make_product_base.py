from load_save import save, load, file_path
from categories import product_category as category
from categories import WrongCategoryError, WrongSubcategoryError, WrongProductError
from categories_file import categories_dict


def add_product(code: int) -> None:
    """
    Adds product to barcode_base
    """
    print("Dodanie nowego produktu do listy kodów kreskowych")
    while 1:
        try:
            product[code] = [category(categories_dict), input("Wprowadź ilość: ")]
        except (WrongSubcategoryError, WrongCategoryError, WrongProductError):
            print("\n!!!Błąd wyboru kategori!!!\n")
            continue
        break


def add_category(code):
    selected_category = input("Wprowadź kategorię produktu: ").lower()
    if selected_category in categories:
        product[code] = [selected_category, input("Wprowadź ilość: ")]
    else:
        print("Nie ma takiej kategorii produktów")
        print(f"Czy chcesz dodać {selected_category} do listy kategorii?")
        while True:  # Y/n input loop. Loops until correct anwser is given
            temp_ans = input("T/N: ")
            temp_ans = temp_ans.upper()
            if temp_ans == "T":
                categories.append(selected_category)
                product[code] = [
                    selected_category,
                    input("Wprowadź ilość: "),
                ]  # To be changed
                return product[code]
            elif temp_ans == "N":
                break
            else:
                print(
                    "udzielono niewłaściwej odpowiedzi. Wprowadź T lub N i potwierdź, naciskając enter... \n"
                )


def scan() -> list:
    """
    returns list of [category,ammount] of scenned product and returns list of it's [category,ammount]
    """
    code = input(
        "zeskanuj lub ręcznie wpisz kod kreskowy (wpisz 'exit', aby wyjść i zapisać): "
    )
    if code.lower() == "exit":
        return "exit"
    if code.isdigit():
        if code not in product:
            print("\n!!!!Nie ma takiego kodu kreskowego w bazie danych...!!!!\n")
            add_product(code)
        update_storage(code)
        return product[code]

    else:
        return "\nCoś jest nie tak z podanym kodem kreskowym... Spróbuj ponownie\n"


def update_storage(code: str) -> None:
    category, amount = product[code]
    amount = int(amount)
    storage[category] = storage.get(category, 0) + amount


def print_dict(dict) -> str:
    dict_str = ""
    for key, value in dict.items():
        dict_str += f"{key}: {value}\n"
    return dict_str


def print_storage() -> None:
    print(f"Obecny stan spiżarni:\n\n{print_dict(storage)}")


def scan_loop():
    a = None
    while 1:
        a = scan()
        if a == "exit":
            save(product, file_path.products)
            save(storage, file_path.storage)
            save(recipes, file_path.recipes)
            save(categories, file_path.categories)
            break
        print(a)


if __name__ == "__main__":
    product = load(file_path.products)
    storage = load(file_path.storage)
    recipes = load(file_path.recipes)
    categories = load(file_path.categories)

    scan_loop()  # includes save()
