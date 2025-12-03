from dataclasses import dataclass, field
from  enums.interaction_objects import InteractableType, InteractionType, InteractionResult

@dataclass
class InteractionContext:

        target_object: InteractableType = field(default=InteractableType)
        interaction_type: InteractionType = field(default=InteractionType)
        interaction_result: InteractionResult = field(default=InteractionResult)