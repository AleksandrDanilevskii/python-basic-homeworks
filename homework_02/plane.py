"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload


class Plane(Vehicle):
    def __init__(self, weight: float = 200, fuel: float = 0, fuel_consumption: float = 10, max_cargo: float = 500,
                 cargo: float = 0):
        super().__init__(weight=weight, fuel=fuel, fuel_consumption=fuel_consumption)
        self.cargo = cargo
        self.max_cargo = max_cargo

    def load_cargo(self, cargo: float):
        new_cargo = self.cargo + cargo
        if new_cargo <= self.max_cargo:
            self.cargo = new_cargo
        else:
            raise CargoOverload

    def remove_all_cargo(self):
        value, self.cargo = self.cargo, 0
        return value
