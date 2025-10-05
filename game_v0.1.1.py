import sys
import readchar

# Ein Spiel zum Verstehen der Grundmechaniken eines Rubiks Würfels.
# Der kleine Zauberer Garry ist in einem 3 dimensionalem Labyrinth gefangen und muss die Räume richtig miteinander verbinden, um herauszufinden.
# Dabei stößt er auf verschiedenste Rätsel und Herausforderungen, die ihm Helfen, den Zauberwürfel zu verstehen.

class Game:

    def __init__(self):
        self.active = True
        self.state = "menu"
        self.last_input = ""
        self.init_controls()
        self.init_map()
        self.init_player()

    def init_player(self):
        self.player_pos = [2,2]

    def init_controls(self):
        self.valid_inputs = {
            "menu": {
                "1": "Option 1",
                "2": "Option 2",
                "3": "Option 3"
            },
            "navigation": {
                "q": "Zurück",
                "e": "Weiter"
            },
            "exit": {
                "J": "Ja",
                "N": "Nein"
            }  
        }
        
    def init_map(self):
        self.rooms = {
            "yellow_room": {
                "width": "6",
                "lentgh": "6",
                "position": "bottom",
                "name": "gelber Raum"
            },
            "white_room": {
                "width": "6",
                "lentgh": "6",
                "position": "top",
                "name": "weißer Raum"
            },
            "green_room": {"width": "6",
                "lentgh": "6",
                "position": "front",
                "name": "grüner Raum"
            },
            "red_room": {
                "width": "6",
                "lentgh": "6",
                "position": "right",
                "name": "roter Raum"
            },
            "blue_room": {
                "width": "6",
                "lentgh": "6",
                "position": "back",
                "name": "blauer Raum"
            },
            "orange_room": {
                "width": "6",
                "lentgh": "6",
                "position": "left",
                "name": "oranger Raum"
            }
        }

    def write_input(self, text):
        print("\nSpieler: [" + text + "]\n")

    # Liest den nächsten Tastendruck des Nutzers und speichert ihn in last_input
    # Schreibt den letzten Input in Großbuchstaben in die Konsole
    # Gibt den Inhalt von last_input zurück
    def get_input(self):
        from readchar import readkey, key
        self.last_input = readkey().lower().strip()     
        self.write_input(self.last_input.upper())       
        return self.last_input                          
                 
    # Prüft ob die Eingabe im Dictionary vorhanden ist und gibt dementsprechend True oder False zurück
    def check_input(self):
        if self.last_input in self.valid_inputs[self.state]:              
            return True                                 
        else:
            return False                                
    
    def show_valid_inputs(self):
        for key, description in self.valid_inputs[self.state].items():
            print(f"[{key.upper()}] {description}")
        print()
        self.choice = self.get_input()
        self.choice_handler()

    def show_all_inputs(self):
        for state_dict in self.valid_inputs.values():  # jedes innere Dict
            for key, desc in state_dict.items():
                print(f"[{key.upper()}] {desc}")
            
        print("")

    def input_exception(self):
        print("---Ungültige Eingabe. Bitte nutze die in [ ] geschriebene Taste zum steuern---")

    def hello(self):
        print("_____________________________________________________________")
        print("\n--- Willkommen zu 'Gefangen im Zauberwürfel Labyrinth'! ---")
        print("\n                   --- Hauptmenü ---")
        print("\n--- Zum steuern bitte die in [ ] geschriebene Taste drücken. ---\n")
        
    def show_menu_options(self):
        print("[1] Spiel starten")
        print("[2] Steuerung")
        print("[3] Spiel verlassen")

    def choice_handler(self):
            if self.choice == "1":
                self.state = "start"
            elif self.choice == "2":
                self.state = "navigation"
            elif self.choice == "3":
                self.state = "exit"

    def menu(self):
        self.hello()
        self.show_menu_options()
        self.choice = self.get_input()

        while not self.check_input():
            self.input_exception()
            self.choice = self.get_input()
        self.choice_handler()
        
    #nächste baustelle
    def start(self):
        print("---Spiel wird gestartet...---")
        self.init_map()
        self.get_input()#breakpoint damit die schleife pausiert
       
    def exit(self):
        print("---Spiel wirklich beenden? [J/N]---")
        self.choice = self.get_input()
        if self.last_input == "j":
            print("--- Spiel wird beendet... ---")
            sys.exit()
        elif self.last_input == "n":
            print("--- Ok, zurück zum Menu. ---\n")
            self.show_menu_options()
            self.choice = self.get_input()
            self.choice_handler()

    def move(self, direction):
        x, y = self.player_pos()
        
        if direction == "w" and y < 6 :
            y += 1
        elif direction == "s" and y > 0:
            y -= 1
        elif direction == "a" and x > 0:
            x -= 1 
        elif direction == "d" and x < 6:
            x += 1
        else:
            print("Du stößt gegen eine Wand!")
        self.player_pos = [x,y 
                           ]
            

        

    def run(self):
        while self.active:
            if self.state == "menu":
                self.menu()
            elif self.state == "start":
                self.start()
            elif self.state == "exit":
                self.exit()
            elif self.state == "navigation":
                self.show_all_inputs()
                self.choice = self.get_input()
                self.choice_handler()

if __name__ == "__main__":
    game = Game()
    game.run()              