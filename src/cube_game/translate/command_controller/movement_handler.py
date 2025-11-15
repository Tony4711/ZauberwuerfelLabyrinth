from enums.commands import Command
from enums.handler import MovementHandler

def handler(game_context):
    
    return {
        MovementHandler.MOVE_STRAIGHT: game_context.engine.move_straight
    }

