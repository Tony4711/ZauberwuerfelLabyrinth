from enum import Enum, auto


class Capabilities(Enum):
    
    IS_MOVEABLE = auto()

class InteractionType(Enum):

    STANDING_ON = "Du stehst auf einer"
    UNLOCK = "Du öffnest mit dem Schlüssel die"
    LOCKED = "Du stehst vor einer verschlossenen"
    WALK_THROUGH = "Du gehst durch eine"

class InteractionResult(Enum):

    ADD_ITEM = "\n  Ein Item wurde deinem Inventar hinzugefügt  "
    ENTER_ROOM = "\n  Du betrittst den {current_room}  "
    KEY_REQ = "\n  Du benötigst einen Schlüssel um sie zu öffnen  "
    ALLREADY_IN_INVENTORY = "\n  Das Item ist bereits in deinem Inventar  "

class InteractableType(Enum):

    DOOR = "Tür"
    PRESSURE_PLATE = "Druckplatte"

class InteractableID(Enum):

    DOOR_BOTTOM_FRONT = auto()
    DOOR_BOTTOM_RIGHT = auto()
    DOOR_BOTTOM_BACK = auto()
    DOOR_BOTTOM_LEFT = auto()
    DOOR_TOP_BACK = auto()
    DOOR_TOP_RIGHT = auto()
    DOOR_TOP_FRONT = auto()
    DOOR_TOP_LEFT = auto()
    DOOR_FRONT_TOP = auto()
    DOOR_FRONT_RIGHT = auto()
    DOOR_FRONT_BOTTOM = auto()
    DOOR_FRONT_LEFT = auto()
    DOOR_RIGHT_TOP = auto()
    DOOR_RIGHT_BACK = auto()
    DOOR_RIGHT_BOTTOM = auto()
    DOOR_RIGHT_FRONT = auto()
    DOOR_BACK_TOP = auto()
    DOOR_BACK_LEFT = auto()
    DOOR_BACK_BOTTOM = auto()
    DOOR_BACK_RIGHT = auto()
    DOOR_LEFT_TOP = auto()
    DOOR_LEFT_FRONT = auto()
    DOOR_LEFT_BOTTOM = auto()
    DOOR_LEFT_BACK =auto()
    PRESSURE_PLATE_LEFT = auto()

class ItemType(Enum):
    
    KEY = "Schlüssel"

class ItemID(Enum):

    KEY_DOOR_BOTTOM_FRONT = "vom {bottom_room} zum {front_room}"
    KEY_DOOR_BOTTOM_RIGHT = "vom {bottom_room} zum {right_room}"
    KEY_DOOR_BOTTOM_BACK = "vom {bottom_room} zum {back_room}"
    KEY_DOOR_BOTTOM_LEFT = "vom {bottom_room} zum {left_room}"
    KEY_DOOR_FRONT_TOP = "vom {front_room} zum {top_room}"
    KEY_DOOR_FRONT_RIGHT = "vom {front_room} zum {right_room}"
    KEY_DOOR_FRONT_BOTTOM = "vom {front_room} zum {bottom_room}"
    KEY_DOOR_FRONT_LEFT = "vom {front_room} zum {left_room}"
    KEY_DOOR_RIGHT_TOP = "vom {right_room} zum {top_room}" 
    KEY_DOOR_RIGHT_BACK = "vom {right_room} zum {back_room}" 
    KEY_DOOR_RIGHT_BOTTOM = "vom {right_room} zum {bottom_room}"
    KEY_DOOR_RIGHT_FRONT = "vom {right_room} zum {front_room}"
    KEY_DOOR_BACK_TOP = "vom {back_room} zum {top_room}"
    KEY_DOOR_BACK_LEFT = "vom {back_room} zum {left_room}"
    KEY_DOOR_BACK_BOTTOM = "vom {back_room} zum {bottom_room}"
    KEY_DOOR_BACK_RIGHT = "vom {back_room} zum {right_room}"
    KEY_DOOR_LEFT_TOP = "vom {left_room} zum {top_room}"
    KEY_DOOR_LEFT_FRONT = "vom {left_room} zum {front_room}"
    KEY_DOOR_LEFT_BOTTOM = "vom {left_room} zum {bottom_room}"
    KEY_DOOR_LEFT_BACK = "vom {left_room} zum {back_room}"
    
