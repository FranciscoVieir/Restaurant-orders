from src.models.dish import Dish
from src.models.ingredient import Ingredient
import pytest

def test_dish():
    dish = Dish("Lasanha", 19.99)

    assert dish.name == "Lasanha"
    assert dish.price == 19.99

    assert dish == Dish("Lasanha", 19.99)
    assert hash(dish) == hash(Dish("Lasanha", 19.99))

    with pytest.raises(AssertionError):
        assert dish.name == "Espaguete"
