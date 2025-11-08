import operator
from enums import CommandTag, Command, GameState, MenuState, PlayerState, Directions, RoomColor, Corner, RouterSignal

translate = {
            RouterSignal.COMMAND_TO_DIRECTION: {
            Command.MOVE_NORTH: (Directions.NORTH, operator.le),
            Command.MOVE_EAST: (Directions.EAST, operator.le),
            Command.MOVE_SOUTH: (Directions.SOUTH, operator.ge),
            Command.MOVE_WEST: (Directions.WEST, operator.ge) 
            },
            RouterSignal.DIRECTION_TO_OFFSET: {
            Directions.NORTH: (0,1),
            Directions.EAST: (1,0),
            Directions.SOUTH: (0, -1),
            Directions.WEST: (-1,0) 
            },
            RouterSignal.OFFSET_TO_CORNER: {
                (0,1): (Corner.TOP_RIGHT, lambda p: p.y),
                (1,0): (Corner.TOP_RIGHT, lambda p: p.x),
                (0,-1): (Corner.BOTTOM_LEFT, lambda p: p.y),
                (-1,0): (Corner.BOTTOM_LEFT, lambda p: p.x)
            },
            RouterSignal.HANDLE_COMMAND: {
                (GameState.MENU, MenuState.MAIN,Command.OP1): GameState.PLAYING, 
                (GameState.MENU, MenuState.MAIN,Command.OP2): MenuState.EXIT,
                (GameState.MENU, MenuState.EXIT,Command.OP1): GameState.EXIT,
                #(GameState.MAP, MenuState.EXIT, Command.OP2): GameState.BACK,
            }
}