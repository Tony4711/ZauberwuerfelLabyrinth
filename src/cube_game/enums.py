"""Centralized state definitions for the game (door, game, etc.)."""
from enum import Enum, auto


class TaggedEnum(Enum):
    """Basisklasse für Enums mit (key, tag)-Struktur."""
    
    def __init__(self, key, tag):
        self._value_ = key
        self._tag_ = tag

    @property
    def key(self):
        return self._value_

    @property
    def tag(self):
        return self._tag_

    def __str__(self):
        return str(self._value_)
    
class CommandTag(Enum):

    MOVEMENT = auto()
    META= auto()
    OPTION = auto()
    CHOICE = auto()
    HORIZONTAL = auto()
    VERTICAL = auto()

class Command(TaggedEnum):

    MOVE_NORTH = ("w", CommandTag.MOVEMENT)
    MOVE_EAST = ("d", CommandTag.MOVEMENT) 
    MOVE_SOUTH = ("s", CommandTag.MOVEMENT)
    MOVE_WEST = ("a", CommandTag.MOVEMENT)
    OPEN_MAP = ("m", CommandTag.META)
    CONTROLS = ("c", CommandTag.META)
    OP1 = ("1", CommandTag.OPTION)
    OP2 = ("2", CommandTag.OPTION)
    OP3 = ("3", CommandTag.OPTION)
    OP4 = ("4", CommandTag.OPTION)
    BACK = ("q", CommandTag.META)
    FORTH = ("e", CommandTag.META)
    #ACCEPT = ("j", CommandTag.CHOICE)
    #DENIE = ("n", CommandTag.CHOICE)
    #EXIT = ("x", CommandTag.META)

class DoorState(Enum):

    OPEN = auto()
    CLOSED = auto()
    LOCKED = auto()


class GameState(Enum):
    
    INIT = "Init"
    PLAYING = "Start"
    EXIT = "Exit"
    IDLE = "Ruhend"
    MENU = "Menu"
    BACK = "Zurück"
    MAP = "Karte"

class MenuState(Enum):

    MAIN = "Hauptmenu"
    SETTINGS = "Einstellungen"
    CONTROLS = "Steuerung"
    EXIT = "Verlassen"

class PlayerState(Enum):

    MOVE = auto()
    STAND = auto()
    WALL = auto()
    DOOR = auto()
    GO_DOOR = auto()

class Directions(Enum):

    NORTH = "Norden"
    EAST = "Osten"
    SOUTH = "Süden"
    WEST = "Westen"

class RoomColor(Enum):
    
    YELLOW = auto()
    WHITE = auto()
    GREEN = auto()
    ORANGE = auto()
    BLUE = auto()
    RED = auto()
    
class Corner(Enum):

    BOTTOM_LEFT = auto()
    TOP_RIGHT = auto()

class LoopSignal(Enum):

    CONTINUE = True
    EXIT = False

class TranslateKey(Enum):

    COMMAND_TO_DIRECTION = "commandMovetoDirection"
    DIRECTION_TO_OFFSET = "directionToOffset"
    OFFSET_TO_CORNER = "offsetToCorner"
    CORNER_TO_AXIS = "cornerToAxis"

    def __str__(self):
        return self.value