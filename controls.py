from enums import GameState, Command
class Controls:

    # Initiert ein Dict mit allen Steuerungen verknüpft an das jeweilige Menu
    def __init__(self):
        self.mapping = {
            GameState.MAIN_MENU: {
                Command.OP1: "Option 1",
                Command.OP2: "Option 2",
                Command.OP3: "Option 3",
                Command.OP4: "Option 4"
            },
            GameState.GLOBAL_CONTROLS: {
                Command.BACK: "Zurück",
                Command.FORTH: "Weiter"
            },
            GameState.EXIT: {
                Command.ACCEPT: "Ja",
                Command.DENIE: "Nein"
            },
            GameState.START: {
                Command.MOVE_NORTH: "Nach Norden gehen",
                Command.MOVE_WEST: "Nach Westen gehen",
                Command.MOVE_SOUTH: "Nach Süden gehen",
                Command.MOVE_EAST: "Nach Osten gehen"
            },
            GameState.MAP: {
                Command.BACK: "Zurück"
            } 
        }
    
    # Getter Methode um auf lokels dict zuzugreifen
    def get_dict(self, dictname):
        d = getattr(self, dictname, None)
        if d is None:
            print(f"Dict '{dictname}' existiert nicht in Controls!")
        return d