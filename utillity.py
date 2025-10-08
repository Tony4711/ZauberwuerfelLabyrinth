import readchar
from controls import Controls

class Utility:

    def __init__(self):
        self.controls = Controls()

    def read_input(self):
        from readchar import readkey, key
        self.input = readkey().lower().strip()

    def validate_input(self):
        while not self.validate_mapping():
            self.input_exception()
            self.input = self.validate_input()
    
    def process_input(self):
        self.read_input()
        self.write_input(self.input.upper()) 
        self.validate_input()
        self.input = self.valid_input

    def get_valid_input(self):
        return self.valid_input
    
    def write_input(self, text):
        print("\nEingabe: [" + text + "]\n")

    # Prüft ob im aktuellen state der Input im dict 'mapping' vorhanden ist
    # Gibt dementsprechend True oder False zurück
    def validate_mapping(self):
        if self.input in self.controls.get_dict("mapping")[self.state].key():              
            return True                                 
        else:
            return False  
    
    # 
    def return_valid_inputs(dict, state):
        return dict.get(state)

    # Fehlermeldung für ungültige Eingaben
    def input_exception(self):
        print("--- Ungültige Eingabe. Bitte nutze: ---\n" )
        self.controls.get_dict("mapping")[self.state].items()

    # Gibt in einer übersicht alle Steuerungen aus
    # Wenn kein state übergeben wurde, werden alle möglichen Eingaben ausgegeben
    def print_dict(self, dictname, state = None):
        # Ruft einmal das über dictname Parameter gewählte dict auf uns speichert es in data
        data = self.controls.get_dict(dictname)

        # Wenn ein state vorhanden ist
        if state:
            # Gebe alle child Daten des parent keys aus
            for state_str, input_descr in data[state].items():
                print(f"[{state_str.upper()}] {input_descr}")
            print("________________________________________")
        else:
            # Ansonsten gebe alle Daten des dict aus
            for state_str, input_descr in data.items():
                print(f"\n[{state_str.upper()}]")
                for key, description in data(dictname).items():
                    print(f"[{key.upper()}] {description}")
            print("________________________________________")
