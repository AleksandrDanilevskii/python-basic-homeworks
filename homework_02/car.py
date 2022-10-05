"""
создайте класс `Car`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02.engine import Engine


class Car(Vehicle):
    def __init__(self, weight: float = 1.5, fuel: float = 0, fuel_consumption: float = 8.2):
        super().__init__(weight=weight, fuel=fuel, fuel_consumption=fuel_consumption)
        self.engine = None

    def set_engine(self, engine: Engine):
        self.engine = engine