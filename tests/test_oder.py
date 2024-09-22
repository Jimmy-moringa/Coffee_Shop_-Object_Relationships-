import pytest
from customer import Customer
from coffee import Coffee
from order import Order

def test_order_creation():
    customer = Customer("Charlie")
    coffee = Coffee("Americano")
    order = Order(customer, coffee, 2.5)
    assert order.price == 2.5
    assert order.customer == customer
    assert order.coffee == coffee
