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
        super().__init__("\nWprowadzony produkt nie istnieje. Wpisz jego nazwę ponownie. \n")


categories = {'do smarowania': {'dżemy i marmolady': ['dżem truskawkowy', 'dżem brzoskwiniowy', 'marmolada wieloowocowa', 'konfitura malinowa'],
                                'kremy': ['nutella', 'masło orzechowe'],
                                'pasty': ['pasta warzywna', 'hummus', 'pasta jajeczna']},
              'nabiał': {'jaja i drożdże': ['jajko', 'drożdże'],
                         'jogurty i serki': ['serek homogenizowany', 'serek waniliowy', 'serek naturalny', 'jogurt naturalny', 'skyr'],
                         'mleko i kefir': ['mleko', 'zsiadłe mleko', 'kefir', 'maślanka'],
                         'produkty twarogowe': ['twaróg', 'almette', 'serek twarogowy'],
                         'sery': ['ser', 'ser pleśniowy', 'ser topiony', 'ser tarty', 'ser żółty', 'serek topiony'],
                         'śmietany': ['śmietana', 'śmietanka 30%']},
              'napoje': {'alkohole': ['rum', 'wódka', 'whiskey'],
                         'napoje gazowane': ['cola', 'fanta', 'sprite'],
                         'soki i nektary': ['sok pomarańczaowy', 'sok jabłkowy', 'nektar z czarnej porzeczki'],
                         'soki wyciskane': ['sok z cytryny', 'sok z limonki', 'sok z pomarańczy'],
                         'syropy': ['syrop malinowy', 'syrop truskawkowy'],
                         'wody': ['woda', 'woda gazowana', 'woda lekko gazowana']},
              'owoce, warzywa, orzechy i grzyby': {'owoce': ['jabłko', 'gruszka', 'malina', 'truskawki', 'winogrona', 'limonka'],
                                                   'warzywa': ['cebula', 'czosnek', 'pomidor', 'fasola', 'marchewka', 'pietruszka', 'papryka', 'szpinak', 'rukola', 'sałata', 'ziemniaki'],
                                                   'orzechy': ['orzech wloski', 'orzech laskowy'],
                                                   'grzyby': ['kurka', 'pieczarka']},
              'pieczywo': {'bułki': ['kajzerka', 'bułka z ziarnami', 'bagietka'],
                           'chleby': ['chleb pszenny', 'chleb tostowy', 'chleb razowy', 'chleb żytni'],
                           'tortille': ['tortilla pszenna', 'tortilla pełnoziarnista', 'lawasz'],
                           'zamienniki pieczywa': ['wafle ryżowe', 'chlebki pełnoziarniste']},
              'produkty gotowe': {'ciasta': ['ciasto na pizze', 'ciasto francuskie'],
                                  'inne': ['kluski', 'frytki', 'kopytka']},
              'produkty mięsne': {'konserwy i pasztety': ['konserwa mięsna', 'konserwa rybna', 'mielonka', 'pasztet drobiowy', 'pasztet wieprzowy'],
                                  'ryby i owoce morza': ['dorsz', 'makrela', 'łosoś', 'paluszki rybne', 'krewetki'],
                                  'świeże mięsa': ['filet z kurczaka', 'mięso mielone', 'mięso z kurczaka', 'kiełbasa'],
                                  'wędliny i mięsa w plastrach': ['szynka', 'polędwica', 'schab', 'kiełbasa żywiecka']},
              'przyprawy i dodatki w proszku': {'przyprawy': ['cynamon', 'kurkuma', 'sól', 'pieprz', 'chilli', 'słodka papryka', 'oregano'],
                                                'dodatki': ['kostka rosołowa', 'soda oczyszczona', 'proszek do pieczenia', 'cukier waniliowy'],
                                                'zioła': ['bazylia','koperek', 'mięta']},
              'sosy i dodatki': {'ketchup, majonez i inne': ['ketchup', 'majonez', 'musztarda sarepska', 'musztarda dijon', 'chrzan'],
                                 'sosy': ['sos sojowy', 'sos słodko-kwaśny']},
              'spiżarnia': {'do słodzenia': ['cukier', 'cukier waniliowy', 'miód', 'ksylitol'],
                            'kasze': ['kasza gryczana', 'kasza jaglana'],
                            'kawa, kakao, herbata': ['kawa rozpuszczalna', 'kawa ziarnista', 'kawa sypana', 'kakao', 'herbata'],
                            'makarony': ['makaron', 'makaron wstążki', 'makaron spaghetti', 'makaron lasagne'],
                            'mąki': ['mąka tortowa', 'mąka pszenna', 'mąka razowa', 'mąka żytnia'],
                            'octy': ['ocet jabłkowy', 'ocet spirytusowy'],
                            'produkty zbożowe': ['płatki owsiane', 'otręby'],
                            'puszki i słoiki': ['buraczki', 'groszek', 'pesto', 'krojone pomidory', 'pomidory suszone', 'passata pomidorowa', 'koncentrat pomidorowy', 'fasola z puszki', 'oliwki'],
                            'ryz': ['ryż', 'ryż paraboiled', 'ryż pełnoziarnisty']},
              'tłuszcze': {'płynne': ['olej', 'olej rzepakowy', 'olej słonecznikowy', 'oliwa'],
                           'twarde': ['masło', 'margaryna', 'smalec']}
              }


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
            choice3 = input('\n')
            if choice3.lower() not in products:
                raise WrongProductError
            else:
                return choice3
