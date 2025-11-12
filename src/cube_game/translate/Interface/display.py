from cube_game.mapping import menu_mapping
from enums.display import Display, MenuPoints, DisplayNavigation
from enums.commands import Command
from mapping import state_command_mapping

def render():

    return {
        MenuPoints: {
                    MenuPoints.MENU_OPTION: menu_mapping.menuMapping,
        },
        DisplayNavigation:{
                    DisplayNavigation.NAVIGATION: state_command_mapping.mapping,
                    DisplayNavigation.ALL_NAVIGATION: state_command_mapping.mapping
        },
}

