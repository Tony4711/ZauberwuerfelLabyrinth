from enum import Enum

class MainMenu(Enum):

    OPTION1 = "Spiel Starten"
    OPTION2 = "Spiel Beenden"
    OPTION3 = "Steuerung"

class ExitMenu(Enum):

    OPTION1 = "Ja"
    OPTION2 = "Nein"

class Menus(Enum):

    MAIN = MainMenu
    EXIT = ExitMenu


