from enums.states import MenuState, GameState, DisplayFunction, SystemState, InteractableState, PlayerState

class DisplayController:

    def __init__(self, game_context):
        self.game_context = game_context

    def state_handler(self, state):
        handler = {
            DisplayFunction: self._display_function_state_handler,
            SystemState: self._system_state_handler,
            PlayerState: self._player_state_handler,
            MenuState: self._menu_state_handler,
            GameState: self._game_state_handler, 
            
        }
        func = handler.get(type(state))
        if func:
            func(state)

    def _display_function_state_handler(self, display_function_state):
        signal = self.game_context.display_state_signal.get(display_function_state)
        func = self.game_context.interface_router.get(signal)
        if func:
            func()

    def _game_state_handler(self, game_state):
        signal = self.game_context.game_state_signal.get(game_state)
        key = self.game_context.interface_router.get(signal)
        self.game_context.interface.format_display(key.string)

    def _player_state_handler(self, player_state):   
        signal = self.game_context.player_state_signal.get(player_state)
        key = self.game_context.interface_router.get(signal)
        self.game_context.interface.format_display(key.string)

    def _menu_state_handler(self, menu_state):
        signal = self.game_context.menu_state_signal.get(menu_state)
        key = self.game_context.interface_router.get(signal)
        self.game_context.interface.format_menu(key, menu_state)
    
    def _system_state_handler(self, system_state):
        signal = self.game_context.system_state_signal.get(system_state)
        key = self.game_context.interface_router.get(signal)
        self.game_context.interface.format_display(key.string)
    
    def update(self):
        state = self.game_context.next_state
        self.state_handler(state)
        return