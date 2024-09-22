class Coffee:
    def __init__(self, name):
        self.name = self._validate_name(name)
        self.orders_list = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = self._validate_name(value)

    def _validate_name(self, name):
        if not isinstance(name, str) or len(name) < 3:
            raise ValueError("Coffee name must be at least 3 characters long.")
        return name

    def add_order(self, order):
        self.orders_list.append(order)

    def orders(self):
        return self.orders_list

    def customers(self):
        return list({order.customer for order in self.orders_list})

    def num_orders(self):
        return len(self.orders_list)

    def average_price(self):
        if not self.orders_list:
            return 0
        return sum(order.price for order in self.orders_list) / len(self.orders_list)
