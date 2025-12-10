from dataclasses import dataclass, field
from data.item import Item

@dataclass
class Inventory:

    size: int=field(default=10)
    items: list[Item]=field(default_factory=list)

    def add_item(self, item):
        if self.has_item(item):
            return False
        else:
            self.items.append(item)
            return True
    
    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
            return True
        else:
            return False
        
    def has_item(self, item):
        if item in self.items: 
            return True
        else: 
            return False
