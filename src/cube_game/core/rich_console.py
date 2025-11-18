from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from rich.text import Text
from rich.table import Table

from rich import box
from rich import print
from enums.geometry import Directions

class RichConsole:

    def __init__(self):
        self.console = Console

    def render_display_panel(self, txt):
        text = Text.from_markup(txt, justify="center")
        panel = Panel(
            text,
            box = box.DOUBLE_EDGE,
            padding = (0, 6),
            expand = False,
            border_style = "green", 
            style = "blue"
        )
        print(Align.center(panel))

    def render_menu_table(self,title, txt):
        table = Table(
            box = box.ROUNDED,
            padding = (0, 6),
            expand = False,
            style = "blue",
            border_style = "green",
            header_style = "bold red",
            row_styles = ["blue"] 
        )
        table.add_column(title)
        table.add_row(txt)
        print(Align.center(table))
    
    def render_navigation_table(self, title, headers, rows):
        table = Table(
            box = box.ROUNDED,
            padding = (0, 2), 
            border_style = "green",
            header_style = "bold red",
            row_styles = ["blue"]
        )
        self.render_display_panel(title)
        for header in headers:
            table.add_column(header)
        table.add_row(*rows)
        print(Align.center(table))
    
    def map_layout(self, map):
        face_size = 12
        table = Table.grid()
        for faces in map:
            row_cells = []
            for face in faces:
                if face == "":
                    row_cells.append(" " * (face_size * 2))
                else:
                    row_cells.append(
                        Panel(
                            " ",
                            border_style = face.hex_color,
                            box = box.HEAVY,
                            width = face_size * 2,
                            height = face_size,
                        )
                    )
            table.add_row(*row_cells)
        print(Align.center(table))
