import sys
import readchar

# Ein Spiel zum Verstehen der Grundmechaniken eines Rubiks Würfels.
# Der kleine Zauberer Garry ist in einem 3 dimensionalem Labyrinth gefangen und muss die Räume richtig miteinander verbinden, um herauszufinden.
# Dabei stößt er auf verschiedenste Rätsel und Herausforderungen, die ihm Helfen, den Zauberwürfel zu verstehen.

class Game:

    def __init__(self):
        self.active = True
        self.state = "main_menu"
        self.last_input = ""
        self.init_controls()
        self.init_map()
        self.init_player()
<<<<<<< Updated upstream
=======
        self.init_main_menu()
>>>>>>> Stashed changes

    def init_player(self):
        self.player_pos = [2,2]

    def init_controls(self):
        self.valid_inputs = {
            "main_menu": {
                "1": "Option 1",
                "2": "Option 2",
                "3": "Option 3"
            },
            "navigation": {
                "q": "Zurück",
                "e": "Weiter"
            },
            "exit": {
                "j": "Ja",
                "n": "Nein"
            },
            "start": {
                "w": "Vorwärts",
                "a": "Nach links",
                "s": "Rückwärts",
                "d": "Nach rechts"
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

<<<<<<< Updated upstream
=======
    def init_main_menu(self):
        self.menu_structure = {
            "main_menu":{
            "1": "Spiel starten",
            "2": "Steuerung",
            "3": "Spiel verlassen"
            },
            "second menu": {
                "4":"test"
            }
        }

>>>>>>> Stashed changes
    def write_input(self, text):
        print("\nSpieler: [" + text + "]\n")

    # Liest den nächsten Tastendruck des Nutzers und speichert ihn in last_input
    # Schreibt den letzten Input in Großbuchstaben in die Konsole
    # Gibt den Inhalt von last_input zurück
    def get_input(self):
        from readchar import readkey, key
        self.last_input = readkey().lower().strip()     
        self.write_input(self.last_input.upper())     
        self.check_state_input()  
        return self.last_input                          
                 
    # Prüft ob die Eingabe für den aktuellen State gültig ist und gibt dementsprechend True oder False zurück
    def check_state_input(self):
        if self.last_input in self.valid_inputs[self.state]:              
            return True                                 
        else:
            #self.input_exception()
            return False
    
    # Nimmt als Parameter welches Dictionary ausgegeben werden soll und den aktuellen State als key
    def print_dict_from_state(self, dictname):
        for key, description in dictname[self.state].items():
            print(f"[{key.upper()}] {description}")
        print("________________________________________")

    def print_dict_all(self):
        for state_dict in self.valid_inputs.values():
            for key, desc in state_dict.items():
                print(f"[{key.upper()}] {desc}")
<<<<<<< Updated upstream
            
        print("")

    def input_exception(self):
        print("---Ungültige Eingabe. Bitte nutze die in [ ] geschriebene Taste zum steuern---")
=======
        print("________________________________________")      

    def input_exception(self):
        print("--- Ungültige Eingabe. Bitte nutze: ---\n" )
        self.print_dict_from_state(self.valid_inputs)
>>>>>>> Stashed changes

    def hello(self):
        print("_____________________________________________________________")
        print("\n--- Willkommen zu 'Gefangen im Zauberwürfel Labyrinth'! ---")
        print("\n                   --- Hauptmenü ---")
        print("\n--- Zum steuern bitte die in [ ] geschriebene Taste drücken. ---\n")
        
    def show_menu_options(self):
<<<<<<< Updated upstream
        print("[1] Spiel starten")
        print("[2] Steuerung")
        print("[3] Spiel verlassen")
=======
        self.print_dict_from_state(self.menu_structure)
>>>>>>> Stashed changes

    def choice_handler(self):
            if self.choice == "1":
                self.save_previous_state()
                self.state = "start"
            elif self.choice == "2":
                self.save_previous_state()
                self.state = "navigation"
            elif self.choice == "3":
                self.save_previous_state()
                self.state = "exit"               

    def save_previous_state(self):
        self.previous_state = self.state

    def main_menu(self):
        self.hello()
        self.show_menu_options()
        self.choice = self.get_input()
        #self.check_state_input()

        while not self.check_state_input():
            self.input_exception()
            self.choice = self.get_input()
        self.choice_handler()
        
    
    def start(self):
        self.state = "start"
        print("---Spiel wird gestartet...---")
        self.init_player()
        self.init_controls()
        self.init_map()
        while True:
            self.choice = self.get_input()
            if self.choice in self.valid_inputs["start"]:
                self.move(self.choice)
                #print(self.player_pos) #Zum überprüfen wo der Spieler steht
            else:
                False
        self.get_input()
       
    def exit(self):
        print("---Spiel wirklich beenden? [J/N]---")
        self.choice = self.get_input()
        if self.last_input == "j":
            print("--- Spiel wird beendet... ---")
            sys.exit()
        elif self.last_input == "n":
<<<<<<< Updated upstream
            print("--- Ok, zurück zum Menu. ---\n")
            self.show_menu_options()
=======
            print("--- Ok, Spiel wird nicht beendet ---\n")
            self.state = self.previous_state
>>>>>>> Stashed changes
            self.choice = self.get_input()
            

    def move(self, direction):
        x, y = self.player_pos
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
        self.player_pos = [x,y]
            

        

    def game_run(self):
        while self.active:
            if self.state == "main_menu":
                self.main_menu()
            elif self.state == "start":
                self.start()
            elif self.state == "exit":
                self.exit()
            elif self.state == "navigation":
                self.print_dict_all()
                self.state = "main_menu"
                self.choice = self.get_input()
                self.choice_handler()

if __name__ == "__main__":
    game = Game()
    game.game_run()              