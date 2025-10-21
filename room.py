from enums import Directions, RoomColor, Corner
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
    pos : dict[Corner, Position]
    
    def __repr__(self):
        return f"{self.name} at {self.pos} with {self.neighbors} as neighbors" 

