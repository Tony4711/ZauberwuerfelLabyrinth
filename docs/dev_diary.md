# Zauberwürfel-Labyrinth – Dev Diary

## 2025-10-27 - Building a Reversible State System — Toward True Game Flow Control

Gestern habe ich das neue State System genutzt, um ein Zustandsverlauf System zu programmieren.
Dieses ermöglicht mir durch Menu- oder Spiel-Zustände sequentiell zurück zu gehen. 
Realisiert habe ich das, durch das einführen einer abstrakten Basisklasse StateStack, die jeweils für MenuStates
als auch GameState Spezialisierungen besitzt. Diese StateStacks speichern bei jedem Zustandswechsel den neuen State im 
jeweiligen StateStack. Um 'Zurück' zu gehen nutze ich pop() und current(). Dadurch erhält der StateManager den 
vorrangegangenen State. Da GameState.BACK keinen Update-Zyklus auslöst, wird dieser auch nicht im StateStack berücksichtigt.
Weiter habe ich die Game-Loop zu einem entkoppelten, vorhersagbaren System umgeschrieben,
indem ich im StateManager einen Boolean-Wert zurück gebe, der in der Main-Loop für running verwendet wird. 
Dieser wird nur False, wenn der Spieler das Spiel beendet. Dadurch vermeide ich, dass Programm durch 
sys.exit() zu beenden.
Durch das entkoppeln vom I/O und der Spiellogik, habe ich nun für jedes Menu einzelne Methoden in der Engine Class.
Das fördert das Single Responsibility Principle enorm und steigert die Lesbarkeit. 
Außerdem setzte ich immer konsequenter Konventionen durch, wie zb ein '_'-Präfix, um zu signalisieren,
dass es sich bei einer Methode um ein internes Werkzeug handelt, dass nicht von außen aufgerufen werden sollte.
---
Yesterday, I used the new State System to program a state history system.
This allows me to go back sequentially through menu or game states. 
I implemented this by introducing an abstract base class, StateStack, which has specializations for both MenuStates
and GameStates. These StateStacks store the new state in the 
respective StateStack each time the state changes. To go ‘back’, I use pop() and current(). This gives the StateManager the 
previous state. Since GameState.BACK does not trigger an update cycle, it is not included in the StateStack.
I also rewrote the game loop into a decoupled, predictable system
by returning a Boolean value in the StateManager, which is used in the main loop for running. 
This only becomes False when the player exits the game. This way, I avoid ending the program with 
sys.exit().
By decoupling the I/O and the game logic, I now have individual methods in the Engine class for each menu.
This greatly promotes the single responsibility principle and increases readability. 
In addition, I am consistently enforcing conventions, such as a ‘_’ prefix to signal
that a method is an internal tool that should not be called from outside.
**Translated with DeepL.com (free version)**

