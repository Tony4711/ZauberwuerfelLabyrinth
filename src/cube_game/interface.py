from enums import Command, Directions, GameState, MenuState, PlayerState, SystemState, RouterSignal, DisplayKey, OutputFunction
from utility import Utility
from functools import lru_cache
from mapping import mapping
from translate.Interface import translate_game, translate_menu, translate_player


class Interface:

    def __init__(self, StateController, Engine):
        from translate.Interface import router, display
        self.router = router.init(self)
        self.display = display
        self.menu_routerSignal = translate_menu.menuState_routerSignal
        self.game_routerSignal = translate_game.gameState_routerSignal
        self.player_routerSignal = translate_player.playerState_routerSignal
        self.stateController = StateController
        self.engine = Engine
        self.utility = Utility()
        self.init_menu_structure()
        self.utility.print_dividing_line()

    def show_pos(self, text, objekt):
        print(text, objekt.pos)

    def show_controls(self, state = None):
        self.utility.print_dict(mapping, state)

    def _menuState_handler(self, menuState):
        signal = self.menu_routerSignal.get(menuState)
        key = self.router.get(signal)
        self.displayController(key, menuState)
        return

    def show_text(self, text):
        for line in text:
            self.utility.centered(line)
        self.utility.print_dividing_line()

    def gameState_handler(self, gameState):
        signal = self.game_routerSignal.get(gameState)
        key = self.router.get(signal)
        self.displayController(key, gameState)
        return

    def _playerState_handler(self, playerState):   
        signal = self.player_routerSignal.get(playerState)
        key = self.router.get(signal)
        self.displayController(key, playerState)
        return
    
    ### CHORE: refactor to use new translate_system.py and displayController
    def _exception_handler(self, systemState):
        if systemState == SystemState.EXCEPTION_INPUT_ERROR:
            self.show_input_exception()
    
    def displayController(self, key, state):
        for section, subdict in self.display.init(self.engine).items():
            if key in subdict:
                value = subdict[key]
                if section is DisplayKey:
                    self.show_text(value)
                elif section is OutputFunction:
                    self.utility.print_dict(value, state)

    def update(self):
        gameState = self.stateController.gameState
        menuState = self.stateController.menuState
        systemState = self.stateController.systemState
        playerState = self.stateController.playerState 
        if systemState != SystemState.OK:
            self._exception_handler(systemState)
            return
        elif gameState == GameState.MENU:
            self._menuState_handler(menuState)
            return
        elif playerState != PlayerState.INIT:
            self._playerState_handler(playerState)
            return
        else:
            self.gameState_handler(gameState)
            return


