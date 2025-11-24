from enums.commands import Command
from enums.states import GameState, MenuState
from mapping import state_command

class InputController:


    def __init__(self, game_context):
        self.game_context = game_context
        self.mapping = state_command.mapping
    
    def read_input(self):
        from readchar import readkey, key
        input = readkey().lower().strip()
        return input
    
    def write_input(self, text):
        print(f"Eingabe: [{text}]\n".rjust(self.game_context.utility.columns))
    
    def process_input(self):
        input = self.read_input()
        #self.write_input(input.upper())
        # parse self.input to self.command
        command = self._get_command_from_input(input)
        valid_command = self._state_trooper( command)
        return valid_command
    
    def _get_command_from_input(self, input: str):
        for command in Command:
            if command.value == input:
                return command
        return None
    
    def _state_trooper(self, command) -> str:
        game_state = self.game_context.state_controller.game_stack._current_state_stack()
        menu_state = self.game_context.state_controller.menu_stack._current_state_stack()
        if game_state == game_state.MENU:
            if self._is_valid_for_menu_state(menu_state, command):
                return command
        else: 
            if self._is_valid_for_game_state(game_state, command):
                return command
        return None

    
    # Prüft ob im aktuellen state der Input im dict 'mapping' vorhanden ist
    # Gibt dementsprechend True oder False zurück
    def _is_valid_for_menu_state(self, menu_state, command) -> bool:
        if command in self.mapping[type(menu_state)][menu_state]:              
            return True                                 
        else:
            return False
    
    def _is_valid_for_game_state(self, game_state, command) -> bool:
        if command in self.mapping[type(game_state)][game_state].keys():              
            return True                                 
        else:
            return False
        
    # Gibt alle values eines dicts anhand des keys 'state' zuück
    def get_commands_for_state(self, dict, state) -> dict[str, str]:
        return dict.get(state)

