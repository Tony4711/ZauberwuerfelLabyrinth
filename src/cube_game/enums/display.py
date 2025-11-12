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

class WallString(Enum):
    STRING = ("--- Du stößt gegen eine Wand ---",)

class ExitMenuString(Enum):
    STRING = ("--- Spiel wirklich beenden? [J/N] ---",)

class ExitConfirmedString(Enum):
    STRING = ("--- Spiel wird beendet ---",)

class InfrontDoorString(Enum):
    STRING = ("--- Du gehst einen Schritt nach {player_direction} ---", "---- Du stehst vor einer Tür ---",)

class RoomEntranceString(Enum):
    STRING = (
                "--- Du öffnest die Tür und gehst einen Schritt in Richtung {player_direction} ---","",
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
    INFRONT_DOOR_TEXT = WallString
    ROOM_ENTRANCE_TEXT = RoomEntranceString
    INPUT_EXCEPTION_TEXT = InputExceptionString

    @property
    def string(self):
        return self.value.STRING.value

class MainMenu(Enum):
    OP1 = "Spiel Starten"
    OP2 = "Spiel Verlassen"
    OP3 = "Steuerung"

class ExitMenu(Enum):
    OP1 = "Ja"
    OP2 = "Nein"

class NavMenu(Enum):
    pass

class Menus(Enum):

    MAIN = MainMenu
    EXIT = ExitMenu
    NAVIGATION = NavMenu

class MenuPoints(Enum):

    MENU_OPTION = Menus
    NAVIGATION = "nav"

class DisplayNavigation(Enum):

    NAVIGATION = auto()
    ALL_NAVIGATION = auto()
    