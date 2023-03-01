from project.gorilla import Gorilla
from project.lizard import Lizard
from project.mammal import Mammal

gorilla = Gorilla("Stella")
print(Gorilla.mro())
print(gorilla.name)

lizard = Lizard("John")
print(lizard.__class__.__bases__[0].__name__)
print(lizard.name)
