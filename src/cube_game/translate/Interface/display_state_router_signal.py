from enums.states import DisplayFunction
from enums.routing import RouterSignal

router_signal = {
            DisplayFunction.NAVIGATION: RouterSignal.NAVIGATION_FUNCTION,
            DisplayFunction.MAP: RouterSignal.MAP_FUNCTION,
            DisplayFunction.SHUFFLE_MAP: RouterSignal.SHUFFLE_FUNCTION,
            DisplayFunction.INSTRUCTION: RouterSignal.SHOW_INSTRUCTION,
            DisplayFunction.INVENTORY: RouterSignal.INVENTORY_FUNCTION,
        }