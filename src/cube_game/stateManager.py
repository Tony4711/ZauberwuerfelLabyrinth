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
    
    def _init_stateHandlerDict(self, nextState):
        stateHandler = {
            GameState: self._update_game,
            MenuState: self._update_menu,
            PlayerState: self._update_player,
            DoorState: self._update_door
        }
        return stateHandler
    
    def _stateHandler_logic(self, nextState, stateHandlerDict):
        if nextState == GameState.INIT:
                self._init_game(nextState)
                return LoopSignal.CONTINUE
        elif nextState == GameState.EXIT:
                self._update_game(nextState)
                return LoopSignal.EXIT
        for states, handler in stateHandlerDict.items():
            if isinstance(nextState, states):
                handler(nextState)
                return LoopSignal.CONTINUE
    
    def _init_game(self, gameState):
        if gameState == GameState.INIT:
            self._update_game(GameState.MENU)
            self._update_menu(MenuState.MAIN)
    
    def _update_game(self, gameState):
        self.gameState = gameState
        self.gameStack._push_stateStack(gameState)
    
    def _update_menu(self, menuState):
        self._update_game(GameState.MENU)
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

    def update(self, nextState):
        stateHandlerDict = self._init_stateHandlerDict(nextState)
        return self._stateHandler_logic(nextState, stateHandlerDict)