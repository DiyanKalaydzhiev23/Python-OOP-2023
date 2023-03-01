from project.car import Car
from project.family_car import FamilyCar
from project.vehicle import Vehicle

vehicle = Vehicle(50, 150)

print(Vehicle.DEFAULT_FUEL_CONSUMPTION)
print(FamilyCar.DEFAULT_FUEL_CONSUMPTION)

print(vehicle.fuel)
print(vehicle.horse_power)
print(vehicle.fuel_consumption)

vehicle.drive(100)
print(vehicle.fuel)

car = Car(150, 150)

car.drive(50)
print(car.fuel)

car.drive(50)
print(car.fuel)

print(car.__class__.__bases__[0].__name__)
