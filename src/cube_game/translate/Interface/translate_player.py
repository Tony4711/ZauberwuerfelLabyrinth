from enums.states import PlayerState
from enums.routing import RouterSignal

playerState_routerSignal = {
    PlayerState.MOVE: RouterSignal.SHOW_MOVE,
    PlayerState.WALL: RouterSignal.SHOW_WALL,
    PlayerState.DOOR: RouterSignal.SHOW_INFRONT_DOOR,
    PlayerState.GO_DOOR: RouterSignal.SHOW_ROOM_ENTRANCE
}
