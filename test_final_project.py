import pytest
from pizza_classes import Margherita, Pepperoni, Hawaiian


def test_pizzas_eq():
    pizza_1 = Margherita("L")
    pizza_2 = Margherita("L")
    assert pizza_1 == pizza_2


def test_pizza_not_eq_size():
    pizza_1 = Hawaiian("L")
    pizza_2 = Hawaiian("XL")
    assert pizza_1 != pizza_2


def test_pizza_not_eq_type():
    pizza_1 = Margherita("L")
    pizza_2 = Pepperoni("XL")
    assert pizza_1 != pizza_2


def test_wrong_size():
    with pytest.raises(TypeError):
        Pepperoni('S')
