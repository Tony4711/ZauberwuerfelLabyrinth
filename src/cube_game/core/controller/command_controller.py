from enums.handler import CommandHandler
from enums.states import GameState, SystemState

class CommandController:

    def __init__(self, game_context):
        self.game_context = game_context

    def get_command(self):
        return self.game_context.input_controller.process_input()

    # Use of different levels of dicts to process command logic.
    # Begins with sorting the command by commandTag, which divides comments into categories.
    def command_handler(self, command):
        # Retrieve a signal from dict whichs matches with the command tag
        signal = self.game_context.commandtag_to_signal.get(command.tag)
        # Use that signal to get the key for the next dict
        handler_key = self.game_context.command_router.get(signal)
        # handlerKey is now a command interpret by its tag which than got forwarded by a router to handle the command based on its categorie
        # How it gets handled is stored by an Enum which gets interpret below
        command_handler_key = self.game_context.command_handler.get(handler_key)
        if handler_key == CommandHandler.META_COMMAND:
            return command_handler_key[command]
        if handler_key == CommandHandler.OPTION_COMMAND:
            # Get current MenuState and store as key
            menu_state_key = self.game_context.state_controller.menu_stack._current_state_stack()
            # Use MenuState as key for command handler dict
            # Store value as key for menu handler dict
            menu_handler_key = command_handler_key[menu_state_key]
            # Use that key and command to access menu handler dict to return corresponding state
            return self.game_context.menu_handler[menu_handler_key][command]
        # If it is a movement command the dict returns a tuple of movement commands with another key for next level dict to interpret the movement
        if handler_key == CommandHandler.MOVEMENT_COMMAND:
            for command_tuple, handler in command_handler_key.items():
                if command in command_tuple:
                    movement_key = handler
            # This key is then used to return a callable of move_player method
            handler = self.game_context.movement_handler.get(movement_key)
            # Call move method with command
            return handler(command)
        
    def process_command(self):
        if self.game_context.state_controller.game_stack._current_state_stack() == GameState.INIT:
            return GameState.INIT
        command = self.get_command()
        if command:
            return self.command_handler(command)
        else:
            return SystemState.EXCEPTION_INPUT_ERROR
