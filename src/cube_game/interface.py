from enums import Command, Directions
from utility import Utility
from functools import lru_cache
from controls import Controls

class Interface:

    def __init__(self):
        self.controls = Controls()
        self.utility = Utility(self.controls)
    
    def read_input(self):
        from readchar import readkey, key
        input = readkey().lower().strip()
        return input
    
    def write_input(self, text):
        print(f"Eingabe: [{text}]\n".rjust(self.columns))

    def init_menu_structure(self):
        self.menu_structure = {
            "main_menu":{
            Command.OP1.value: "Spiel starten",
            Command.OP2.value: "Spiel verlassen",
            }
        }
                                         
    @lru_cache(maxsize=1)
    def hello(self):
        self.utility.print_dividing_line()
        self.utility.centered("--- Willkommen zu 'Gefangen im Zauberwürfel Labyrinth'! ---\n")
        self.utility.centered("--- Hauptmenü ---\n")
        self.utility.centered("--- Zum steuern bitte die in [ ] geschriebene Taste drücken ---\n")

    def show_controls(self):
        self.utility.print_dict(self.controls.get_dict("mapping"))

    # chore: add menu strg as paramter to use as key instead of hardcoding "main_menu"
    def show_menu_options(self):
        self.utility.print_dict(self.menu_structure, "main_menu")
    
    def show_map(self):
         self.utility.print_map(self.green_room, self.map_dict)
    
    def display_update(self):
        pas

    def print_map(self, room, map : dict):
       front = room.color
       left = self._lookup_neighbor(room, Directions.WEST)
       right = self._lookup_neighbor(room, Directions.EAST)
       up = self._lookup_neighbor(room, Directions.NORTH)
       down = self._lookup_neighbor(room, Directions.SOUTH)
       back = self._lookup_neighbor(map.get(right), Directions.EAST)

       print(f"              [{map.get(up).name}]") 
       print(f"[{map.get(left).name}][{map.get(front).name}][{map.get(right).name}][{map.get(back).name}]")
       print(f"              [{map.get(down).name}]\n")
       self.print_dividing_line()
    
    def print_pos(self, text, objekt):
        print(text, objekt.pos)