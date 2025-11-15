from enums.handler import MenuOptionHandler
from enums.commands import Command
from enums.states import GameState, MenuState, DisplayState

menu_option = {
    MenuOptionHandler.MAIN: {
        Command.OP1: GameState.PLAYING,
        Command.OP2: MenuState.EXIT,
        Command.OP3: DisplayState.NAVIGATION
    },
    MenuOptionHandler.EXIT: {
        Command.OP1: GameState.EXIT,
        Command.OP2: GameState.BACK 
    }
}

