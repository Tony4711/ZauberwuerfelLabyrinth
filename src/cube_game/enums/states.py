from enum import Enum, auto


class InteractableState(Enum):

    OPEN = auto()
    CLOSED = auto()
    LOCKED = auto()
    PRESSED = auto()
    DEPRESSED = auto()

class SystemState(Enum):

    OK = "OK"
    EXCEPTION_INPUT_ERROR = "Eingabefehler"

class GameState(Enum):
    
    INIT = "Init"
    PLAYING = "Spiel"
    EXIT = "Exit"
    IDLE = "Ruhend"
    MENU = "Menu"
    BACK = "Zurück"

class MenuState(Enum):

    MAIN = "Hauptmenu"
    SETTINGS = "Einstellungen"
    EXIT = "Beenden"
    
class PlayerState(Enum):

    INIT = auto()
    MOVE = auto()
    TURN = auto()
    WALL = auto()
    INTERACTION = auto()
    INTERACTION_EXCEPTION = auto()

class DisplayFunction(Enum):
    
    INIT = "INIT"
    MAP = "Karte"
    NAVIGATION = "Steuerungen"
    SHUFFLE_MAP = "Mischen"
    INSTRUCTION = "Spielanleitung"
    INVENTORY = "Inventar"