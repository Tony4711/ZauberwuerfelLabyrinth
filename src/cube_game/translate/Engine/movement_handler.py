from enums.commands import Command
from enums.handler import MovementHandler

def handler(engine):
    
    return {
        MovementHandler.MOVE_STRAIGHT: engine.move_straight
    }
