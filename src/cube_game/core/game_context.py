from enums.system import LoopSignal
from enums.geometry import Directions
from enums.states import GameState
from core.player_movement import PlayerMovement
from core.interface import Interface
from core.controller.input_controller import InputController
from core.controller.state_controller import StateController
from core.controller.command_controller import CommandController
from core.controller.display_controller import DisplayController
from core.world import World
from utils.utility import Utility
from data.player import Player
from data.position import Position
from translate.command_controller import command_handler, command_router, translate_commandTag, movement_handler, menu_handler
from translate import offset, geometry, direction
from translate.interface import translate_game, translate_menu, translate_player, translate_system, interface_router
from template import interface

class GameContext:
    
    def __init__(self):
        
        # Main instances
        self.running = LoopSignal.CONTINUE
        self.next_state = GameState.INIT
        self.player_movement = PlayerMovement(self)
        self.interface = Interface(self)

        # Game Objects
        self.world = World(self)
        self.starting_room = self.world.green_room
        self.player = self._new_player()

        # Utils
        self.utility = Utility()

        # Controller
        self.input_controller = InputController(self)
        self.command_controller = CommandController(self)
        self.state_controller = StateController(self)
        self.display_controller = DisplayController(self)

        # Translate CommandHandler
        self.command_router = command_router.routing
        self.commandtag_to_signal = translate_commandTag.commandtag_router_signal
        self.command_handler = command_handler.handler()
        self.menu_handler = menu_handler.menu_option
        self.movement_handler = movement_handler.handler(self)

        # Translate Engine
        self.direction_to_offset = offset.offset_translate
        self.offset_to_corner = geometry.corner_translate
        self.command_to_direction = direction.command_direction

        # Translate Interface
        self.interface_router = interface_router.routing
        self.menu_to_signal = translate_menu.menuState_routerSignal
        self.game_to_signal = translate_game.gameState_routerSignal
        self.player_to_signal = translate_player.playerState_routerSignal
        self.system_to_signal = translate_system.systemState_routerSignal

        # Template
        self.template = interface.template

    
    def _new_player(self):
        return Player("Garry", Directions.NORTH, self.world.starting_room, Position(8,10))



