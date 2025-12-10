from enum import Enum, auto

class Moved(Enum):

    RIGHT="rechts"
    LEFT="links"
    BACK="hinten"
    FORWARD="vorn"
    NONE="none"

class Facing(Enum):
    
    NORTH="Norden"
    EAST="Osten"
    SOUTH="Süden"
    WEST="Westen"

class RoomColor(Enum):
    
    YELLOW="Gelben"
    WHITE="Weißen"
    GREEN="Grünen"
    ORANGE="Orangenen"
    BLUE="Blauen"
    RED="Roten"
    
class Corner(Enum):

    BOTTOM_LEFT=auto()
    TOP_RIGHT=auto()

class Edge(Enum):

    LEFT_FRONT=[(6,12),(6,6)]
    FRONT_RIGHT=[(12,12),(12,6)]
    RIGHT_BACK=[(18,12),(18,6)]
    FRONT_TOP=[(12,12),(6,12)]
    BOTTOM_FRONT=[(12,6),(6,6)]
    BOTTOM_BACK=[(6,0),(18,6)]
    BACK_TOP=[(24,12),(12,18)]
    LEFT_BACK=[(0,6),(24,12)]
    RIGHT_TOP=[(18,12),(12,12)]
    LEFT_TOP=[(6,12),(24,12)]
    RIGHT_BOTTOM=[(12,6),(18,6)]
    LEFT_BOTTOM=[(0,6),(6,6)]

class Faces(Enum):

    BOTTOM=[Edge.LEFT_BOTTOM, Edge.BOTTOM_FRONT, Edge.RIGHT_BOTTOM, Edge.BOTTOM_BACK]
    TOP=[Edge.BACK_TOP, Edge.LEFT_TOP, Edge.FRONT_TOP, Edge.RIGHT_TOP]
    FRONT=[Edge.FRONT_TOP, Edge.FRONT_RIGHT, Edge.LEFT_FRONT, Edge.BOTTOM_FRONT]
    RIGHT=[Edge.RIGHT_TOP, Edge.RIGHT_BACK, Edge.RIGHT_BOTTOM, Edge.FRONT_RIGHT]
    BACK=[Edge.BACK_TOP, Edge.LEFT_BACK, Edge.RIGHT_BACK, Edge.BOTTOM_BACK]
    LEFT=[Edge.LEFT_BACK, Edge.LEFT_BOTTOM, Edge.LEFT_FRONT, Edge.LEFT_TOP]
    