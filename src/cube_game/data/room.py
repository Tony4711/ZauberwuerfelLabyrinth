from enums.geometry import Directions, RoomColor, Corner
from dataclasses import dataclass
from data.position import Position
from data.door import Door

@dataclass
class Room:
    
    color: RoomColor
    width: int
    length: int
    name: str
    hex_color: hex
    doors: dict[Directions, Door]
    neighbors: dict[Directions, RoomColor]
    pos : dict[Corner, Position]
    
    def __repr__(self):
        return f"{self.name} at {self.pos} with {self.neighbors} as neighbors" 


