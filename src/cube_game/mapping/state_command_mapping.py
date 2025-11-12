from enums.commands import Command
from enums.states import GameState, MenuState


mapping = {
            MenuState:{
                MenuState.MAIN:{
                    Command.OP1: "Option 1",
                    Command.OP2: "Option 2",
                    Command.OP3: "Option 3"
                },
                MenuState.EXIT:{
                    Command.OP1: "Ja",
                    Command.OP2: "Nein"
                },
                MenuState.MAP:{
                    Command.BACK: "Zurück"
                },
                MenuState.NAVIGATION: {
                    Command.BACK: "Zurück"
                },
                MenuState.ALL_NAVIGATIONS: {
                    Command.BACK: "Zurück"
                }
            },
            GameState:{
                GameState.PLAYING: {
                    Command.MOVE_NORTH: "Nach Norden gehen",
                    Command.MOVE_WEST: "Nach Westen gehen",
                    Command.MOVE_SOUTH: "Nach Süden gehen ",
                    Command.MOVE_EAST: "Nach Osten gehen ",
                    Command.OPEN_MAP: "Öffne die Karte",
                    Command.EXIT: "Spiel beenden",
                    Command.NAVIGATION: "Steuerungen"
                },
                GameState.INIT:{

                },
                GameState.EXIT:{

                },
                GameState.IDLE:{

                },
                GameState.BACK:{
                }   
            }
        }
