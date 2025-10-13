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
    GLOBAL_CONTROLS = "Steuerung"

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