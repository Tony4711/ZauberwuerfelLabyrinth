from enums.commands import CommandTag
from enums.routing import RouterSignal

commandTag_routerSignal = {
    CommandTag.META: RouterSignal.META_HANDLER,
    CommandTag.MOVEMENT:RouterSignal.MOVEMENT_HANDLER, 
    CommandTag.OPTION: RouterSignal.OPTION_HANDLER,
    
}
