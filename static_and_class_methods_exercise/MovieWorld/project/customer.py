from typing import List
from project.dvd import DVD


class Customer:
    def __init__(self, name: str, age: int, id_number: int):
        self.name = name
        self.age = age
        self.id = id_number
        self.rented_dvds: List[DVD] = []

    def __repr__(self):
        return f"{self.id}: {self.name} of age {self.age} has {len(self.rented_dvds)} " \
               f"rented DVD's ({', '.join(d.name for d in self.rented_dvds)})"
