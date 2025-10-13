from dataclasses import dataclass, field
from position import Position
from room import Room

@dataclass(frozen=True)
class Player:

    name: str
    current_room: Room | None = None
    pos: Position = field(default_factory=lambda: Position(2,2)) 
    
