from enums.commands import Command

def template(game_context):
    return {
            "MOVE_NORTH": "Gehe nach Norden",
            "MOVE_WEST": "Gehe nach Westen",
            "MOVE_SOUTH": "Gehe nach Süden",
            "MOVE_EAST": "Gehe nach Osten",
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
            "player_direction": game_context.player.direction.value,
            "current_room": game_context.player.current_room.name,
            #"map": game_context.world.map(game_context.starting_room)
        }