from engine import Engine
from world import World
from interface import Interface
from utility import Utility
from controls import Controls
class Main:

    def __init__(self):
        self.world = World()
        self.interface = Interface()
        self.engine = Engine()
        self.controls = Controls()
        self.utility = Utility
        self.running = True
        self.command
    
    def run(self):
        while self.running:
            self.interface.display_update()
            self.engine.update()
            self.command = self.controls.process_input(self.engine.state)
            self.engine.process_command(self.command)
            

if __name__ == "__main__":
    main = Main()
    main.run()