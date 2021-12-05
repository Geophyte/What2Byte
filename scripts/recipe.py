# Alternatywa dla klas Category i Item:
# 
# from dataclasses import dataclass
# 
# @dataclass
# class Category:
#     id: int
#     name: str
# 
# 
# @dataclass
# class Item:
#     code: int
#     category: "Category"


class Category:
    def __init__(self, id, name):
        self._id = id
        self._name = name

    def id(self):
        return self._id

    def name(self):
        return self._name


class Item:
    def __init__(self, code, category):
        self._code = code
        self._category = category

    def code(self):
        return self._code

    def category(self):
        return self._category


class Recipe:
    def __init__(self, id, name, ingredients, text):
        self._id = id
        self._name = name
        self._ingredients = ingredients
        self._text = text

    def id(self):
        return self._id

    def name(self):
        return self._name

    def ingredients(self):
        return self._ingredients

    def text(self):
        return self._text

    def __str__(self):
        return f"{self._name}\n{self._text}"

    def is_doable(self, storage):
        for ingredient, amount in self._ingredients.items():
            if amount > storage.get(ingredient, 0):
                return False
        return True

    def subtract_ingredients(self, storage):
        for ingredient, amount in self._ingredients.items():
            storage[ingredient] -= amount
        return storage

    def check(self, storage):
        lacking_ingredients = {}
        for ingredient, amount in self._ingredients.items():
            if amount > storage.get(ingredient, 0):
                lacking_ingredients[ingredient] = amount - storage.get(ingredient, 0)
        return lacking_ingredients
