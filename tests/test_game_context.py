from cube_game.core.game_context import GameContext

def test_game_context_initializes():
    gc = GameContext()

    # Sanity-Checks: existieren die zentralen Komponenten?
    assert gc.state_controller is not None
    assert gc.player_movement is not None
    assert gc.input_controller is not None
    assert gc.interface is not None
