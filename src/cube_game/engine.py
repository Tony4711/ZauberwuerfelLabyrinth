import copy
import operator
from enums import CommandTag, Command, DoorState, GameState, MenuState, PlayerState, Directions, RoomColor, Corner, TranslateKey
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
        self.player = Player("Garry", Directions.NORTH, self.world.starting_room, Position(8,10))
    
    def _cube_wrap_around(self):
        if self.player.pos.x < 0:
            self.player.pos.x = self.player.current_room.pos[Corner.TOP_RIGHT].x
        if self.player.pos.x > 24:
            self.player.pos.x = self.player.current_room.pos[Corner.BOTTOM_LEFT].x
        if self.player.pos.y < 0:
            self.player.pos.y = self.player.current_room.pos[Corner.TOP_RIGHT].y
        if self.player.pos.y > 18:
            self.player.pos.y = self.player.current_room.pos[Corner.BOTTOM_LEFT].y

    def _change_room(self, direction):
        # Get RoomColor.ENUM of room behind door from doors{} dict by using Direction.ENUM as key to return door objekt and read leads_to parameter from it
        next_room_color = self.player.current_room.doors[direction].leads_to
        # Use RoomColor.ENUM as key to return Room object from map_dict{}
        next_room = self.world.map_dict.get(next_room_color)
        # Get offset tuple from dict{} by using Direction.ENUM as key
        # kein Interface Update da kein return PlayerState.MOVE
        self.player.direction = direction
        self.player.current_room = next_room
        self._cube_wrap_around()

    ### BUG: The method only checks for doors for last moved direction
    # If player moves side ways to a door, it is not recognised. And if a room has more than one door,
    # the door which has the same direction as the last move of a player  get recognised even if it is not
    # the door right next to the player. 
    ### CHORE: Methods need to check surrounding for doors
    # The door direction needs to fit the player direction too while the postion of the player needs to be right
    # infront of the door
    def _door_infront(self, direction):
        (dx, dy) = self._translate_(TranslateKey.DIRECTION_TO_OFFSET, direction)
        infront = self.player.pos + (dx, dy)
        try:
            door = self._get_door(direction)
        except KeyError:
            return False
        if infront == door.pos:
            return True 
        else: 
            False

    def _get_door(self, direction):
        door = self.player.current_room.doors[direction]
        return door
    
    def _translate_(self, key, inner_key):
        translate = {
            TranslateKey.COMMAND_TO_DIRECTION: {
            Command.MOVE_NORTH: (Directions.NORTH, operator.le),
            Command.MOVE_EAST: (Directions.EAST, operator.le),
            Command.MOVE_SOUTH: (Directions.SOUTH, operator.ge),
            Command.MOVE_WEST: (Directions.WEST, operator.ge) 
            },
            TranslateKey.DIRECTION_TO_OFFSET: {
            Directions.NORTH: (0,1),
            Directions.EAST: (1,0),
            Directions.SOUTH: (0, -1),
            Directions.WEST: (-1,0) 
            },
            TranslateKey.OFFSET_TO_CORNER: {
                (0,1): (Corner.TOP_RIGHT, lambda p: p.y),
                (1,0): (Corner.TOP_RIGHT, lambda p: p.x),
                (0,-1): (Corner.BOTTOM_LEFT, lambda p: p.y),
                (-1,0): (Corner.BOTTOM_LEFT, lambda p: p.x)
            },
            TranslateKey.STATE_TRANSITION: {
                (GameState.MENU, MenuState.MAIN,Command.OP1): GameState.PLAYING, 
                (GameState.MENU, MenuState.MAIN,Command.OP2): MenuState.EXIT,
                (GameState.MENU, MenuState.EXIT,Command.OP1): GameState.EXIT,
                (GameState.MAP, MenuState.EXIT, Command.OP2): GameState.BACK,
                (Command.CONTROLS): MenuState.CONTROLS
            }

        }
        return translate[key][inner_key]

    def move(self, directional_command):
        # Use directional_command to translate into direction and comparison operator
        direction, op = self._translate_(TranslateKey.COMMAND_TO_DIRECTION, directional_command)
        # Use direction to translate into offset
        (dx,dy) = self._translate_(TranslateKey.DIRECTION_TO_OFFSET, direction)
        # Use offset to translate into corner and axis lambda function
        corner, axis_func = self._translate_(TranslateKey.OFFSET_TO_CORNER, (dx,dy))
        # axis function for player position + offset
        player_axis_val = axis_func(self.player.pos + (dx, dy))
        # axis function for room position at corner
        room_axis_val   = axis_func(self.player.current_room.pos[corner])
        # if condition to compare player position with borders of current room before moving
        print(f"Player: {player_axis_val}")
        print(f"Room Border: {room_axis_val}")
        print(f"Door: {self.player.current_room.doors[direction].pos}")
        if op(player_axis_val, room_axis_val):
            self.player.pos.move(dx,dy)
            self.player.direction = direction
            if self._door_infront(direction):
                return PlayerState.DOOR
            elif self.player.pos == self._get_door(direction).pos:
                self._change_room(direction)
                self.player.pos.move(dx,dy)
                return PlayerState.GO_DOOR
            else:
                return PlayerState.MOVE
        else:
            return PlayerState.WALL

    #translated    
    def menu_handler(self, command):
        menuState = self.stateManager.menuState
        if menuState == MenuState.MAIN:
            return self.main_menu(command)
        elif menuState == MenuState.EXIT:
            return self.exit_menu(command)

    #translated
    def main_menu(self, command):
        if command == Command.OP1:
            return GameState.PLAYING
        elif command == Command.OP2:
            return MenuState.EXIT
    
    #translated
    def exit_menu(self, command):
        # Wenn 'JA' dann beende das Spiel
        if command == Command.OP1:
            return GameState.EXIT
        # Wenn 'NEIN' dann zurück
        if command == Command.OP2:
            return GameState.BACK

    def process_command(self, command):
            if command == Command.CONTROLS:
                return MenuState.CONTROLS 
            elif command == Command.OPEN_MAP:
                return GameState.MAP
            elif command.tag == CommandTag.MOVEMENT:
                return self.move(command)
            elif command.tag == CommandTag.OPTION:
                return self.menu_handler(command)

    def update(self):
        gameState = self.stateManager.gameState
        menuState = self.stateManager.menuState
        if gameState == GameState.INIT:
            return gameState
        self.command = self.controls.process_input(gameState, menuState)
        return self.process_command(self.command) 