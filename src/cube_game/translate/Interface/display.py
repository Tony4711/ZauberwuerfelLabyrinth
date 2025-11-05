from enums import DisplayStrings, DisplayMenuStructure, Command, DisplayControls, MenuState
from mapping import menuStructure_mapping, state_command_mapping

def init(engine):

    return {
        DisplayStrings: {
                    DisplayStrings.HELLO_TEXT: ("--- Willkommen zu 'Gefangen im Zauberwürfel Labyrinth'! ---", "",
                                            "--- Zum steuern bitte die in [ ] geschriebene Taste drücken ---", "",
                                            f"--- Benutze [{Command.CONTROLS.value.upper()}] um dir die Steuerung anzeigen zu lassen ---"),                    
                    DisplayStrings.START_TEXT: ("--- Spiel wird gestartet ---",),
                    DisplayStrings.EXIT_MENU_TEXT: ("--- Spiel wirklich beenden? [J/N] ---",),
                    DisplayStrings.EXIT_CONFIRMED_TEXT: ("--- Spiel wird beendet ---",),
                    DisplayStrings.MOVE_TEXT: (f"--- Du gehst einen Schritt nach {engine.player.direction.value} ---",),
                    DisplayStrings.WALL_TEXT: ("--- Du stößt gegen eine Wand ---",),
                    DisplayStrings.INFRONT_DOOR_TEXT: (f"--- Du gehst einen Schritt nach {engine.player.direction.value} ---", "---- Du stehst vor einer Tür ---",),                    DisplayStrings.ROOM_ENTRANCE_TEXT: (f"--- Du öffnest die Tür und gehst einen Schritt in Richtung {engine.player.direction.value} ---","",
                                                    f"--- Du betrittst den {engine.player.current_room.name} ---",),
                    DisplayStrings.INPUT_EXCEPTION_TEXT: ("--- Ungültige Eingabe ---",),
                    DisplayStrings.MAP_TEXT: (engine.world.map(engine.player.current_room)),
                    #DisplayStrings.CONTROLS_TEXT: commandList
                },
        DisplayMenuStructure: {
                    DisplayMenuStructure.MENU_OPTION: menuStructure_mapping.menuStructure,
        },
        DisplayControls:{
                    DisplayControls.CONTROLS: state_command_mapping.mapping,
                    DisplayControls.ALL_CONTROLS: state_command_mapping.mapping
        }
}

