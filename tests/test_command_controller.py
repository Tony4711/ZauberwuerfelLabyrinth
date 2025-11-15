from cube_game.core.gamecontext import GameContext
from cube_game.enums.commands import Command
from cube_game.enums.states import PlayerState

def test_command_controller_returns_move_method():
    gc = GameContext()

    command = Command.MOVE_EAST
    gc.command_controller.command_handler(command)

    assert PlayerState.MOVE