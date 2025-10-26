import readchar
import shutil
from enums import GameState, Directions, RoomColor, Command

class Utility:

    def __init__(self) -> None:
        self.columns, self.rows = shutil.get_terminal_size()

    # Gibt in einer übersicht alle Steuerungen aus
    # Wenn kein state übergeben wurde, werden alle möglichen Eingaben ausgegeben
    def print_dict(self, dictname : dict, key = None):
        
        # Wenn ein state vorhanden ist
        if key:
            # Gebe alle child Daten des parent keys aus
            for key, value in dictname[key].items():
                key_str = str(getattr(key, "value", key))
                self.centered(f"[{key_str.upper()}] {value}")
            self.print_dividing_line()
        else:
            # Ansonsten gebe alle Daten des dict aus
            for key, value in dictname.items():
                key_str = str(getattr(key, "value", key))
                print(f"\n[{key_str}]")
                for key, description in value.items():
                    key_str = str(getattr(key, "value", key))
                    print(f"[{key_str.upper()}] {description}")
            self.print_dividing_line()
    
    def centered(self, text: str):
        print(text.center(self.columns))
    
    def print_dividing_line(self):
        print(f"_"*self.columns,"\n")