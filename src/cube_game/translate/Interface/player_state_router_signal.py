from enums.states import PlayerState
from enums.routing import RouterSignal

router_signal = {
    PlayerState.MOVE: RouterSignal.SHOW_MOVE,
    PlayerState.TURN: RouterSignal.SHOW_TURN,
    PlayerState.WALL: RouterSignal.SHOW_WALL,
    PlayerState.DOOR: RouterSignal.SHOW_INFRONT_DOOR,
    PlayerState.ENTER_ROOM: RouterSignal.SHOW_ROOM_ENTRANCE,
    PlayerState.BLOCKED: RouterSignal.SHOW_CLOSED,
    PlayerState.DOOR_UNLOCKED: RouterSignal.SHOW_DOOR_UNLOCKED,
}
