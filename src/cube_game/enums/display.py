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
    STRING = ("--- Du gehst einen Schritt nach {player_moved} ---",)

class TurnString(Enum):
    STRING = ("--- Du drehst dich nach {player_moved}---",)

class WallString(Enum):
    STRING = ("--- Du stößt gegen eine Wand ---",)

class ExitMenuString(Enum):
    STRING = ("--- Spiel wirklich beenden? [J/N] ---",)

class ExitConfirmedString(Enum):
    STRING = ("--- Spiel wird beendet ---",)

class InfrontDoorString(Enum):
    STRING = (
            "--- Du gehst einen Schritt nach {player_facing} ---\n",
            "---- Du stehst vor einer Tür ---",
            )

class RoomEntranceString(Enum):
    STRING = (
                "--- Du gehst durch eine Tür und befindest dich im ---\n",
                "--- {object} Raum ---",
            )

class InputExceptionString(Enum):
    STRING = ("--- Ungültige Eingabe ---",)

class MapString(Enum):
    STRING = (
                "--- Die Karte des Zauberwürferl Labyrinths ---",
            )

class InstructionString(Enum):
    STRING = (
                "Du befindest dich in einem Labyrinth. Deine Aufgabe ist es dich durch die verschiedenen Räume des Würfels zu navigieren.",
                "Dort erwarten dich Rätsel, die es zu lösen gilt, um den Würfel wieder in seine Korrekte anordnung zu bringen."
    )

class ClosedString(Enum):
    STRING = (
                "--- Du findest eine verschlossene {object} ---\n",
                "--- Du benötigst einen Schlüssel um sie zu öffnen"
    )

class DoorUnlockedString(Enum):
    STRING = (
                "--- Du schließt die Tür mit dem {object} auf ---",
    )

class InteractionString(Enum):
    STRING = (
                "--- {interaction_type} {object} ---\n",
                "--- {interaction_result} ---"
    )

class Display(Enum):

    HELLO_TEXT = HelloString
    START_TEXT = StartString
    MAP_TEXT = MapString
    EXIT_MENU_TEXT = ExitMenuString
    EXIT_CONFIRMED_TEXT = ExitConfirmedString
    MOVE_TEXT = MoveString
    TURN_TEXT = TurnString
    WALL_TEXT = WallString
    CLOSED_TEXT = ClosedString
    INFRONT_DOOR_TEXT = InfrontDoorString
    ROOM_ENTRANCE_TEXT = RoomEntranceString
    INPUT_EXCEPTION_TEXT = InputExceptionString
    INSTRUCTION_TEXT = InstructionString
    DOOR_UNLOCKED_TEXT = DoorUnlockedString
    INTERACTION_TEX = InteractionString
    

    @property
    def string(self):
        return self.value.STRING.value


class NavMenu(Enum):
    ALL = Command

