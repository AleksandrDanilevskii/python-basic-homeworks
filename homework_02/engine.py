"""
create dataclass `Engine`
"""
from dataclasses import dataclass

@dataclass()
def Engine():
    volume: float
    pistons: int
