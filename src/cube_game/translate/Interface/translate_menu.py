from enums import MenuState, RouterSignal

menuState_routerSignal = {
    MenuState.MAIN: RouterSignal.SHOW_MENU_OPTIONS,
    MenuState.NAVIGATION: RouterSignal.SHOW_NAVIGATION,
    MenuState.EXIT: RouterSignal.SHOW_EXIT_MENU,
    MenuState.SETTINGS: RouterSignal.SHOW_MENU_OPTIONS,
    MenuState.MAP: RouterSignal.SHOW_MAP,
    MenuState.ALL_NAVIGATIONS: RouterSignal.SHOW_ALL_NAVIGATION
}