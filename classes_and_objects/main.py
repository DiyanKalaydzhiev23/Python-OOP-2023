class Car:
    """This is a demo doc"""
    COLOR = "black"

    def __init__(self, manufacturer: str, model: str):
        self.manufacturer = manufacturer
        self.model = model

    def change_color(self):
        Car.COLOR = "white"

    def __repr__(self):
        return f"This a {self.manufacturer} {self.model}"



nissan = Car("Nissan", "GT-R")
toyota = Car("Toyota", "Yaris GR")

print(nissan.COLOR)
print(toyota.COLOR)

nissan.change_color()

print(nissan.COLOR)
print(toyota.COLOR)

print(nissan.__dict__)