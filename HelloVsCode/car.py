# from singleton import Singleton
# from singleton import singleton
from vehicle import Vehicle


# @singleton
class Car(Vehicle):
    def __init__(self):
        print("Constructor: Car is starting")

    def print_car(self):
        print("Car is running")
