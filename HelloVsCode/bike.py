# from singleton import Singleton
# from singleton import singleton
from vehicle import Vehicle


# @singleton
class Bike(Vehicle):
    def __init__(self):
        print("Constructor: Bike is starting")
        pass

    def print_bike(self):
        print("Bike is running")
