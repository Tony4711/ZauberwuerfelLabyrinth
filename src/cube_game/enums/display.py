from enum import Enum, auto
from enums.commands import Command

class HelloString(Enum):
    STRING = (
                "--- Willkommen zu 'Gefangen im Zauberwürfel Labyrinth'! ---\n",
                "Zum steuern bitte die in [ ] geschriebene Taste drücken\n",
                "Benutze im Spiel [{navigation_command}] um dir die Steuerung anzeigen zu lassen"
            )
    
class StartString(Enum):
    STRING = ("--- Spiel wird gestartet ---",)

class MoveString(Enum):
    STRING = ("--- Du gehst einen Schritt nach {player_direction} ---",)

class WallString(Enum):
    STRING = ("--- Du stößt gegen eine Wand ---",)

class ExitMenuString(Enum):
    STRING = ("--- Spiel wirklich beenden? [J/N] ---",)

class ExitConfirmedString(Enum):
    STRING = ("--- Spiel wird beendet ---",)

class InfrontDoorString(Enum):
    STRING = (
            "--- Du gehst einen Schritt nach {player_direction} ---\n",
            "---- Du stehst vor einer Tür ---",
            )

class RoomEntranceString(Enum):
    STRING = (
                "--- Du öffnest die Tür und gehst einen Schritt in Richtung {player_direction} ---\n",
                "--- Du betrittst den {current_room} ---",
            )

class InputExceptionString(Enum):
    STRING = ("--- Ungültige Eingabe ---",)

class MapString(Enum):
    STRING = (
                "--- Die Karte des Zauberwürferl Labyrinths ---",
                "{map}"
            )

class Display(Enum):

    HELLO_TEXT = HelloString
    START_TEXT = StartString
    MAP_TEXT = MapString
    EXIT_MENU_TEXT = ExitMenuString
    EXIT_CONFIRMED_TEXT = ExitConfirmedString
    MOVE_TEXT = MoveString
    WALL_TEXT = WallString
    INFRONT_DOOR_TEXT = InfrontDoorString
    ROOM_ENTRANCE_TEXT = RoomEntranceString
    INPUT_EXCEPTION_TEXT = InputExceptionString

    @property
    def string(self):
        return self.value.STRING.value


class NavMenu(Enum):
    ALL = Command


class DisplayNavigation(Enum):

    NAVIGATION = auto()
    ALL_NAVIGATION = auto()
    
