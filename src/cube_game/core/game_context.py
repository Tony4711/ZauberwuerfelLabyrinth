from enums.system import LoopSignal
from enums.geometry import Facing, Moved
from enums.states import GameState
from core.player_movement import PlayerMovement
from core.interface import Interface
from core.controller.input_controller import InputController
from core.controller.state_controller import StateController
from core.controller.command_controller import CommandController
from core.controller.display_controller import DisplayController
from core.world import World
from core.rich_console import RichConsole
from data.player import Player
from data.position import Position
from translate.command_controller import command_handler, command_router, movement_handler, menu_handler, commandtag_router_signal
from translate import opposite, turn, facing_op, facing_offset, offset_corner
from translate.interface import interface_router, game_state_router_signal, menu_state_router_signal, player_state_router_signal, system_state_router_signal, display_state_router_signal
from template import interface
from mapping import state_command

class GameContext:
    
    def __init__(self):
        
        # Main Objects
        self.running = LoopSignal.CONTINUE
        self.next_state = GameState.INIT
        self.previous_state = GameState.INIT
        self.player_movement = PlayerMovement(self)
        self.interface = Interface(self)
        self.console = RichConsole()

        # Game Objects
        self.world = World(self)
        self.starting_room = self.world.front_room
        self.player = self._new_player()

        # Controller
        self.input_controller = InputController(self)
        self.command_controller = CommandController(self)
        self.state_controller = StateController(self)
        self.display_controller = DisplayController(self)

        # Translate CommandHandler
        self.command_router = command_router.router
        self.commandtag_signal = commandtag_router_signal.router_signal
        self.command_handler = command_handler.handler()
        self.menu_handler = menu_handler.menu_option
        self.movement_handler = movement_handler.handler(self)

        # Translate
        self.facing_offset = facing_offset.offset
        self.offset_corner = offset_corner.corner
        self.opposite_facing = opposite.facing
        self.turn_left = turn.left
        self.turn_right = turn.right
        self.facing_op = facing_op.op

        # Translate Interface
        self.interface_router = interface_router.router(self)
        self.menu_state_signal = menu_state_router_signal.router_signal
        self.game_state_signal = game_state_router_signal.router_signal
        self.player_state_signal = player_state_router_signal.router_signal
        self.system_state_signal = system_state_router_signal.router_signal
        self.display_state_signal = display_state_router_signal.router_signal

        # Template
        self.template = interface.template

        # Mapping
        self.state_command = state_command.mapping

    
    def _new_player(self):
        return Player("Garry", Facing.NORTH, Moved.NONE, self.world.starting_room, Position(8,10))



