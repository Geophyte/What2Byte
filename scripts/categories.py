from categories_file import categories_dict as categories


class WrongCategoryError(Exception):
    def __init__(self):
        super().__init__(
            "\nPodany numer nie pasuje do żadnej kategorii. Wybierz kategorię ponownie.\n")


class WrongSubcategoryError(Exception):
    def __init__(self):
        super().__init__("\nPodany numer nie pasuje do żadnej podkategorii. Wybierz podkategorię ponownie.\n")


class WrongProductError(Exception):
    def __init__(self):
        super().__init__("\nPodany numer nie pasuje do żadnego produktu. Wybierz produkt ponownie.\n")


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


def product_category(categories: dict, path: str) -> str:
    """Zwraca nazwę (pod)kategorii produktu wybranej ze słownika"""

    print("Wybierz kategorię: ")
    for count, category in enumerate(categories):
        print(count+1, category)
    id_list = list(categories.keys())
    choice1 = int(input('\nWprowadź numer kategorii: '))-1
    if choice1 < 0 or choice1 > len(id_list)-1:
        raise WrongCategoryError
    if choice1 == len(id_list)-1:
        own_categories = open_own_categories_list(path)
        for count, subcategory in enumerate(own_categories):
            print(count+1, subcategory)
        print(len(own_categories)+1, "Dodaj własną kategorię")
        choice_other = int(input('\nWprowadź numer podkategorii: '))-1
        if choice_other == len(own_categories):
            own_category_name = input("Podaj nazwę produktu: ")
            print("Czy na pewno chcesz dodać produkt o nazwie: " +
                  own_category_name + "?")
            confirmation = input("tak/nie: ")
            if confirmation == 'tak':
                add_own_category(path, own_category_name)
                return("Pomyślnie dodano produkt.")
            else:
                return("Dodawanie produktu nie powiodło się.")
        elif choice_other < 0 or choice_other > len(own_categories):
            raise WrongSubcategoryError
        else:
            return own_categories[choice_other]
    else:
        subcategories = categories[id_list[choice1]]
        print("\nWybierz podkategorię: ")
        for count, subcategory in enumerate(subcategories):
            print(count+1, subcategory)
        id_list2 = list(subcategories.keys())
        choice2 = int(input('\nWprowadź numer podkategorii: '))-1
        if choice2 < 0 or choice2 > len(id_list2)-1:
            raise WrongSubcategoryError
        else:
            products = categories[id_list[choice1]][id_list2[choice2]]
            print("\nWybierz produkt: ")
            for count, product in enumerate(products):
                print(count+1, product)
            choice3 = int(input('\nWprowadź numer produktu: '))-1
            if choice3 < 0 or choice3 > len(products)-1:
                raise WrongProductError
            else:
                return products[choice3]


print(product_category(categories, '/home/jakubkow1/PZSP1/own_categories.txt'))
