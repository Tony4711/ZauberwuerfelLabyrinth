print("Loaded Room from:", __file__)
from dataclasses import dataclass, field
from typing import Literal

# Defines values
Color = Literal["yellow", "blue", "green", "red", "white", "orange"]
Direction = Literal["north", "east", "south", "west"]

@dataclass(frozen=True)
class Room:
    
    color: str
    width: int
    length: int
    position : str
    name: str
    neighbors: dict[Direction, Color]

    def __repr__(self):
        return f"{self.name} at {self.position} with {self.neighbors} as neighbors" 

    