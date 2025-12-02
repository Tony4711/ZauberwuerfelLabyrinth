from enums.states import DoorState
from enums.geometry import Facing
from enums.objects import InteractableType, ItemType
from data.position import Position
from data.item import KeyItem
from dataclasses import dataclass, field

@dataclass
class Door:

    interactable_type: InteractableType
    leads_to: str
    entry_facing: Facing
    req_key: KeyItem | None = None
    state: DoorState = DoorState.OPEN
    pos: Position = field(default_factory=lambda: Position(-1,-1))
    
    
