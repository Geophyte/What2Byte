from recipe import Recipe


# Ten plik i inne testy powinny się znaleźć w folderze tests


def test_is_doable():
    ingrediants = {'a': 10, 'b': 20, 'c': 30}
    storage1 = {'a': 10, 'b': 20, 'c': 30}
    storage2 = {'a': 20, 'b': 30, 'd': 40}
    storage3 = {'a': 10, 'b': 20, 'c': 20}
    storage4 = {}
    recipe = Recipe(0, 'a', ingrediants, '')

    assert recipe.is_doable(storage1)
    assert not recipe.is_doable(storage2)
    assert not recipe.is_doable(storage3)
    assert not recipe.is_doable(storage4)


def test_subtract_ingredients():
    storage = {'a': 100, 'b': 200, 'c': 300, 'd': 400}
    recipe1 = Recipe(0, 'a', {'a': 300, 'b': 400}, '')
    recipe2 = Recipe(0, 'a', {'a': 20, 'b': 30}, '')
    recipe3 = Recipe(0, 'a', {'c': 300, 'd': 400}, '')

    recipe1.subtract_ingredients(storage)
    assert storage == {'a': 100, 'b': 200, 'c': 300, 'd': 400}

    recipe2.subtract_ingredients(storage)
    assert storage == {'a': 80, 'b': 170, 'c': 300, 'd': 400}

    recipe3.subtract_ingredients(storage)
    assert storage == {'a': 80, 'b': 170}
