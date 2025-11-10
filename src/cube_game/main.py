from core.interface import Interface
from core.engine import Engine
from core.state_controller import StateController
from enums import LoopSignal

class Main:

    def __init__(self):
        self.running = LoopSignal.CONTINUE
        self.stateController = StateController()
        self.engine = Engine(self.stateController) 
        self.interface = Interface(self.stateController, self.engine)
    
    def tick(self) -> LoopSignal:
        self.interface.update()
        next_state = self.engine.update()
        self.running = self.stateController.update(next_state)
        return self.running
        
    def run(self):
        while self.running is LoopSignal.CONTINUE:
            self.tick()
            
if __name__ == "__main__":
    main = Main()
    main.run()