import pytest
from coffee import Coffee
from customer import Customer
from order import Order

def test_coffee_creation():
    coffee = Coffee("Espresso")
    assert coffee.name == "Espresso"

def test_average_price():
    coffee = Coffee("Cappuccino")
    customer = Customer("Bob")
    customer.create_order(coffee, 4.0)
    customer.create_order(coffee, 5.0)
    assert coffee.average_price() == 4.5
