from load_save import save, load, file_path


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


def print_dict(dict) -> str:
    dict_str = ""
    for key, value in dict.items():
        dict_str += f"{key}: {value}\n"
    return dict_str




# def scan_loop():
#     a = None
#     while 1:
#         # a = scan()
#         if a == "exit":
#             save(product, file_path.products)
#             save(storage, file_path.storage)
#             save(recipes, file_path.recipes)
#             save(categories, file_path.categories)
#             break
#         print(a)


product = load(file_path.products)
storage = load(file_path.storage)
recipes = load(file_path.recipes)
    # scan_loop()  # includes save()
