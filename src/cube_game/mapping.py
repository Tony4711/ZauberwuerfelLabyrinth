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
            GameState.PLAYING: {
                Command.MOVE_NORTH: "Nach Norden gehen",
                Command.MOVE_WEST: "Nach Westen gehen",
                Command.MOVE_SOUTH: "Nach Süden gehen ",
                Command.MOVE_EAST: "Nach Osten gehen "
            },
            GameState.INIT:{

            },
            GameState.EXIT:{

            },
            GameState.IDLE:{

            },
            GameState.BACK:{

            },
            GameState.MAP:{

            }
        }