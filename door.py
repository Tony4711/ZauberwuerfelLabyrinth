from enums import DoorState, Directions
from position import Position
from dataclasses import dataclass, field

@dataclass
class Door:

    leads_to: str
    direction: Directions
    key_req: bool = False
    state: DoorState = DoorState.CLOSED
    pos: Position = field(default_factory=lambda: Position(-1,-1))
    
    