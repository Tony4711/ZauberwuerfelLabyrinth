from enums import Command, MovementHandler

def handler(engine):
    
    return {
        MovementHandler.MOVE_STRAIGHT: engine.move_straight
    }