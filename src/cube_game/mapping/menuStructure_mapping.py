from enums.states import MenuState
from enums.commands import Command

menuStructure = {
        MenuState.MAIN: {
            Command.OP1.value: "Spiel starten",
            Command.OP2.value: "Spiel verlassen",
            Command.OP3.value: "Steuerung" 
        },
        MenuState.EXIT: {
            Command.OP1.value: "Ja",
            Command.OP2.value: "Nein"
        }
    }
