class Controls:

    def __init__(self):
        self.mappings = {
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

    def get_valid_inputs(self, state):
        return self.mappings.get(state)
    
    def print_dict(self, state = None):
        if state:
            for state_str, input_descr in self.mappings[state].items():
                print(f"[{state_str.upper()}] {input_descr}")
            print("________________________________________")
        else:
            for state_str, input_descr in self.mappings.items():
                print(f"\n[{state_str.upper()}]")
                for key, description in self.mappings.items():
                    print(f"[{key.upper()}] {description}")
            print("________________________________________")
