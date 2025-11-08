from enums import RouterSignal, CommandHandler

routing = {
    RouterSignal.META_HANDLER: CommandHandler.META_COMMAND,
    RouterSignal.MOVEMENT_HANDLER: CommandHandler.MOVEMENT_COMMAND,
    RouterSignal.OPTION_HANDLER: CommandHandler.OPTION_COMMAND
}