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
    MOVE_WEST = ("a", CommandTag.MOVEMENT)
    MOVE_SOUTH = ("s", CommandTag.MOVEMENT)
    MOVE_EAST = ("d", CommandTag.MOVEMENT) 
    OPEN_MAP = ("m", CommandTag.META)
    NAVIGATION = ("c", CommandTag.META)
    OP1 = ("1", CommandTag.OPTION)
    OP2 = ("2", CommandTag.OPTION)
    OP3 = ("3", CommandTag.OPTION)
    OP4 = ("4", CommandTag.OPTION)
    BACK = ("q", CommandTag.META)
    FORTH = ("e", CommandTag.META)
    ACCEPT = ("j", CommandTag.OPTION)
    DENIE = ("n", CommandTag.OPTION)
    EXIT = ("x", CommandTag.META)

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

class Directions(Enum):

    NORTH = "Norden"
    EAST = "Osten"
    SOUTH = "Süden"
    WEST = "Westen"

class RoomColor(Enum):
    
    YELLOW = "Gelb"
    WHITE = "Weiß"
    GREEN = "Grün"
    ORANGE = "Orange"
    BLUE = "Blau"
    RED = "Rot"
    
class Corner(Enum):

    BOTTOM_LEFT = auto()
    TOP_RIGHT = auto()

class LoopSignal(Enum):

    CONTINUE = True
    EXIT = False

class TranslateKey(Enum):

    COMMAND_TO_DIRECTION = "commandMovetoDirection"
    DIRECTION_TO_OFFSET = "directionToOffset"
    OFFSET_TO_CORNER = "offsetToCorner"
    CORNER_TO_AXIS = "cornerToAxis"
    HANDLE_COMMAND = "commandToState"

    def __str__(self):
        return self.value

class RouterSignal(Enum):

    SHOW_HELLO = auto()
    SHOW_START = auto()
    SHOW_NAVIGATION = auto()
    SHOW_MENU_OPTIONS = auto()
    SHOW_MAP = auto()
    SHOW_EXIT_MENU = auto()
    SHOW_EXIT_CONFIRMED = auto()
    SHOW_MOVE = auto()
    SHOW_WALL = auto()
    SHOW_INFRONT_DOOR = auto() 
    SHOW_ROOM_ENTRANCE = auto()
    SHOW_INPUT_EXCEPTION = auto()
    SHOW_ALL_NAVIGATION = auto()
    META_HANDLER = auto()
    MOVEMENT_HANDLER = auto()
    OPTION_HANDLER = auto()
    
class DisplayStrings(Enum):

    HELLO_TEXT = "hello"
    START_TEXT = "start"
    NAVIGATION_TEXT = "navigation"
    MENU_OPTIONS_TEXT = "menu_options"
    MAP_TEXT = "map"
    EXIT_MENU_TEXT = "exit_menu"
    EXIT_CONFIRMED_TEXT = "exit_confirmed"
    MOVE_TEXT = "move"
    WALL_TEXT = "wall"
    INFRONT_DOOR_TEXT = "infront_door"
    ROOM_ENTRANCE_TEXT = "room_entrance"
    INPUT_EXCEPTION_TEXT = "input_exception"

class DisplayMenuStructure(Enum):

    MENU_OPTION = auto()
    NAVIGATION = auto()

class DisplayNavigation(Enum):

    NAVIGATION = auto()
    ALL_NAVIGATION = auto()

class DisplayMap(Enums):

    MINI_MAP = auto()

class CommandHandler(Enum):

    META_COMMAND = auto()
    MOVEMENT_COMMAND = auto()
    OPTION_COMMAND = auto()

class MenuOptionHandler(Enum):

    MAIN = auto()
    EXIT = auto()

class MovementHandler(Enum):
    
    MOVE_STRAIGHT = auto()