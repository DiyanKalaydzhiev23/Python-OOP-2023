class Shop:
    def __init__(self, name, items):
        self.name = name
        self.items = items

    def get_items_count(self):
        return len(self.items)


lidl = Shop("Lidl", ["Apples", "Bananas", "Cucumbers"])
bila = Shop("Lidl", ["Apples", "Bananas", "Cucumbers"])
