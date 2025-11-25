from data.position import Position
from enums.geometry import RoomColor, Corner, Moved, Edge, Faces, Facing
from data.door import Door
from data.room import Room
import random

class World:

    def __init__(self, game_context):
        self.game_context = game_context
        self.init_rooms()
        self.init_map()
        self.starting_room = self.front_room

    def init_rooms(self):
        self.bottom_room = Room(
            face = Faces.BOTTOM,
            color = RoomColor.YELLOW,
            width = 6,
            length = 6,
            pos = {
                Corner.BOTTOM_LEFT: Position(6,0),
                Corner.TOP_RIGHT: Position(12,6)
                },
            hex_color = "#F7E642",
            name = "Gelben Raum",
            neighbors = [
                Faces.FRONT,
                Faces.BACK,
                Faces.LEFT,
                Faces.RIGHT
            ],
            doors = [
                Door(leads_to = Faces.FRONT, entry_facing = None, pos=Position(8,6)),
                Door(leads_to = Faces.RIGHT, entry_facing = Facing.NORTH, pos=Position(12,4)),
                Door(leads_to = Faces.BACK, entry_facing = Facing.NORTH, pos=Position(8,0)),
                Door(leads_to = Faces.LEFT, entry_facing = Facing.NORTH, pos=Position(6,4))
                ]
            )
        self.top_room = Room(
            face = Faces.TOP,
            color = RoomColor.WHITE,
            width = 6,
            length = 6,
            pos = {
                Corner.BOTTOM_LEFT: Position(6,12),
                Corner.TOP_RIGHT: Position(12,18)
                },
            hex_color = "#FDFDFD",
            name = "Weißen Raum",
            neighbors = [
                Faces.BACK,
                Faces.RIGHT,
                Faces.LEFT,
                Faces.FRONT
            ],
            doors = [
                Door(leads_to = Faces.BACK, entry_facing = Facing.SOUTH, pos=Position(8,18)),
                Door(leads_to = Faces.RIGHT, entry_facing = Facing.SOUTH, pos=Position(12,16)),
                Door(leads_to = Faces.FRONT, entry_facing = None, pos=Position(8,12)),
                Door(leads_to = Faces.LEFT, entry_facing = Facing.SOUTH, pos=Position(6,16))   
            ]
        )
        self.front_room = Room(
            face = Faces.FRONT,
            color = RoomColor.GREEN,
            width = 6,
            length = 6,
            pos = {
                Corner.BOTTOM_LEFT: Position(6,6),
                Corner.TOP_RIGHT: Position(12,12)
                },
            hex_color = "#43A047",
            name = "Grünen Raum",
            neighbors = [
                Faces.TOP,
                Faces.RIGHT,
                Faces.LEFT,
                Faces.BOTTOM
            ],
            doors = [
                Door(leads_to = Faces.TOP, entry_facing = None, pos=Position(8,12)),
                Door(leads_to = Faces.RIGHT, entry_facing = None, pos=Position(12,8)),
                Door(leads_to = Faces.BOTTOM, entry_facing = None, pos=Position(8,6)),
                Door(leads_to = Faces.LEFT, entry_facing = None, pos=Position(6,8)) 
            ]
        )
        self.right_room = Room(
            face = Faces.RIGHT,
            color = RoomColor.RED,
            width = 6,
            length = 6,
            pos = {
                Corner.BOTTOM_LEFT: Position(12,6),
                Corner.TOP_RIGHT: Position(18,12)
                },
            hex_color = "#E53935",
            name = "Roten Raum",
            neighbors = [
                Faces.TOP,
                Faces.BACK,
                Faces.FRONT,
                Faces.BOTTOM
            ],
            doors = [
                Door(leads_to = Faces.TOP, entry_facing = Facing.WEST, pos=Position(15,12)),
                Door(leads_to = Faces.BACK, entry_facing = None, pos=Position(18,8)),
                Door(leads_to = Faces.BOTTOM, entry_facing = Facing.WEST, pos=Position(15,6)),
                Door(leads_to = Faces.FRONT, entry_facing = None, pos=Position(12,8))
            ]
        )
        self.back_room = Room(
            face = Faces.BACK,
            color = RoomColor.BLUE,
            width = 6,
            length = 6,
            pos = {
                Corner.BOTTOM_LEFT: Position(18,6),
                Corner.TOP_RIGHT: Position(24,12)
                },
            hex_color = "#1976D2",
            name = "Blauen Raum",
            neighbors = [
                Faces.TOP,
                Faces.LEFT,
                Faces.RIGHT,
                Faces.BOTTOM
            ],
            doors = [
                Door(leads_to = Faces.TOP, entry_facing = Facing.WEST, pos=Position(21,12)),
                Door(leads_to = Faces.LEFT, entry_facing = None, pos=Position(24,8)),
                Door(leads_to = Faces.BOTTOM, entry_facing = Facing.WEST, pos=Position(21,6)),
                Door(leads_to = Faces.RIGHT, entry_facing = None, pos=Position(18,8))
            ]
        )
        self.left_room = Room(
            face = Faces.LEFT,
            color = RoomColor.ORANGE,
            width = 6,
            length = 6,
            pos = {
                Corner.BOTTOM_LEFT: Position(0,6),
                Corner.TOP_RIGHT: Position(6,12)
                },
            hex_color = "#FF9800",
            name = "Orangen Raum",
            neighbors = [
                Faces.FRONT,
                Faces.BACK,
                Faces.TOP,
                Faces.BOTTOM
            ],
            doors = [ 
                Door(leads_to = Faces.TOP, entry_facing = Facing.EAST, pos = Position(3,12)),
                Door(leads_to = Faces.FRONT, entry_facing = None, pos = Position(6,8)),
                Door(leads_to = Faces.BOTTOM, entry_facing = Facing.EAST, pos = Position(3,6)),
                Door(leads_to = Faces.BACK, entry_facing = None, pos = Position(0,8))
            ]
        )
        ### DEBUG PRINT ###
        # print("Door-Setup Left Room:")
        # for i, d in enumerate(self.left_room.doors):
        #     print(i, d.leads_to, d.pos, id(d.pos))
        # print("Door-Setup Back Room:")
        # for i, d in enumerate(self.back_room.doors):
        #     print(i, d.leads_to, d.pos, id(d.pos))
        # print("Door-Setup top Room:")
        # for i, d in enumerate(self.top_room.doors):
        #     print(i, d.leads_to, d.pos, id(d.pos))
        # print("Door-Setup Bottom Room:")
        # for i, d in enumerate(self.bottom_room.doors):
        #     print(i, d.leads_to, d.pos, id(d.pos))
        # print("Door-Setup Right Room:")
        # for i, d in enumerate(self.right_room.doors):
        #     print(i, d.leads_to, d.pos, id(d.pos))
        # print("Door-Setup Front Room:")
        # for i, d in enumerate(self.front_room.doors):
        #     print(i, d.leads_to, d.pos, id(d.pos))

    
    def init_map(self):
        self.map_dict = {
            Faces.BOTTOM: self.bottom_room,
            Faces.TOP: self.top_room,
            Faces.FRONT: self.front_room,
            Faces.LEFT: self.left_room,
            Faces.BACK: self.back_room,
            Faces.RIGHT: self.right_room
        }
    
    def shuffle_map(self):
        room_pos = []
        for faces, room in self.map_dict.items():
            room_pos.append(room.pos)
        random.shuffle(room_pos)
        for (faces, room), new_pos in zip(self.map_dict.items(), room_pos):
            room.pos = new_pos
    
    def map(self, room):
        front = room
        left = self.left_room
        right = self.right_room
        top = self.top_room
        bottom  = self.bottom_room
        back = self.back_room
        gap = ""
        upper = [gap, top, gap, gap]
        middle = [left, front, right, back]
        lower = [gap, bottom, gap, gap]
        map = [upper, middle, lower]
        return map


    # Change room in wich player is located based on the neighbor room at the direction the player is facing
    def change_room(self, door):
        # Get Faces.ENUM of room behind door from doors.door.lead_to
        next_room_face = door.leads_to
        # Use Faces.ENUM as key to return Room object from map_dict{}
        next_room = self.game_context.world.map_dict.get(next_room_face)
        # Update Room where player is located now
        entry_pos = self.get_entry_pos(next_room)
        self.game_context.player.pos.x = entry_pos.x
        self.game_context.player.pos.y = entry_pos.y
        # Update room the player is currently inside
        self.game_context.player.current_room = next_room

    def has_door(self):
        ### DEBUG PRINT ###
        # print("Door-Setup Left Room:")
        # for i, d in enumerate(self.left_room.doors):
        #     print(i, d.leads_to, d.pos, id(d.pos))
        # print("Door-Setup Back Room:")
        # for i, d in enumerate(self.back_room.doors):
        #     print(i, d.leads_to, d.pos, id(d.pos))
        # print("Door-Setup top Room:")
        # for i, d in enumerate(self.top_room.doors):
        #     print(i, d.leads_to, d.pos, id(d.pos))
        # print("Door-Setup Bottom Room:")
        # for i, d in enumerate(self.bottom_room.doors):
        #     print(i, d.leads_to, d.pos, id(d.pos))
        # print("Door-Setup Right Room:")
        # for i, d in enumerate(self.right_room.doors):
        #     print(i, d.leads_to, d.pos, id(d.pos))
        # print("Door-Setup Front Room:")
        # for i, d in enumerate(self.front_room.doors):
        #     print(i, d.leads_to, d.pos, id(d.pos))
        doors: list = self.game_context.player.current_room.doors
        is_on_door = any(door.pos == self.game_context.player.pos for door in doors)
        return is_on_door
    
    def get_door(self):
        doors: list = self.game_context.player.current_room.doors
        matching_door = next(
            (door for door in doors if door.pos == self.game_context.player.pos),
            None
        )
        return matching_door
    
    def get_entry_pos(self, next_room):
        doors = next_room.doors
        current_room = self.game_context.player.current_room
        door = next(
            (door for door in doors if door.leads_to == current_room.face),
            None
        )
        return door.pos