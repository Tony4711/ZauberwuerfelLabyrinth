from enums.states import DoorState
from data.position import Position
from dataclasses import dataclass, field

@dataclass
class Door:

    leads_to: str
    key_req: bool = False
    state: DoorState = DoorState.OPEN
    pos: Position = field(default_factory=lambda: Position(-1,-1))
    
    
