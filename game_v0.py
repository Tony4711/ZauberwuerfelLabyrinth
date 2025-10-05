import sys
import readchar
from readchar import readkey, key


print("Willkommen zu SPIELNAME!")

while True:

    print("Spiel starten? [J/N]")
    k = readkey().lower() 

    if k == "j":

        print(k.upper())
        print("Spiel wird gestartet...")
        break
     
    elif k == "n":
        print(k.upper())
        while True:
             
            print("Spiel verlassen? [J/N]")
            k2 = readkey().lower()

            if k2 == "j":
             
                print(k2.upper())
                print("Spiel wird beendet...")
                sys.exit()

            elif k2 == "n":
             
                print(k2.upper())
                break

            else:
                print("Ungueltige Eingabe. Bitte J oder N drücken.")
    else:
        print("Ungueltige Eingabe. Bitte J oder N drücken.")