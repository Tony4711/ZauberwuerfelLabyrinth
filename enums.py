"""Centralized state definitions for the game (door, game, etc.)."""
from enum import Enum, auto

class DoorState(Enum):

    OPEN = auto()
    CLOSED = auto()
    LOCKED = auto()

class GameState(Enum):
    
    INIT = "Init"
    MAIN_MENU = "Main Menu"
    START = "Start"
    EXIT = "Exit"
    IDLE = "Ruhend"

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

    MOVE_NORTH = "w"
    MOVE_EAST = "d"
    MOVE_SOUTH = "s"
    MOVE_WEST = "a"
    START = "Start"
    QUIT = "Schließen"
    MAP = "Karte"
    GLOBAL_CONTROLS = "Steuerung"
    MAP = "Karte"
    OP1 = "1"
    OP2 = "2"
    OP3 = "3"
    OP4 = "4"
    BACK = "q"
    FORTH = "e"
    ACCEPT = "j"
    DENIE = "n"