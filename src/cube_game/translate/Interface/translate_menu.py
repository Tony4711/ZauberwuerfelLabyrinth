from enums import MenuState, RouterSignal

menuState_routerSignal = {
    MenuState.MAIN: RouterSignal.SHOW_MENU_OPTIONS,
    MenuState.CONTROLS: RouterSignal.SHOW_CONTROLS,
    MenuState.EXIT: RouterSignal.SHOW_EXIT_MENU,
    MenuState.SETTINGS: RouterSignal.SHOW_MENU_OPTIONS,
    MenuState.MAP: RouterSignal.SHOW_MAP
}