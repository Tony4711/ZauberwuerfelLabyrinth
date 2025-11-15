import readchar
import shutil
from enums.states import GameState, MenuState
from enums.geometry import Directions, RoomColor
from enums.commands import Command

class Utility:

    def __init__(self) -> None:
        self.columns, self.rows = shutil.get_terminal_size()

    def format_dict(self, dictname : dict, key = None):
        dict_display = ""
        # Wenn ein state vorhanden ist
        if key:
            # Gebe alle child Daten des parent keys aus
            dict_display += "--- " + key.value + " ---, ," 
            for key, value in dictname[key].items():
                key_str = str(getattr(key, "value", key))
                dict_display += (f"[{key_str.upper()}] {value}") + ","
        else:
            # Ansonsten gebe alle Daten des dict aus
            for key, value in dictname.items():
                key_str = str(getattr(key, "value", key))
                dict_display += "," + (f"[{key_str}]")
                for key, description in value.items():
                    key_str = str(getattr(key, "value", key))
                    dict_display += "," +(f"[{key_str.upper()}] {description}")
                dict_display += ","
        return dict_display

    # Credits: https://www.reddit.com/r/learnpython/comments/1c19y94/comment/kz25chm/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button
    def format_text_in_box(self, txt: str, top: str = "^", side: str = "*", margin: int = 4):
        display_list = []
        if len(top) != 1:
            raise ValueError("'top' must be a single character")
        margin_width = margin
        horizontal_border_char = top
        vertical_border_char = side
        lines = txt.split(',')
        max_line_length = max(len(line) for line in lines)
        max_line_length += 2 * margin_width
        horizontal_border = (
            vertical_border_char +
            horizontal_border_char * max_line_length +
            vertical_border_char
        )
        display_list.append(horizontal_border)
        for line in lines:
            # Calculate margin widths.
            left_margin = (max_line_length - len(line)) // 2
            right_margin = max_line_length - (len(line) + left_margin)
            formatted_line = (
                f"{vertical_border_char}"
                f"{' ' * left_margin}{line}{' ' * right_margin}"
                f"{vertical_border_char}"
            )
            display_list.append(formatted_line)
        display_list.append(horizontal_border)
        return display_list
    
    def centered(self, text: str):
        print(text.center(self.columns))
    
    def print_dividing_line(self):
        print(f"_"*self.columns)
