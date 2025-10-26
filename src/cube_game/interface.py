from enums import Command, Directions, GameState, MenuState
from utility import Utility
from functools import lru_cache
from mapping import mapping

class Interface:

    def __init__(self, StateManager):
        self.stateManager = StateManager
        self.utility = Utility()
        self.init_menu_structure()
        
    
    def read_input(self):
        from readchar import readkey, key
        input = readkey().lower().strip()
        return input
    
    def write_input(self, text):
        print(f"Eingabe: [{text}]\n".rjust(self.utility.columns))

    def init_menu_structure(self):
        self.menu_structure = {
            MenuState.MAIN: {
                Command.OP1.value: "Spiel starten",
                Command.OP2.value: "Spiel verlassen",
            },
            MenuState.SETTINGS: {

            }
        }
                                         
    @lru_cache(maxsize=1)
    def hello(self):
        self.utility.print_dividing_line()
        self.utility.centered("--- Willkommen zu 'Gefangen im Zauberwürfel Labyrinth'! ---\n")
        self.utility.centered("--- Hauptmenü ---\n")
        self.utility.centered("--- Zum steuern bitte die in [ ] geschriebene Taste drücken ---\n")

    @lru_cache(maxsize=1)
    def start(self):
        self.utility.centered("--- Spiel wird gestartet ---\n")
        self.utility.centered(f"--- Bitte nutze [{Command.CONTROLS.value.upper()}] um dir die Steuerung anzeigen zu lassen ---\n")
       
    
    def show_controls(self):
        self.utility.print_dict(mapping)

    def show_menu_options(self, menu: str):
        self.utility.print_dict(self.menu_structure, menu)
    
    def show_map(self):
         self.utility.print_map(self.green_room, self.map_dict)
    
    def update(self):
        gameState = self.stateManager.gameState
        menuState = self.stateManager.menuState
        if gameState == GameState.INIT:
            self.hello()
        elif gameState == GameState.MENU:
            if menuState == MenuState.MAIN:
                self.show_menu_options(MenuState.MAIN)
            elif menuState == MenuState.CONTROLS:
                self.show_controls()
            elif menuState == MenuState.SETTINGS:
                self.show_menu_options(MenuState.SETTINGS)
        elif gameState == GameState.PLAYING:
            self.start()

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
