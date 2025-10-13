import sys
import readchar
from functools import lru_cache
from enums import DoorState, GameState, Directions, RoomColor
from position import Position
from room import Room
from door import Door
from controls import Controls
from player import Player
from utility import Utility

# Ein Spiel zum Verstehen der Grundmechaniken eines Rubiks Würfels.
# Der kleine Zauberer Garry ist in einem 3 dimensionalem Labyrinth gefangen und muss die Räume richtig miteinander verbinden, um herauszufinden.
# Dabei stößt er auf verschiedenste Rätsel und Herausforderungen, die ihm Helfen, den Zauberwürfel zu verstehen.

class Game:

    def __init__(self):
        self.active = True
        self.state = GameState.MAIN_MENU
        self.last_input = ""
        self.controls = Controls()
        self.utility = Utility(self.controls)
        self.init_rooms()
        self.init_player()
        self.init_menu_structure()
       

    def init_player(self):
        self.player = Player("Garry", current_room=self.yellow_room)

    def init_rooms(self):
       self.yellow_room = Room(
           color = RoomColor.YELLOW,
           width = 6,
           length = 6,
           position = Position(6,0) ,
           name = "Gelber Raum",
           neighbors = {
               Directions.NORTH: RoomColor.GREEN,
               Directions.EAST: RoomColor.RED,
               Directions.SOUTH: RoomColor.BLUE,
               Directions.WEST: RoomColor.ORANGE
           },
          door = Door(leads_to=RoomColor.GREEN, direction=Directions.NORTH, state=DoorState.OPEN, position=(6,12))
       )
       self.white_room = Room(
            color = RoomColor.WHITE,
            width = 6,
            length = 6,
            position = Position(6,12),
            name = "Weißer Raum",
            neighbors = {
                Directions.NORTH: RoomColor.BLUE,
                Directions.EAST: RoomColor.RED,
                Directions.SOUTH: RoomColor.GREEN,
                Directions.WEST: RoomColor.ORANGE
            },
            door = Door(leads_to=RoomColor.GREEN, direction=Directions.SOUTH, position=(6,12))

       )
       self.green_room = Room(
            color = RoomColor.GREEN,
            width = 6,
            length = 6,
            position = Position(6,6),
            name = "Grüner Raum",
            neighbors = {
                Directions.NORTH: RoomColor.WHITE,
                Directions.EAST: RoomColor.RED,
                Directions.SOUTH: RoomColor.YELLOW,
                Directions.WEST: RoomColor.ORANGE
            },
            door = Door(leads_to=RoomColor.ORANGE , direction=Directions.WEST, position=(6,6))
        )
       self.red_room = Room(
            color = RoomColor.RED,
            width = 6,
            length = 6,
            position = Position(12,6),
            name = "Roter Raum",
            neighbors = {
                Directions.NORTH: RoomColor.WHITE,
                Directions.EAST: RoomColor.BLUE,
                Directions.SOUTH: RoomColor.YELLOW,
                Directions.WEST: RoomColor.GREEN
            },
            door = Door(leads_to=RoomColor.GREEN, direction=Directions.WEST, position=(12,6))
        )
       self.blue_room = Room(
            color = RoomColor.BLUE,
            width = 6,
            length = 6,
            position = Position(18,6),
            name = "Blauer Raum",
            neighbors = {
                Directions.NORTH: RoomColor.WHITE,
                Directions.EAST: RoomColor.ORANGE,
                Directions.SOUTH: RoomColor.YELLOW,
                Directions.SOUTH: RoomColor.RED
            },
            door = Door(leads_to=RoomColor.RED, direction=Directions.WEST, position=(18,6))
        )
       self.orange_room = Room(
            color = RoomColor.ORANGE,
            width = 6,
            length = 6,
            position = Position(0,6),
            name = "Oranger Raum",
            neighbors = {
                Directions.NORTH: RoomColor.WHITE,
                Directions.EAST: RoomColor.GREEN,
                Directions.SOUTH: RoomColor.YELLOW,
                Directions.WEST: RoomColor.BLUE
            },
            door = Door(leads_to=RoomColor.BLUE, direction=Directions.WEST, position=(0,6))
       )
    
    def init_map(self):
        self.map_dict = {
            self.yellow_room,
            self.white_room,
            self.green_room,
            self.orange_room,
            self.blue_room,
            self.red_room
        }
        self.utility.print_map(self.map_dict)
    
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

    def main_menu(self):
        self.hello()
        self.show_menu_options()
        self.player_choice = self.utility.process_input(self.state)
        self.choice_handler()
        
    
    def start(self):
        print("--- Spiel wird gestartet ---\n")
        while True:
            self.player_choice = self.utility.process_input(self.state)
            # Wenn der Input Teil der Bewegungssteuerung ist, bewege dich, sonst False
            if self.player_choice in self.utility.return_valid_inputs(self.controls.mapping, self.state):
                self.move(self.player_choice)
            else:
                False
            #self.utility.process_input(self.state)
       
    def exit(self):
        print("--- Spiel wirklich beenden? [J/N] ---\n")
        self.player_choice = self.utility.process_input(self.state)
        if self.player_choice == "j":
            print("--- Spiel wird beendet ---")
            sys.exit()
        elif self.player_choice == "n":
            print("--- Ok, Spiel wird nicht beendet ---")
            print("_______________________________________\n")
            self.state = GameState.MAIN_MENU
            
            

    def move(self, direction):
        if direction == "w" and self.player.pos.y+1 < self.player.current_room.length:
            self.player.pos.move(dx=0,dy=1)
            print("--- Du gehst einen Schritt nach Norden ---\n")
        elif direction == "s" and self.player.pos.y-1 > 0:
            self.player.pos.move(dx=0,dy=-1)
            print("--- Du gehst einen Schritt nach Süden ---\n")
        elif direction == "a" and self.player.pos.x-1 > 0:
            self.player.pos.move(dx=-1,dy=0)
            print("--- Du gehst einen Schritt nach Westen ---\n")
        elif direction == "d" and self.player.pos.x+1 < self.player.current_room.width:
            self.player.pos.move(dx=1,dy=0)
            print("--- Du gehst einen Schritt nach Osten ---\n")
        else:
            print("--- Du stößt gegen eine Wand! ---\n")
        
        
            
    def choice_handler(self):
            if self.player_choice == "1":
                self.state = GameState.START
            elif self.player_choice == "2":
                self.state = GameState.GLOBAL_CONTROLS
            elif self.player_choice == "3":
                self.state = GameState.EXIT    

    def game_run(self):
        while self.active:
            if self.state == GameState.MAIN_MENU:
                self.main_menu()
            elif self.state == GameState.START:
                self.start()
            elif self.state == GameState.EXIT:
                self.exit()
            elif self.state == GameState.GLOBAL_CONTROLS:
                self.utility.print_dict(self.controls.get_dict("mapping"))
                self.state = GameState.MAIN_MENU
                self.player_choice = self.utility.process_input(self.state)
                self.choice_handler()

if __name__ == "__main__":
    game = Game()
    game.game_run()              