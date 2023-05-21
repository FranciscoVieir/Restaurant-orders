import csv
from typing import Set
from models.dish import Dish
from models.ingredient import Ingredient


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.source_path = source_path
        self.dishes: Set[Dish] = set()
        self._load_menu_data()

    def _load_menu_data(self) -> None:
        with open(self.source_path, newline='') as file:
            reader = csv.reader(file)
            next(reader)

            for row in reader:
                dish_na, dish_price, ingrent_name, ingrent_qutity = row

                dish = self._get_or_create_dish(dish_na, float(dish_price))
                ingredient = self._get_or_create_ingredient(dish, ingrent_name)

                dish.add_ingredient_dependency(ingredient, int(ingrent_qutity))

    def _get_or_create_dish(self, name: str, price: float) -> Dish:
        for dish in self.dishes:
            if dish.name == name and dish.price == price:
                return dish

        dish = Dish(name, price)
        self.dishes.add(dish)
        return dish

    def _get_or_create_ingredient(self, dish: Dish, name: str) -> Ingredient:
        for ingredient in dish.recipe.keys():
            if ingredient.name == name:
                return ingredient

        ingredient = Ingredient(name)
        dish.add_ingredient_dependency(ingredient, 0)
        return ingredient
