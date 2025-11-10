from enums.display import DisplayStrings, DisplayMenuStructure, DisplayNavigation
from enums.commands import Command
from mapping import menuStructure_mapping, state_command_mapping

def render(engine):
    current_room = engine.player.current_room.name
    starting_room = engine.world.map(engine.world.starting_room)
    player_direction = engine.player.direction.value
    return {
        DisplayStrings: {
                    DisplayStrings.HELLO_TEXT: ("--- Willkommen zu 'Gefangen im Zauberwürfel Labyrinth'! ---", "",
                                            "--- Zum steuern bitte die in [ ] geschriebene Taste drücken ---", "",
                                            f"--- Benutze [{Command.NAVIGATION.value.upper()}] um dir die Steuerung anzeigen zu lassen ---"),                    
                    DisplayStrings.START_TEXT: ("--- Spiel wird gestartet ---",),
                    DisplayStrings.EXIT_MENU_TEXT: ("--- Spiel wirklich beenden? [J/N] ---",),
                    DisplayStrings.EXIT_CONFIRMED_TEXT: ("--- Spiel wird beendet ---",),
                    DisplayStrings.MOVE_TEXT: (f"--- Du gehst einen Schritt nach {player_direction} ---",),
                    DisplayStrings.WALL_TEXT: ("--- Du stößt gegen eine Wand ---",),
                    DisplayStrings.INFRONT_DOOR_TEXT: (f"--- Du gehst einen Schritt nach {player_direction} ---", "---- Du stehst vor einer Tür ---",),                    
                    DisplayStrings.ROOM_ENTRANCE_TEXT: (f"--- Du öffnest die Tür und gehst einen Schritt in Richtung {player_direction} ---","",
                                                    f"--- Du betrittst den {current_room} ---",),
                    DisplayStrings.INPUT_EXCEPTION_TEXT: ("--- Ungültige Eingabe ---",),
                    DisplayStrings.MAP_TEXT: starting_room,

                },
        DisplayMenuStructure: {
                    DisplayMenuStructure.MENU_OPTION: menuStructure_mapping.menuStructure,
        },
        DisplayNavigation:{
                    DisplayNavigation.NAVIGATION: state_command_mapping.mapping,
                    DisplayNavigation.ALL_NAVIGATION: state_command_mapping.mapping
        },
}

