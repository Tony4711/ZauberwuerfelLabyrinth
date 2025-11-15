from enums.commands import Command
from enums.states import GameState, MenuState, PlayerState, SystemState
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
        self.game_context = gameContext
        self.window = WindowBuffer()      

    def show_pos(self, text, objekt):
        print(text, objekt.pos)

    def show_text(self, text):
        self.window.push()
        self.window.update(text)
        for line in text:
            self.game_context.utility.centered(line)
        return

    def _format_tuple(self, value):
        context = self.game_context.template(self.game_context)
        strg = ""
        strg += ",".join(value)
        strg = strg.format(**context)
        txt = self.game_context.utility.format_text_in_box(strg, "^", "*")
        self.show_text(txt)
        print()
    
    def _create_menu_tuple(self, menu, menu_state):
        trans_key = self.game_context.template(self.game_context)
        string = ""
        menu_tuple = (f"--- {menu_state.value} ---",)
        for option in menu.value:
            key_char = option.name
            enum = option.value
            string =  f"[{'{' + key_char + '}' }] {enum}"
            string = string.format(**trans_key)
            menu_tuple += (string,)
        self._format_tuple(menu_tuple)
    
    ##CHORE 
    def _navigation_tuple(self):
        pass
    
    ##CHORE
    def _map_tuple(self):
        pass
