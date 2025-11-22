from enums.geometry import RoomColor, Corner, Faces
from dataclasses import dataclass
from data.position import Position
from data.door import Door

@dataclass
class Room:
    
    face: Faces
    color: RoomColor
    width: int
    length: int
    name: str
    hex_color: hex
    doors: list[Door]
    neighbors: list[Faces]
    pos : dict[Corner, Position]
    
    def __repr__(self):
        return f"{self.name} at {self.pos} with {self.neighbors} as neighbors" 


