from enums import MenuOptionHandler, Command, GameState, MenuState

menuOption = {
    MenuOptionHandler.MAIN: {
        Command.OP1: GameState.PLAYING,
        Command.OP2: MenuState.EXIT,
        Command.OP3: MenuState.ALL_NAVIGATIONS
    },
    MenuOptionHandler.EXIT: {
        Command.ACCEPT: GameState.EXIT,
        Command.DENIE: GameState.BACK 
    }
}