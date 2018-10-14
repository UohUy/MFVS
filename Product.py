import re


class Product:
    def __init__(self, id, name, unit, brand, price, inventory, source, production_date, expiry_day, status='good'):
        self.id = id
        self.name = name
        self.unit = unit
        self.brand = brand
        self.price = price
        self.inventory = inventory
        self.source = source
        self.production_date = production_date
        self.expiry_day = expiry_day
        self.status = status

    def update_production_date(self, new_date):
        self.production_date = new_date

    @staticmethod
    def price_validation(price):
        return re.match(r'[+-]?((/d+(/./d*)?)|(/./d+))', price)

    def __str__(self):
        return '{},{},{},{},{},{},{},{},{},{}'.format(self.id, self.name, self.unit, self.__class__.__name__.lower(),
                                                      self.brand, self.price, self.inventory, self.source,
                                                      self.production_date, self.expiry_day, self.status)


class Fruit(Product):
    def __init__(self, id, name, unit, brand, price, inventory, source, production_date, expiry_day, status='good'):
        super().__init__( id, name, unit, brand, price, inventory, source, production_date, expiry_day, status)


class Vegetable(Product):
    def __init__(self, id, name, unit, brand, price, inventory, source, production_date, expiry_day, status='good'):
        super().__init__(id, name, unit, brand, price, inventory, source, production_date, expiry_day, status)
