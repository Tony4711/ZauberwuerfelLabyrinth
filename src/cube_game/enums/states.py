from enum import Enum, auto


class DoorState(Enum):

    OPEN = auto()
    CLOSED = auto()
    LOCKED = auto()

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
    MAP = "Karte"
    

class MenuState(Enum):

    MAIN = "Hauptmenu"
    SETTINGS = "Einstellungen"
    NAVIGATION = "Steuerung"
    EXIT = "Verlassen"
    MAP = "Karte"
    ALL_NAVIGATIONS = "Alle Steuerungen"

class PlayerState(Enum):

    INIT = auto()
    MOVE = auto()
    STAND = auto()
    WALL = auto()
    DOOR = auto()
    GO_DOOR = auto()