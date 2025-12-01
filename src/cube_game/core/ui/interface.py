from enums.commands import Command
from enums.states import DisplayFunction, GameState
from enums.display import Display
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

    def __init__(self, game_context):
        self.game_context = game_context
        self.window = WindowBuffer()      

    def format_display(self, string_tuple):
        context = self.game_context.template(self.game_context)
        string = ""
        string += "\n".join(string_tuple)
        string = string.format(**context)
        self.game_context.console.render_display_panel(string)
    
    def format_menu(self, menu, menu_state):
        trans_key = self.game_context.template(self.game_context)
        lines = ""
        title = f"--- {menu_state.value} ---"
        for option in menu.value:
            key_char = option.name
            enum = option.value
            line =  f"[[yellow]{'{' + key_char + '}' }[/]] {enum}"
            lines += line + "\n" 
            lines = lines.format(**trans_key)
        lines = lines.rstrip("\n")
        self.game_context.console.render_menu_table(title,lines)
    
    def format_navigation(self):
        state = self.game_context.state_controller.game_stack._current_state_stack()
        if state == GameState.MENU: 
            state = self.game_context.state_controller.menu_stack._current_state_stack()
        trans_enum = self.game_context.template(self.game_context)
        title = f"--- {DisplayFunction.NAVIGATION.value} ---"
        lines = None
        headers = []
        rows = []
        for command in Command:
            header = command.tag.value
            if header not in headers: 
                headers.append(header)
                if lines:
                    rows.append(lines.rstrip("\n"))
                lines = ""
            line = self._format_state_command(state, command)
            lines += line + "\n"
            lines = lines.format(**trans_enum)
        rows.append(lines.rstrip("\n"))
        self.game_context.console.render_navigation_table(title, headers, rows)
    
    def _format_state_command(self, state, command):
        state_command = self._try_state_command(state)
        key_char = command.value.upper()
        enum = command.name
        if state_command and state_command.get(command):
            line = f"[[yellow]{key_char}[/]] [bold underline cyan]{'{' + enum + '}'}[/]"
            return line
        else:
            line = f"[[yellow]{key_char}[/]] {'{' + enum + '}'}"
            return line

    
    def _try_state_command(self, state):
        try:
            state_command = self.game_context.state_command[type(state)][state]
            return state_command
        except:
            KeyError
            return None
        
    def format_map(self):
        map = self.game_context.world.map(self.game_context.starting_room)
        self.game_context.console.map_layout(map)
    
    def shuffle_room_color(self):
        self.game_context.world.shuffle_room_color()
        self.format_map()