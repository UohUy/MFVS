import Product

class Cart:
    def __init__(self):
        self.item_list = {} # Product: (qty, unit)
        self.total_due = 0

    def calculate_total_due(self):
        sum = 0
        for key, value in self.item_list:
            sum += key.price * value[0]
        self.total_due = sum

    def add_item(self, item):
        if item in self.item_list.keys():
            return False
        else:
            self.item_list[item] = (None, None)

    def clear(self):
        self.item_list.clear()
        self.total_due = 0

    # After add a new item, calculate total due
    def __setitem__(self, key, value):
        self.item_list[key] = value
        self.calculate_total_due()

    def __len__(self):
        return len(self.item_list)

    def __iter__(self):
        return iter(self.item_list)

    def __getitem__(self, item):
        return self.item_list[item]

    def __delitem__(self, key):
        del self.item_list[key]