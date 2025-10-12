from enum import Enum, auto
from position import Position
from state import DoorState
from dataclasses import dataclass, field

@dataclass
class Door:

    position: Position = field(default_factory=lambda: Position(-1,-1))
    direction: str
    state: DoorState = DoorState.CLOSED
    key_req: bool = False
    leads_to: str