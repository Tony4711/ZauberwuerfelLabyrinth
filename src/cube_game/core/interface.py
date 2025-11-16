from enums.commands import Command
from enums.states import DisplayState
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

    def format_display(self, string_tuple):
        context = self.game_context.template(self.game_context)
        string = ""
        string += "\n".join(string_tuple)
        string = string.format(**context)
        self.game_context.console.render_welcome_panel(string)
    
    def create_menu(self, menu, menu_state):
        trans_key = self.game_context.template(self.game_context)
        lines = f"--- {menu_state.value} ---"
        for option in menu.value:
            key_char = option.name
            enum = option.value
            line =  f"[{'{' + key_char + '}' }] {enum}"
            lines += "\n" + line
            lines = lines.format(**trans_key)
        self.game_context.console.render_panel(lines)
    
    def create_navigation(self):
        state = self.game_context.previous_state
        trans_enum = self.game_context.template(self.game_context)
        state_command = self.game_context.state_command[type(state)][state]
        lines = f"--- {DisplayState.NAVIGATION.value} ---"
        for command in Command:
            key_char = command.value.upper()
            enum = command.name
            if state_command.get(command):
                line =  f"[bold blue][{key_char}] {'{' + enum + '}'}[/bold blue]"
            else:
                line =  f"[{key_char}] {'{' + enum + '}'}"
            lines += "\n" + line
            lines = lines.format(**trans_enum)
        self.game_context.console.render_panel(lines)
    
    ##CHORE
    def create_map(self):
        pass
