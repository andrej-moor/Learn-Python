from car import Car
my_car = Car("Mercedes", "rot")
my_car.speed = 200
my_car.speed = 250 # Wert verändert
my_car.speed = my_car.speed + 10


print(my_car.speed)