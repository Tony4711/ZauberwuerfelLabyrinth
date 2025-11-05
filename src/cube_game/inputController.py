from enums import Command, GameState, MenuState
from interface import Interface
from mapping import state_command_mapping
from utility import Utility

class InputController:


    def __init__(self, StateController):
        self.utility = Utility()
        self.mapping = state_command_mapping.mapping
    
    def read_input(self):
        from readchar import readkey, key
        input = readkey().lower().strip()
        return input
    
    def write_input(self, text):
        print(f"Eingabe: [{text}]\n".rjust(self.utility.columns))
    
    def process_input(self,  gameState: GameState, menuState: MenuState):
        input = self.read_input()
        self.write_input(input.upper())
        # parse self.input to self.command
        command = self._get_command_from_input(input)
        valid_command = self._state_trooper(gameState, menuState, command)
        return valid_command
    
    def _get_command_from_input(self, input: str):
        for command in Command:
            if command.value == input:
                return command
        return None
    
    def _state_trooper(self, gameState, menuState, command) -> str:
        if gameState == GameState.MENU:
            if self._is_valid_for_menuState(menuState, command):
                return command
        else: 
            if self._is_valid_for_gameState(gameState, command):
                return command
        return None

    
    # Prüft ob im aktuellen state der Input im dict 'mapping' vorhanden ist
    # Gibt dementsprechend True oder False zurück
    def _is_valid_for_menuState(self, menuState, command) -> bool:
        if command in self.mapping[MenuState][menuState]:              
            return True                                 
        else:
            return False
    
    def _is_valid_for_gameState(self, gameState, command) -> bool:
        if command in self.mapping[GameState][gameState].keys():              
            return True                                 
        else:
            return False
        
    # Gibt alle values eines dicts anhand des keys 'state' zuück
    def get_commands_for_state(self, dict, state) -> dict[str, str]:
        return dict.get(state)