from dataclasses import dataclass, field
from enums.objects import ItemID

@dataclass
class Item:

    id: ItemID = field(init=False)
    name: str
    descr: str

    def use(self, item_id):
        if item_id == self.id: 
            return True 
        else: 
            return False

@dataclass
class KeyItem(Item):
    def __post_init__(self):
        self.id = ItemID.KEY 