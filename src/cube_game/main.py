from interface import Interface
from engine import Engine
from stateManager import StateManager

class Main:

    def __init__(self):
        self.stateManager = StateManager() 
        self.interface = Interface(self.stateManager)
        self.engine = Engine(self.stateManager)
        self.running = True

    
    def run(self):
        while self.running:
            self.interface.update()
            next_state = self.engine.update()
            self.stateManager.update(next_state)
            

            

if __name__ == "__main__":
    main = Main()
    main.run()