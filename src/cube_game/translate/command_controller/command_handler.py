from enums.commands import Command
from enums.states import MenuState, GameState, DisplayFunction
from enums.handler import CommandHandler, MenuOptionHandler, MovementHandler

def handler():

    return {
    CommandHandler.META_COMMAND: {
        Command.NAVIGATION: DisplayFunction.NAVIGATION,
        Command.OPEN_MAP: DisplayFunction.MAP,
        Command.BACK: GameState.BACK,
        Command.EXIT: MenuState.EXIT,
        Command.SHUFFLE_MAP: DisplayFunction.SHUFFLE_MAP,
        Command.INVENTORY: DisplayFunction.INVENTORY,
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

