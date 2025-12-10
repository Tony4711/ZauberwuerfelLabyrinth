from data.position import Position
from enums.geometry import RoomColor, Corner, Faces, Facing
from data.interactable import Door, PressurePlate, Obstacle
from data.room import Room
from enums.states import InteractableState
from  enums.interaction_objects import InteractableID, Capabilities
import random

class World:

    def __init__(self, game_context):
        self.game_context=game_context
        self.init_rooms()
        self.init_map()
        self.starting_room=self.front_room

    def init_rooms(self):
        self.bottom_room=Room(
            face=Faces.BOTTOM,
            color=RoomColor.YELLOW,
            width=6,
            length=6,
            pos={
                Corner.BOTTOM_LEFT: Position(6,0),
                Corner.TOP_RIGHT: Position(12,6)
                },
            hex_color="#F7E642",
            value="Gelben Raum",
            neighbors=[
                Faces.FRONT,
                Faces.BACK,
                Faces.LEFT,
                Faces.RIGHT
            ],
            doors=[
                Door(interactable_id=InteractableID.DOOR_BOTTOM_FRONT, leads_to=Faces.FRONT, entry_facing=None, pos=Position(8,6)),
                Door(interactable_id=InteractableID.DOOR_BOTTOM_RIGHT, leads_to=Faces.RIGHT, entry_facing=Facing.NORTH, pos=Position(12,4)),
                Door(interactable_id=InteractableID.DOOR_BOTTOM_BACK, leads_to=Faces.BACK, entry_facing=Facing.NORTH, pos=Position(8,0)),
                Door(interactable_id=InteractableID.DOOR_BOTTOM_LEFT, leads_to=Faces.LEFT, entry_facing=Facing.NORTH, pos=Position(6,4))
                ]
            )
        self.top_room=Room(
            face=Faces.TOP,
            color=RoomColor.WHITE,
            width=6,
            length=6,
            pos={
                Corner.BOTTOM_LEFT: Position(6,12),
                Corner.TOP_RIGHT: Position(12,18)
                },
            hex_color="#FDFDFD",
            value="Weißen Raum",
            neighbors=[
                Faces.BACK,
                Faces.RIGHT,
                Faces.LEFT,
                Faces.FRONT
            ],
            doors=[
                Door(interactable_id=InteractableID.DOOR_TOP_BACK, leads_to=Faces.BACK, entry_facing=Facing.SOUTH, pos=Position(8,18)),
                Door(interactable_id=InteractableID.DOOR_TOP_RIGHT, leads_to=Faces.RIGHT, entry_facing=Facing.SOUTH, pos=Position(12,16)),
                Door(interactable_id=InteractableID.DOOR_TOP_FRONT, leads_to=Faces.FRONT, entry_facing=None, pos=Position(8,12)),
                Door(interactable_id=InteractableID.DOOR_TOP_LEFT, leads_to=Faces.LEFT, entry_facing=Facing.SOUTH, pos=Position(6,16))   
            ]
        )
        self.front_room=Room(
            face=Faces.FRONT,
            color=RoomColor.GREEN,
            width=6,
            length=6,
            pos={
                Corner.BOTTOM_LEFT: Position(6,6),
                Corner.TOP_RIGHT: Position(12,12)
                },
            hex_color="#43A047",
            value="Grünen Raum",
            neighbors=[
                Faces.TOP,
                Faces.RIGHT,
                Faces.LEFT,
                Faces.BOTTOM
            ],
            doors=[
                Door(interactable_id=InteractableID.DOOR_FRONT_TOP, leads_to=Faces.TOP, entry_facing=None, req_key=self.game_context.items.key_front_top, state=InteractableState.CLOSED, pos=Position(8,12)),
                Door(interactable_id=InteractableID.DOOR_BOTTOM_RIGHT, leads_to=Faces.RIGHT, entry_facing=None, pos=Position(12,8)),
                Door(interactable_id=InteractableID.DOOR_FRONT_BOTTOM, leads_to=Faces.BOTTOM, entry_facing=None, pos=Position(8,6)),
                Door(interactable_id=InteractableID.DOOR_FRONT_LEFT, leads_to=Faces.LEFT, entry_facing=None, pos=Position(6,8)) 
            ]
        )
        self.right_room=Room(
            face=Faces.RIGHT,
            color=RoomColor.RED,
            width=6,
            length=6,
            pos={
                Corner.BOTTOM_LEFT: Position(12,6),
                Corner.TOP_RIGHT: Position(18,12)
                },
            hex_color="#E53935",
            value="Roten Raum",
            neighbors=[
                Faces.TOP,
                Faces.BACK,
                Faces.FRONT,
                Faces.BOTTOM
            ],
            doors=[
                Door(interactable_id=InteractableID.DOOR_RIGHT_TOP, leads_to=Faces.TOP, entry_facing=Facing.WEST, pos=Position(15,12)),
                Door(interactable_id=InteractableID.DOOR_RIGHT_BACK, leads_to=Faces.BACK, entry_facing=None, pos=Position(18,8)),
                Door(interactable_id=InteractableID.DOOR_RIGHT_BOTTOM, leads_to=Faces.BOTTOM, entry_facing=Facing.WEST, pos=Position(15,6)),
                Door(interactable_id=InteractableID.DOOR_RIGHT_FRONT, leads_to=Faces.FRONT, entry_facing=None, pos=Position(12,8))
            ]
        )
        self.back_room=Room(
            face=Faces.BACK,
            color=RoomColor.BLUE,
            width=6,
            length=6,
            pos={
                Corner.BOTTOM_LEFT: Position(18,6),
                Corner.TOP_RIGHT: Position(24,12)
                },
            hex_color="#1976D2",
            value="Blauen Raum",
            neighbors=[
                Faces.TOP,
                Faces.LEFT,
                Faces.RIGHT,
                Faces.BOTTOM
            ],
            doors=[
                Door(interactable_id=InteractableID.DOOR_BACK_TOP, leads_to=Faces.TOP, entry_facing=Facing.WEST, pos=Position(21,12)),
                Door(interactable_id=InteractableID.DOOR_BACK_LEFT, leads_to=Faces.LEFT, entry_facing=None, pos=Position(24,8)),
                Door(interactable_id=InteractableID.DOOR_BACK_BOTTOM, leads_to=Faces.BOTTOM, entry_facing=Facing.WEST, pos=Position(21,6)),
                Door(interactable_id=InteractableID.DOOR_BACK_RIGHT, leads_to=Faces.RIGHT, entry_facing=None, pos=Position(18,8))
            ]
        )
        self.left_room=Room(
            face=Faces.LEFT,
            color=RoomColor.ORANGE,
            width=6,
            length=6,
            pos={
                Corner.BOTTOM_LEFT: Position(0,6),
                Corner.TOP_RIGHT: Position(6,12)
                },
            hex_color="#FF9800",
            value="Orangen Raum",
            neighbors=[
                Faces.FRONT,
                Faces.BACK,
                Faces.TOP,
                Faces.BOTTOM
            ],
            doors=[ 
                Door(interactable_id=InteractableID.DOOR_LEFT_TOP, leads_to=Faces.TOP, entry_facing=Facing.EAST, pos=Position(3,12)),
                Door(interactable_id=InteractableID.DOOR_LEFT_FRONT, leads_to=Faces.FRONT, entry_facing=None, pos=Position(6,8)),
                Door(interactable_id=InteractableID.DOOR_LEFT_BOTTOM, leads_to=Faces.BOTTOM, entry_facing=Facing.EAST, pos=Position(3,6)),
                Door(interactable_id=InteractableID.DOOR_LEFT_BACK, leads_to=Faces.BACK, entry_facing=None, pos=Position(0,8)),
            ],
            interactables=[
                PressurePlate(interactable_id=InteractableID.PRESSURE_PLATE_LEFT, pos=Position(4,8)),
                Obstacle(interactable_id=InteractableID.OBSTACLE_LEFT, pos=Position(5,8), capabilities=[Capabilities.IS_MOVEABLE]),
            ]
        )

    def init_map(self):
        self.map_dict={
            Faces.BOTTOM: self.bottom_room,
            Faces.TOP: self.top_room,
            Faces.FRONT: self.front_room,
            Faces.LEFT: self.left_room,
            Faces.BACK: self.back_room,
            Faces.RIGHT: self.right_room
        }
    
    def shuffle_room_color(self):
        room_colors=[]
        color_theme=[]
        for _ , room in self.map_dict.items():
            color_theme=[room.color, room.hex_color, room.value]
            room_colors.append(color_theme)
        random.shuffle(room_colors)
        for (_ , room), (color, hex_color, value)  in zip(self.map_dict.items(), room_colors):
            room.color=color
            room.hex_color=hex_color
            room.value=value
    
    def map(self, room):
        front=room
        left=self.left_room
        right=self.right_room
        top=self.top_room
        bottom =self.bottom_room
        back=self.back_room
        gap=""
        upper=[gap, top, gap, gap]
        middle=[left, front, right, back]
        lower=[gap, bottom, gap, gap]
        map=[upper, middle, lower]
        return map


    # Change room in wich player is located based on the neighbor room at the direction the player is facing
    def change_room(self, door):
        # Get Faces.ENUM of room behind door from door.leads_to
        next_room_face=door.leads_to
        # Use Faces.ENUM as key to return Room object from map_dict{}
        next_room=self.game_context.world.map_dict.get(next_room_face)
        # Update Room where player is located now
        entry_pos=self.get_entry_pos(next_room)
        self.game_context.player.pos.x=entry_pos.x
        self.game_context.player.pos.y=entry_pos.y
        # Update room the player is currently inside
        self.game_context.player.current_room=next_room

    def has_door(self):
        doors: list=self.game_context.player.current_room.doors
        is_on_door=any(door.pos==self.game_context.player.pos for door in doors)
        return is_on_door
    
    def get_door(self):
        doors: list=self.game_context.player.current_room.doors
        matching_door=next(
            (door for door in doors if door.pos==self.game_context.player.pos),
            None
        )
        return matching_door
    
    def get_entry_pos(self, next_room):
        doors=next_room.doors
        current_room=self.game_context.player.current_room
        door=next(
            (door for door in doors if door.leads_to==current_room.face),
            None
        )
        return door.pos
    
    def has_interactbale_on_player(self):
        interactables: list=self.game_context.player.current_room.interactables
        matching_interactable=next(
            (interactable for interactable in interactables if interactable.pos==self.game_context.player.pos),
            None
        )
        return matching_interactable

    def get_interactable(self, interactable_type):
        interactables: list=self.game_context.player.current_room.interactables
        matching_interactable=next(
            (interactable for interactable in interactables if type(interactable)==interactable_type),
            None
        )
        return matching_interactable