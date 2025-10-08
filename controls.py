class Controls:

    # Initiert ein Dict mit allen Steuerungen verknüpft an das jeweilige Menu
    def __init__(self):
        self.mapping = {
            "main_menu": {
                "1": "Option 1",
                "2": "Option 2",
                "3": "Option 3"
            },
            "navigation": {
                "q": "Zurück",
                "e": "Weiter"
            },
            "exit": {
                "j": "Ja",
                "n": "Nein"
            },
            "start": {
                "w": "Vorwärts",
                "a": "Nach links",
                "s": "Rückwärts",
                "d": "Nach rechts"
            } 
        }
    
    # Getter Methode um auf lokels dict zuzugreifen
    def get_dict(self, dictname):
        d = getattr(self, dictname, None)
        if d is None:
            print(f"Dict '{dictname}' existiert nicht in Controls!")
        return d