from enums import CommandTag, Command, DoorState, GameState, MenuState, PlayerState, Directions, RoomColor, Corner, RouterSignal, SystemState, TranslateKey
from data.position import Position
from data.room import Room
from data.door import Door
from core.inputController import InputController
from data.player import Player
from utils.utility import Utility
from data.world import World
from translate.Engine import offset, geometry, direction

# Ein Spiel zum Verstehen der Grundmechaniken eines Rubiks Würfels.
# Der kleine Zauberer Garry ist in einem 3 dimensionalem Labyrinth gefangen und muss die Räume richtig miteinander verbinden, um herauszufinden.
# Dabei stößt er auf verschiedenste Rätsel und Herausforderungen, die ihm Helfen, den Zauberwürfel zu verstehen.

class Engine:

    def __init__(self, StateController):
        self.controls = InputController(StateController)
        self.utility = Utility()
        self.world = World()
        self.stateController = StateController
        self.offset = offset
        self.geometry = geometry
        self.direction = direction
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
        

    def _door_infront(self, direction):
        (dx, dy) = self.offset.offset_translate[direction]
        infront = self.player.pos + (dx, dy)
        door = self._get_door(direction)
        if door == None:
            return False
        if infront == door.pos:
            return True 
        else: 
            False

    def _get_door(self, direction):
        try:
            door = self.player.current_room.doors[direction]
        except KeyError:
            return None
        return door

    def move(self, directional_command):
        # Use directional_command to translate into direction and comparison operator
        direction , op = self.direction.command_direction[directional_command]
        # Use direction to translate into offset
        (dx,dy) = self.offset.offset_translate[direction]
        # Use offset to translate into corner and axis lambda function
        corner, axis_func = self.geometry.corner_translate[(dx,dy)]
        # axis function for player position + offset
        player_axis_val = axis_func(self.player.pos + (dx, dy))
        # axis function for room position at corner
        room_axis_val   = axis_func(self.player.current_room.pos[corner])
        # if condition to compare player position with borders of current room before moving
        door = self._get_door(direction)
        #print(f"Door: {self.player.current_room.doors[direction].pos}")
        if op(player_axis_val, room_axis_val):
            self.player.pos.move(dx,dy)
            self.player.direction = direction
            #print(f"Player: {self.player.pos}") #---DEBUG PRINT---
            #print(f"Room: {self.player.current_room.pos[corner]}") #---DEBUG PRINT---
            if self._door_infront(direction):
                self.player.pos.move(dx,dy)
                return PlayerState.DOOR
            else:
                return PlayerState.MOVE
        elif door is not None and self.player.pos == door.pos:
            self._change_room(direction)
            self.player.pos.move(dx,dy)
            self._cube_wrap_around()
            #print(f"Player: {self.player.pos}") #---DEBUG PRINT---
            return PlayerState.GO_DOOR
        else:
            return PlayerState.WALL

    #translated    
    def menu_handler(self, command):
        menuState = self.stateController.menuState
        if menuState == MenuState.MAIN:
            return self.main_menu(command)
        elif menuState == MenuState.EXIT:
            return self.exit_menu(command)

    #translated
    def main_menu(self, command):
        if command == Command.OP1:
            #return GameState.STARTING
            return GameState.PLAYING
        elif command == Command.OP2:
            return MenuState.EXIT
        elif command == Command.OP3:
            return MenuState.ALL_CONTROLS
    
    #translated
    def exit_menu(self, command):
        # Wenn 'JA' dann beende das Spiel
        if command == Command.ACCEPT: #OP1
            return GameState.EXIT
        # Wenn 'NEIN' dann zurück
        if command == Command.DENIE: #OP2
            return GameState.BACK

    def handle_command(self, command):
        if command == Command.CONTROLS:
            return MenuState.CONTROLS 
        elif command == Command.OPEN_MAP:
            return MenuState.MAP
        elif command == Command.BACK:
            return GameState.BACK
        elif command == Command.EXIT:
            return MenuState.EXIT
        elif command.tag == CommandTag.MOVEMENT:
            return self.move(command)
        elif command.tag == CommandTag.OPTION:
            return self.menu_handler(command)

    def update(self):
        gameState = self.stateController.gameState
        menuState = self.stateController.menuState
        self.stateController.systemState = SystemState.OK
        if gameState == GameState.INIT:
            return gameState
        self.command = self.controls.process_input(gameState, menuState)
        if self.command == None:
            return SystemState.EXCEPTION_INPUT_ERROR
        return self.handle_command(self.command) 