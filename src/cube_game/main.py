from core.game_context import GameContext
from enums.system import LoopSignal

class Main:

    def __init__(self):
        
        self.game_context = GameContext()
        self.state_controller = self.game_context.state_controller
        self.input_controller = self.game_context.input_controller
        self.command_controller = self.game_context.command_controller
        self.player_movement = self.game_context.player_movement
        self.interface = self.game_context.interface
        self.display_controller = self.game_context.display_controller
        
    def run(self):
        while self.game_context.running == LoopSignal.CONTINUE:
            self.display_controller.update()
            next_state = self.command_controller.process_command()
            self.state_controller.update(next_state)
            
if __name__ == "__main__":
    main = Main()
    main.run()

