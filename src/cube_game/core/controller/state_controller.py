from enums.states import GameState, MenuState, PlayerState, InteractableState, SystemState, DisplayFunction
from enums.system import LoopSignal

class StateStack:
    
    # Initialize a stack with a starting state.
    def __init__(self, init_state):
        self.state_stack=[init_state]

    # Push a new state onto the stack.
    def _push_state_stack(self, state):
        self.state_stack.append(state)
    
    # Pop the latest state if more than one exists, otherwise return current.
    def _pop_state_stack(self):
        if len(self.state_stack)>1:
            return self.state_stack.pop()
        return self.state_stack[-1]
    
    # Return the current (top) state.
    def _current_state_stack(self):
        return self.state_stack[-1]
    
    # Return the previous state if available.
    def _previous_state_stack(self):
        if len(self.state_stack)>1:
            return self.state_stack[-2]
    
class GameStack(StateStack):

    # Initialize game state stack with INIT state.
    def __init__(self):
        super().__init__(GameState.INIT)

class MenuStack(StateStack):

    # Initialize menu state stack with MAIN state.
    def __init__(self):
        super().__init__(MenuState.MAIN)

class PlayerStack(StateStack):

    # Initialize player state stack with INIT state.
    def __init__(self):
        super().__init__(PlayerState.INIT)

class SystemStack(StateStack):

    # Initialize system state stack with OK state.
    def __init__(self):
        super().__init__(SystemState.OK)

class DisplayStack(StateStack):

    # Initialize display function stack with INIT state.
    def __init__(self):
        super().__init__(DisplayFunction.INIT)

class StateController:
    
    # Initialize controller with default states, stacks, and handlers.
    def __init__(self, game_context):
        self.game_context=game_context
        self.game_state=GameState.INIT
        self.menu_state=MenuState.MAIN
        self.player_state=PlayerState.INIT
        self.interactable_state=InteractableState.CLOSED
        self.system_state=SystemState.OK
        self.display_function_state=DisplayFunction.INIT
        self.game_stack=GameStack()
        self.menu_stack=MenuStack()
        self.player_stack=PlayerStack()
        self.system_stack=SystemStack()
        self.display_function_stack=DisplayStack()
        self.state_handler_dict=self._init_state_handler()
        self.exception_handler_dict=self._init_exception_handler()
    
    # Build mapping from state types to update handlers.
    def _init_state_handler(self):
        state_handler={
            GameState: self._update_game,
            MenuState: self._update_menu,
            PlayerState: self._update_player,
            InteractableState: self._update_interactbale,
            SystemState: self._reset_system,
            DisplayFunction: self._update_display_function,
        }
        return state_handler
    
    # Build mapping for exception-like game state transitions.
    def _init_exception_handler(self):
        exception_handler={
            GameState.INIT: self._init_game,
            GameState.EXIT: self._exit_game,
            GameState.BACK: self._state_back,
        }
        return exception_handler
    
    # Core dispatch logic to route next_state through exception or normal handlers.
    def _state_handler_logic(self, next_state, state_handler, exception_handler):
        handler=exception_handler.get(next_state)
        if handler:
            self._update_loopsignal(LoopSignal.CONTINUE)
            return handler(next_state)
        
        handler=state_handler.get(type(next_state))
        if handler:
            self._update_loopsignal(LoopSignal.CONTINUE)
            return handler(next_state)
        
        self._update_loopsignal(LoopSignal.CONTINUE)
    
    # Handle game initialization by setting menu state.
    def _init_game(self, *_):
        self._update_game(GameState.MENU)
        return self._update_menu(MenuState.MAIN)
        
    # Handle exiting the game and signal loop termination.
    def _exit_game(self, game_state):
        self._update_game(game_state)
        self._update_loopsignal(LoopSignal.EXIT)
        return game_state

    # Update current game state and push to stack.
    def _update_game(self, game_state):
        self.game_state=game_state
        self.game_stack._push_state_stack(game_state)
        return game_state
    
    # Update current menu state (also pushes menu and game stacks).
    def _update_menu(self, menu_state):
        self._update_game(GameState.MENU)
        self.menu_state=menu_state
        self.menu_stack._push_state_stack(menu_state)
        return menu_state

    # Update player state and push to stack.
    def _update_player(self, player_state):
        self.player_state=player_state
        self.player_stack._push_state_stack(player_state)
        return player_state
    
    # Update interactable state without stacking.
    def _update_interactbale(self, interactable_state):
        self.interactable_state=interactable_state
    
    # Update display function state and push to stack.
    def _update_display_function(self, display_state):
        self.display_function_state=display_state
        self.display_function_stack._push_state_stack(display_state)
        return display_state

    # Reset system state and push to stack.
    def _reset_system(self, system_state):
        self.system_state=system_state 
        self.system_stack._push_state_stack(system_state) 
        return system_state
        
    # Step back to previous game/menu states.
    def _state_back(self, *_):
        self.game_stack._pop_state_stack()
        self.game_state=self.game_stack._current_state_stack()
        if self.game_state==GameState.MENU:
            self.menu_stack._pop_state_stack()
            self.menu_state=self.menu_stack._current_state_stack()
        
    # Update main loop signal used by runner.
    def _update_loopsignal(self, loopsignal):
        self.game_context.running=loopsignal

    # Public update entry: process next state and write back into context.
    def update(self, next_state):
        self.game_context.previous_state=self.game_context.next_state
        state=self._state_handler_logic(next_state, self.state_handler_dict, self.exception_handler_dict)
        self.game_context.next_state=state

