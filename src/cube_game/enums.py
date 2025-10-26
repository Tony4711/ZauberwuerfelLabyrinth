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
    QUIT = ("x", CommandTag.META)
    OPEN_MAP = ("m", CommandTag.META)
    CONTROLS = ("c", CommandTag.META)
    OP1 = ("1", CommandTag.OPTION)
    OP2 = ("2", CommandTag.OPTION)
    OP3 = ("3", CommandTag.OPTION)
    OP4 = ("4", CommandTag.OPTION)
    BACK = ("q", CommandTag.META)
    FORTH = ("e", CommandTag.META)
    ACCEPT = ("j", CommandTag.CHOICE)
    DENIE = ("n", CommandTag.CHOICE)
    EXIT = ("x", CommandTag.META)

class DoorState(Enum):

    OPEN = auto()
    CLOSED = auto()
    LOCKED = auto()

class IsGlobal(Enum):

    TRUE = True
    FALSE = False

class GameState(TaggedEnum):
    
    INIT = ("Init", IsGlobal.TRUE)
    PLAYING = ("Start", IsGlobal.TRUE)
    EXIT = ("Exit", IsGlobal.FALSE)
    IDLE = ("Ruhend", IsGlobal.FALSE)
    GLOBAL_CONTROLS = ("Globale Steuerungen", IsGlobal.TRUE)
    MENU = ("Menu", IsGlobal.FALSE)

class MenuState(Enum):

    MAIN = "Hauptmenu"
    SETTINGS = "Einstellungen"
    CONTROLS = "Steuerung"

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