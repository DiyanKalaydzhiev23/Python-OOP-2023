# class Person:
#     def __init__(self, name, height):
#         self.name = name
#         self.height = height
#
#     def grow(self, centimeters):
#         self.height += centimeters
#
# maria = Person("Maria", 170)
#
# print(maria.__dict__)

searched_pokemon = "Pickachu"
pokemons = ["Pickachu", "Charzard"]

result = filter(lambda x: x == x, pokemons)  # ["Pickachu", "Charzard"]

print(next(result))
print(next(result))
print(next(result))