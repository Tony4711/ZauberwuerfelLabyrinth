from enums.states import GameState, PlayerState, SystemState
from enums.geometry import Corner

# Ein Spiel zum Verstehen der Grundmechaniken eines Rubiks Würfels.
# Der kleine Zauberer Garry ist in einem 3 dimensionalem Labyrinth gefangen und muss die Räume richtig miteinander verbinden, um herauszufinden.
# Dabei stößt er auf verschiedenste Rätsel und Herausforderungen, die ihm Helfen, den Zauberwürfel zu verstehen.

class Engine:

    def __init__(self, gameContext):
        self.game_context = gameContext
    
    # If player coordinate goes out of bounce due to switching rooms that are neighbors but are not located next to each other in 2D map
    # the player coordinates get updated based on the current room and its two corner coordinates.
    # This works because the topology is handled seperatly from coordinates 
    ## CHORE: change hardcoded ints to values read from world to determine if a player is out of bounce
    def _cube_wrap_around(self):
        if self.game_context.player.pos.x < 0:
            self.game_context.player.pos.x = self.game_context.player.current_room.pos[Corner.TOP_RIGHT].x
        if self.game_context.player.pos.x > 24:
            self.game_context.player.pos.x = self.game_context.player.current_room.pos[Corner.BOTTOM_LEFT].x
        if self.game_context.player.pos.y < 0:
            self.game_context.player.pos.y = self.game_context.player.current_room.pos[Corner.TOP_RIGHT].y
        if self.game_context.player.pos.y > 18:
            self.game_context.player.pos.y = self.game_context.player.current_room.pos[Corner.BOTTOM_LEFT].y

    # Change room in wich player is located based on the neighbor room at the direction the player is facing
    def _change_room(self, direction):
        # Get RoomColor.ENUM of room behind door from doors{} dict by using Direction.ENUM as key to return door objekt and read leads_to parameter from it
        next_room_color = self.game_context.player.current_room.doors[direction].leads_to
        # Use RoomColor.ENUM as key to return Room object from map_dict{}
        next_room = self.game_context.world.map_dict.get(next_room_color)
        # Update direction player is looking
        self.game_context.player.direction = direction
        # Update Room where player is located now 
        self.game_context.player.current_room = next_room
        
    # Test if there is a door one step further of the player location in the facing direction
    def _door_infront(self, direction):
        (dx, dy) = self.game_context.direction_to_offset[direction]
        infront = self.game_context.player.pos + (dx, dy)
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
            door = self.game_context.player.current_room.doors[direction]
        except KeyError:
            return None
        return door

    # Movement method with straigth steps for each direction.
    def move_straight(self, directional_command):
        # Use directional_command to translate into direction and comparison operator
        direction , op = self.game_context.command_to_direction[directional_command]
        # Use direction to translate into offset
        (dx,dy) = self.game_context.direction_to_offset[direction]
        # Use offset to translate into corner and axis lambda function
        corner, axis_func = self.game_context.offset_to_corner[(dx,dy)]
        # axis function for player position + offset
        player_axis_val = axis_func(self.game_context.player.pos + (dx, dy))
        # axis function for room position at corner
        room_axis_val   = axis_func(self.game_context.player.current_room.pos[corner])
        # try to find a door at the direction the player is facing and store it as local variable
        door = self._get_door(direction)
        #print(f"Door: {self.player.current_room.doors[direction].pos}")
        # Compare player position with borders of current room before moving
        if op(player_axis_val, room_axis_val):
            self.game_context.player.pos.move(dx,dy)
            self.game_context.player.direction = direction
            #print(f"Player: {self.player.pos}") #---DEBUG PRINT---
            #print(f"Room: {self.player.current_room.pos[corner]}") #---DEBUG PRINT---
            if self._door_infront(direction):
                self.game_context.player.pos.move(dx,dy)
                return PlayerState.DOOR
            else:
                return PlayerState.MOVE
        elif door is not None and self.game_context.player.pos == door.pos:
            self._change_room(direction)
            self.game_context.player.pos.move(dx,dy)
            self._cube_wrap_around()
            #print(f"Player: {self.player.pos}") #---DEBUG PRINT---
            return PlayerState.GO_DOOR
        else:
            return PlayerState.WALL

    # Update engine based on player input
    def update(self):
        # Retriev states from state_controller class
        sc = self.game_context.stateController
        self.game_context.stateController.systemState = SystemState.OK
        # If init return since it is the first tic of game-loop and state_controller will proccess initial state
        if sc.gameState == GameState.INIT:
            return sc.gameState
        # Get user input from input_controller and store it as command
        self.command = self.game_context.inputController.process_input(sc.gameState, sc.menuState)
        # If input_controller does not return command return SystemState exception so Interface can outprint coresponding error message
        if self.command == None:
            return SystemState.EXCEPTION_INPUT_ERROR
        return self.command_controller(self.command) 

