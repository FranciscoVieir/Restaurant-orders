from src.models.ingredient import Ingredient, Restriction


def test_ingredient():
    ingredient_name = "queijo mussarela"
    ingredient = Ingredient(ingredient_name)

    assert isinstance(ingredient, Ingredient)

    assert ingredient.name == ingredient_name

    expected_restrictions = {Restriction.LACTOSE, Restriction.ANIMAL_DERIVED}
    assert ingredient.restrictions == expected_restrictions

    expected_repr = f"Ingredient('{ingredient_name}')"
    assert repr(ingredient) == expected_repr

    ingredient2 = Ingredient(ingredient_name)
    assert ingredient == ingredient2

    ingredient3 = Ingredient("farinha")
    assert ingredient != ingredient3

    assert hash(ingredient) == hash(ingredient2)
    assert hash(ingredient) != hash(ingredient3)
