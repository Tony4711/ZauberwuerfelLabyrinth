from dataclasses import dataclass, field
from position import Position
from room import Room

@dataclass
class Player:

    name: str
    current_room: Room | None = None
    pos: Position = field(default_factory=lambda: Position(7,7)) 
    
