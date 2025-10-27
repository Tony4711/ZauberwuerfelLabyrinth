from enums import Command, GameState, MenuState


mapping = {
            GameState.MENU:{
                MenuState.MAIN:{
                    Command.OP1: "Option 1",
                    Command.OP2: "Option 2",
                    Command.OP3: "Option 3",
                    Command.OP4: "Option 4"
                },
                MenuState.EXIT:{
                    Command.OP1: "Ja",
                    Command.OP2: "Nein"
                }
            },
            GameState.GLOBAL_CONTROLS: {
                Command.BACK: "Zurück",
                Command.FORTH: "Weiter",
                Command.EXIT: "Spiel verlassen",
                Command.OPEN_MAP: "Karte öffnen",
                Command.CONTROLS: "Steuerung anzeigen"
            },
            GameState.EXIT: {
                Command.ACCEPT: "Ja",
                Command.DENIE: "Nein"
            },
            GameState.PLAYING: {
                Command.MOVE_NORTH: "Nach Norden gehen",
                Command.MOVE_WEST: "Nach Westen gehen",
                Command.MOVE_SOUTH: "Nach Süden gehen ",
                Command.MOVE_EAST: "Nach Osten gehen "
            }
        }