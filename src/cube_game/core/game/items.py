from data.item import Item, KeyItem
from data.position import Position
from enums.objects import ItemID

class Items:

    def __init__(self, game_context):
        self.game_context = game_context
        self.key_top_room = self._new_key(item_id=ItemID.TOP_KEY, name=ItemID.TOP_KEY.value, descr="Ein Schlüssel zum öffnen einer Tür")
        self.key_bottom_room = self._new_key(item_id=ItemID.BOTTOM_KEY, name=ItemID.BOTTOM_KEY.value, descr="Ein Schlüssel zum öffnen einer Tür")

    
    def _new_item(self, item_id, name, descr):
        return Item(item_id, name, descr)
    
    def _new_key(self, item_id, name, descr):
        return KeyItem(item_id, name, descr)