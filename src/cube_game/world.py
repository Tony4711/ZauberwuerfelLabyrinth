from position import Position
from enums import RoomColor, Corner, Directions
from door import Door
from room import Room
import random

class World:

    def __init__(self):
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
        
    def calc_neighbor(self):
        pass

    def _lookup_neighbor(self, room, direction):
        target = room.neighbors.get(direction)
        if target is None:
            return None
        return target
    
    def map(self, room):
        front = room.color
        left = self._lookup_neighbor(room, Directions.WEST)
        right = self._lookup_neighbor(room, Directions.EAST)
        up = self._lookup_neighbor(room, Directions.NORTH)
        down = self._lookup_neighbor(room, Directions.SOUTH)
        back = self._lookup_neighbor(self.map_dict.get(right), Directions.EAST)
        display = (
            f"[{self.map_dict.get(up).name}]",
            f"          [{self.map_dict.get(left).name}][{self.map_dict.get(front).name}][{self.map_dict.get(right).name}][{self.map_dict.get(back).name}]",
            f"[{self.map_dict.get(down).name}]"
        )
        return display