from enums.states import InteractableState, PlayerState
from enums.interaction_objects import InteractableID
from  enums.interaction_objects import InteractionType, InteractionResult

class Interaction:

    # Initialize interaction handler with the shared game context.
    def __init__(self, game_context):
        self.game_context=game_context

    # Process door interaction: enter if open, attempt to unlock if closed.
    def door(self, door):
        # If door is open enter room
        if door.state==InteractableState.OPEN:
            self._enter_room(door)
        # If door is closed/locked check if player has key in inventory to unlock the door
        elif door.state==InteractableState.CLOSED:
            if self.player_has_key(door):
                # If inventory has key unlock door and update interaction_context therefore
                door.state=InteractableState.OPEN
                self._update_interaction_context(door.interactable_type, InteractionType.UNLOCK)
            else:
                # Else update interaction_context to indicate player needs a key
                self._update_interaction_context(target_obj=door.interactable_type, interaction_type=InteractionType.LOCKED, interaction_result=InteractionResult.KEY_REQ)
        # Return interaction state so display_controller knows player interacted with something
        return PlayerState.INTERACTION
    
    # Simple method for better readebility
    # Return True if the player inventory holds the required key for the target.
    def player_has_key(self, interactable):
        return self.game_context.player.inventory.has_item(interactable.req_key)
    
    # Move the player through the door into the linked room and set facing if needed.
    def _enter_room(self, door):
        if door.entry_facing:
                self.game_context.player.facing=door.entry_facing
        self.game_context.world.change_room(door)
        self._update_interaction_context(target_obj=door.interactable_type, interaction_type=InteractionType.WALK_THROUGH, interaction_result=InteractionResult.ENTER_ROOM)

    # Try to add an item to the player's inventory and update the interaction result
    # if the item is already present.
    # If item was added call interface to display new item in inventory.
    def _update_inventory(self, item):
        added=self.game_context.player.inventory.add_item(item)
        if not added:
            self.game_context.interaction_context.interaction_result=InteractionResult.ALLREADY_IN_INVENTORY
        else: 
            self.game_context.interface.format_inventory()

    # Set the given interactable to a new state.
    def _update_interactable_state(self, interactable, new_state):
        interactable.state=new_state

    # Record the latest interaction target, type, and optional result in shared context.
    def _update_interaction_context(self, target_obj, interaction_type, interaction_result=None):
        self.game_context.interaction_context.target_object=target_obj
        self.game_context.interaction_context.interaction_type=interaction_type
        self.game_context.interaction_context.interaction_result=interaction_result
    
    # Trigger side effects tied to an interaction result (e.g., awarding items).
    def _interaction_event(self, interaction_result, event_obj):
        handler={
            InteractionResult.ADD_ITEM: lambda: self._update_inventory(event_obj)
        }
        func=handler.get(interaction_result)
        if func:
            func()
    
    # Generic interaction flow applying state change, context update, and side effects.
    def _interaction(self, interactable, context):
        (interactable_state, interaction_type, interaction_result, event_obj)=context
        self._update_interactable_state(interactable, interactable_state)
        self._update_interaction_context(target_obj=interactable.interactable_type, interaction_type=interaction_type, interaction_result=interaction_result)
        self._interaction_event(interaction_result, event_obj)

    
    # Entry point: route interactable to its handler and return player interaction state.
    def interact_with(self, interactable):
        # Dict with ID of interactable as key and context tuple as value
        handler={
            InteractableID.PRESSURE_PLATE_LEFT: (
                InteractableState.PRESSED, 
                InteractionType.STANDING_ON, 
                InteractionResult.ADD_ITEM, 
                self.game_context.items.key_front_top
            )
        }
        interaction_context=handler.get(interactable.interactable_id)
        if interaction_context:
            self._interaction(interactable=interactable, context=interaction_context)
            return PlayerState.INTERACTION
        else:
            return PlayerState.INTERACTION_EXCEPTION
