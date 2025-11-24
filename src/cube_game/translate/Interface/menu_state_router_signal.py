from enums.states import MenuState, DisplayState
from enums.routing import RouterSignal

router_signal = {
    MenuState.MAIN: RouterSignal.SHOW_MAIN_MENU,
    DisplayState.NAVIGATION: RouterSignal.SHOW_NAVIGATION,
    MenuState.EXIT: RouterSignal.SHOW_EXIT_MENU,
    DisplayState.MAP: RouterSignal.SHOW_MAP,
}

