from enums.states import GameState, PlayerState, SystemState
from enums.geometry import Corner

# Ein Spiel zum Verstehen der Grundmechaniken eines Rubiks Würfels.
# Der kleine Zauberer Garry ist in einem 3 dimensionalem Labyrinth gefangen und muss die Räume richtig miteinander verbinden, um herauszufinden.
# Dabei stößt er auf verschiedenste Rätsel und Herausforderungen, die ihm Helfen, den Zauberwürfel zu verstehen.

class PlayerMovement:

    def __init__(self, gameContext):
        self.game_context = gameContext
    
    # Movement method with steps for each direction.
    def move_player(self, directional_command):
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
        door = self.game_context.world.get_door(direction)
        #print(f"Door: {self.player.current_room.doors[direction].pos}")
        # Compare player position with borders of current room before moving
        if op(player_axis_val, room_axis_val):
            self.game_context.player.pos.move(dx,dy)
            self.game_context.player.direction = direction
            #print(f"Player: {self.player.pos}") #---DEBUG PRINT---
            #print(f"Room: {self.player.current_room.pos[corner]}") #---DEBUG PRINT---
            if self.game_context.world.door_infront(direction):
                self.game_context.player.pos.move(dx,dy)
                return PlayerState.DOOR
            else:
                return PlayerState.MOVE
        elif door is not None and self.game_context.player.pos == door.pos:
            self.game_context.world.change_room(direction)
            self.game_context.player.pos.move(dx,dy)
            self.game_context.world.cube_wrap_around()
            #print(f"Player: {self.player.pos}") #---DEBUG PRINT---
            return PlayerState.GO_DOOR
        else:
            return PlayerState.WALL


