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
    MOVE_EAST = ("d", CommandTag.MOVEMENT) 
    MOVE_SOUTH = ("s", CommandTag.MOVEMENT)
    MOVE_WEST = ("a", CommandTag.MOVEMENT)
    OPEN_MAP = ("m", CommandTag.META)
    CONTROLS = ("c", CommandTag.META)
    OP1 = ("1", CommandTag.OPTION)
    OP2 = ("2", CommandTag.OPTION)
    OP3 = ("3", CommandTag.OPTION)
    OP4 = ("4", CommandTag.OPTION)
    BACK = ("q", CommandTag.META)
    FORTH = ("e", CommandTag.META)

class DoorState(Enum):

    OPEN = auto()
    CLOSED = auto()
    LOCKED = auto()

class SystemState(Enum):

    OK = "OK"
    EXCEPTION_INPUT_ERROR = "Eingabefehler"

class GameState(Enum):
    
    INIT = "Init"
    PLAYING = "spielt"
    EXIT = "Exit"
    IDLE = "Ruhend"
    MENU = "Menu"
    BACK = "Zurück"
    MAP = "Karte"
    

class MenuState(Enum):

    MAIN = "Hauptmenu"
    SETTINGS = "Einstellungen"
    CONTROLS = "Steuerung"
    EXIT = "Verlassen"
    MAP = "Karte"

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

    SHOW_HELLO = "show_hello"
    SHOW_START = "show_start"
    SHOW_CONTROLS = "show_controls"
    SHOW_MENU_OPTIONS = "show_menu_options"
    SHOW_MAP = "show_map"
    SHOW_EXIT_MENU = "show_exit_menu"
    SHOW_EXIT_CONFIRMED = "show_exit_confirmed"
    SHOW_MOVE = "show_move"
    SHOW_WALL = "show_wall"
    SHOW_INFRONT_DOOR = "show_infront_door"
    SHOW_ROOM_ENTRANCE = "show_room_entrance"
    SHOW_INPUT_EXCEPTION = "show_input_exception"

    def __str__(self):
        return self.value
    
class DisplayKey(Enum):

    HELLO_TEXT = "hello"
    START_TEXT = "start"
    CONTROLS_TEXT = "controls"
    MENU_OPTIONS_TEXT = "menu_options"
    MAP_TEXT = "map"
    EXIT_MENU_TEXT = "exit_menu"
    EXIT_CONFIRMED_TEXT = "exit_confirmed"
    MOVE_TEXT = "move"
    WALL_TEXT = "wall"
    INFRONT_DOOR_TEXT = "infront_door"
    ROOM_ENTRANCE_TEXT = "room_entrance"
    INPUT_EXCEPTION_TEXT = "input_exception"

class OutputFunction(Enum):

    SHOW_MENU_OPTION = auto()