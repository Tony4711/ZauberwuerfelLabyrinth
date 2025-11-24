from enums.geometry import Facing, Faces

facing = {
            Facing.NORTH: Facing.SOUTH,
            Facing.SOUTH: Facing.NORTH,
            Facing.EAST: Facing.WEST,
            Facing.WEST: Facing.EAST
        }

faces = {
    Faces.TOP: Faces.BACK,
    Faces.BACK: Faces.TOP,
    Faces.LEFT: Faces.RIGHT,
    Faces.RIGHT: Faces.LEFT
}