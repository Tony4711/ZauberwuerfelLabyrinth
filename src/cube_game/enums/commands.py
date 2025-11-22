from enum import Enum, auto
from enums.tagged_enum import TaggedEnum


class CommandTag(Enum):

    MOVEMENT = "Bewegung"
    META= "Meta"
    OPTION = "Auswahl"

class Command(TaggedEnum):

    MOVE_FORWARD = ("w", CommandTag.MOVEMENT)
    TURN_LEFT = ("a", CommandTag.MOVEMENT)
    MOVE_BACK = ("s", CommandTag.MOVEMENT)
    TURN_RIGHT = ("d", CommandTag.MOVEMENT) 
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


