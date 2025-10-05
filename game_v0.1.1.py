import sys
import readchar

# Ein Spiel zum Verstehen der Grundmechaniken eines Rubiks Würfels.
# Der kleine Zauberer Garry ist in einem 3 dimensionalem Labyrinth gefangen und muss die Räume richtig miteinander verbinden, um herauszufinden.
# Dabei stößt er auf verschiedenste Rätsel und Herausforderungen, die ihm Helfen, den Zauberwürfel zu verstehen.

class Game:

    def __init__(self):
        self.active = True
        self.state = "menu"
        self.last_input = ""

        self.valid_inputs = {
            "j": "Ja",
            "n": "Nein",
            "1": "Option 1",
            "2": "Option 2",
            "3": "Option 3",

        }

    #muss noch fertiggestellt werden. Soll eine Methode sein um den aktuellen Status zu prüfen
    def is_active(self):
        self.active

    def write_input(self, text):
        print("\nSpieler: [" + text + "]\n")

    # Liest den nächsten Tastendruck des Nutzers und speichert ihn in last_input
    # Schreibt den letzten Input in Großbuchstaben in die Konsole
    # Gibt den Inhalt von last_input zurück
    def get_input(self):
        from readchar import readkey, key
        self.last_input = readkey().lower().strip()     
        self.write_input(self.last_input.upper())       
        return self.last_input                          
             
    # Neue Variante braucht ein Array mit allen gültigen Eingaben das geprüft wird
    # Prüft ob last_input ein J oder ein N ist
    # Wenn ja, gibt er Richtig zurück
    # Wenn nein, gibt er Falsch zurück
    def check_last_input(self):
        if self.last_input in self.valid_inputs:              
            return True                                 
        else:
            return False                                
    
    def show_valid_inputs(self):
        for key, desc in self.valid_inputs.items():
            print(f"[{key.upper()}] - {desc}")
        print()

    def input_exception(self):
        print("---Ungültige Eingabe. Bitte nutze die in [ ] geschriebene Taste zum steuern---")

    def start(self):
        print("---Spiel wird gestartet...---")
        self.active = True
        self.state = "running"

       
    def exit(self):
        print("---Spiel wirklich beenden? [J/N]---")
        self.choice = self.get_input()
        if self.last_input == "j":
            print("--- Spiel wird beendet... ---")
            sys.exit()
        else:
            print("--- Ok, was möchtest du dann machen? ---")
            self.choice = self.get_input()
            self.menu_choice_handler()



    def hello(self):
        print("_____________________________________________________________")
        print("\n--- Willkommen zu 'Gefangen im Zauberwürfel Labyrinth'! ---")
        print("\n                   --- Hauptmenü ---")
        print("\n--- Zum steuern bitte die in [ ] geschriebene Taste drücken. ---\n")
        
    def show_menu_options(self):
        print("[1] Spiel starten")
        print("[2] Einstellungen")
        print("[3] Spiel verlassen")

    def menu_choice_handler(self):
            if self.choice == "1":
                self.state = "start"
            elif self.choice == "2":
                self.state = "settings"
            elif self.choice == "3":
                self.state = "exit"

    # Methode für die Spielweite Steuerung
    def global_navigation(self):
        if self.choice == "q":
            self.state = "back"

    def menu(self):
        self.hello()
        self.show_menu_options()
        self.choice = self.get_input()

        while not self.check_last_input():
            self.input_exception()
            self.choice = self.get_input()
        self.menu_choice_handler()
        
    def settings(self):
        self.show_valid_inputs()
        self.choice = self.get_input()

        

    def pause(self):
        pass

    def save(self):
        pass

    def running(self):
        print("\n---Spiel läuft---")

        if self.choice == "p":
            self.state = "pause"
        elif self.choice == "q":
            self.state = "exit"

    def idle(self):
        print("--- Warte auf Eingabe ---")
        

    def run(self):
        while self.active:
            if self.state == "menu":
                self.menu()
            elif self.state == "start":
                self.start()
            elif self.state == "exit":
                self.exit()
            elif self.state == "pause":
                self.pause()
            elif self.state == "save":
                self.save()
            elif self.state == "running":
                self.running()
            elif self.state == "settings":
                self.settings()
            elif self.state == "idle":
                self.idle()
            #elif self.state == "back":



if __name__ == "__main__":
    game = Game()
    game.run()              