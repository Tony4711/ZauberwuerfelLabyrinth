from enums.states import PlayerState, InteractableState
from enums.commands import Command
from enums.geometry import Moved
from  enums.interaction_objects import Capabilities

# Ein Spiel zum Verstehen der Grundmechaniken eines Rubiks Würfels.
# Der kleine Zauberer Garry ist in einem 3 dimensionalem Labyrinth gefangen und muss die Räume richtig miteinander verbinden, um herauszufinden.
# Dabei stößt er auf verschiedenste Rätsel und Herausforderungen, die ihm Helfen, den Zauberwürfel zu verstehen.

class PlayerMovement:

    # Initialize movement handler with the shared game context.
    def __init__(self, game_context):
        self.game_context=game_context
    
    # Movement method with steps for each direction.
    # Advance the player in the requested direction, resolving interactions and walls.
    def move_player(self, directional_command):
        # Set facing from player as local variable for readebility
        facing=self.game_context.player.facing 
        facing=self._update_player_facing(directional_command, facing)
        # Use facing to get offset to determine which axis should increase oder decrease
        (dx,dy)=self.game_context.facing_offset[facing]
        if self._player_in_bound(facing):
            infront=self.game_context.player.pos + (dx,dy)
            interactable_infront=self._interactable_infront(infront)
            if interactable_infront:
                if self._blocking(interactable_infront):
                    return PlayerState.WALL
            self.game_context.player.pos.move(dx,dy)
            #CHORE above checks for an interactable infront of the player and below again calls the same method but after moving so it is an redundant calling but above can return None
            interactable=self.game_context.world.has_interactbale_on_pos(self.game_context.player.pos)
            if interactable: 
                return self.game_context.interaction.interact_with(interactable)
            return PlayerState.MOVE
        elif self.game_context.world.has_door():
            door=self.game_context.world.get_door()
            return self.game_context.interaction.process_door(door)
        else:
            return PlayerState.WALL
    
    # Rotate the player left or right and update movement state.
    def turn_player(self, directional_command):
        if directional_command==Command.TURN_LEFT:
            facing=self.game_context.turn_left[self.game_context.player.facing]
            self.game_context.player.moved=Moved.LEFT
        elif directional_command==Command.TURN_RIGHT:
            facing=self.game_context.turn_right[self.game_context.player.facing]
            self.game_context.player.moved=Moved.RIGHT
        self.game_context.player.facing=facing
        return PlayerState.TURN
    
    # Update player facing based on movement command, handling forward/back logic.
    def _update_player_facing(self, directional_command, facing):
        # If command is back use opposite facing of player
        if directional_command==Command.MOVE_BACK:
            self.game_context.player.moved=Moved.BACK
            facing=self.game_context.opposite_facing[facing]
            return facing
        else:
            self.game_context.player.facing=facing
            self.game_context.player.moved=Moved.FORWARD
            return facing
        
    # Validate that the intended move stays inside current room bounds.
    def _player_in_bound(self, facing):
        # Use facing to determine >, < operator
        op=self.game_context.facing_op[facing]
        (dx,dy)=self.game_context.facing_offset[facing]
        # Use offset to translate into corner and axis lambda function
        # Offset tells which axis gets manipulated so it is mapped to the axis of the corner
        # e.g. y decreases, which means border is an bottom wall so Corner.BOTTOM_LEFT is used
        # and since player moves on y-axis BOTTOM_LEFT: Position(y) is used
        corner, axis_func=self.game_context.offset_corner[(dx,dy)]
        # axis function for player position + offset
        player_axis_value=axis_func(self.game_context.player.pos + (dx,dy))
        # axis function for room position at corner
        room_axis_value=axis_func(self.game_context.player.current_room.pos[corner])
        # Compare player position with borders of current room before moving
        if op(player_axis_value, room_axis_value):
            return True
    
    def _interactable_infront(self, infront):
        interactable_infront=self.game_context.world.has_interactbale_on_pos(infront)
        return interactable_infront
    
    def _blocking(self, interactable):
        capabilities=interactable.capabilities
        is_blocking=any(capabile==Capabilities.BLOCKING for capabile in capabilities)
        return is_blocking
