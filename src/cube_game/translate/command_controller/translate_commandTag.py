from enums.commands import CommandTag
from enums.routing import RouterSignal

commandtag_router_signal = {
    CommandTag.META: RouterSignal.META_HANDLER,
    CommandTag.MOVEMENT:RouterSignal.MOVEMENT_HANDLER, 
    CommandTag.OPTION: RouterSignal.OPTION_HANDLER,
    
}

