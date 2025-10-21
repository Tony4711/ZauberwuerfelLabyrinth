import sys
import readchar
from functools import lru_cache
from enums import DoorState, GameState, Directions, RoomColor, Command, CommandTag, Corner
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
        
       

    def init_player(self):
        self.player = Player("Garry", current_room=self.starting_room)

    def init_rooms(self):
       self.yellow_room = Room(
           color = RoomColor.YELLOW,
           width = 6,
           length = 6,
            pos = {
                Corner.BOTTOM_LEFT: Position(6,0),
                Corner.TOP_RIGHT: Position(12,6)
                },
           name = "Gelber Raum",
           neighbors = {
               Directions.NORTH: RoomColor.GREEN,
               Directions.EAST: RoomColor.RED,
               Directions.SOUTH: RoomColor.BLUE,
               Directions.WEST: RoomColor.ORANGE
           },
          door = Door(leads_to=RoomColor.GREEN, direction=Directions.NORTH, state=DoorState.OPEN, pos=Position(6,12))
       )
       self.white_room = Room(
            color = RoomColor.WHITE,
            width = 6,
            length = 6,
            pos = {
                Corner.BOTTOM_LEFT: Position(6,12),
                Corner.TOP_RIGHT: Position(12,18)
                },
            name = "Weißer Raum",
            neighbors = {
                Directions.NORTH: RoomColor.BLUE,
                Directions.EAST: RoomColor.RED,
                Directions.SOUTH: RoomColor.GREEN,
                Directions.WEST: RoomColor.ORANGE
            },
            door = Door(leads_to=RoomColor.GREEN, direction=Directions.SOUTH, pos=Position(6,12))

       )
       self.green_room = Room(
            color = RoomColor.GREEN,
            width = 6,
            length = 6,
            pos = {
                Corner.BOTTOM_LEFT: Position(6,6),
                Corner.TOP_RIGHT: Position(12,12)
                },
            name = "Grüner Raum",
            neighbors = {
                Directions.NORTH: RoomColor.WHITE,
                Directions.EAST: RoomColor.RED,
                Directions.SOUTH: RoomColor.YELLOW,
                Directions.WEST: RoomColor.ORANGE
            },
            door = Door(leads_to=RoomColor.ORANGE , direction=Directions.WEST, pos=Position(6,6))
        )
       self.red_room = Room(
            color = RoomColor.RED,
            width = 6,
            length = 6,
            pos = {
                Corner.BOTTOM_LEFT: Position(12,6),
                Corner.TOP_RIGHT: Position(18,12)
                },
            name = "Roter Raum",
            neighbors = {
                Directions.NORTH: RoomColor.WHITE,
                Directions.EAST: RoomColor.BLUE,
                Directions.SOUTH: RoomColor.YELLOW,
                Directions.WEST: RoomColor.GREEN
            },
            door = Door(leads_to=RoomColor.GREEN, direction=Directions.WEST, pos=Position(12,6))
        )
       self.blue_room = Room(
            color = RoomColor.BLUE,
            width = 6,
            length = 6,
            pos = {
                Corner.BOTTOM_LEFT: Position(18,6),
                Corner.TOP_RIGHT: Position(24,12)
                },
            name = "Blauer Raum",
            neighbors = {
                Directions.NORTH: RoomColor.WHITE,
                Directions.EAST: RoomColor.ORANGE,
                Directions.SOUTH: RoomColor.YELLOW,
                Directions.SOUTH: RoomColor.RED
            },
            door = Door(leads_to=RoomColor.RED, direction=Directions.WEST, pos=Position(18,6))
        )
       self.orange_room = Room(
            color = RoomColor.ORANGE,
            width = 6,
            length = 6,
            pos = {
                Corner.BOTTOM_LEFT: Position(0,6),
                Corner.TOP_RIGHT: Position(6,12)
                },
            name = "Oranger Raum",
            neighbors = {
                Directions.NORTH: RoomColor.WHITE,
                Directions.EAST: RoomColor.GREEN,
                Directions.SOUTH: RoomColor.YELLOW,
                Directions.WEST: RoomColor.BLUE
            },
            door = Door(leads_to=RoomColor.BLUE, direction=Directions.WEST, pos= Position(0,6))
       )
       self.starting_room = self.green_room
    
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
            Command.OP2.value: "Spiel verlassen",
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
        print(f"{'--- Spiel wird gestartet ---\n':^64}")
        print(f"{'--- Bitte nutze [' + Command.CONTROLS.value.upper() + '] um dir die Steuerung anzeigen zu lassen ---\n':^64}")
        while True:
            self.command = self.utility.process_input(self.state, isGlobal=True)
            # Wenn der Input Teil der Bewegungssteuerung ist, bewege dich, sonst False
            if self.command in self.utility.get_commands_for_state(self.controls.mapping, self.state):
                self.move(self.command)
                #---DEBUG print---
                #self.utility.print_pos("Player:", self.player)
                #self.utility.print_pos("Door:",self.player.current_room.door)
                #print(self.player.current_room.name)
                #print(self.player.current_room.pos)
                #print(self.player.current_room.length)
                #print(self.player.current_room.width)
            else:
                self.process_command()
       
    def exit(self):
        print(f"{'--- Spiel wirklich beenden? [J/N] ---\n':^64}")
        prev_state = self.state
        self.state = GameState.EXIT
        self.command = self.utility.process_input(self.state, False)
        if self.command == Command.ACCEPT:
            print(f"{'--- Spiel wird beendet ---':^64}")
            self.utility.print_dividing_line()
            self.state = GameState.EXIT
            self.running = False
            sys.exit()
        elif self.command == Command.DENIE:
            self.state = prev_state
            print(f"{'--- Ok, Spiel wird nicht beendet ---':^64}")
            self.utility.print_dividing_line()

    def check_door(self):
        if (self.player.pos.x == self.player.current_room.door.pos.x) and (self.player.pos.y == self.player.current_room.door.pos.y):
            return True 
        else: 
            False

    def check_door(self):
        if (self.player.pos.x == self.player.current_room.door.pos.x) and (self.player.pos.y == self.player.current_room.door.pos.y):
            return True 
        else: 
    
            False
    def move_through_door(self, directional_command):
        directional_step = {
            Command.MOVE_NORTH: (Directions.NORTH, (0, 1),),
            Command.MOVE_SOUTH: (Directions.SOUTH, (0, -1)),
            Command.MOVE_EAST:  (Directions.EAST, (1, 0)),
            Command.MOVE_WEST:  (Directions.WEST, (-1, 0))
        }
        next_room_color = self.player.current_room.door.leads_to
        # Use color to find next room object
        next_room = self.map_dict.get(next_room_color)
        (dx, dy) = directional_step[directional_command][1]
        direction = directional_step[directional_command][0]
        self.player.pos.move(dx, dy)
        self.player.current_room = next_room
        print(f"{'--- Du gehst durch eine Tür in richtung ' + direction.value + ' und betrittst den ' + self.player.current_room.name +' ---\n':^64}")
        

    def move(self, directional_command):
        if directional_command == Command.MOVE_NORTH:
            if self.check_door():
                self.move_through_door(directional_command)    
            elif self.player.pos.y+1 <= self.player.current_room.pos[Corner.TOP_RIGHT].y:
                self.player.pos.move(dx=0,dy=1)
                print(f"{'--- Du gehst einen Schritt nach Norden ---\n':^64}")
            else:
                print(f"{'--- Du stößt gegen eine Wand! ---\n':^64}")
        elif directional_command == Command.MOVE_SOUTH:
            if self.check_door():
                self.move_through_door(directional_command)
            elif self.player.pos.y-1 >= self.player.current_room.pos[Corner.BOTTOM_LEFT].y:
                self.player.pos.move(dx=0,dy=-1)
                print(f"{'--- Du gehst einen Schritt nach Süden ---\n':^64}")
            else:
                print(f"{'--- Du stößt gegen eine Wand! ---\n':^64}")
        elif directional_command == Command.MOVE_WEST:
            if self.check_door():
                self.move_through_door(directional_command)
            elif self.player.pos.x-1 >= self.player.current_room.pos[Corner.BOTTOM_LEFT].x:
                self.player.pos.move(dx=-1,dy=0)
                print(f"{'--- Du gehst einen Schritt nach Westen ---\n':^64}")
            else:
                print(f"{'--- Du stößt gegen eine Wand! ---\n':^64}")
        elif directional_command == Command.MOVE_EAST:
            if self.check_door():
                self.move_through_door(directional_command)
            elif self.player.pos.x+1 <= self.player.current_room.pos[Corner.TOP_RIGHT].x:
                self.player.pos.move(dx=1,dy=0)
                print(f"{'--- Du gehst einen Schritt nach Osten ---\n':^64}")
            else:
                print(f"{'--- Du stößt gegen eine Wand! ---\n':^64}")            
        
       

    def move_old(self, direction):
        if direction == Command.MOVE_NORTH and self.player.pos.y+1 <= self.player.current_room.length:
            self.player.pos.move(dx=0,dy=1)
            print(f"{'--- Du gehst einen Schritt nach Norden ---\n':^64}")
        elif direction == Command.MOVE_SOUTH and self.player.pos.y-1 > 0:
            self.player.pos.move(dx=0,dy=-1)
            print(f"{'--- Du gehst einen Schritt nach Süden ---\n':^64}")
        elif direction == Command.MOVE_WEST and self.player.pos.x-1 > 0:
            self.player.pos.move(dx=-1,dy=0)
            print(f"{'--- Du gehst einen Schritt nach Westen ---\n':^64}")
        elif direction == Command.MOVE_EAST and self.player.pos.x+1 <= self.player.current_room.width:
            self.player.pos.move(dx=1,dy=0)
            print(f"{'--- Du gehst einen Schritt nach Osten ---\n':^64}")
        elif self.check_door():
            print(f"{'--- Du stehst vor einer Tür ---\n':^64}")
            self.prepare_room_transition()
        else:
            print(f"{'--- Du stößt gegen eine Wand! ---\n':^64}")
                   
    def process_command(self):
            if self.command == Command.CONTROLS:
                self.show_controls()
            elif self.command == Command.EXIT:
                self.exit()
            elif self.command == Command.OPEN_MAP:
                self.show_map() 
            elif self.command.tag == CommandTag.OPTION:
                self.menu_handler()

    def menu_handler(self):
        if self.command == Command.OP1:
            self.state = GameState.PLAYING
            self.isGlobal = True
            self.start()
        elif self.command == Command.OP2:
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