from enums import DisplayKey, OutputFunction, MenuState, Command

def init(engine):

    menuStructure = {
        MenuState.MAIN: {
            Command.OP1.value: "Spiel starten",
            Command.OP2.value: "Spiel verlassen"
        },
        MenuState.EXIT: {
            Command.OP1.value: "Ja",
            Command.OP2.value: "Nein"
        }
    }

    return {
        DisplayKey: {
                    DisplayKey.HELLO_TEXT: ("--- Willkommen zu 'Gefangen im Zauberwürfel Labyrinth'! ---\n",
                                            "--- Hauptmenü ---\n",
                                            "--- Zum steuern bitte die in [ ] geschriebene Taste drücken ---\n",
                                            f"--- Bitte nutze [{Command.CONTROLS.value.upper()}] um dir die Steuerung anzeigen zu lassen ---"),                    
                    DisplayKey.START_TEXT: ("--- Spiel wird gestartet ---",),
                    DisplayKey.EXIT_MENU_TEXT: ("--- Spiel wirklich beenden? ---",),
                    DisplayKey.EXIT_CONFIRMED_TEXT: ("--- Spiel wird beendet ---",),
                    DisplayKey.MOVE_TEXT: (f"--- Du gehst einen Schritt nach {engine.player.direction.value} ---",),
                    DisplayKey.WALL_TEXT: ("--- Du stößt gegen eine Wand ---",),
                    DisplayKey.INFRONT_DOOR_TEXT: (f"--- Du gehst einen Schritt nach {engine.player.direction.value} ---\n", "---- Du stehst vor einer Tür ---",),
                    DisplayKey.ROOM_ENTRANCE_TEXT: (f"--- Du öffnest die Tür und gehst einen Schritt in Richtung {engine.player.direction.value} ---\n",
                                                    f"--- Du betrittst den {engine.player.current_room.name} ---",),
                    DisplayKey.INPUT_EXCEPTION_TEXT: ("--- Ungültige Eingabe ---",),
                    DisplayKey.MAP_TEXT: (engine.world.map(engine.player.current_room))
                },
        OutputFunction: {
                    OutputFunction.SHOW_MENU_OPTION: menuStructure
        }
}

