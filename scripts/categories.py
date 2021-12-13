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
        super().__init__(
            "\nWprowadzony produkt nie istnieje. Wpisz jego nazwę ponownie. \n"
        )


def product_category(categories: dict) -> str:
    """Zwraca nazwę (pod)kategorii produktu wybranej ze słownika"""

    print("Wybierz kategorię: ")
    for count, category in enumerate(categories):
        print(count+1, category)
    id_list = list(categories.keys())
    choice1 = int(input('\nWprowadź numer kategorii: '))-1
    if choice1 < 0 or choice1 > len(id_list)-1:
        raise WrongCategoryError
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
            choice3 = int(input('\nWprowadź numer produktu:'))-1
            if choice3 < 0 or choice3 > len(products)-1:
                raise WrongProductError
            else:
                return products[choice3]

if __name__ == "__main__":
    while 1:
        try:
            print(product_category(categories))
        except Exception:
            pass
