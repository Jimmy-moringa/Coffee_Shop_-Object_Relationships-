class Customer:
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
        if not isinstance(name, str) or not (1 <= len(name) <= 15):
            raise ValueError("Name must be a string between 1 and 15 characters.")
        return name

    def create_order(self, coffee, price):
        order = order(self, coffee, price)  # Ensure 'Order' is defined elsewhere
        self.orders_list.append(order)
        coffee.add_order(order)

    def orders(self):
        return self.orders_list

    def coffees(self):
        return list({order.coffee for order in self.orders_list})
