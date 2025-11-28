from enums.states import DisplayState
from enums.routing import RouterSignal

router_signal = {
            DisplayState.NAVIGATION: RouterSignal.NAVIGATION_FUNCTION,
            DisplayState.MAP: RouterSignal.MAP_FUNCTION,
            DisplayState.SHUFFLE_MAP: RouterSignal.SHUFFLE_FUNCTION,
        }