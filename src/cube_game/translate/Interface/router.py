from enums import RouterSignal, DisplayKey, OutputFunction

def init(interface):
    return{
        RouterSignal.SHOW_MENU_OPTIONS: OutputFunction.SHOW_MENU_OPTION,
        RouterSignal.SHOW_CONTROLS: DisplayKey.CONTROLS_TEXT,
        RouterSignal.SHOW_EXIT_MENU: DisplayKey.EXIT_MENU_TEXT,
        RouterSignal.SHOW_HELLO: DisplayKey.HELLO_TEXT,
        RouterSignal.SHOW_START: DisplayKey.START_TEXT,
        RouterSignal.SHOW_EXIT_CONFIRMED: DisplayKey.EXIT_CONFIRMED_TEXT,
        RouterSignal.SHOW_MAP: DisplayKey.MAP_TEXT,
        RouterSignal.SHOW_MOVE: DisplayKey.MOVE_TEXT,
        RouterSignal.SHOW_WALL: DisplayKey.WALL_TEXT,
        RouterSignal.SHOW_INFRONT_DOOR: DisplayKey.INFRONT_DOOR_TEXT,
        RouterSignal.SHOW_ROOM_ENTRANCE: DisplayKey.ROOM_ENTRANCE_TEXT,
        RouterSignal.SHOW_INPUT_EXCEPTION: DisplayKey.INPUT_EXCEPTION_TEXT
    }


