from enums.geometry import Facing
import operator

op={
    Facing.NORTH: operator.le,
    Facing.EAST: operator.le,
    Facing.SOUTH: operator.ge,
    Facing.WEST: operator.ge 
}