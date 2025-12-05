from enums.states import PlayerState
from enums.routing import RouterSignal

router_signal = {
    PlayerState.MOVE: RouterSignal.SHOW_MOVE,
    PlayerState.TURN: RouterSignal.SHOW_TURN,
    PlayerState.WALL: RouterSignal.SHOW_WALL,
    PlayerState.INTERACTION: RouterSignal.SHOW_INTERACTION,
}
