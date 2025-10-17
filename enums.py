"""Centralized state definitions for the game (door, game, etc.)."""
from enum import Enum, auto

class DoorState(Enum):

    OPEN = auto()
    CLOSED = auto()
    LOCKED = auto()

class GameState(Enum):
    
    INIT = "Init"
    MAIN_MENU = "Main Menu"
    PLAYING = "Start"
    EXIT = "Exit"
    IDLE = "Ruhend"
    GLOBAL_CONTROLS = "Globale Steuerungen"

class Directions(Enum):

    NORTH = auto()
    EAST = auto()
    SOUTH = auto()
    WEST = auto()

class RoomColor(Enum):
    
    YELLOW = auto()
    WHITE = auto()
    GREEN = auto()
    ORANGE = auto()
    BLUE = auto()
    RED = auto()

class CommandTag(Enum):
    MOVEMENT = auto()
    META= auto()
    OPTION = auto()
    CHOICE = auto()

class Command(Enum):

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

    def __init__(self, key, tag):
        self._value_ = key
        self.tag = tag