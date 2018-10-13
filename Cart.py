import Product

class Cart:
    def __init__(self):
        self.item_list = {} # Product: (qty, unit)
        self.total_due = 0

    def calculate_total_due(self):
        sum = 0
        # TODO Total due is also determined by product's unit
        for key, value in self.item_list:
            sum += key.price * value[0]

    def add_item(self, item):
        if item in self.item_list.keys():
            return False
        else:
            self.item_list[item] = (None, None)

    # After add a new item, calculate total due
    def __setitem__(self, key, value):
        self.item_list[key] = value
        self.calculate_total_due()
