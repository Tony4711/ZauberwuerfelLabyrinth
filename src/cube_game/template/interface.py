from enums.commands import Command
from enums.geometry import Moved

def template(game_context):
    return {
            "MOVE_FORWARD": f"Einen Schritt nach {Moved.FORWARD.value}",
            "TURN_LEFT": f"Drehe dich nach {Moved.LEFT.value}",
            "MOVE_BACK": f"Einen Schritt nach {Moved.BACK.value}",
            "TURN_RIGHT": f"Drehe dich nach {Moved.RIGHT.value}",
            "OPEN_MAP": "Karte öffnen",
            "NAVIGATION": "Steuerung anzeigen",
            "SHUFFLE_MAP": "Räume mischen",
            "OP1": "Menu Auswahl 1",
            "OP2": "Menu Auswahl 2",
            "OP3": "Menu Auswahl 3",
            "OP4": "Menu Auswahl 4",
            "BACK": "Zurück",
            "FORTH": "Weiter",
            "ACCEPT": "Ja",
            "DENIE": "Nein",
            "EXIT": "Verlassen",
            "OPTION1": "1",
            "OPTION2": "2",
            "OPTION3": "3",
            "OPTION4": "4",
            "navigation_command": f"[yellow]{Command.NAVIGATION.value.upper()}[/]",
            "player_facing": game_context.player.facing.value,
            "player_moved": game_context.player.moved.value,
            "current_room": game_context.player.current_room.name,
            #"map": game_context.world.map(game_context.starting_room)
        }