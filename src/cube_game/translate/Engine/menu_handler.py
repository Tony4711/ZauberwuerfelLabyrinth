from enums.handler import MenuOptionHandler
from enums.commands import Command
from enums.states import GameState, MenuState

menuOption = {
    MenuOptionHandler.MAIN: {
        Command.OP1: GameState.PLAYING,
        Command.OP2: MenuState.EXIT,
        Command.OP3: MenuState.ALL_NAVIGATIONS
    },
    MenuOptionHandler.EXIT: {
        Command.OP1: GameState.EXIT,
        Command.OP2: GameState.BACK 
    }
}
