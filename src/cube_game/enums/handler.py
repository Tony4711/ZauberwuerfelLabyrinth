from enum import Enum, auto

class CommandHandler(Enum):

    META_COMMAND=auto()
    MOVEMENT_COMMAND=auto()
    OPTION_COMMAND=auto()

class MenuOptionHandler(Enum):

    MAIN=auto()
    EXIT=auto()

class MovementHandler(Enum):
    
    MOVE=auto()
    TURN=auto()