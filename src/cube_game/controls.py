from enums import Command, GameState, MenuState
from interface import Interface
from mapping import mapping
from utility import Utility

class Controls:

 
    def __init__(self, StateManager):
        self.interface = Interface(StateManager)
        self.utility = Utility()
    
    def process_input(self,  gameState: GameState, menuState: MenuState, isGlobal: False):
        input = self.interface.read_input()
        self.interface.write_input(input.upper())
        # parse self.input to self.command
        command = self._get_command_from_input(input)
        if command is None:
            return self._input_exception(gameState, command, isGlobal)
        else:
            valid_command = self._state_trooper(gameState, menuState, command, isGlobal)
            return valid_command
    
    def _get_command_from_input(self, input: str):
        for command in Command:
            if command.value == input:
                return command
        return None
    
    def _state_trooper(self, gameState, menuState, command, isGlobal) -> str:
        if gameState == GameState.MENU:
            self._is_valid_for_menuState(menuState, command)
            return command
        while not self._is_valid_for_gameState(gameState, command):
            if isGlobal and self._is_valid_for_gameState(GameState.GLOBAL_CONTROLS, command):
                return command
            else:
                command = self._input_exception(gameState, command, isGlobal)
        return command
    
    # Prüft ob im aktuellen state der Input im dict 'mapping' vorhanden ist
    # Gibt dementsprechend True oder False zurück
    def _is_valid_for_menuState(self, menuState, command) -> bool:
        if command in mapping[GameState.MENU][menuState]:              
            return True                                 
        else:
            return False
    
    def _is_valid_for_gameState(self, gameState, command) -> bool:
        if command in mapping[gameState].keys():              
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