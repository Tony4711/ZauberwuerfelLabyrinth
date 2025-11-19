from enum import Enum, auto
from enums.tagged_enum import TaggedEnum


class CommandTag(Enum):

    MOVEMENT = "Bewegung"
    META= "Meta"
    OPTION = "Auswahl"

class Command(TaggedEnum):

    MOVE_NORTH = ("w", CommandTag.MOVEMENT)
    MOVE_WEST = ("a", CommandTag.MOVEMENT)
    MOVE_SOUTH = ("s", CommandTag.MOVEMENT)
    MOVE_EAST = ("d", CommandTag.MOVEMENT) 
    OP1 = ("1", CommandTag.OPTION)
    OP2 = ("2", CommandTag.OPTION)
    OP3 = ("3", CommandTag.OPTION)
    OP4 = ("4", CommandTag.OPTION)
    BACK = ("q", CommandTag.META)
    FORTH = ("e", CommandTag.META)
    EXIT = ("x", CommandTag.META)
    OPEN_MAP = ("m", CommandTag.META)
    NAVIGATION = ("c", CommandTag.META)
    SHUFFLE_MAP = ("y", CommandTag.META)


