from categories_file import categories_dict as categories


class WrongCategoryError(Exception):
    def __init__(self):
        super().__init__(
            "\nWprowadzona kategoria nie istnieje. Wpisz kategorię ponownie.\n"
        )


class WrongSubcategoryError(Exception):
    def __init__(self):
        super().__init__(
            "\nWprowadzona podkategoria nie istnieje. Wpisz podkategorię ponownie.\n"
        )


class WrongProductError(Exception):
    def __init__(self):
        super().__init__(
            "\nWprowadzony produkt nie istnieje. Wpisz jego nazwę ponownie. \n"
        )


def product_category(categories: dict) -> str:
    """Zwraca nazwę (pod)kategorii produktu wybranej ze słownika"""

    print("Wybierz kategorię: ")
    for category in categories:
        print(category)
    choice1 = input("\n")
    if choice1.lower() not in categories.keys():
        raise WrongCategoryError
    if choice1.lower() in categories.keys():
        subcategories = categories[choice1.lower()]
        print("\nWybierz podkategorię: ")
        for subcategory in subcategories:
            print(subcategory)
        choice2 = input("\n")
        if choice2.lower() not in subcategories:
            raise WrongSubcategoryError
        else:
            products = categories[choice1.lower()][choice2.lower()]
            print("\nWybierz produkt: ")
            for product in products:
                print(product)
            choice3 = input("\n")
            if choice3.lower() not in products:
                raise WrongProductError
            else:
                return choice3


if __name__ == "__main__":
    while 1:
        try:
            print(product_category(categories))
        except Exception:
            pass
