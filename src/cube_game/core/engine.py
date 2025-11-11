from enums.commands import CommandTag, Command
from enums.states import DoorState, GameState, MenuState, PlayerState, SystemState
from enums.geometry import Directions, RoomColor, Corner
from enums.routing import RouterSignal
from enums.handler import CommandHandler, MovementHandler, MenuOptionHandler
from data.position import Position
from core.input_controller import InputController
from data.player import Player
from utils.utility import Utility
from core.world import World
from translate.Engine import translate_offset, translate_geometry, translate_direction, translate_commandTag, router, command_handler, menu_handler, movement_handler

# Ein Spiel zum Verstehen der Grundmechaniken eines Rubiks Würfels.
# Der kleine Zauberer Garry ist in einem 3 dimensionalem Labyrinth gefangen und muss die Räume richtig miteinander verbinden, um herauszufinden.
# Dabei stößt er auf verschiedenste Rätsel und Herausforderungen, die ihm Helfen, den Zauberwürfel zu verstehen.

class Engine:

    def __init__(self, StateController):
        self.commandTagToSignal = translate_commandTag.commandTag_routerSignal
        self.router = router.routing
        self.commandHandler = command_handler.handler()
        self.menuHandler = menu_handler.menuOption
        self.movementHandler = movement_handler.handler(self)
        self.inputController = InputController()
        self.utility = Utility()
        self.world = World()
        self.stateController = StateController
        self.directionToOffset = translate_offset.offset_translate
        self.offsetToCorner = translate_geometry.corner_translate
        self.commandToDirection = translate_direction.command_direction
        self.init_player()

    def init_player(self):
        self.player = Player("Garry", Directions.NORTH, self.world.starting_room, Position(8,10))
    
    # If player coordinate goes out of bounce due to switching rooms that are neighbors but are not located next to each other in 2D map
    # the player coordinates get updated based on the current room and its two corner coordinates.
    # This works because the topology is handled seperatly from coordinates 
    ## CHORE: change hardcoded ints to values read from world to determine if a player is out of bounce
    def _cube_wrap_around(self):
        if self.player.pos.x < 0:
            self.player.pos.x = self.player.current_room.pos[Corner.TOP_RIGHT].x
        if self.player.pos.x > 24:
            self.player.pos.x = self.player.current_room.pos[Corner.BOTTOM_LEFT].x
        if self.player.pos.y < 0:
            self.player.pos.y = self.player.current_room.pos[Corner.TOP_RIGHT].y
        if self.player.pos.y > 18:
            self.player.pos.y = self.player.current_room.pos[Corner.BOTTOM_LEFT].y

    # Change room in wich player is located based on the neighbor room at the direction the player is facing
    def _change_room(self, direction):
        # Get RoomColor.ENUM of room behind door from doors{} dict by using Direction.ENUM as key to return door objekt and read leads_to parameter from it
        next_room_color = self.player.current_room.doors[direction].leads_to
        # Use RoomColor.ENUM as key to return Room object from map_dict{}
        next_room = self.world.map_dict.get(next_room_color)
        # Update direction player is looking
        self.player.direction = direction
        # Update Room where player is located now 
        self.player.current_room = next_room
        
    # Test if there is a door one step further of the player location in the facing direction
    def _door_infront(self, direction):
        (dx, dy) = self.directionToOffset[direction]
        infront = self.player.pos + (dx, dy)
        door = self._get_door(direction)
        if door == None:
            return False
        if infront == door.pos:
            return True 
        else: 
            False

    # Try to find a door at the direction the player is facing
    def _get_door(self, direction):
        try:
            door = self.player.current_room.doors[direction]
        except KeyError:
            return None
        return door

    # Movement method with straigth steps for each direction.
    def move_straight(self, directional_command):
        # Use directional_command to translate into direction and comparison operator
        direction , op = self.commandToDirection[directional_command]
        # Use direction to translate into offset
        (dx,dy) = self.directionToOffset[direction]
        # Use offset to translate into corner and axis lambda function
        corner, axis_func = self.offsetToCorner[(dx,dy)]
        # axis function for player position + offset
        player_axis_val = axis_func(self.player.pos + (dx, dy))
        # axis function for room position at corner
        room_axis_val   = axis_func(self.player.current_room.pos[corner])
        # try to find a door at the direction the player is facing and store it as local variable
        door = self._get_door(direction)
        #print(f"Door: {self.player.current_room.doors[direction].pos}")
        # Compare player position with borders of current room before moving
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

    # Use of different levels of dicts to process command logic.
    # Begins with sorting the command by commandTag, which divides comments into categories.
    def command_controller(self, command):
        # Retrieve a signal from dict whichs matches with the command tag
        signal = self.commandTagToSignal.get(command.tag)
        # Use that signal to get the key for the next dict
        handlerKey = self.router.get(signal)
        # handlerKey is now a command interpret by its tag which than got forwarded by a router to handle the command based on its categorie
        # How it gets handled is stored by an Enum which gets interpret below
        commandHandlerKey = self.commandHandler.get(handlerKey)
        if handlerKey == CommandHandler.META_COMMAND:
            return commandHandlerKey[command]
        if handlerKey == CommandHandler.OPTION_COMMAND:
            # Get current MenuState and store as key
            mSkey = self.stateController.menuState
            # Use MenuState as key for command handler dict
            # Store value as key for menu handler dict
            mHkey = commandHandlerKey[mSkey]
            # Use that key and command to access menu handler dict to return corresponding state
            return self.menuHandler[mHkey][command]
        # If it is a movement command the dict returns a tuple of movement commands with another key for next level dict to interpret the movement
        if handlerKey == CommandHandler.MOVEMENT_COMMAND:
            for command_tuple, handler in commandHandlerKey.items():
                if command in command_tuple:
                    movementKey = handler
            # This key is then used to return a callable of move_straight method
            handler = self.movementHandler.get(movementKey)
            # Call move method with command
            return handler(command)

    # Update engine based on player input
    def update(self):
        # Retriev states from state_controller class
        sc = self.stateController
        self.stateController.systemState = SystemState.OK
        # If init return since it is the first tic of game-loop and state_controller will proccess initial state
        if sc.gameState == GameState.INIT:
            return sc.gameState
        # Get user input from input_controller and store it as command
        self.command = self.inputController.process_input(sc.gameState, sc.menuState)
        # If input_controller does not return command return SystemState exception so Interface can outprint coresponding error message
        if self.command == None:
            return SystemState.EXCEPTION_INPUT_ERROR
        return self.command_controller(self.command) 
