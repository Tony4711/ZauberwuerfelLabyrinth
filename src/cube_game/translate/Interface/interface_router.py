from enums.routing import RouterSignal
from enums.display import Display, DisplayNavigation
from enums.menus import Menus

routing = {
        RouterSignal.SHOW_MAIN_MENU: Menus.MAIN,
        RouterSignal.SHOW_EXIT_MENU: Menus.EXIT,
        RouterSignal.SHOW_MAP: Display.MAP_TEXT,
        RouterSignal.SHOW_NAVIGATION: DisplayNavigation.NAVIGATION,
        RouterSignal.SHOW_HELLO: Display.HELLO_TEXT,
        RouterSignal.SHOW_START: Display.START_TEXT,
        RouterSignal.SHOW_EXIT_CONFIRMED: Display.EXIT_CONFIRMED_TEXT,
        RouterSignal.SHOW_MOVE: Display.MOVE_TEXT,
        RouterSignal.SHOW_WALL: Display.WALL_TEXT,
        RouterSignal.SHOW_INFRONT_DOOR: Display.INFRONT_DOOR_TEXT,
        RouterSignal.SHOW_ROOM_ENTRANCE: Display.ROOM_ENTRANCE_TEXT,
        RouterSignal.SHOW_INPUT_EXCEPTION: Display.INPUT_EXCEPTION_TEXT,
        RouterSignal.SHOW_ALL_NAVIGATION: DisplayNavigation.ALL_NAVIGATION
    }



