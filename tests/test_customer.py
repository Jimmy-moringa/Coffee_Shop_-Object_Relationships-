import pytest
from customer import Customer
from coffee import Coffee

def test_customer_creation():
    customer = Customer("Alice")
    assert customer.name == "Alice"

def test_create_order():
    customer = Customer("Alice")
    coffee = Coffee("Latte")
    customer.create_order(coffee, 3.5)
    assert len(customer.orders()) == 1
    assert customer.orders()[0].price == 3.5
