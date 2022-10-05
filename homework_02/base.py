from abc import ABC
from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):

    def __init__(self, weight: float = 0, fuel: float = 0, fuel_consumption: float = 0):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.started = False

    def start(self):
        if self.started is False:
            if self.fuel > 0:
                self.started = True
            else:
                raise LowFuelError

    def move(self, distance: float):
        if self.fuel >= self.fuel_consumption * distance:
            self.fuel -= self.fuel_consumption * distance
        else:
            raise NotEnoughFuel
