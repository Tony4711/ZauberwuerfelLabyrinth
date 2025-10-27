import sys
from enums import CommandTag, Command, DoorState, IsGlobal, GameState, MenuState, Directions, RoomColor, Corner
from position import Position
from room import Room
from door import Door
from controls import Controls
from player import Player
from utility import Utility
from world import World

# Ein Spiel zum Verstehen der Grundmechaniken eines Rubiks Würfels.
# Der kleine Zauberer Garry ist in einem 3 dimensionalem Labyrinth gefangen und muss die Räume richtig miteinander verbinden, um herauszufinden.
# Dabei stößt er auf verschiedenste Rätsel und Herausforderungen, die ihm Helfen, den Zauberwürfel zu verstehen.

class Engine:

    def __init__(self, StateManager):
        self.controls = Controls(StateManager)
        self.utility = Utility()
        self.world = World()
        self.stateManager = StateManager
        self.init_player()

    def init_player(self):
        self.player = Player("Garry", current_room=self.world.starting_room)

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

    # CHORE: Refactor method to fit new framework
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

    # CHORE: Refactor method to fit new framework    
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
                next_state = MenuState.CONTROLS
                return next_state
            elif command == Command.EXIT:
                self.exit()
            elif command == Command.OPEN_MAP:
                return # e.g. render_state str which triggers rigth method from interface class 
            elif command.tag == CommandTag.OPTION:
                next_state = self.menu_handler(command)
                return next_state
            elif command.tag == CommandTag.MOVEMENT:
                self.move(command)
                next_state = GameState.PLAYING
                return next_state
    
    def menu_handler(self, command):
        menuState = self.stateManager.menuState
        if menuState == MenuState.MAIN:
            return self.main_menu(command)
        elif menuState == MenuState.EXIT:
            return self.exit_menu(command)

    def main_menu(self, command):
        if command == Command.OP1:
            next_state = GameState.PLAYING
            return next_state
        elif command == Command.OP2:
            next_state = MenuState.EXIT
            return next_state
    
    def exit_menu(self, command):
        # Wenn 'JA' dann beende das Spiel
        if command == Command.OP1:
            next_state = GameState.EXIT
            return next_state
        # Wenn 'NEIN' dann zurück
        if command == Command.OP2:
            next_state = GameState.BACK
            return next_state


    def update(self):
        gameState = self.stateManager.gameState
        menuState = self.stateManager.menuState
        isGlobal = self.stateManager.isGlobal
        if gameState == GameState.INIT:
            return gameState
        self.command = self.controls.process_input(gameState, menuState, isGlobal)
        return self.process_command(self.command) 