from enum import Enum, auto

class Directions(Enum):

    NORTH = "Norden"
    EAST = "Osten"
    SOUTH = "Süden"
    WEST = "Westen"

class RoomColor(Enum):
    
    YELLOW = "Gelb"
    WHITE = "Weiß"
    GREEN = "Grün"
    ORANGE = "Orange"
    BLUE = "Blau"
    RED = "Rot"
    
class Corner(Enum):

    BOTTOM_LEFT = auto()
    TOP_RIGHT = auto()