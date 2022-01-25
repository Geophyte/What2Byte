from categories_file import categories_dict as categories
from load_save import _get_abs_path


# class WrongCategoryError(Exception):
#     def __init__(self):
#         super().__init__(
#             "\nBłędnie wprowadziłeś numer kategorii. Wybierz kategorię ponownie.\n")


# class WrongSubcategoryError(Exception):
#     def __init__(self):
#         super().__init__("\nBłędnie wprowadziłeś numer podkategorii. Wybierz podkategorię ponownie.\n")


# class WrongProductError(Exception):
#     def __init__(self):
#         super().__init__("\nBłędnie wprowadziłeś numer produktu. Wybierz produkt ponownie.\n")

# def check_choice(choice: str, product_list: list, error_type: str) -> int:
#     """Sprawdza poprawność wyboru użykownika i konwertuje go na odpowiedni typ"""
#     if error_type == 'category':
#         error_type = WrongCategoryError
#     elif error_type == 'subcategory':
#         error_type = WrongSubcategoryError
#     elif error_type == 'product':
#         error_type = WrongProductError
#     if not choice.isdigit():
#         raise error_type
#     elif int(choice) < 1 or int(choice) > len(product_list):
#         raise error_type
#     else:
#         return int(choice)-1

def open_own_categories_list(path: str) -> list:
    """Otwiera plik tekstowy, w którym znajdują się produkty użytkownika"""
    own_categories = []
    with open(path, 'r') as handle:
        for category in handle:
            own_categories.append(category.rstrip())
    return own_categories


def add_own_category(path: str, category: str) -> None:
    """Dodaje produkt do pliku tekstowego z kategoriami użytkownika"""
    with open(path, 'a') as handle:
        handle.write('\n'+category)


def product_categories(categories: dict) -> str:
    """Zwraca listę nazw kategorii"""
    categories_names = list(categories.keys())
    return categories_names


def product_subcategories(categories: dict, category: str):
    """Zwraca listę nazw podkategorii"""
    if category == "inne":
        path = _get_abs_path("../data/own_categories.txt")
        own_categories = open_own_categories_list(path)
        return own_categories
    else:
        subcategories = list(categories[category].keys())
        return subcategories


def product_names(categories: dict, category: str, subcategory: str):
    """Zwraca listę nazw produktów"""
    products = categories[category][subcategory]
    return products

if __name__ == "__main__":
    print(product_subcategories(categories, 'do smarowania'))
