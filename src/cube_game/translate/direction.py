from enums.commands import Command
from enums.geometry import Directions
import operator

command_direction = {
            Command.MOVE_FORWARD: (Directions.FORWARD, operator.le),
            Command.TURN_RIGHT: (Directions.RIGHT, operator.le),
            Command.MOVE_BACK: (Directions.BACK, operator.ge),
            Command.TURN_LEFT: (Directions.LEFT, operator.ge) 
            }
