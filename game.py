import sys
import readchar
from functools import lru_cache
from room import Room
from controls import Controls
from player import Player
from utility import Utility

# Ein Spiel zum Verstehen der Grundmechaniken eines Rubiks Würfels.
# Der kleine Zauberer Garry ist in einem 3 dimensionalem Labyrinth gefangen und muss die Räume richtig miteinander verbinden, um herauszufinden.
# Dabei stößt er auf verschiedenste Rätsel und Herausforderungen, die ihm Helfen, den Zauberwürfel zu verstehen.

class Game:

    def __init__(self):
        self.active = True
        self.state = "main_menu"
        self.last_input = ""
        self.controls = Controls()
        self.utility = Utility(self.controls, self.state)
        self.init_rooms()
        self.init_player()
        self.init_menu_structure()

    def init_player(self):
        self.player = Player("Garry", [2,2])
        self.player_pos = [2,2] 
        
    def init_rooms(self):
       self.rooms = {
            "yellow_room": Room(
                color = "yellow",
                width = 6,   
                length = 6,
                position = "bottom",
                name = "gelber Raum",
                neighbors = {
                    "north": "green_room",
                    "east": "red_room",
                    "south": "blue_room",
                    "west": "orange_room",
                }
            ),
            "white_room": Room(
                color = "white",
                width = 6,
                length = 6,
                position = "top",
                name = "weißer Raum",
                neighbors = {
                    "north": "blue_room",
                    "east": "red_room",
                    "south": "green_room",
                    "west": "orange_room",
                }
            ),
            "green_room": Room(
                color = "green",
                width = 6,
                length = 6,
                position = "front",
                name = "grüner Raum",
                neighbors = {
                    "north": "white_room",
                    "east": "red_room",
                    "south": "yellow_room",
                    "west": "orange_room",
                }
            ),
            "red_room": Room(
                color = "red",
                width = 6,
                length = 6,
                position = "right",
                name = "roter Raum",
                neighbors = {
                    "north": "white_room",
                    "east": "blue_room",
                    "south": "yellow_room",
                    "west": "green_room",
                }
            ),
            "blue_room": Room(
                color = "blue",
                width = 6,
                length = 6,
                position = "back",
                name = "blauer Raum",
                neighbors = {
                    "north": "white_room",
                    "east": "orange_room",
                    "south": "yellow_room",
                    "west": "red_room",
                }
            ),
            "orange_room": Room(
                color = "orange",
                width = 6,
                length = 6,
                position = "left",
                name = "oranger Raum",
                neighbors = {
                    "north": "white_room",
                    "east": "green_room",
                    "south": "yellow_room",
                    "west": "blue_room",
                }
            )
        }
    
    def init_menu_structure(self):
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
                                         
    @lru_cache(maxsize=1)
    def hello(self):
        print("_____________________________________________________________")
        print("\n--- Willkommen zu 'Gefangen im Zauberwürfel Labyrinth'! ---")
        print("\n                   --- Hauptmenü ---")
        print("\n--- Zum steuern bitte die in [ ] geschriebene Taste drücken ---\n")

    # Funktioniert nicht, weil ich keinen state übergebe wie es die methode verlangt. 
    # Ich kann nicht das dict ändern das ausgelesen wird, lediglich den state.
    # In controls ist fest definiert das aus mapping{} ausgelesen wird.
    # Ich brauche also hier eine neue Methode die das gleiche macht nur mit dem passenden Dict.
    def show_menu_options(self):
        self.utility.print_dict(self.menu_structure, "main_menu")
               
    def save_previous_state(self):
        self.previous_state = self.state

    def main_menu(self):
        self.hello()
        self.show_menu_options()
        self.player_choice = self.utility.process_input(self.state)
        self.choice_handler()
        
    
    def start(self):
        print("--- Spiel wird gestartet ---")
        while True:
            self.player_choice = self.utility.process_input(self.state)
            # Wenn der Input Teil der Bewegungssteuerung ist, bewege dich, sonst False
            if self.player_choice in self.utility.return_valid_inputs(self.controls.mapping, self.state):
                self.move(self.player_choice)
                #print(self.player_pos) #Zum überprüfen wo der Spieler steht
            else:
                False
            self.utility.process_input(self.state)
       
    def exit(self):
        print("--- Spiel wirklich beenden? [J/N] ---")
        self.player_choice = self.utility.process_input(self.state)
        if self.player_choice == "j":
            print("--- Spiel wird beendet ---")
            sys.exit()
        elif self.player_choice == "n":
            print("--- Ok, Spiel wird nicht beendet ---")
            print("_______________________________________\n")
            self.state = "main_menu"
            
            

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
            print("--- Du stößt gegen eine Wand! ---")
        self.player_pos = [x,y]
            
    def choice_handler(self):
            if self.player_choice == "1":
                self.save_previous_state()
                self.state = "start"
            elif self.player_choice == "2":
                self.save_previous_state()
                self.state = "navigation"
            elif self.player_choice == "3":
                self.save_previous_state()
                self.state = "exit"    

    def game_run(self):
        while self.active:
            if self.state == "main_menu":
                self.main_menu()
            elif self.state == "start":
                self.start()
            elif self.state == "exit":
                self.exit()
            elif self.state == "navigation":
                self.utility.print_dict(self.controls.get_dict("mapping"))
                self.state = "main_menu"
                self.player_choice = self.utility.process_input(self.state)
                self.choice_handler()

if __name__ == "__main__":
    game = Game()
    game.game_run()              