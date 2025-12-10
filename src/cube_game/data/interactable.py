from dataclasses import dataclass, field
from  enums.interaction_objects import InteractableType, InteractableID, Capabilities
from enums.states import InteractableState
from enums.geometry import Facing, Faces
from data.position import Position
from data.item import KeyItem

@dataclass
class Interactable:

    pos: Position
    interactable_id: InteractableID
    capabilities: list[Capabilities] = field(default_factory=list)

@dataclass
class Door(Interactable):

    leads_to: Faces 
    entry_facing: Facing
    req_key: KeyItem | None = None
    interactable_type: InteractableType = field(default=InteractableType.DOOR)
    state: InteractableState = field(default=InteractableState.OPEN)
    
@dataclass
class PressurePlate(Interactable):

    interactable_type: InteractableType = field(default=InteractableType.PRESSURE_PLATE)
    state: InteractableState = field(default=InteractableState.DEPRESSED)

