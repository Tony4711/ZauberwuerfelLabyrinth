from enums.routing import RouterSignal
from enums.handler import CommandHandler

router={
    RouterSignal.META_HANDLER: CommandHandler.META_COMMAND,
    RouterSignal.MOVEMENT_HANDLER: CommandHandler.MOVEMENT_COMMAND,
    RouterSignal.OPTION_HANDLER: CommandHandler.OPTION_COMMAND
}

