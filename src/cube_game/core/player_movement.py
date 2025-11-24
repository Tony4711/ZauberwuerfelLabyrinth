from enums.states import PlayerState
from enums.commands import Command
from enums.geometry import Moved

# Ein Spiel zum Verstehen der Grundmechaniken eines Rubiks Würfels.
# Der kleine Zauberer Garry ist in einem 3 dimensionalem Labyrinth gefangen und muss die Räume richtig miteinander verbinden, um herauszufinden.
# Dabei stößt er auf verschiedenste Rätsel und Herausforderungen, die ihm Helfen, den Zauberwürfel zu verstehen.

class PlayerMovement:

    def __init__(self, gameContext):
        self.game_context = gameContext
    
    # Movement method with steps for each direction.
    def move_player(self, directional_command):
        # Set facing from player as local variable for readebility
        facing = self.game_context.player.facing
        # If command is back use opposite facing of player 
        if directional_command == Command.MOVE_BACK:
            facing = self.game_context.opposite_facing[facing]
            self.game_context.player.moved = Moved.BACK
        else:
            self.game_context.player.facing = facing
            self.game_context.player.moved = Moved.FORWARD
        # Use facing to determine >, < operator
        op = self.game_context.facing_op[facing]
        # Use facing to get offset to determine which axis should increase oder decrease
        (dx,dy) = self.game_context.facing_offset[facing]
        # Use offset to translate into corner and axis lambda function
        # Offset tells which axis gets manipulated so it is mapped to the axis of the corner
        # e.g. y decreases, which means border is an bottom wall so Corner.BOTTOM_LEFT is used
        # and since player moves on y-axis BOTTOM_LEFT: Position(y) is used
        corner, axis_func = self.game_context.offset_corner[(dx,dy)]
        # axis function for player position + offset
        player_axis_val = axis_func(self.game_context.player.pos + (dx, dy))
        # axis function for room position at corner
        room_axis_val   = axis_func(self.game_context.player.current_room.pos[corner])
        # try to find a door at the direction the player is facing and store it as local variable
        door = self.game_context.world.get_door()
        # Compare player position with borders of current room before moving
        if op(player_axis_val, room_axis_val):
            self.game_context.player.pos.move(dx,dy)
            print(f"Player: {self.game_context.player.pos}") #---DEBUG PRINT---
            #print(f"Room: {self.game_context.player.current_room.doors[direction]}") #---DEBUG PRINT---
            return PlayerState.MOVE
        elif self.game_context.world.has_door():
            self.game_context.world.change_room(door)
            print(f"Player: {self.game_context.player.pos}") #---DEBUG PRINT---
            #print(f"Player after room switch: {self.game_context.player.pos}") #---DEBUG PRINT---
            #print(f"Player direction: {self.game_context.player.direction}") #---DEBUG PRINT---
            return PlayerState.ROOM_ENTRANCE
        else:
            return PlayerState.WALL
    
    def turn_player(self, directional_command):
        if directional_command == Command.TURN_LEFT:
            facing = self.game_context.turn_left[self.game_context.player.facing]
            self.game_context.player.moved = Moved.LEFT
        elif directional_command == Command.TURN_RIGHT:
            facing = self.game_context.turn_right[self.game_context.player.facing]
            self.game_context.player.moved = Moved.RIGHT
        self.game_context.player.facing = facing
        return PlayerState.TURN