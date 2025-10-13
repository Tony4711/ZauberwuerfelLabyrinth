import readchar
from enums import GameState

class Utility:

    def __init__(self, controls) -> None:
        self.controls = controls
    
    def process_input(self, state = None) -> str:
        self.read_input()
        self.write_input(self.input.upper()) 
        self.valid_input = self.validate_input(state)
        return self.valid_input
    
    def read_input(self) -> None:
        from readchar import readkey, key
        self.input = readkey().lower().strip()
    
    def write_input(self, text) -> None:
        print("Eingabe: [" + text + "]\n")

    def validate_input(self, state = None) -> str:
        while not self.validate_mapping(state):
            self.input_exception(state)
            self.input = self.process_input(state)
        return self.input

    # Prüft ob im aktuellen state der Input im dict 'mapping' vorhanden ist
    # Gibt dementsprechend True oder False zurück
    def validate_mapping(self, state = None) -> bool:
        if self.input in self.controls.get_dict("mapping")[state].keys():              
            return True                                 
        else:
            return False  
    
    # 
    def return_valid_inputs(self, dict, state) -> dict[str, str]:
        return dict.get(state)

    # Fehlermeldung für ungültige Eingaben
    def input_exception(self, state):
        print("--- Ungültige Eingabe. Bitte nutze: ---\n" )
        #self.controls.get_dict("mapping")[state].items()
        self.print_dict(self.controls.get_dict("mapping"), state)

    # Gibt in einer übersicht alle Steuerungen aus
    # Wenn kein state übergeben wurde, werden alle möglichen Eingaben ausgegeben
    def print_dict(self, dictname : dict, key = None):
        
        # Wenn ein state vorhanden ist
        if key:
            # Gebe alle child Daten des parent keys aus
            for key, value in dictname[key].items():
                key_str = str(getattr(key, "value", key))
                print(f"[{key_str.upper()}] {value}")
            print("________________________________________\n")
        else:
            # Ansonsten gebe alle Daten des dict aus
            for key, value in dictname.items():
                key_str = str(getattr(key, "value", key))
                print(f"\n[{key_str}]")
                for key, description in value.items():
                    key_str = str(getattr(key, "value", key))
                    print(f"[{key_str.upper()}] {description}")
            print("________________________________________\n")

    #wip   
    def print_map(self, map : dict):
        for rooms in map.items():
            print(rooms)
            
