from data.position import Position
from enums.geometry import RoomColor, Corner, Directions
from data.door import Door
from data.room import Room
import random

class World:

    def __init__(self, game_context):
        self.game_context = game_context
        self.init_rooms()
        self.init_map()
        self.starting_room = self.green_room

    def init_rooms(self):
        self.yellow_room = Room(
            color = RoomColor.YELLOW,
            width = 6,
            length = 6,
            pos = {
                Corner.BOTTOM_LEFT: Position(6,0),
                Corner.TOP_RIGHT: Position(12,6)
                },
            hex_color = "#F7E642",
            name = "Gelben Raum",
            neighbors = {
                Directions.NORTH: RoomColor.GREEN,
                Directions.EAST: RoomColor.RED,
                Directions.SOUTH: RoomColor.BLUE,
                Directions.WEST: RoomColor.ORANGE
                },
            doors = {
                Directions.NORTH: Door(leads_to=RoomColor.GREEN, pos=Position(8,6)),
                Directions.SOUTH: Door(leads_to=RoomColor.WHITE, pos=Position(8,0))
                }
            )
        self.white_room = Room(
            color = RoomColor.WHITE,
            width = 6,
            length = 6,
            pos = {
                Corner.BOTTOM_LEFT: Position(6,12),
                Corner.TOP_RIGHT: Position(12,18)
                },
            hex_color = "#FDFDFD",
            name = "Weißen Raum",
            neighbors = {
                Directions.NORTH: RoomColor.BLUE,
                Directions.EAST: RoomColor.RED,
                Directions.SOUTH: RoomColor.GREEN,
                Directions.WEST: RoomColor.ORANGE
            },
            doors = {
                Directions.SOUTH: Door(leads_to=RoomColor.GREEN, pos=Position(8,12)),
                Directions.NORTH: Door(leads_to=RoomColor.YELLOW, pos=Position(8,18))
            }
        )
        self.green_room = Room(
            color = RoomColor.GREEN,
            width = 6,
            length = 6,
            pos = {
                Corner.BOTTOM_LEFT: Position(6,6),
                Corner.TOP_RIGHT: Position(12,12)
                },
            hex_color = "#43A047",
            name = "Grünen Raum",
            neighbors = {
                Directions.NORTH: RoomColor.WHITE,
                Directions.EAST: RoomColor.RED,
                Directions.SOUTH: RoomColor.YELLOW,
                Directions.WEST: RoomColor.ORANGE
            },
            doors = {
                Directions.WEST: Door(leads_to=RoomColor.ORANGE , pos=Position(6,8)),
                Directions.EAST: Door(leads_to=RoomColor.RED, pos=Position(12,8)),
                Directions.NORTH: Door(leads_to=RoomColor.WHITE, pos=Position(8,12)),
                Directions.SOUTH: Door(leads_to=RoomColor.YELLOW, pos=Position(8,6))
            }
        )
        self.red_room = Room(
            color = RoomColor.RED,
            width = 6,
            length = 6,
            pos = {
                Corner.BOTTOM_LEFT: Position(12,6),
                Corner.TOP_RIGHT: Position(18,12)
                },
            hex_color = "#E53935",
            name = "Roten Raum",
            neighbors = {
                Directions.NORTH: RoomColor.WHITE,
                Directions.EAST: RoomColor.BLUE,
                Directions.SOUTH: RoomColor.YELLOW,
                Directions.WEST: RoomColor.GREEN
            },
            doors = {
                Directions.WEST: Door(leads_to=RoomColor.GREEN, pos=Position(12,8)),
                Directions.EAST: Door(leads_to=RoomColor.BLUE, pos=Position(18,8))
            }
        )
        self.blue_room = Room(
            color = RoomColor.BLUE,
            width = 6,
            length = 6,
            pos = {
                Corner.BOTTOM_LEFT: Position(18,6),
                Corner.TOP_RIGHT: Position(24,12)
                },
            hex_color = "#1976D2",
            name = "Blauen Raum",
            neighbors = {
                Directions.NORTH: RoomColor.WHITE,
                Directions.EAST: RoomColor.ORANGE,
                Directions.SOUTH: RoomColor.YELLOW,
                Directions.SOUTH: RoomColor.RED
            },
            doors = {
                Directions.WEST: Door(leads_to=RoomColor.RED, pos=Position(18,8)),
                Directions.EAST: Door(leads_to=RoomColor.ORANGE, pos=Position(24,8))

            }
        )
        self.orange_room = Room(
            color = RoomColor.ORANGE,
            width = 6,
            length = 6,
            pos = {
                Corner.BOTTOM_LEFT: Position(0,6),
                Corner.TOP_RIGHT: Position(6,12)
                },
            hex_color = "#FF9800",
            name = "Orangen Raum",
            neighbors = {
                Directions.NORTH: RoomColor.WHITE,
                Directions.EAST: RoomColor.GREEN,
                Directions.SOUTH: RoomColor.YELLOW,
                Directions.WEST: RoomColor.BLUE
            },
            doors = {
                Directions.WEST: Door(leads_to=RoomColor.BLUE, pos=Position(0,8)),
                Directions.EAST: Door(leads_to=RoomColor.GREEN, pos=Position(6,8))
            }
        )
    
    def init_map(self):
        self.map_dict = {
            RoomColor.YELLOW: self.yellow_room,
            RoomColor.WHITE: self.white_room,
            RoomColor.GREEN: self.green_room,
            RoomColor.ORANGE: self.orange_room,
            RoomColor.BLUE: self.blue_room,
            RoomColor.RED: self.red_room
        }
    
    def shuffle_map(self):
        room_pos = []
        for key, value in self.map_dict.items():
            room_pos.append(value.pos)
        random.shuffle(room_pos)
        for (color, room), new_pos in zip(self.map_dict.items(), room_pos):
            room.pos = new_pos


    def _lookup_neighbor(self, room, direction):
        target = room.neighbors.get(direction)
        if target is None:
            return None
        return target
    
    def map(self, room):
        front = room
        left = self.map_dict[self._lookup_neighbor(room, Directions.WEST)]
        right = self.map_dict[self._lookup_neighbor(room, Directions.EAST)]
        top = self.map_dict[self._lookup_neighbor(room, Directions.NORTH)]
        down = self.map_dict[self._lookup_neighbor(room, Directions.SOUTH)]
        back = self.map_dict[self._lookup_neighbor(self.map_dict.get(right.color), Directions.EAST)]
        gap = ""
        upper = [gap, top, gap, gap]
        middle = [left, front, right, back]
        lower = [gap, down, gap, gap]
        map = [upper, middle, lower]
        return map

    # If player coordinate goes out of bounce due to switching rooms that are neighbors but are not located next to each other in 2D map
    # the player coordinates get updated based on the current room and its two corner coordinates.
    # This works because the topology is handled seperatly from coordinates 
    ## CHORE: change hardcoded ints to values read from world to determine if a player is out of bounce
    def cube_wrap_around(self):
        if self.game_context.player.pos.x < 0:
            self.game_context.player.pos.x = self.game_context.player.current_room.pos[Corner.TOP_RIGHT].x
        if self.game_context.player.pos.x > 24:
            self.game_context.player.pos.x = self.game_context.player.current_room.pos[Corner.BOTTOM_LEFT].x
        if self.game_context.player.pos.y < 0:
            self.game_context.player.pos.y = self.game_context.player.current_room.pos[Corner.TOP_RIGHT].y
        if self.game_context.player.pos.y > 18:
            self.game_context.player.pos.y = self.game_context.player.current_room.pos[Corner.BOTTOM_LEFT].y

    # Change room in wich player is located based on the neighbor room at the direction the player is facing
    def change_room(self, direction):
        # Get RoomColor.ENUM of room behind door from doors{} dict by using Direction.ENUM as key to return door objekt and read leads_to parameter from it
        next_room_color = self.game_context.player.current_room.doors[direction].leads_to
        # Use RoomColor.ENUM as key to return Room object from map_dict{}
        next_room = self.game_context.world.map_dict.get(next_room_color)
        # Update direction player is looking
        self.game_context.player.direction = direction
        # Update Room where player is located now 
        self.game_context.player.current_room = next_room
        
    # Test if there is a door one step further of the player location in the facing direction
    def door_infront(self, direction):
        (dx, dy) = self.game_context.direction_to_offset[direction]
        infront = self.game_context.player.pos + (dx, dy)
        door = self.get_door(direction)
        if door == None:
            return False
        if infront == door.pos:
            return True 
        else: 
            False

    # Try to find a door at the direction the player is facing
    def get_door(self, direction):
        try:
            door = self.game_context.player.current_room.doors[direction]
        except KeyError:
            return None
        return door
