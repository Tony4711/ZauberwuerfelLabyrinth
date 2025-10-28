from dataclasses import dataclass, field
from position import Position
from room import Room
from enums import Directions

@dataclass
class Player:

    name: str
    direction: Directions
    current_room: Room | None = None
    pos: Position = field(default_factory=lambda: Position(7,7)) 
    
