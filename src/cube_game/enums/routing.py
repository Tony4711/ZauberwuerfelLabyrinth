from enum import Enum, auto

class RouterSignal(Enum):

    SHOW_HELLO = auto()
    SHOW_START = auto()
    SHOW_NAVIGATION = auto()
    SHOW_MAIN_MENU = auto()
    SHOW_MAP = auto()
    SHOW_EXIT_MENU = auto()
    SHOW_EXIT_CONFIRMED = auto()
    SHOW_MOVE = auto()
    SHOW_TURN = auto()
    SHOW_WALL = auto()
    SHOW_INFRONT_DOOR = auto() 
    SHOW_ROOM_ENTRANCE = auto()
    SHOW_INPUT_EXCEPTION = auto()
    SHOW_HOWTO = auto()
    META_HANDLER = auto()
    MOVEMENT_HANDLER = auto()
    OPTION_HANDLER = auto()
    NAVIGATION_FUNCTION = auto()
    MAP_FUNCTION = auto()
    SHUFFLE_FUNCTION = auto()
    

