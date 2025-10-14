from enums import Directions, RoomColor
from dataclasses import dataclass, field
from typing import Literal
from position import Position
from door import Door

@dataclass(frozen=True)
class Room:
    
    color: RoomColor
    width: int
    length: int
    name: str
    door: Door
    neighbors: dict[Directions, RoomColor]
    position : Position = field(default_factory=lambda: Position(2,2))
    
    def __repr__(self):
        return f"{self.name} at {self.position} with {self.neighbors} as neighbors" 

