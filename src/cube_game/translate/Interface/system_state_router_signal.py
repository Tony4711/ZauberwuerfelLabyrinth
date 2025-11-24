from enums.states import SystemState
from enums.routing import RouterSignal

router_signal = {
    SystemState.EXCEPTION_INPUT_ERROR: RouterSignal.SHOW_INPUT_EXCEPTION
}
