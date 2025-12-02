from enum import Enum

class InteractableType(Enum):

    NONE = "None"
    DOOR = "Tür"

class ItemType(Enum):
    
    KEY = "Schlüssel"

class ItemID(Enum):

    BOTTOM_KEY = "Schlüssel für unteren Raum"
    TOP_KEY = "Schlüssel für oberen Raum"
