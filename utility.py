import readchar
import shutil
from enums import GameState, Directions, RoomColor, Command

class Utility:

    def __init__(self, controls) -> None:
        self.controls = controls
        self.columns, self.rows = shutil.get_terminal_size()
    
    def process_input(self,  state: GameState, isGlobal: False):
        input = self.read_input()
        self.write_input(input.upper())
        # parse self.input to self.command
        command = self.get_command_from_input(input)
        if command is None:
            return self.input_exception(state, command, isGlobal)
        else:
            valid_command = self.state_trooper(state, command, isGlobal)
            return valid_command
    
    def read_input(self) -> None:
        from readchar import readkey, key
        input = readkey().lower().strip()
        return input
    
    def write_input(self, text) -> None:
        
        print("Eingabe: [" + text + "]\n")
    
    def get_command_from_input(self, input: str):
        for command in Command:
            if command.value == input:
                return command
        return None


    def state_trooper(self, state, command, isGlobal) -> str:
        while not self.is_valid_for_state(state, command):
            if isGlobal and self.is_valid_for_state(GameState.GLOBAL_CONTROLS, command):
                return command
            else:
                command = self.input_exception(state, command, isGlobal)
        return command

    # Prüft ob im aktuellen state der Input im dict 'mapping' vorhanden ist
    # Gibt dementsprechend True oder False zurück
    def is_valid_for_state(self, state, command) -> bool:
        if command in self.controls.get_dict("mapping")[state].keys():              
            return True                                 
        else:
            return False  
    
    # Gibt alle values eines dicts anhand des keys 'state' zuück
    def get_commands_for_state(self, dict, state) -> dict[str, str]:
        return dict.get(state)

    # Fehlermeldung für ungültige Eingaben
    def input_exception(self, state, command, isGlobal):
        print(f"{'--- Ungültige Eingabe. Bitte nutze: ---\n':^64}" )
        self.print_dict(self.controls.get_dict("mapping"), state)
        command = self.process_input(state, isGlobal)
        return command

    # Gibt in einer übersicht alle Steuerungen aus
    # Wenn kein state übergeben wurde, werden alle möglichen Eingaben ausgegeben
    def print_dict(self, dictname : dict, key = None):
        
        # Wenn ein state vorhanden ist
        if key:
            # Gebe alle child Daten des parent keys aus
            for key, value in dictname[key].items():
                key_str = str(getattr(key, "value", key))
                print(f"[{key_str.upper()}] {value}")
            #print("________________________________________________________________\n")
            self.print_dividing_line()
        else:
            # Ansonsten gebe alle Daten des dict aus
            for key, value in dictname.items():
                key_str = str(getattr(key, "value", key))
                print(f"\n[{key_str}]")
                for key, description in value.items():
                    key_str = str(getattr(key, "value", key))
                    print(f"[{key_str.upper()}] {description}")
            #print("________________________________________________________________\n")
            self.print_dividing_line()

    def _lookup_neighbor(self, room, direction):
        target = room.neighbors.get(direction)
        if target is None:
            return None
        return target


    
    def print_map(self, room, map : dict):
       front = room.color
       left = self._lookup_neighbor(room, Directions.WEST)
       right = self._lookup_neighbor(room, Directions.EAST)
       up = self._lookup_neighbor(room, Directions.NORTH)
       down = self._lookup_neighbor(room, Directions.SOUTH)
       back = self._lookup_neighbor(map.get(right), Directions.EAST)

       print(f"              [{map.get(up).name}]") 
       print(f"[{map.get(left).name}][{map.get(front).name}][{map.get(right).name}][{map.get(back).name}]")
       print(f"              [{map.get(down).name}]\n")
       #print("________________________________________________________________\n")
       self.print_dividing_line()

    def print_pos(self, text, objekt):
        print(text, objekt.pos)

    def print_dividing_line(self):
        print(f"_"*self.columns,"\n")