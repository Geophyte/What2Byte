from pathlib import Path
import json


barcode_base_name = Path(__file__).parent / "../data/barcode_base.json"
categories_list_name = Path(__file__).parent / "../data/categories_list.json"


def add_product(code: int) -> None:
    """
    Adds product to barcode_base
    """
    print("Dodanie nowego produktu do listy kodów kreskowych")
    product_category = input("Wprowadź kategorię produktu: ").lower()
    if product_category in categories:
        product[code] = [product_category, input("Wprowadź ilość: ")]
    else:
        print("Nie ma takiej kategorii produktów")
        print(f"Czy chcesz dodać {product_category} do listy kategorii?")
        while True:  # Y/n input loop. Loops until correct anwser is given
            temp_ans = input("T/N: ")
            temp_ans = temp_ans.upper()
            if temp_ans == "T":
                categories.append(product_category)
                product[code] = [
                    product_category,
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
        save()
        return "exit"
    if code.isdigit():
        if code in product:
            return product[code]
        else:
            print("\n!!!!Nie ma takiego kodu kreskowego w bazie danych...!!!!\n")
            return add_product(code)
    else:
        return "\nCoś jest nie tak z podanym kodem kreskowym... Spróbuj ponownie\n"


def scan_loop():
    a = None
    while 1:
        a = scan()
        if a == "exit":
            save()
            break
        print(a)


def save() -> None:
    """
    This will save new list and dict to their files
    """
    dict_file = open(barcode_base_name, "w")
    json.dump(product, dict_file)  # dups product dict into file product_base.py
    dict_file.close()
    categories_file = open(categories_list_name, "w")
    json.dump(categories, categories_file)  # dups types list into file product_base.py
    categories_file.close()


def load():
    global product
    global categories
    try:  # tries to open files if failes saves blanc dict and list to create blank database file
        product = json.load(open(barcode_base_name))
        categories = json.load(open(categories_list_name))
    except FileNotFoundError:
        print("Nie znaleziono bazy danych, tworzenie pustych baz")
        product = {}
        categories = []
        save()


if __name__ == "__main__":
    load()  # opens and downloads files from DB
    scan_loop()  # includes save()
