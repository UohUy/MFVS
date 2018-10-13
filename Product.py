class Product:
    _quantity = {}

    def __init__(self, id, name, unit, type, brand, price, quantity, inventory, source, production_date, expiry_day, status):
        self.id = id
        self.name = name
        self.unit = unit
        self.type = type
        self.brand = brand
        self.price = price
        self.quantity = quantity
        self.inventory = inventory
        self.source = source
        self.production_date = production_date
        self.expiry_day = expiry_day
        self.status = status

    def update_production_date(self, new_date):
        self.production_date = new_date

    def __str__(self):
        return 'Name: {}\nBrand: {}\nPrice: {}\nExpiry Day: {}'.format(self.name, self.brand, self.price,
                                                                       self.expiry_day)
