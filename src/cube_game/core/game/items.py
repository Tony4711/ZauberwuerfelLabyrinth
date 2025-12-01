from data.item import Item, KeyItem

class Items:

    def __init__(self, game_context):
        self.game_context = game_context
        self.key_top_room = self._new_key(name="Schlüssel Top Raum", descr= "Ein Schlüssel zum öffnen der Tür")

    
    def _new_item(self, id, name, descr):
        return Item(id, name, descr)
    
    def _new_key(self, name, descr):
        return KeyItem(name, descr)