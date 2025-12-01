from enums.states import DoorState, PlayerState

class Interaction:

    def __init__(self, game_context):
        self.game_context = game_context

    def door(self, door):
        self.game_context.interaction_context.target_object = door.type
        if door.state == DoorState.OPEN:
            return self._enter_door(door)
        elif door.state == DoorState.CLOSED:
                if self.open_interactable(door):
                    door.state = DoorState.OPEN
                    self.game_context.interaction_context.target_object = door.req_key.id
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
        return PlayerState.ROOM_ENTRANCE
        