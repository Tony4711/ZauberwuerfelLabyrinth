from enums import GameState, MenuState, PlayerState, DoorState, LoopSignal, SystemState

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

class SystemStack(StateStack):

    def __init__(self):
        super().__init__(SystemState.OK)

class StateController:
    
    def __init__(self):
        self.gameState = GameState.INIT
        self.menuState = MenuState.MAIN
        self.playerState = PlayerState.STAND
        self.doorState = DoorState.CLOSED
        self.systemState = SystemState.OK
        self.gameStack = GameStack()
        self.menuStack = MenuStack()
        self.playerStack = PlayerStack()
        self.systemStack = SystemStack()
        self.stateHandlerDict = self._init_stateHandlerDict()
        self.exceptionHandlerDict = self._init_exceptionHandlerDict()
    
    def _init_stateHandlerDict(self):
        stateHandler = {
            GameState: self._update_game,
            MenuState: self._update_menu,
            PlayerState: self._update_player,
            DoorState: self._update_door,
            SystemState:self._reset_system,
        }
        return stateHandler
    
    def _init_exceptionHandlerDict(self):
        exceptionHandler = {
            GameState.INIT: self._init_game,
            GameState.EXIT: self._exit_game,
            GameState.BACK: self._state_back
        }
        return exceptionHandler
    
    def _state_handler_logic(self, nextState, stateHandlerDict, exceptionHandlerDict):
        handler = exceptionHandlerDict.get(nextState)
        if handler:
            return handler(nextState) or LoopSignal.CONTINUE
        handler = stateHandlerDict.get(type(nextState))
        if handler:
            return handler(nextState) or LoopSignal.CONTINUE
        return LoopSignal.CONTINUE
    

    
    def _init_game(self, gameState):
        if gameState == GameState.INIT:
            self._update_game(GameState.MENU)
            self._update_menu(MenuState.MAIN)
    
    def _exit_game(self, gameState):
        self._update_game(gameState)
        return LoopSignal.EXIT
    
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

    def _reset_system(self, systemState):
        self.systemState = SystemState.OK if systemState != SystemState.OK else systemState 
        self.systemStack._push_stateStack(systemState)
        
    
    def _state_back(self):
        self.gameStack._pop_stateStack()
        self.gameState = self.gameStack._current_stateStack()
        if self.gameState == GameState.MENU:
            self.menuStack._pop_stateStack()
            self.menuState = self.menuStack._current_stateStack()

    def update(self, nextState):
        
        return self._state_handler_logic(nextState, self.stateHandlerDict, self.exceptionHandlerDict)