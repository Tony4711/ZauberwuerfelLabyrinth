from interface import Interface
from engine import Engine
from stateManager import StateManager

class Main:

    def __init__(self):
        self.running = True
        self.stateManager = StateManager()
        self.engine = Engine(self.stateManager) 
        self.interface = Interface(self.stateManager, self.engine)
        
    def run(self):
        while self.running:
            self.interface.update()
            next_state = self.engine.update()
            self.running = self.stateManager.update(next_state)
            
if __name__ == "__main__":
    main = Main()
    main.run()