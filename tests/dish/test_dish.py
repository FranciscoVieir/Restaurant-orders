from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient
import pytest


def test_dish():
    dish = Dish("Lasagna", 14.80)

    with pytest.raises(
        ValueError, match="Dish price must be greater then zero."
    ):
        Dish("Lasagna", 0)

    with pytest.raises(TypeError, match="Dish price must be float."):
        Dish("Lasagna", "24")

    assert dish.name == "Lasagna"
    assert dish.price == 14.80
    assert dish == Dish("Lasagna", 14.80)
    assert hash(dish) == hash("Dish('Lasagna', R$14.80)")
    assert repr(dish) == "Dish('Lasagna', R$14.80)"

    dish.add_ingredient_dependency(Ingredient("meat"), 1)

    assert dish.get_ingredients() == {Ingredient('meat')}
    assert not dish.get_restrictions()
    assert dish.recipe == {Ingredient("meat"): 1}
