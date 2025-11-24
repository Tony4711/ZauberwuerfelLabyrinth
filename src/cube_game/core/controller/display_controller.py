from enums.states import MenuState, GameState, DisplayState, SystemState, DoorState, PlayerState

class DisplayController:

    def __init__(self, game_context):
        self.game_context = game_context

    def state_handler(self, state):
        handler = {
            DisplayState: self._display_state_handler,
            SystemState: self._system_state_handler,
            PlayerState: self._player_state_handler,
            MenuState: self._menu_state_handler,
            GameState: self._game_state_handler, 
            
        }
        func = handler.get(type(state))
        if func:
            func(state)

    def _display_state_handler(self, display_state):
        handler = {
            DisplayState.NAVIGATION: self.game_context.interface.format_navigation,
            DisplayState.MAP: self.game_context.interface.format_map,
            DisplayState.SHUFFLE_MAP: self.game_context.interface.shuffle_map
        }
        func = handler.get(display_state)
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
        menu = self.game_context.interface_router.get(signal)
        self.game_context.interface.format_menu(menu, menu_state)
    
    def _system_state_handler(self, system_state):
        signal = self.game_context.system_state_signal.get(system_state)
        key = self.game_context.interface_router.get(signal)
        self.game_context.interface.format_display(key.string)
    
    def update(self):
        state = self.game_context.next_state
        self.state_handler(state)
        return