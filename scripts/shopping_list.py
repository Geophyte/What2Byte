_shopping_list = dict()


# Resetuje listę zakupów
def clear() -> None:
    _shopping_list.clear()


# Dodaje pojedynczy składnik do listy zakupów
def add_item(name: str, ammount: int) -> None:
    try:
        _shopping_list[name] += ammount
    except KeyError:
        _shopping_list[name] = ammount


# Dodaje słownik składników do listy zakupów.
# Klucze słownika to nazwy produktów, wartości to brakująca ilość.
# Powinna być używana w połączeniu z Recipe.check()
def add_items(items: dict) -> None:
    for name in items:
        add_item(name, items[name])


# Zwraca listę ciągów znaków
def to_list_of_str() -> list:
    s_list = sorted(_shopping_list.items())
    s_list = [f'{item[0]}: {item[1]}' for item in s_list]
    return s_list


# Łączy listę i zwraca pojedynczy ciąg zanków
def to_str() -> str:
    return "\n".join(to_list_of_str())


if __name__ == "__main__":
    ingredients = {
        'a': 100,
        'c': 400,
        'b': 200,
        'cc': 500
    }

    more = {
        'd': 10,
        'c': 300,
        'f': 500,
        'cc': 100
    }

    add_items(ingredients)
    print(to_list_of_str())

    add_items(more)
    print(to_list_of_str())

    clear()
