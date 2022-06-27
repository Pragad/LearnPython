from bike import Bike
from car import Car


def foo():
    car = Car()
    car.print_car()
    car2 = Car()
    car2.print_car()
    print(car is car2)

def bar():
    bike = Bike()
    bike.print_bike()
    bike2 = Bike()
    bike2.print_bike()
    print(bike is bike2)

msg = "Hello World"
print(msg)

foo()
bar()
