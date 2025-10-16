import sys
import readchar
from functools import lru_cache
from enums import DoorState, GameState, Directions, RoomColor, Command
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
        self.running = True
        self.state = GameState.MAIN_MENU
        self.isGlobal = False
        self.last_input = ""
        self.controls = Controls()
        self.utility = Utility(self.controls)
        self.init_rooms()
        self.init_player()
        self.init_map()
        self.init_menu_structure()
        self.movement_commands = {
            Command.MOVE_NORTH,
            Command.MOVE_EAST,
            Command.MOVE_SOUTH,
            Command.MOVE_WEST
        }
        self.option_commands = {
            Command.OP1,
            Command.OP2,
            Command.OP2,
            Command.OP3,
            Command.OP4
        }
        
       

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
            RoomColor.YELLOW: self.yellow_room,
            RoomColor.WHITE: self.white_room,
            RoomColor.GREEN: self.green_room,
            RoomColor.ORANGE: self.orange_room,
            RoomColor.BLUE: self.blue_room,
            RoomColor.RED: self.red_room
        }
    
    def init_menu_structure(self):
        self.menu_structure = {
            "main_menu":{
            Command.OP1.value: "Spiel starten",
            Command.OP2.value: "Steuerung",
            Command.OP3.value: "Karte öffnen",
            Command.OP4.value: "Spiel verlassen"
            },
            "second menu": {
                "4":"test"
            }
        }
                                         
    @lru_cache(maxsize=1)
    def hello(self):
        print("________________________________________________________________")
        print("\n--- Willkommen zu 'Gefangen im Zauberwürfel Labyrinth'! ---")
        print("\n                   --- Hauptmenü ---")
        print("\n--- Zum steuern bitte die in [ ] geschriebene Taste drücken ---\n")

    def show_controls(self):
        self.utility.print_dict(self.controls.get_dict("mapping"))

    def show_menu_options(self):
        self.utility.print_dict(self.menu_structure, "main_menu")
    
    def show_map(self):
         self.utility.print_map(self.green_room, self.map_dict)
    
    def start(self):
        print("--- Spiel wird gestartet ---\n")
        while True:
            self.command = self.utility.process_input(self.state, True)
            # Wenn der Input Teil der Bewegungssteuerung ist, bewege dich, sonst False
            if self.command in self.utility.get_commands_for_state(self.controls.mapping, self.state):
                self.move(self.command)
            else:
                self.process_command()
       
    def exit(self):
        print("--- Spiel wirklich beenden? [J/N] ---\n")
        prev_state = self.state
        self.state = GameState.EXIT
        self.command = self.utility.process_input(self.state)
        if self.command == Command.ACCEPT:
            print("--- Spiel wird beendet ---")
            self.state = GameState.EXIT
            self.running = False
        elif self.command == Command.DENIE:
            self.state = prev_state
            print("--- Ok, Spiel wird nicht beendet ---")
            print("________________________________________________________________\n")

    def move(self, direction):
        if direction is Command.MOVE_NORTH and self.player.pos.y+1 < self.player.current_room.length:
            self.player.pos.move(dx=0,dy=1)
            print("--- Du gehst einen Schritt nach Norden ---\n")
        elif direction is Command.MOVE_SOUTH and self.player.pos.y-1 > 0:
            self.player.pos.move(dx=0,dy=-1)
            print("--- Du gehst einen Schritt nach Süden ---\n")
        elif direction is Command.MOVE_WEST and self.player.pos.x-1 > 0:
            self.player.pos.move(dx=-1,dy=0)
            print("--- Du gehst einen Schritt nach Westen ---\n")
        elif direction is Command.MOVE_EAST and self.player.pos.x+1 < self.player.current_room.width:
            self.player.pos.move(dx=1,dy=0)
            print("--- Du gehst einen Schritt nach Osten ---\n")
        else:
            print("--- Du stößt gegen eine Wand! ---\n")
                   
    def process_command(self):
            if self.command is Command.CONTROLS:
                self.show_controls()
            elif self.command == Command.EXIT:
                self.exit()
            elif self.command is Command.OPEN_MAP:
                self.show_map() 
            elif self.command in self.movement_commands:
                self.move(self.command)
            elif self.command in self.option_commands:
                self.menu_handler()

    def menu_handler(self):
        if self.command is Command.OP1:
            self.state = GameState.PLAYING
            self.isGlobal = True
            self.start()
        elif self.command is Command.OP2:
            self.show_controls()
        elif self.command is Command.OP3:
            self.show_map()
        elif self.command is Command.OP4:
             self.exit()

    def game_run(self):
        self.hello()
        self.show_menu_options()
        while self.running:
            self.command = self.utility.process_input(self.state, self.isGlobal)
            self.process_command()


if __name__ == "__main__":
    game = Game()
    game.game_run()              