from enums import GameState, MenuState, DoorState

class StateManager:
    
    def __init__(self):
        self.isGlobal = False
        self.gameState = GameState.INIT
        self.menuState = MenuState.MAIN
        self.doorState = DoorState.CLOSED
    
    def update(self, nextState):
        if nextState == GameState.INIT:
            self._update_game(GameState.MENU)
            self._update_menu(MenuState.MAIN)
        elif nextState == GameState.MENU:
            pass
        elif nextState == GameState.PLAYING:
            self._update_game(GameState.PLAYING)
        elif nextState == MenuState.CONTROLS:
            self._update_game(GameState.MENU)
            self._update_menu(MenuState.CONTROLS)
    
    def _update_game(self, gameState):
        self.gameState = gameState
    
    def _update_menu(self, menuState):
        self.menuState = menuState
    
    def _update_door(self, doorState):
        self.doorState = doorState
    

