from rich.console import Console, Group
from rich.panel import Panel
from rich.align import Align
from rich.text import Text
from rich.table import Table
from rich.layout import Layout
from rich.live import Live
from rich import box
from core.controller.state_controller import StateStack

class RichConsole:

    def __init__(self):
        self.console = Console()
        self.layout = self._build_layout()
        self.live: Live | None = None
        self.history_stack = StateStack(None)
        self.history_stack.state_stack = []  # start empty
        self.max_history_items = 10
        self.map_cell_size = 6
        self._ensure_live()

    def _build_layout(self) -> Layout:
        layout = Layout(name="root")
        layout.split_row(
            Layout(name="left", ratio=1),
            Layout(name="right", ratio=2)
        )
        layout["left"].update(Align.center(Text()))
        layout["right"].update(Align.center(Text()))
        return layout

    def _ensure_live(self):
        if self.live is None:
            self.live = Live(self.layout, console=self.console, refresh_per_second=10, auto_refresh=False)
        if not getattr(self.live, "started", False):
            self.live.start()

    def _update_section(self, section_name: str, renderable):
        self._ensure_live()
        if section_name == "map":
            # allow map to consume full width/height of the right layout
            self.layout["right"].update(renderable)
        elif section_name in {"navigation", "inventory"}:
            vertical_centered = Align.center(renderable, vertical="middle")
            self.layout["right"].update(vertical_centered)
        elif section_name in {"menu", "display"}:
            self._update_history_stack(renderable)
        else:
            vertical_centered = Align.center(renderable, vertical="middle")
            self.layout["right"].update(vertical_centered)
        if self.live:
            self.live.update(self.layout, refresh=True)

    def _update_history_stack(self, renderable):
        # newest at bottom, drop oldest when exceeding history
        self.history_stack._push_state_stack(renderable)
        if len(self.history_stack.state_stack) > self.max_history_items:
            self.history_stack.state_stack.pop(0)
        self.layout["left"].update(Group(*self.history_stack.state_stack))

    def __del__(self):
        if self.live and getattr(self.live, "started", False):
            self.live.stop()
        
    def render_inventory(self, inventory:list):
        table = Table(
            box = box.ROUNDED,
            padding = (0, 2), 
            expand=True,
            border_style = "green",
            header_style = "bold red",
            row_styles = ["blue"]
        )
        table.add_column("Item")
        table.add_column("Beschreibung")
        for item in inventory:
            (item_type, item_descr, item_id) = item
            table.add_row(item_type, f"{item_descr} {item_id}")
        self._update_section("inventory", table)
        

    def render_display_panel(self, txt):
        text = Text.from_markup(txt, justify="center")
        panel = Panel(
            text,
            box = box.ROUNDED,
            padding = (0, 6),
            expand = False,
            border_style = "green", 
            style = "blue"
        )
        self._update_section("display", Align.center(panel))

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
        self._update_section("menu", Align.center(table))
    
    def render_navigation_table(self, headers, rows):
        table = Table(
            box = box.ROUNDED,
            padding = (0, 2), 
            border_style = "green",
            header_style = "bold red",
            row_styles = ["blue"]
        )
        for header in headers:
            table.add_column(header)
        table.add_row(*rows)
        self._update_section("navigation", Align.center(table))
    
    def render_map(self, map):
        table = Table.grid(padding=0, expand=True)
        max_cols = max((len(faces) for faces in map), default=0)
        for _ in range(max_cols):
            table.add_column(ratio=1)
        for faces in map: 
            row_cells = [] 
            for face in faces: 
                if face == "":
                    row_cells.append("") 
                else: 
                    row_cells.append( 
                        Panel( 
                            self.build_coord_grid(self.map_cell_size),
                            box = box.MINIMAL, 
                            style= f"on {face.hex_color}", 
                            expand = True, 
                            padding = 0
                        ) 
                    ) 
            table.add_row(*row_cells) 
        self._update_section("map", table)
            
    def build_coord_grid(self, size): 
        table = Table( 
            show_header=False, 
            show_lines=True, 
            padding=0, 
            pad_edge=False,
            box=box.DOUBLE, 
            expand=True, 
            border_style="black"
        ) 
        for _ in range(size): 
            table.add_column() 
        for _ in range(size): 
            table.add_row() 
        return table
