from enum import Enum, auto

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
    

