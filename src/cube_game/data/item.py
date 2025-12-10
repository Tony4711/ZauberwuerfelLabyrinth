from dataclasses import dataclass, field
from  enums.interaction_objects import ItemType, ItemID
from data.position import Position

@dataclass
class Item:

    pos: Position
    item_id: ItemID

@dataclass
class KeyItem(Item):
    
    descr: str=field(default="Ein Schlüssel zum öffnen einer Tür")
    item_type: ItemType=field(default=ItemType.KEY) 