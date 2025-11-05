from enums import Command, Directions, GameState, MenuState, PlayerState, SystemState, RouterSignal, DisplayStrings, DisplayMenuStructure, DisplayControls
from utils.utility import Utility
from mapping import state_command_mapping
from translate.Interface import translate_game, translate_menu, translate_player, translate_system
import os


class WindowBuffer:

    def __init__(self):
        self.stack = []
        self.current = []

    def push(self):
        self.stack.append(self.current)

    def pop(self):
        if self.stack:
            self.stack.pop()

    def update(self, lines):
        self.current = lines

    def render(self):
        os.system('cls')
        for line in self.current:
            return line

class Interface:

    def __init__(self, StateController, Engine):
        from translate.Interface import router, display
        self.router = router.init(self)
        self.display = display
        self.menu_routerSignal = translate_menu.menuState_routerSignal
        self.game_routerSignal = translate_game.gameState_routerSignal
        self.player_routerSignal = translate_player.playerState_routerSignal
        self.system_routerSignal = translate_system.systemState_routerSignal
        self.stateController = StateController
        self.engine = Engine
        self.utility = Utility()
        self.window = WindowBuffer()

    def show_pos(self, text, objekt):
        print(text, objekt.pos)

    def show_controls(self, state = None):
        self.utility.format_dict(state_command_mapping, state)

    def show_text(self, text):
        self.window.push()
        self.window.update(text)
        for line in text:
            self.utility.centered(line)
    
    def show_table(self, left, right):
        self.window.push()
        self.window.update(left)
        self.window.update(right)
        

    def _menuState_handler(self, menuState):
        signal = self.menu_routerSignal.get(menuState)
        key = self.router.get(signal)
        self.displayController(key, menuState)
        return

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
    
    def _exception_handler(self, systemState):
        signal = self.system_routerSignal.get(systemState)
        key = self.router.get(signal)
        self.displayController(key, systemState)
        return
    
    def displayController(self, key, state):
        for section, subdict in self.display.init(self.engine).items():
            if key in subdict:
                value = subdict[key]
                if section is DisplayStrings:
                    t = ""
                    t += ",".join(value)
                    txt = self.utility.format_text_in_box(t, "^", "*")
                    self.show_text(txt)
                    print()
                elif section is DisplayMenuStructure:
                    txt = self.utility.format_dict(value, state)
                    menu = self.utility.format_text_in_box(txt)
                    menu_tuple = tuple(menu)
                    self.show_text(menu_tuple)
                elif section is DisplayControls:
                    if state == MenuState.ALL_CONTROLS:
                        txt = self.utility.format_dict(value[MenuState])
                        txt += self.utility.format_dict(value[GameState])
                    else:
                        self.stateController.gameStack._pop_stateStack()
                        previousState = self.stateController.gameStack._current_stateStack()
                        if isinstance(previousState, MenuState):
                            txt = self.utility.format_dict(value[MenuState],previousState)
                        else:
                            txt = self.utility.format_dict(value[GameState], previousState)
                    menu = self.utility.format_text_in_box(txt)
                    menu_tuple = tuple(menu)
                    self.show_text(menu_tuple)

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


