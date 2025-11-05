from enums import Command, Directions
import operator

command_direction = {
            Command.MOVE_NORTH: (Directions.NORTH, operator.le),
            Command.MOVE_EAST: (Directions.EAST, operator.le),
            Command.MOVE_SOUTH: (Directions.SOUTH, operator.ge),
            Command.MOVE_WEST: (Directions.WEST, operator.ge) 
            }