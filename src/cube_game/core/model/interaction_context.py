from enums.objects import InteractableID

class InteractionContext:

    def __init__(self, game_context):
        self.game_context = game_context
        self.target_object = InteractableID.NONE