"""Centralized state definitions for the game (door, game, etc.)."""
from enum import Enum, auto

class DoorState(Enum):

    OPEN = auto()
    CLOSED = auto()
    LOCKED = auto()

class GameState(Enum):
    
    INIT = auto()
    MAIN_MENU = auto()
    START = auto()
    EXIT = auto()
    GLOBAL_CONTROLS = auto()

class Directions(Enum):

    NORTH = auto()
    EAST = auto()
    SOUTH = auto()
    WEST = auto()
