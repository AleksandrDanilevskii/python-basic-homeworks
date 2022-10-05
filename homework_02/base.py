from abc import ABC
import exceptions


class Vehicle(ABC):

    def __init__(self, weight: float = 1000, fuel: float = 5, fuel_consumption: float = 1, started: bool = False):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.started = started

    def start(self):
        if self.started is False:
            if self.fuel > 0:
                self.started = True
            else:
                raise exceptions.LowFuelError

    def move(self, distance: float):
        if self.fuel >= self.fuel_consumption * distance:
            self.fuel -= self.fuel_consumption * distance
        else:
            raise exceptions.NotEnoughFuel
