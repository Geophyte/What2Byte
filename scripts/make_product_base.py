import json


def add_product(code: int) -> None:
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


def scan():
    while 1:
        code = input("Pls scan or manualy type barcode ('exit' to leave and save): ")
        if code.lower() == "exit":
            save()
            break
        if code.isdigit():
            if code in product:
                print(product[code])
            else:
                print("\n!!!!There is no such barcode in data base...!!!!\n")
                add_product(code)
        else:
            print("\nThere is something wrong with given barcode... Pls try again\n")
            continue


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


if __name__ == "__main__":
    # definition of file adress
    barcode_base_name = "./data/barcode_base.json"
    categories_list_name = "./data/categories_list.json"
    try:  # tries to open files if failes saves blanc dict and list to create blank database file
        product = json.load(open(barcode_base_name))
        categories = json.load(open(categories_list_name))
    except FileNotFoundError:
        print("No database was found, crating blank bases")
        product = {}
        categories = []
        save()
    scan()
