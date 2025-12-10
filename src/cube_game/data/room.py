from enums.geometry import RoomColor, Corner, Faces
from dataclasses import dataclass, field
from data.position import Position
from data.interactable import Door, PressurePlate

@dataclass
class Room:
    
    face: Faces
    color: RoomColor
    width: int
    length: int
    value: str
    hex_color: hex
    doors: list[Door]=field(default_factory=list)
    neighbors: list[Faces]=field(default_factory=list)
    pos : dict[Corner, Position]=field(default_factory=list)
    pressure_plates: list [PressurePlate]=field(default_factory=list)
    
    def __repr__(self):
        return f"{self.value} at {self.pos} with {self.neighbors} as neighbors" 


