from dataclasses import dataclass, field
from data.position import Position
from data.room import Room
from enums.geometry import Facing, Moved

@dataclass
class Player:

    name: str
    facing: Facing
    moved: Moved
    current_room: Room | None = None
    pos: Position = field(default_factory=lambda: Position(7,7)) 
    
