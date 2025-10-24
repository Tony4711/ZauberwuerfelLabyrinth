import sys
import readchar
import random
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

class Engine:

    def __init__(self):
        self.running = True
        self.state = GameState.MAIN_MENU
        self.isGlobal = False
        self.last_input = ""
        self.controls = Controls()
        self.utility = Utility(self.controls)
        self.init_player()

        
    def init_player(self):
        self.player = Player("Garry", current_room=self.starting_room)
    
    def start(self):
        self.utility.centered(f"--- Spiel wird gestartet ---\n")
        self.utility.centered(f"--- Bitte nutze [{Command.CONTROLS.value.upper()}] um dir die Steuerung anzeigen zu lassen ---\n")
        while True:
            self.command = self.utility.process_input(self.state, isGlobal=True)
            # Wenn der Input Teil der Bewegungssteuerung ist, bewege dich, sonst False
            if self.command in self.utility.get_commands_for_state(self.controls.mapping, self.state):
                self.move(self.command)
                #---DEBUG print---
                #print(f"Player:\nx={self.player.pos.x}, y={self.player.pos.y}")
                #print(self.player.current_room.name)

            else:
                #Ansonsten neuen Input einholen
                self.process_command()
       
    def exit(self):
        self.utility.centered(f"--- Spiel wirklich beenden? [J/N] ---\n")
        prev_state = self.state
        self.state = GameState.EXIT
        self.command = self.utility.process_input(self.state, False)
        if self.command == Command.ACCEPT:
            self.utility.centered(f"--- Spiel wird beendet ---")
            self.utility.print_dividing_line()
            self.state = GameState.EXIT
            self.running = False
            sys.exit()
        elif self.command == Command.DENIE:
            self.state = prev_state
            self.utility.centered(f"--- Ok, Spiel wird nicht beendet ---")
            self.utility.print_dividing_line()

    def _check_door(self, direction):
        try:
            door = self.player.current_room.doors[direction]
        except KeyError:
            return False
        if (self.player.pos.x == door.pos.x) and (self.player.pos.y == door.pos.y):
            self._move_through_door(direction)
            return True 
        else: 
            False
    
    def _cube_wrap_around(self):
        if self.player.pos.x < 0:
            self.player.pos.x = self.player.current_room.pos[Corner.TOP_RIGHT].x
        if self.player.pos.x > 24:
            self.player.pos.x = self.player.current_room.pos[Corner.BOTTOM_LEFT].x
        if self.player.pos.y < 0:
            self.player.pos.y = self.player.current_room.pos[Corner.TOP_RIGHT].y
        if self.player.pos.y > 18:
            self.player.pos.y = self.player.current_room.pos[Corner.BOTTOM_LEFT].y

    def _move_through_door(self, direction):
        offset = {
            Directions.NORTH: (0,1),
            Directions.EAST: (1,0),
            Directions.SOUTH: (0, -1),
            Directions.WEST: (-1,0) 
        }
        # Get RoomColor.ENUM of room behind door from doors{} dict by using Direction.ENUM as key to return door objekt and read leads_to parameter from it
        next_room_color = self.player.current_room.doors[direction].leads_to
        # Use RoomColor.ENUM as key to return Room object from map_dict{}
        next_room = self.map_dict.get(next_room_color)
        # Get offset tuple from dict{} by using Direction.ENUM as key
        (dx, dy) = offset.get(direction)
        self.player.pos.move(dx, dy)
        self.player.current_room = next_room
        self._cube_wrap_around()
        self.utility.centered(f"--- Du gehst durch eine Tür in Richtung {direction.value} ---\n")
        self.utility.centered(f"--- Du betrittst den {self.player.current_room.name} ---\n")
        
    def move(self, directional_command):
        if directional_command == Command.MOVE_NORTH:
            if not self._check_door(Directions.NORTH):
                if self.player.pos.y+1 <= self.player.current_room.pos[Corner.TOP_RIGHT].y:
                    self.player.pos.move(dx=0,dy=1)
                    result = {
                        
                    }
                    return result
        elif directional_command == Command.MOVE_SOUTH:
            if not self._check_door(Directions.SOUTH):
                if self.player.pos.y-1 >= self.player.current_room.pos[Corner.BOTTOM_LEFT].y:
                    self.player.pos.move(dx=0,dy=-1)
                    self.utility.centered(f"--- Du gehst einen Schritt nach Süden ---\n")
                else:
                    self.utility.centered(f"--- Du stößt gegen eine Wand! ---\n")
        elif directional_command == Command.MOVE_WEST:
            if not self._check_door(Directions.WEST):
                if self.player.pos.x-1 >= self.player.current_room.pos[Corner.BOTTOM_LEFT].x:
                    self.player.pos.move(dx=-1,dy=0)
                    self.utility.centered(f"--- Du gehst einen Schritt nach Westen ---\n")
                else:
                    self.utility.centered(f"--- Du stößt gegen eine Wand! ---\n")
        elif directional_command == Command.MOVE_EAST:
            if not self._check_door(Directions.EAST):
                if self.player.pos.x+1 <= self.player.current_room.pos[Corner.TOP_RIGHT].x:
                    self.player.pos.move(dx=1,dy=0)
                    self.utility.centered(f"{'--- Du gehst einen Schritt nach Osten ---\n':^64}")
                else:
                    self.utility.centered(f"--- Du stößt gegen eine Wand! ---\n")           
                   
    def process_command(self, command):
            if command == Command.CONTROLS:
                return # e.g. render_state str which triggers rigth method from interface class 
            elif command == Command.EXIT:
                self.exit()
            elif command == Command.OPEN_MAP:
                return # e.g. render_state str which triggers rigth method from interface class 
            elif command.tag == CommandTag.OPTION:
                self.menu_handler() # chore: for new archtiecture menu_handler needs to be reworked so interface class displays the menu

    def menu_handler(self):
        if self.command == Command.OP1:
            self.state = GameState.PLAYING
            self.isGlobal = True
            self.start()
        elif self.command == Command.OP2:
             self.exit()

    def update(self):
        pass



