from enum import Enum, auto

class HelloString(Enum):
    STRING = (
                "--- Willkommen zu 'Gefangen im Zauberwürfel Labyrinth'! ---", "",
                "--- Zum steuern bitte die in [ ] geschriebene Taste drücken ---", "",
                "--- Benutze [{navigation_command}] um dir die Steuerung anzeigen zu lassen ---"
            )
    
class StartString(Enum):
    STRING = ("--- Spiel wird gestartet ---",)

class MoveString(Enum):
    STRING = ("--- Du gehst einen Schritt nach {player_direction} ---",)

class Display(Enum):

    HELLO_TEXT = HelloString
    START_TEXT = StartString
    NAVIGATION_TEXT = "navigation"
    MENU_OPTIONS_TEXT = "menu_options"
    MAP_TEXT = "map"
    EXIT_MENU_TEXT = "exit_menu"
    EXIT_CONFIRMED_TEXT = "exit_confirmed"
    MOVE_TEXT = MoveString
    WALL_TEXT = "wall"
    INFRONT_DOOR_TEXT = "infront_door"
    ROOM_ENTRANCE_TEXT = "room_entrance"
    INPUT_EXCEPTION_TEXT = "input_exception"

    @property
    def string(self):
        return self.value.STRING.value

class DisplayMenuStructure(Enum):

    MENU_OPTION = auto()
    NAVIGATION = auto()

class DisplayNavigation(Enum):

    NAVIGATION = auto()
    ALL_NAVIGATION = auto()
    