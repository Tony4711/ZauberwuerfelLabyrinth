from enums import GameState, Command
from interface import Interface
from mapping import mapping
from utility import Utility

class Controls:

 
    def __init__(self, StateManager):
        self.interface = Interface(StateManager)
        self.utility = Utility()
    
    def process_input(self,  state: GameState, isGlobal: False):
        input = self.interface.read_input()
        self.interface.write_input(input.upper())
        # parse self.input to self.command
        command = self._get_command_from_input(input)
        if command is None:
            return self._input_exception(state, command, isGlobal)
        else:
            valid_command = self._state_trooper(state, command, isGlobal)
            return valid_command
    
    def _get_command_from_input(self, input: str):
        for command in Command:
            if command.value == input:
                return command
        return None
    
    def _state_trooper(self, state, command, isGlobal) -> str:
        while not self._is_valid_for_state(state, command):
            if isGlobal and self._is_valid_for_state(GameState.GLOBAL_CONTROLS, command):
                return command
            else:
                command = self._input_exception(state, command, isGlobal)
        return command
    
    # Prüft ob im aktuellen state der Input im dict 'mapping' vorhanden ist
    # Gibt dementsprechend True oder False zurück
    def _is_valid_for_state(self, state, command) -> bool:
        if command in mapping[state].keys():              
            return True                                 
        else:
            return False
        
    # Gibt alle values eines dicts anhand des keys 'state' zuück
    def get_commands_for_state(self, dict, state) -> dict[str, str]:
        return dict.get(state)
    
    # Fehlermeldung für ungültige Eingaben
    def _input_exception(self, state, command, isGlobal):
        self.utility.centered(f"--- Ungültige Eingabe. Bitte nutze: ---\n" )
        self.utility.print_dict(mapping, state)
        command = self.process_input(state, isGlobal)
        return command