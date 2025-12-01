from dataclasses import dataclass, field
from data.position import Position
from data.room import Room
from data.door import Door
from data.inventory import Inventory
from enums.geometry import Facing, Moved

@dataclass
class Player:

    name: str
    facing: Facing
    moved: Moved
    inventory: Inventory = field(default_factory=Inventory)
    current_room: Room | None = None
    pos: Position = field(default_factory=lambda: Position(7,7)) 
    
