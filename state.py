"""Centralized state definitions for the game (door, game, etc.)."""
from enum import Enum, auto

class DoorState(Enum):

    OPEN = auto()
    CLOSED = auto()
    LOCKED = auto()

class GameState(Enum):
    
    INIT = auto()
