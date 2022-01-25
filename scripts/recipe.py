from dataclasses import dataclass


@dataclass
class Category:
    id: int
    name: str


@dataclass
class Item:
    code: int
    category: "Category"


class Recipe:
    def __init__(self, id: int, name: str, ingredients: dict, text: str):
        self._id = id
        self._name = name
        self._ingredients = ingredients
        self._text = text

    def id(self) -> int:
        return self._id

    def name(self) -> str:
        return self._name

    def ingredients(self) -> dict:
        return self._ingredients

    def text(self) -> str:
        return self._text

    def __str__(self) -> str:
        text = self.name() + "\n\n"
        text += "Składniki:\n"

        for name in self._ingredients:
            text += f"{name}: {self.ingredients()[name]}\n"

        text += f"\nKroki:\n{self.text()}"

        return text

    # Zwraca listę składników jako string
    def ingredients_str(self) -> str:
        text = str()
        for name in self._ingredients:
            text += f"{name}: {self._ingredients[name]}\n"
        return text

    # Sprawdza czy można przygotować przepis ze składników w 'storage'
    # Zwraca True jeśli to możliwe
    def is_doable(self, storage: dict) -> bool:
        for ingredient in self.ingredients().keys():
            if ingredient not in storage.keys():
                return False
            if self.ingredients()[ingredient] > storage[ingredient]:
                return False
        return True

    # Odejmuje składniki z 'storage' wykorzystane do przygotowania przepisu
    # Zwraca 'storage' po modyfikacji
    def subtract_ingredients(self, storage: dict) -> dict:
        if not self.is_doable(storage):
            return storage

        for ingredient in self.ingredients().keys():
            storage[ingredient] -= self.ingredients()[ingredient]
            if storage[ingredient] == 0:
                del storage[ingredient]
        return storage

    # Sprawdza jakich składników brakuje do przygotowania przepisów
    # Zwraca słownik gdzie nazwy są kluczami, a brakująca ilość wartością
    def check(self, storage):
        lacking_ingredients = {}
        for ingred, amount in self._ingredients.items():
            if amount > storage.get(ingred, 0):
                lacking_ingredients[ingred] = amount - storage.get(ingred, 0)
        return lacking_ingredients


if __name__ == "__main__":
    ingredients = {
        "a": 20,
        "b": 30,
        "c": 40
    }
    text = "abcdef\ndabcdef\ndffss\nndf"
    recipe = Recipe(0, "a", ingredients, text)
    print(recipe)
    print(recipe.ingredients_str())
