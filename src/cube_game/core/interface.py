from enums.commands import Command
from enums.geometry import Directions
from enums.states import GameState, MenuState, PlayerState, SystemState
from enums.display import Display, MenuPoints, DisplayNavigation, Menus, MainMenu, ExitMenu
from mapping import state_command_mapping
from translate.Interface import translate_game, translate_menu, translate_player, translate_system, router, display
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

    def __init__(self, gameContext):
        self.GameContext = gameContext
        self.window = WindowBuffer()
        self.router = router.routing
        self.renderDisplay = display
        self.menuToSignal = translate_menu.menuState_routerSignal
        self.gameToSignal = translate_game.gameState_routerSignal
        self.playerToSignal = translate_player.playerState_routerSignal
        self.systemToSignal = translate_system.systemState_routerSignal
        
        
        
    def show_pos(self, text, objekt):
        print(text, objekt.pos)

    def show_text(self, text):
        self.window.push()
        self.window.update(text)
        for line in text:
            self.GameContext.utility.centered(line)
        
    def _template(self):
        return {
            "navigation_command": Command.NAVIGATION.value.upper(),
            "player_direction": self.GameContext.player.direction.value,
            "current_room": self.GameContext.player.current_room.name,
            "map": self.GameContext.world.map(self.GameContext.starting_room)
        }

    def show_displayStrings(self, value):
        context = self._template()
        strg = ""
        strg += ",".join(value)
        strg = strg.format(**context)
        txt = self.GameContext.utility.format_text_in_box(strg, "^", "*")
        self.show_text(txt)
        print()
    
    def show_displayMenuStructure(self, value, state):
        txt = self.GameContext.utility.format_dict(value, state)
        menu = self.GameContext.utility.format_text_in_box(txt)
        menu_tuple = tuple(menu)
        self.show_text(menu_tuple)
    
    def show_displayNavigation(self, value, state):
        if state == MenuState.ALL_NAVIGATIONS:
            txt = self.GameContext.game_context.utility.format_dict(value[MenuState])
            txt += self.GameContext.utility.format_dict(value[GameState])
        else:
            previousState = self.GameContext.stateController.gameStack._previous_stateStack()
            if isinstance(previousState, MenuState):
                txt = self.GameContext.utility.format_dict(value[MenuState],previousState)
            else:
                txt = self.GameContext.utility.format_dict(value[GameState], previousState)
        menu = self.GameContext.utility.format_text_in_box(txt)
        menu_tuple = tuple(menu)
        self.show_text(menu_tuple)

    def _menuState_handler(self, menuState):
        m = {
            MenuState.MAIN: Menus.MAIN,
            MenuState.EXIT: Menus.EXIT
        }
        menu = m[menuState]
        option_string = ""
        option_tuple = (f"--- {menuState.value} ---",)
        i = 1
        for option in menu.value:
            option_string =  f"[{i}] {option.value}"
            i += 1
            option_tuple += (option_string,) 
        self.show_displayStrings(option_tuple)
        #self.display_controller(key, menuState)
        return 

    def gameState_handler(self, gameState):
        signal = self.gameToSignal.get(gameState)
        key = self.router.get(signal)
        self.display_controller(key, gameState)
        return

    def _playerState_handler(self, playerState):   
        signal = self.playerToSignal.get(playerState)
        key = self.router.get(signal)
        self.display_controller(key, playerState)
        return
    
    def _exception_handler(self, systemState):
        signal = self.systemToSignal.get(systemState)
        key = self.router.get(signal)
        self.display_controller(key, systemState)
        return
    
    def display_controller(self, key, state):
        rD =  self.renderDisplay.render()
        for section, subdict in rD.items():
            if key in subdict:
                d = {
                    MenuPoints: lambda value, state = None: self.show_displayMenuStructure(value, state),
                    DisplayNavigation: lambda value, state = None: self.show_displayNavigation(value, state)
                }
                value = subdict[key]
                handler = d.get(section)
                if handler:
                    handler(value, state)
                return
            else:
                self.show_displayStrings(key.string)
                return

    def update(self): 
        sc = self.GameContext.stateController
        if sc.systemState != SystemState.OK:
            return self._exception_handler(sc.systemState)
        if sc.gameState == GameState.MENU:
            return self._menuState_handler(sc.menuState)
        if sc.playerState != PlayerState.INIT:
            return self._playerState_handler(sc.playerState)
        return self.gameState_handler(sc.gameState)

