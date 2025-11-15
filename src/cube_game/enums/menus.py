from enum import Enum

class MainMenu(Enum):

    OP1 = "Spiel Starten"
    OP2 = "Spiel Beenden"
    OP3 = "Steuerung"

class ExitMenu(Enum):

    OP1 = "Ja"
    OP2 = "Nein"

class Menus(Enum):

    MAIN = MainMenu
    EXIT = ExitMenu


