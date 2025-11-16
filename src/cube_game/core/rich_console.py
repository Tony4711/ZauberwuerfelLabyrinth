from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from rich.text import Text

from rich import box
from rich import print

class RichConsole:

    def __init__(self):
        self.console = Console

    def render_welcome_panel(self, txt):
        panel = Panel(
            Text(txt, justify = "center"),
            box = box.DOUBLE_EDGE,
            padding = (0, 6),
            expand = False,
            style = "green", 
        )
        print(Align.center(panel))

    def render_panel(self, txt):
        panel = Panel(
            txt,
            box = box.DOUBLE_EDGE,
            padding = (0, 6),
            expand = False,
            style = "green", 
        )
        print(Align.center(panel))
