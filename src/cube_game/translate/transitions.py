from enums import GameState, MenuState, Command, CommandTag

menuTrans = {
    (GameState.MENU, MenuState.MAIN,Command.OP1): GameState.PLAYING, 
    (GameState.MENU, MenuState.MAIN,Command.OP2): MenuState.EXIT,
    (GameState.MENU, MenuState.EXIT,Command.OP1): GameState.EXIT,
}

commandTrans = {
    (Command.CONTROLS): MenuState.CONTROLS,

}

commandTagTrans = {
}