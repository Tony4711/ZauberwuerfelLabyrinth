import sys
import readchar


class Game:

    def __init__(self):
        self.active = True
        self.state = "menu"

    #muss noch fertiggestellt werden. Soll eine Methode sein um den aktuellen Status zu prüfen
    def is_active(self):
        self.active

    def get_input(self, prompt=""):
        from readchar import readkey, key
        print(prompt, end="", flush=True)
        self.last_input = readkey().lower().strip()
        return self.last_input
    
    def write(self, text):
        print(text)

    def start(self):
        print("Spiel wird gestartet...")
        self.active = True

    def ende(self):
        print("Spiel wird beendet.")
        self.active = False
        sys.exit()

    #hier hast du gestern aufgehört. Diese methode muss noch fertiggestellt werden
    def exit_choice(self):
        while self.active:
                k2 = self.get_input("Möchtest du das Spiel beenden? [J/N]")
                self.write(self.last_input.upper())

                if k2 == "j":
                    self.ende()

                elif k2 == "n":
                    k2 = self.get_input("Für eine Sache musst du dich entscheiden. Hast du etwa Angst, Potter? Also, Spiel starten? [J]")
                    self.write(self.last_input.upper())

    def menu(self):
        print("Willkommen zu [SPIELNAME]")
        k = self.get_input("Möchtest du das Spiel starten? [J/N]")
        self.write(self.last_input.upper())

        if k == "j":
            self.start()

        elif k == "n":
            self.exit_choice()
                