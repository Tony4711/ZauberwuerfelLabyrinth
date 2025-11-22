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
            Command.MOVE_FORWARD, 
            Command.MOVE_BACK
        )                       : MovementHandler.MOVE,
        (
            Command.TURN_LEFT,
            Command.TURN_RIGHT
        )                       : MovementHandler.TURN
    }
}    

