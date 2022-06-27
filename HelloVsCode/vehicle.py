from abc import ABC

from singleton import Singleton
# from singleton import singleton


# @singleton
# class Vehicle(ABC):
class Vehicle(ABC, metaclass=Singleton):

    def __init__(self, vehicle_type, can_fly: bool = False, enable_timeout: bool = False):
        self._vehicle_type = vehicle_type
        self._can_fly = can_fly
        self._enable_timeout = enable_timeout
