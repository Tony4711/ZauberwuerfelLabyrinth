from dataclasses import dataclass, field
from enums.system import LoopSignal
from core.engine import Engine
from core.interface import Interface
from core.input_controller import InputController
from core.state_controller import StateController
from core.world import World
from utils.utility import Utility
from data.player import Player
from data.door import Door
from data.room import Room
from translate.Interface.router import Router
from translate.Interface.display import Display
from translate.Interface.translate_game import TranslateGame
from translate.Interface.translate_menu import TranslateMenu
from translate.Interface.translate_player import TranslatePlayer
from translate.Interface.translate_system import TranslateSystem
from translate.Engine.router import Router
from translate.Engine.movement_handler import Handler
from translate.Engine.command_handler import Handler
from translate.Engine.menu_handler import Handler
from translate.Engine.translate_commandTag import Handler
from translate.Engine.translate_direction import Hnadler
from translate.Engine.translate_geometry import Handler
from translate.Engine.translate_offset import Handler

@dataclass
class GameContext:
    
    # Core instances
    interface: Interface = field(init=False)
    engine: Engine = field(init=False)
    stateController: StateController = field(init=False)
    input_controller: InputController = field(init=False)
    world: World = field(init=False)
    
    # dataclasses
    player: Player = field(init=False)
    door: Door = field(init=False)
    room: Room = field(init=False)

    # Utils
    utility: Utility = field(init=False)

    # Translation Interface
    router: Router = field(init=False)
    renderDisplay: Display = field(init=False)
    gameToSignal: TranslateGame = field(init=False)
    menuToSignal: TranslateMenu = field(init=False)
    playerToSignal: TranslatePlayer = field(init=False)
    systemToSignal: TranslateSystem = field(init=False)

    # Translation Engine
    router: Router

