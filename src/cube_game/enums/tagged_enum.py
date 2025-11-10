from enum import Enum, auto

class TaggedEnum(Enum):
    """Basisklasse für Enums mit (key, tag)-Struktur."""
    
    def __init__(self, key, tag):
        self._value_ = key
        self._tag_ = tag

    @property
    def key(self):
        return self._value_

    @property
    def tag(self):
        return self._tag_

    def __str__(self):
        return str(self._value_)