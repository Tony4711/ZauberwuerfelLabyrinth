from enums.states import InteractableState, PlayerState
from  enums.interaction_objects import InteractionType, InteractionResult
from data.interactable import PressurePlate

class Interaction:

    def __init__(self, game_context):
        self.game_context = game_context

    def door(self, door):
        if door.state == InteractableState.OPEN:
            self._enter_room(door)
        elif door.state == InteractableState.CLOSED:
            if self.player_has_key(door):
                door.state = InteractableState.OPEN
                self._update_interaction_context(door.interactable_type, InteractionType.UNLOCK)
                #return PlayerState.DOOR_UNLOCKED
            else:
                self._update_interaction_context(door.interactable_type, InteractionType.LOCKED)
                #return PlayerState.BLOCKED
        return PlayerState.INTERACTION
    
    def player_has_key(self, interactable):
        if self.game_context.player.inventory.has_item(interactable.req_key):
            return True
        else:
            return False
    
    def _enter_room(self, door):
        # check if door has an entry facing value
        if door.entry_facing:
                self.game_context.player.facing = door.entry_facing
        self.game_context.world.change_room(door)
        self._update_interaction_context(target_obj=door.interactable_type, interaction_type=InteractionType.WALK_THROUGH, interaction_result=InteractionResult.ENTER)
        #return PlayerState.ENTER_ROOM

    def _pressure_plate_interaction(self, pressure_plate):
        pressure_plate.state = InteractableState.PRESSED
        self._update_interaction_context(pressure_plate.interactable_type, InteractionType.STANDING_ON, InteractionResult.ADD_ITEM)
        self.game_context.player.inventory.add_item(self.game_context.items.key_front_top)
    
    def _update_interaction_context(self, target_obj, interaction_type, interaction_result = None):
        self.game_context.interaction_context.target_object = target_obj
        self.game_context.interaction_context.interaction_type = interaction_type
        self.game_context.interaction_context.interaction_result = interaction_result

    def interact_with(self, interactable):
        handler = {
            PressurePlate:self._pressure_plate_interaction
        }
        func = handler.get(type(interactable))
        if func:
            func(interactable)