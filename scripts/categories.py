from categories_file import categories_dict as categories
from load_save import _get_abs_path


class WrongCategoryError(Exception):
    def __init__(self):
        super().__init__(
            "\nBłędnie wprowadziłeś numer kategorii. Wybierz kategorię ponownie.\n")


class WrongSubcategoryError(Exception):
    def __init__(self):
        super().__init__("\nBłędnie wprowadziłeś numer podkategorii. Wybierz podkategorię ponownie.\n")


class WrongProductError(Exception):
    def __init__(self):
        super().__init__("\nBłędnie wprowadziłeś numer produktu. Wybierz produkt ponownie.\n")


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


def check_choice(choice: str, product_list: list, error_type: str) -> int:
    """Sprawdza poprawność wyboru użykownika i konwertuje go na odpowiedni typ"""
    if error_type == 'category':
        error_type = WrongCategoryError
    elif error_type == 'subcategory':
        error_type = WrongSubcategoryError
    elif error_type == 'product':
        error_type = WrongProductError
    if not choice.isdigit():
        raise error_type
    elif int(choice) < 1 or int(choice) > len(product_list):
        raise error_type
    else:
        return int(choice)-1


def choose_own_category() -> str:
    """Pozwala na wybór lub dodanie własnej kategorii"""
    path = _get_abs_path("../data/own_categories.txt")
    own_categories = open_own_categories_list(path)
    for count, subcategory in enumerate(own_categories):
        print(count+1, subcategory)
    choice_other = input('\nWprowadź numer produktu: ')
    choice_other = check_choice(choice_other, own_categories, 'product')
    if choice_other == 0:
        own_category_name = input("Podaj nazwę produktu: ")
        print(
            f'Czy na pewno chcesz dodać produkt o nazwie: "{own_category_name}"?')
        confirmation = input("tak/nie: ")
        if confirmation == 'tak':
            add_own_category(path, own_category_name)
            return("Pomyślnie dodano produkt.")
        else:
            return("Dodawanie produktu nie powiodło się.")
    else:
        return own_categories[choice_other]


def product_category(categories: dict) -> str:
    """Zwraca nazwę (pod)kategorii produktu wybranej ze słownika"""
    print("Wybierz kategorię: ")
    for count, category in enumerate(categories):
        print(count+1, category)
    id_list = list(categories.keys())
    choice1 = input('\nWprowadź numer kategorii: ')
    choice1 = check_choice(choice1, id_list, 'category')
    if choice1 == len(id_list)-1:
        return choose_own_category()
    else:
        subcategories = categories[id_list[choice1]]
        print("\nWybierz podkategorię: ")
        for count, subcategory in enumerate(subcategories):
            print(count+1, subcategory)
        id_list2 = list(subcategories.keys())
        choice2 = input('\nWprowadź numer podkategorii: ')
        choice2 = check_choice(choice2, id_list2, 'subcategory')
        products = categories[id_list[choice1]][id_list2[choice2]]
        print("\nWybierz produkt: ")
        for count, product in enumerate(products):
            print(count+1, product)
        choice3 = input('\nWprowadź numer produktu: ')
        choice3 = check_choice(choice3, products, 'product')
        return products[choice3]
