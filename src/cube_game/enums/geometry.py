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

class Edge(Enum):

    LEFT_FRONT = None
    FRONT_RIGHT = None
    RIGHT_BACK = None
    FRONT_TOP = None
    BOTTOM_FRONT = None
    BOTTOM_BACK = Directions.NORTH
    BACK_TOP = Directions.SOUTH
    LEFT_BACK = None
    RIGHT_TOP = Directions.SOUTH
    LEFT_TOP = Directions.SOUTH
    RIGHT_BOTTOM = Directions.NORTH
    LEFT_BOTTOM =Directions.NORTH