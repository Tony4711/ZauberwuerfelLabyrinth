from enums.commands import Command
from enums.states import GameState, MenuState
from mapping import state_command

class InputController:


    # Initialize input controller with game context and command mapping.
    def __init__(self, game_context):
        self.game_context=game_context
        self.mapping=state_command.mapping
    
    # Read raw keyboard input and normalize it.
    def read_input(self):
        from readchar import readkey, key
        input=readkey().lower().strip()
        return input
    
    # Print formatted input echo to output.
    def write_input(self, text):
        print(f"Eingabe: [{text}]\n".rjust(self.game_context.utility.columns))
    
    # Convert raw input to validated command based on current state.
    def process_input(self):
        input=self.read_input()
        #self.write_input(input.upper())
        # parse self.input to self.command
        command=self._get_command_from_input(input)
        valid_command=self._state_trooper( command)
        return valid_command
    
    # Translate raw string input into Command enum if applicable.
    def _get_command_from_input(self, input: str):
        for command in Command:
            if command.value==input:
                return command
        return None
    
    # Validate a command against current game or menu state.
    def _state_trooper(self, command) -> str:
        game_state=self.game_context.state_controller.game_stack._current_state_stack()
        menu_state=self.game_context.state_controller.menu_stack._current_state_stack()
        if game_state==game_state.MENU:
            if self._is_valid_for_menu_state(menu_state, command):
                return command
        else: 
            if self._is_valid_for_game_state(game_state, command):
                return command
        return None

    
    # PrǬft ob im aktuellen state der Input im dict 'mapping' vorhanden ist
    # Gibt dementsprechend True oder False zurǬck
    # Check whether command is allowed in the current menu state.
    def _is_valid_for_menu_state(self, menu_state, command) -> bool:
        if command in self.mapping[type(menu_state)][menu_state]:              
            return True                                 
        else:
            return False
    
    # Check whether command is allowed in the current game state.
    def _is_valid_for_game_state(self, game_state, command) -> bool:
        if command in self.mapping[type(game_state)][game_state].keys():              
            return True                                 
        else:
            return False
        
    # Gibt alle values eines dicts anhand des keys 'state' zuǬck
    # Return all commands mapped to a given state.
    def get_commands_for_state(self, dict, state) -> dict[str, str]:
        return dict.get(state)
