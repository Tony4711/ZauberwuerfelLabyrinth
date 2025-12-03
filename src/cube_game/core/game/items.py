from data.item import Item, KeyItem
from data.position import Position
from enums.interaction import ItemID

class Items:

    def __init__(self, game_context):
        self.game_context = game_context
        self._init_keys()
        

    def _init_keys(self):
        # Keys for the bottom room doors
        self.key_bottom_front = self._new_key(pos=Position(-1,-1), item_id=ItemID.KEY_DOOR_BOTTOM_FRONT)
        self.key_bottom_right = self._new_key(pos=Position(-1,-1), item_id=ItemID.KEY_DOOR_BOTTOM_RIGHT)
        self.key_bottom_back = self._new_key(pos=Position(-1,-1), item_id=ItemID.KEY_DOOR_BOTTOM_BACK)
        self.key_bottom_left = self._new_key(pos=Position(-1,-1), item_id=ItemID.KEY_DOOR_BOTTOM_LEFT)

        # Keys for the front room doors
        self.key_front_top = self._new_key(pos=Position(-1,-1), item_id=ItemID.KEY_DOOR_FRONT_TOP)
        self.key_front_right = self._new_key(pos=Position(-1,-1), item_id=ItemID.KEY_DOOR_FRONT_RIGHT)
        self.key_front_bottom = self._new_key(pos=Position(-1,-1), item_id=ItemID.KEY_DOOR_FRONT_BOTTOM)
        self.key_front_left = self._new_key(pos=Position(-1,-1), item_id=ItemID.KEY_DOOR_FRONT_LEFT)

        # Keys for the right room doors
        self.key_right_top = self._new_key(pos=Position(-1,-1), item_id=ItemID.KEY_DOOR_RIGHT_TOP)
        self.key_right_back = self._new_key(pos=Position(-1,-1), item_id=ItemID.KEY_DOOR_RIGHT_BACK)
        self.key_right_bottom = self._new_key(pos=Position(-1,-1), item_id=ItemID.KEY_DOOR_RIGHT_BACK)
        self.key_right_front = self._new_key(pos=Position(-1,-1), item_id=ItemID.KEY_DOOR_RIGHT_FRONT)
        
        # Keys for the back room doors
        self.key_back_top = self._new_key(pos=Position(-1,-1), item_id=ItemID.KEY_DOOR_BACK_TOP)
        self.key_back_front = self._new_key(pos=Position(-1,-1), item_id=ItemID.KEY_DOOR_BACK_LEFT)
        self.key_back_bottom = self._new_key(pos=Position(-1,-1), item_id=ItemID.KEY_DOOR_BACK_BOTTOM)
        self.key_back_right = self._new_key(pos=Position(-1,-1), item_id=ItemID.KEY_DOOR_BACK_RIGHT)
        
        # Keys for the left room doors
        self.key_left_top = self._new_key(pos=Position(-1,-1), item_id=ItemID.KEY_DOOR_LEFT_TOP)
        self.key_left_front = self._new_key(pos=Position(-1,-1), item_id=ItemID.KEY_DOOR_LEFT_FRONT)
        self.key_left_bottom = self._new_key(pos=Position(-1,-1), item_id=ItemID.KEY_DOOR_LEFT_BOTTOM)
        self.key_left_back = self._new_key(pos=Position(-1,-1), item_id=ItemID.KEY_DOOR_LEFT_BACK)
    
    def _new_key(self, item_id, pos):
        return KeyItem(item_id=item_id, pos=pos)