from pathlib import Path
import json


barcode_base_name = Path(__file__).parent / "../data/barcode_base.json"
categories_list_name = Path(__file__).parent / "../data/categories_list.json"
storage_dict_name = Path(__file__).parent / "../data/storage_dict.json"


def add_product(code: int) -> None:
    """
    Adds product to barcode_base
    """
    print("Adding new product to barcode list")
    product_category = input("Pls input product category: ").lower()
    if product_category in categories:
        product[code] = [product_category, input("Pls input amount: ")]
    else:
        print("There is no such product category")
        print(f"Do you want to add {product_category} to categories list?")
        while True:  # Y/n input loop. Loops until correct anwser is given
            temp_ans = input("Y/N: ")
            temp_ans = temp_ans.upper()
            if temp_ans == "Y":
                categories.append(product_category)
                product[code] = [
                    product_category,
                    input("Pls input amount: "),
                ]  # To be changed
                break
            elif temp_ans == "N":
                break
            else:
                print(
                    "inproper anwser has been given. Pls pass Y or N and confirm with enter...\n"
                )


def scan() -> list:
    """
    returns list of [category,ammount] of scenned product and returns list of it's [category,ammount]
    """
    code = input("Pls scan or manualy type barcode ('exit' to leave and save): ")
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
        return "\nThere is something wrong with given barcode... Pls try again\n"


def update_storage(code: str) -> None:
    category, amount = product[code]
    amount = int(amount)
    storage[code] = storage.get(code, 0) + amount


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


def load():
    global product
    global categories
    global storage
    try:  # tries to open files if failes saves blanc dict and list to create blank database file
        product = json.load(open(barcode_base_name))
        categories = json.load(open(categories_list_name))
        storage = json.load(open(storage_dict_name))
    except FileNotFoundError:
        print("No database was found, crating blank bases")
        product = {}
        categories = []
        storage = {}
        save()


if __name__ == "__main__":
    load()  # opens and downloads files from DB
    scan_loop()  # includes save()
