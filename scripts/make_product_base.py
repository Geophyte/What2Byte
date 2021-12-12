from pathlib import Path
import json


barcode_base_name = Path(__file__).parent / "../data/barcode_base.json"
categories_list_name = Path(__file__).parent / "../data/categories_list.json"
storage_dict_name = Path(__file__).parent / "../data/storage_dict.json"


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
                    "udzielono niewłaściwej odpowiedzi. Wprowadź Y lub N i potwierdź, naciskając enter... \n"
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
        if code not in product:
            print("\n!!!!There is no such barcode in data base...!!!!\n")
            add_product(code)
        update_storage(code)
        save()
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
    storage_file = open(storage_dict_name, "w")
    json.dump(storage, storage_file)  # dups types list into file product_base.py
    storage_file.close()


def load():
    global product
    global categories
    global storage
    try:  # tries to open files if failes saves blanc dict and list to create blank database file
        product = json.load(open(barcode_base_name))
        categories = json.load(open(categories_list_name))
        storage = json.load(open(storage_dict_name))
    except FileNotFoundError:
        print("Nie znaleziono bazy danych, tworzenie pustych baz")
        product = {}
        categories = []
        storage = {}
        save()


if __name__ == "__main__":
    load()  # opens and downloads files from DB
    scan_loop()  # includes save()
