from enums.system import LoopSignal
from enums.geometry import Directions
from enums.commands import Command
from core.engine import Engine
from core.interface import Interface
from core.input_controller import InputController
from core.state_controller import StateController
from core.world import World
from utils.utility import Utility
from data.player import Player
from data.door import Door
from data.room import Room
from data.position import Position


class GameContext:
    
    def __init__(self):
        
        # Main instances
        self.stateController = StateController(self)
        self.engine = Engine(self)
        self.interface = Interface(self)

        # Game Objects
        self.world = World()
        self.starting_room = self.world.green_room
        self.player = self._new_player()
        

        # Utils
        self.utility = Utility()
        self.inputController = InputController(self)

    
    def _new_player(self):
        return Player("Garry", Directions.NORTH, self.world.starting_room, Position(8,10))


