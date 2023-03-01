from project.product import Product


class Food(Product):
    QUANTITY = 15

    def __init__(self, name: str):
        super().__init__(name, Food.QUANTITY)
