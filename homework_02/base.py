from abc import ABC
import exceptions


class Vehicle(ABC):

    def __init__(self, weight: float = 0, fuel: float = 0, fuel_consumption: float = 0, started: bool = False):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.started = started

    def start(self):
        if not self.started:
            if self.fuel > 0:
                self.started = True
            else:
                raise exceptions.LowFuelError

    def move(self, distance: float):
        if self.fuel >= self.fuel_consumption * distance:
            self.fuel -= self.fuel_consumption * distance
        else:
            raise exceptions.NotEnoughFuel


if __name__ == '__main__':
    v = Vehicle(fuel=1, fuel_consumption=0.2)
    print(v.fuel, v.fuel_consumption, v.started)
    v.start()
    print(v.fuel, v.fuel_consumption, v.started)
    v.move(1)
    print(v.fuel, v.fuel_consumption, v.started)
