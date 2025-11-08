from enums import GameState, RouterSignal, MenuState

gameState_routerSignal = {
    GameState.INIT: RouterSignal.SHOW_HELLO,
    GameState.PLAYING: RouterSignal.SHOW_START,
    GameState.EXIT: RouterSignal.SHOW_EXIT_CONFIRMED,
    
}
