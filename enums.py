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

class Command(Enum):

    MOVE_NORTH = ("w", "movement")
    MOVE_EAST = ("d", "movement") 
    MOVE_SOUTH = ("s", "movement")
    MOVE_WEST = ("a", "movement")
    QUIT = ("x", "meta")
    OPEN_MAP = ("m", "meta")
    CONTROLS = ("c", "meta")
    OP1 = ("1", "option")
    OP2 = ("2", "option")
    OP3 = ("3", "option")
    OP4 = ("4", "option")
    BACK = ("q", "meta")
    FORTH = ("e", "meta")
    ACCEPT = ("j", "choice")
    DENIE = ("n", "choice")
    EXIT = ("x", "choice")

    def __init__(self, key, tag):
        self._value_ = key
        self.tag = tag