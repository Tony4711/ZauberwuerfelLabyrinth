from enums.geometry import Facing

left = {
    Facing.NORTH: Facing.WEST,
    Facing.WEST:  Facing.SOUTH,
    Facing.SOUTH: Facing.EAST,
    Facing.EAST:  Facing.NORTH,
}

right = {
    Facing.NORTH: Facing.EAST,
    Facing.EAST:  Facing.SOUTH,
    Facing.SOUTH: Facing.WEST,
    Facing.WEST:  Facing.NORTH,
}
