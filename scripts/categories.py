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
                                                'zioła': ['bazylia', 'koperek', 'mięta']},
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
