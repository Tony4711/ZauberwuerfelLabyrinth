from enums import DoorState, Directions
from position import Position
from enums import DoorState
from dataclasses import dataclass, field

@dataclass
class Door:

    position: Position = field(default_factory=lambda: Position(-1,-1))
    direction: Directions
    state: DoorState = DoorState.CLOSED
    key_req: bool = False
    leads_to: str