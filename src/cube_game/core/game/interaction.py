from enums.states import InteractableState, PlayerState
from enums.interaction import InteractionType, InteractionResult
from data.interactable import PressurePlate

class Interaction:

    def __init__(self, game_context):
        self.game_context = game_context

    def door(self, door):
        self.game_context.interaction_context.target_object = door.interactable_type
        if door.state == InteractableState.OPEN:
            return self._enter_door(door)
        elif door.state == InteractableState.CLOSED:
            if self.open_interactable(door):
                door.state = InteractableState.OPEN
                self.game_context.interaction_context.target_object = door.req_key.item_type
                return PlayerState.DOOR_UNLOCKED
            else:
                return PlayerState.BLOCKED
    
    def open_interactable(self, interactable):
        if self.game_context.player.inventory.has_item(interactable.req_key):
            return True
        else:
            return False
    
    def _enter_door(self, door):
        if door.entry_facing:
                self.game_context.player.facing = door.entry_facing
        self.game_context.world.change_room(door)
        return PlayerState.ENTER_ROOM

    def _pressure_plate_interaction(self, pressure_plate):
        pressure_plate.state = InteractableState.PRESSED
        self._update_interaction_context(pressure_plate, InteractionType.STANDING_ON, InteractionResult.ADD_ITEM)
        self.game_context.player.inventory.add_item(self.game_context.items.key_front_top)
        self.game_context.player.inventory.add_item(self.game_context.items.key_front_bottom)
    
    def _update_interaction_context(self, target_obj, interaction_type, interaction_result):
        self.game_context.interaction_context.target_object = target_obj.interactable_type
        self.game_context.interaction_context.interaction_type = interaction_type
        self.game_context.interaction_context.interaction_result = interaction_result

    def interact_with(self, interactable):
        handler = {
            PressurePlate:self._pressure_plate_interaction
        }
        func = handler.get(type(interactable))
        if func:
            func(interactable)