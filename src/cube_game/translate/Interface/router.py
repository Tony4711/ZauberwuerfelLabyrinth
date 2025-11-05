from enums import RouterSignal, DisplayStrings, DisplayMenuStructure, DisplayControls

def init(interface):
    return{
        RouterSignal.SHOW_MENU_OPTIONS: DisplayMenuStructure.MENU_OPTION,
        RouterSignal.SHOW_CONTROLS: DisplayControls.CONTROLS,
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
        RouterSignal.SHOW_ALL_CONTROLS: DisplayControls.ALL_CONTROLS
    }


