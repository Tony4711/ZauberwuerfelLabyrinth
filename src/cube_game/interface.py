from enums import Command, Directions, GameState, MenuState, PlayerState
from utility import Utility
from functools import lru_cache
from mapping import mapping

class Interface:

    def __init__(self, StateManager, Engine):
        self.stateManager = StateManager
        self.engine = Engine
        self.utility = Utility()
        self.init_menu_structure()

    def init_menu_structure(self):
        self.menu_structure = {
            MenuState.MAIN: {
                Command.OP1.value: "Spiel starten",
                Command.OP2.value: "Spiel verlassen",
            },
            MenuState.SETTINGS: {

            },
            MenuState.EXIT: {
                Command.OP1.value: "Ja",
                Command.OP2.value: "Nein"
            }
        }

    def show_map(self, room, map : dict):
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
    
    def show_pos(self, text, objekt):
        print(text, objekt.pos)

    @lru_cache(maxsize=1)
    def show_hello(self):
        self.utility.print_dividing_line()
        self.utility.centered("--- Willkommen zu 'Gefangen im Zauberwürfel Labyrinth'! ---\n")
        self.utility.centered("--- Hauptmenü ---\n")
        self.utility.centered("--- Zum steuern bitte die in [ ] geschriebene Taste drücken ---\n")

    @lru_cache(maxsize=1)
    def show_start(self):
        self.utility.centered("--- Spiel wird gestartet ---\n")
        self.utility.centered(f"--- Bitte nutze [{Command.CONTROLS.value.upper()}] um dir die Steuerung anzeigen zu lassen ---\n")    
    
    def show_controls(self):
        self.utility.print_dict(mapping)

    def show_menu_options(self, menu: str):
        self.utility.print_dict(self.menu_structure, menu)
    
    def show_map(self):
        self.utility.print_map(self.green_room, self.map_dict)

    def show_exit_menu(self):
        self.utility.centered(f"--- Spiel wirklich beenden? ---\n")
    
    def show_exit_confirmed(self):
        self.utility.centered(f"--- Spiel wird beendet ---")
    
    def show_move(self):
        self.utility.centered(f"--- Du gehst einen Schritt nach {self.engine.player.direction.value} ---\n")
    
    def show_wall(self):
        self.utility.centered("--- Du stößt gegen eine Wand ---\n")
    
    def show_infront_door(self):
        self.utility.centered("---- Du stehst vor einer Tür ---\n")

    def show_room_entrance(self):
        self.utility.centered(f"--- Du gehst durch eine Tür in Richtung {self.engine.player.direction.value} ---\n")
        self.utility.centered(f"--- Du betrittst den {self.engine.player.current_room.name} ---\n")

    def _menuState_handler(self, menuState):
        if menuState == MenuState.MAIN:
            self.show_menu_options(MenuState.MAIN)
        elif menuState == MenuState.CONTROLS:
            self.show_controls()
        elif menuState == MenuState.SETTINGS:
            self.show_menu_options(MenuState.SETTINGS)
        elif menuState == MenuState.EXIT:
            self.show_exit_menu()
            self.show_menu_options(MenuState.EXIT)

    def gameState_handler(self, gameState):
        playerState = self.stateManager.playerState
        if gameState == GameState.INIT:
            self.show_hello()
            return
        elif gameState == GameState.PLAYING:
            self.show_start()
            self._playerState_handler(playerState)
            return
        elif gameState == GameState.EXIT:
            self.show_exit_confirmed()
        elif gameState == GameState.MAP:
            self.show_map()

    def _playerState_handler(self, playerState):    
            if playerState == PlayerState.MOVE:
                self.show_move()
            elif playerState == PlayerState.WALL:
                self.show_wall()
            elif playerState == PlayerState.DOOR:
                self.show_move()
                self.show_infront_door()
            elif playerState == PlayerState.GO_DOOR:
                self.show_room_entrance()

    def update(self):
        gameState = self.stateManager.gameState
        menuState = self.stateManager.menuState
        if gameState == GameState.MENU:
            self._menuState_handler(menuState)
            return
        self.gameState_handler(gameState)


