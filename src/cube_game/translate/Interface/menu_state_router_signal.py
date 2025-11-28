from enums.states import MenuState, DisplayState
from enums.routing import RouterSignal

router_signal = {
    MenuState.MAIN: RouterSignal.SHOW_MAIN_MENU,
    MenuState.EXIT: RouterSignal.SHOW_EXIT_MENU,
}

