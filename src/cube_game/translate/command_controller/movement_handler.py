from enums.handler import MovementHandler

def handler(game_context):
    
    return {
        MovementHandler.MOVE: game_context.player_movement.move_player,
        MovementHandler.TURN: game_context.player_movement.turn_player
    }

