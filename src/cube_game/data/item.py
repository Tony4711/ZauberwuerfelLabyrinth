from dataclasses import dataclass, field
from enums.objects import ItemType, ItemID
from data.position import Position

@dataclass
class Item:

    name: str
    descr: str
    item_type: ItemType = field(init=False)
    item_id: ItemID = field(default_factory=lambda:ItemID)
    pos: Position = field(default_factory=lambda:Position(-1,-1))
    


@dataclass
class KeyItem(Item):
    def __post_init__(self):
        self.item_type = ItemType.KEY 