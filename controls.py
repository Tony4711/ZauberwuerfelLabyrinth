from enums import GameState
class Controls:

    # Initiert ein Dict mit allen Steuerungen verknüpft an das jeweilige Menu
    def __init__(self):
        self.mapping = {
            GameState.MAIN_MENU: {
                "1": "Option 1",
                "2": "Option 2",
                "3": "Option 3",
                "4": "Option 4"
            },
            GameState.GLOBAL_CONTROLS: {
                "q": "Zurück",
                "e": "Weiter"
            },
            GameState.EXIT: {
                "j": "Ja",
                "n": "Nein"
            },
            GameState.START: {
                "w": "Vorwärts",
                "a": "Nach links",
                "s": "Rückwärts",
                "d": "Nach rechts"
            },
            GameState.MAP: {
                "q": "Zurück"
            } 
        }
    
    # Getter Methode um auf lokels dict zuzugreifen
    def get_dict(self, dictname):
        d = getattr(self, dictname, None)
        if d is None:
            print(f"Dict '{dictname}' existiert nicht in Controls!")
        return d