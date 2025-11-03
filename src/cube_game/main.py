from interface import Interface
from engine import Engine
from stateController import StateController

class Main:

    def __init__(self):
        self.running = True
        self.stateController = StateController()
        self.engine = Engine(self.stateController) 
        self.interface = Interface(self.stateController, self.engine)
        
    def run(self):
        while self.running:
            self.interface.update()
            next_state = self.engine.update()
            self.running = self.stateController.update(next_state)
            
if __name__ == "__main__":
    main = Main()
    main.run()