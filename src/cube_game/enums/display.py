from enum import Enum, auto

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