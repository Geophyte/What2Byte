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


categories = {
    "do smarowania": ["dżemy i marmolady", "kremy", "pasty"],
    "nabiał": [
        "jaja i drożdże",
        "jogurty i serki",
        "mleko i kefir",
        "produkty twarogowe",
        "sery",
        "śmietany",
    ],
    "napoje": None,
    "owoce i orzechy": None,
    "pieczywo": ["bułki", "chleby", "tortille", "zamienniki pieczywa"],
    "produkty gotowe": None,
    "produkty mięsne": [
        "konserwy i pasztety",
        "ryby i owoce morza",
        "świeże mięsa",
        "wędliny i mięsa w plastrach",
    ],
    "przyprawy i dodatki w proszku": None,
    "sosy i dodatki": ["ketchup, majonez, musztarda", "Sosy"],
    "spiżarnia": [
        "do słodzenia",
        "kasze i ryż",
        "kawa, kakao, herbata",
        "makarony",
        "mąki",
        "ocet",
        "produkty zbożowe",
        "puszki i słoiki",
    ],
    "tłuszcze": None,
    "warzywa i grzyby": None,
}


def product_category(categories: dict = categories) -> str:
    """Zwraca nazwę (pod)kategorii wybranej ze słownika"""

    print("Wybierz kategorię: ")
    for category in categories:
        print(category)
    choice1 = input("\n")
    if choice1.lower() not in categories.keys():
        raise WrongCategoryError
    if not categories[choice1.lower()]:
        return choice1.lower()
    if choice1.lower() in categories.keys():
        subcategories = categories[choice1.lower()]
        print("\nWybierz podkategorię: ")
        for subcategory in subcategories:
            print(subcategory)
        choice2 = input("\n")
        if choice2.lower() not in subcategories:
            raise WrongSubcategoryError
        else:
            return choice2.lower()
