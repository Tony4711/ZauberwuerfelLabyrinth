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

    MOVE_NORTH = "Nach Norden gehen"
    MOVE_EAST = "Nach Osten gehen"
    MOVE_SOUTH = "Nach Süden gehen"
    MOVE_WEST = "Nach Westen gehen"
    QUIT = "Schließen"
    MAP = "Karte"
    GLOBAL_CONTROLS = "Steuerung"
    MAP = "Karte"