"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02.base import Vehicle


class Plane(Vehicle):
    def __init__(self, weight: float = 200, fuel: float = 0, fuel_consumption: float = 10, max_cargo: float = 500, cargo: float = 0):
        super().__init__(weight=weight, fuel=fuel, fuel_consumption=fuel_consumption)
        self.cargo = cargo
        self.max_cargo = max_cargo


if __name__ == '__main__':
    p = Plane()
    print(p)
    print(p.__dict__)
