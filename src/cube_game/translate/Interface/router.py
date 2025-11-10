from enums.routing import RouterSignal
from enums.display import DisplayStrings, DisplayMenuStructure, DisplayNavigation


routing = {
        RouterSignal.SHOW_MENU_OPTIONS: DisplayMenuStructure.MENU_OPTION,
        RouterSignal.SHOW_NAVIGATION: DisplayNavigation.NAVIGATION,
        RouterSignal.SHOW_EXIT_MENU: DisplayStrings.EXIT_MENU_TEXT,
        RouterSignal.SHOW_HELLO: DisplayStrings.HELLO_TEXT,
        RouterSignal.SHOW_START: DisplayStrings.START_TEXT,
        RouterSignal.SHOW_EXIT_CONFIRMED: DisplayStrings.EXIT_CONFIRMED_TEXT,
        RouterSignal.SHOW_MAP: DisplayStrings.MAP_TEXT,
        RouterSignal.SHOW_MOVE: DisplayStrings.MOVE_TEXT,
        RouterSignal.SHOW_WALL: DisplayStrings.WALL_TEXT,
        RouterSignal.SHOW_INFRONT_DOOR: DisplayStrings.INFRONT_DOOR_TEXT,
        RouterSignal.SHOW_ROOM_ENTRANCE: DisplayStrings.ROOM_ENTRANCE_TEXT,
        RouterSignal.SHOW_INPUT_EXCEPTION: DisplayStrings.INPUT_EXCEPTION_TEXT,
        RouterSignal.SHOW_ALL_NAVIGATION: DisplayNavigation.ALL_NAVIGATION
    }


