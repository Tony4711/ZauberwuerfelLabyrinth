from core.interface import Interface
from core.engine import Engine
from core.state_controller import StateController
from core.gamecontext import GameContext
from enums.system import LoopSignal

class Main:

    def __init__(self):
        gameContext = GameContext()
        self.running = LoopSignal.CONTINUE
        self.stateController = gameContext.stateController
        self.engine = gameContext.engine
        self.interface = gameContext.interface
        
    def run(self):
        while self.running is LoopSignal.CONTINUE:
            self.interface.update()
            next_state = self.engine.update()
            self.running = self.stateController.update(next_state)
            
if __name__ == "__main__":
    main = Main()
    main.run()
