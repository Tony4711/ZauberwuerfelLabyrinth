from enums import GameState, MenuState, DoorState

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

class StateManager:
    
    def __init__(self):
        self.isGlobal = False
        self.gameState = GameState.INIT
        self.menuState = MenuState.MAIN
        self.doorState = DoorState.CLOSED
        self.gameStack = GameStack()
        self.menuStack = MenuStack()
    
    def update(self, nextState):
        if nextState == GameState.INIT:
            self._update_game(GameState.MENU)
            self._update_menu(MenuState.MAIN)
            return True
        elif nextState == GameState.MENU:
            pass
        elif nextState == GameState.PLAYING:
            self._update_game(GameState.PLAYING)
            return True
        elif nextState == MenuState.CONTROLS:
            self._update_game(GameState.MENU)
            self._update_menu(MenuState.CONTROLS)
            return True
        elif nextState == MenuState.EXIT:
            self._update_game(GameState.MENU)
            self._update_menu(MenuState.EXIT)
            return True
        elif nextState == GameState.EXIT:
            self._update_game(GameState.EXIT)
            return False
        elif nextState == GameState.BACK:
            self._state_back()
            return True
    
    def _update_game(self, gameState):
        self.gameState = gameState
        self.gameStack._push_stateStack(gameState)
    
    def _update_menu(self, menuState):
        self.menuState = menuState
        self.menuStack._push_stateStack(menuState)
    
    def _update_door(self, doorState):
        self.doorState = doorState
    
    def _state_back(self):
        self.gameStack._pop_stateStack()
        self.gameState = self.gameStack._current_stateStack()
        if self.gameState == GameState.MENU:
            self.menuStack._pop_stateStack()
            self.menuState = self.menuStack._current_stateStack()