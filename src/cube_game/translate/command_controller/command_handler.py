from enums.commands import Command
from enums.states import MenuState, GameState, DisplayState
from enums.handler import CommandHandler, MenuOptionHandler, MovementHandler

def handler():

    return {
    CommandHandler.META_COMMAND: {
        Command.NAVIGATION: DisplayState.NAVIGATION,
        Command.OPEN_MAP: DisplayState.MAP,
        Command.BACK: GameState.BACK,
        Command.EXIT: MenuState.EXIT,
        Command.SHUFFLE_MAP: DisplayState.SHUFFLE_MAP,
    },
    CommandHandler.OPTION_COMMAND: {
        MenuState.MAIN: MenuOptionHandler.MAIN,
        MenuState.EXIT: MenuOptionHandler.EXIT 
    },
    CommandHandler.MOVEMENT_COMMAND: {
        (
            Command.MOVE_EAST, 
            Command.MOVE_NORTH, 
            Command.MOVE_SOUTH, 
            Command.MOVE_WEST
        )                       : MovementHandler.MOVE_STRAIGHT
    }
}
    

