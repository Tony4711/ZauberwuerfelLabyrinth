from enums import GameState, MenuState, PlayerState, DoorState, LoopSignal

class StateStack:
    
    def __init__(self, init_state):
        self.stateStack = [init_state]

    def _push_stateStack(self, state):
        self.stateStack.append(state)
    
    def _pop_stateStack(self):
        if len(self.stateStack)>1:
            return self.stateStack.pop()
        return self.stateStack[-1]
    
    def _current_stateStack(self):
        return self.stateStack[-1]
    
class GameStack(StateStack):

    def __init__(self):
        super().__init__(GameState.INIT)

class MenuStack(StateStack):

    def __init__(self):
        super().__init__(MenuState.MAIN)

class PlayerStack(StateStack):

    def __init__(self):
        super().__init__(PlayerState.STAND)

class StateManager:
    
    def __init__(self):
        self.gameState = GameState.INIT
        self.menuState = MenuState.MAIN
        self.playerState = PlayerState.STAND
        self.doorState = DoorState.CLOSED
        self.gameStack = GameStack()
        self.menuStack = MenuStack()
        self.playerStack = PlayerStack()

    # CHORE: write mapping dict instead of conditions to alow direct access 
    def update(self, nextState):
        if nextState == GameState.EXIT:
            self._update_game(nextState)
            return LoopSignal.EXIT.value
        else:
            if isinstance(nextState, GameState):
                if nextState == GameState.INIT:
                    self._update_game(GameState.MENU)
                    self._update_menu(MenuState.MAIN)
                else:
                    self._update_game(nextState)
            elif isinstance(nextState, MenuState):
                self._update_game(GameState.MENU)
                self._update_menu(nextState)
            elif isinstance(nextState, PlayerState):
                self._update_player(nextState)
            return LoopSignal.CONTINUE.value
    
    def _update_game(self, gameState):
        self.gameState = gameState
        self.gameStack._push_stateStack(gameState)
    
    def _update_menu(self, menuState):
        self.menuState = menuState
        self.menuStack._push_stateStack(menuState)

    def _update_player(self, playerState):
        self.playerState = playerState
        self.playerStack._push_stateStack(playerState)
    
    def _update_door(self, doorState):
        self.doorState = doorState
    
    def _state_back(self):
        self.gameStack._pop_stateStack()
        self.gameState = self.gameStack._current_stateStack()
        if self.gameState == GameState.MENU:
            self.menuStack._pop_stateStack()
            self.menuState = self.menuStack._current_stateStack()