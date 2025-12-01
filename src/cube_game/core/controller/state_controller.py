from enums.states import GameState, MenuState, PlayerState, DoorState, SystemState, DisplayFunction
from enums.system import LoopSignal

class StateStack:
    
    def __init__(self, init_state):
        self.state_stack = [init_state]

    def _push_state_stack(self, state):
        self.state_stack.append(state)
    
    def _pop_state_stack(self):
        if len(self.state_stack)>1:
            return self.state_stack.pop()
        return self.state_stack[-1]
    
    def _current_state_stack(self):
        return self.state_stack[-1]
    
    def _previous_state_stack(self):
        if len(self.state_stack)>1:
            return self.state_stack[-2]
    
class GameStack(StateStack):

    def __init__(self):
        super().__init__(GameState.INIT)

class MenuStack(StateStack):

    def __init__(self):
        super().__init__(MenuState.MAIN)

class PlayerStack(StateStack):

    def __init__(self):
        super().__init__(PlayerState.STAND)

class SystemStack(StateStack):

    def __init__(self):
        super().__init__(SystemState.OK)

class DisplayStack(StateStack):

    def __init__(self):
        super().__init__(DisplayFunction.INIT)

class StateController:
    
    def __init__(self, game_context):
        self.game_context = game_context
        self.game_state = GameState.INIT
        self.menu_state = MenuState.MAIN
        self.player_state = PlayerState.INIT
        self.door_state = DoorState.CLOSED
        self.system_state = SystemState.OK
        self.display_function_state = DisplayFunction.INIT
        self.game_stack = GameStack()
        self.menu_stack = MenuStack()
        self.player_stack = PlayerStack()
        self.system_stack = SystemStack()
        self.display_function_stack = DisplayStack()
        self.state_handler_dict = self._init_state_handler()
        self.exception_handler_dict = self._init_exception_handler()
    
    def _init_state_handler(self):
        state_handler = {
            GameState: self._update_game,
            MenuState: self._update_menu,
            PlayerState: self._update_player,
            DoorState: self._update_door,
            SystemState: self._reset_system,
            DisplayFunction: self._update_display_function,
        }
        return state_handler
    
    def _init_exception_handler(self):
        exception_handler = {
            GameState.INIT: self._init_game,
            GameState.EXIT: self._exit_game,
            GameState.BACK: self._state_back,
        }
        return exception_handler
    
    def _state_handler_logic(self, next_state, state_handler, exception_handler):
        handler = exception_handler.get(next_state)
        if handler:
            self._update_loopsignal(LoopSignal.CONTINUE)
            return handler(next_state)
        
        handler = state_handler.get(type(next_state))
        if handler:
            self._update_loopsignal(LoopSignal.CONTINUE)
            return handler(next_state)
        
        self._update_loopsignal(LoopSignal.CONTINUE)
    
    def _init_game(self, *_):
        self._update_game(GameState.MENU)
        return self._update_menu(MenuState.MAIN)
        
    def _exit_game(self, game_state):
        self._update_game(game_state)
        self._update_loopsignal(LoopSignal.EXIT)
        return game_state

    def _update_game(self, game_state):
        self.game_state = game_state
        self.game_stack._push_state_stack(game_state)
        return game_state
    
    def _update_menu(self, menu_state):
        self._update_game(GameState.MENU)
        self.menu_state = menu_state
        self.menu_stack._push_state_stack(menu_state)
        return menu_state

    def _update_player(self, player_state):
        self.player_state = player_state
        self.player_stack._push_state_stack(player_state)
        return player_state
    
    def _update_door(self, door_state):
        self.door_state = door_state
    
    def _update_display_function(self, display_state):
        self.display_function_state = display_state
        self.display_function_stack._push_state_stack(display_state)
        return display_state

    def _reset_system(self, system_state):
        self.system_state = system_state 
        self.system_stack._push_state_stack(system_state) 
        return system_state
        
    def _state_back(self, *_):
        self.game_stack._pop_state_stack()
        self.game_state = self.game_stack._current_state_stack()
        if self.game_state == GameState.MENU:
            self.menu_stack._pop_state_stack()
            self.menu_state = self.menu_stack._current_state_stack()
        
    def _update_loopsignal(self, loopsignal):
        self.game_context.running = loopsignal

    def update(self, next_state):
        self.game_context.previous_state = self.game_context.next_state
        state = self._state_handler_logic(next_state, self.state_handler_dict, self.exception_handler_dict)
        self.game_context.next_state = state

