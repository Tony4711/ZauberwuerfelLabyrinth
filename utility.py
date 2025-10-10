import readchar
#from controls import Controls

class Utility:

    def __init__(self, controls):
        self.controls = controls
        #self.state = state

    def read_input(self):
        from readchar import readkey, key
        self.input = readkey().lower().strip()

    def validate_input(self):
        while not self.validate_mapping():
            self.input_exception()
            self.input = self.read_input()
        return self.input
    
    def process_input(self, state = None):
        self.state = state
        self.read_input()
        self.write_input(self.input.upper()) 
        self.valid_input = self.validate_input()
        return self.valid_input
            
    def write_input(self, text):
        print("\nEingabe: [" + text + "]\n")

    # Prüft ob im aktuellen state der Input im dict 'mapping' vorhanden ist
    # Gibt dementsprechend True oder False zurück
    def validate_mapping(self):
        if self.input in self.controls.get_dict("mapping")[self.state].keys():              
            return True                                 
        else:
            return False  
    
    # 
    def return_valid_inputs(self, dict, state):
        return dict.get(state)

    # Fehlermeldung für ungültige Eingaben
    def input_exception(self):
        print("--- Ungültige Eingabe. Bitte nutze: ---\n" )
        self.controls.get_dict("mapping")[self.state].items()

    # Gibt in einer übersicht alle Steuerungen aus
    # Wenn kein state übergeben wurde, werden alle möglichen Eingaben ausgegeben
    def print_dict(self, dictname : dict, state = None):
        
        # Wenn ein state vorhanden ist
        if state:
            # Gebe alle child Daten des parent keys aus
            for state_str, input_descr in dictname[state].items():
                print(f"[{state_str.upper()}] {input_descr}")
            print("________________________________________")
        else:
            # Ansonsten gebe alle Daten des dict aus
            for state_str, input_descr in dictname.items():
                print(f"\n[{state_str.upper()}]")
                for key, description in input_descr.items():
                    print(f"[{key.upper()}] {description}")
            print("________________________________________")
