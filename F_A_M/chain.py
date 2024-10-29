def start_game_main_window(save_name, from_menu=0):
    from game_main_window import MainGameWindow
    return MainGameWindow(save_name, from_menu)


def start_load_window():
    from main_load_window import LoadWindow
    return LoadWindow()


def start_main_window():
    from main_window import MainWindow
    return MainWindow()


def start_settings_window():
    from main_settings_window import SettingsWindow
    return SettingsWindow()


def start_create_window():
    from main_create_window import CreateWindow
    return CreateWindow()


def start_first_island_window():
    from first_island_window import FirstIsland
    return FirstIsland()


def start_tavern_window():
    from first_island_tavern_window import TavernWindow
    return TavernWindow()


def start_worm_field_window():
    from first_island_worms_field_window import WormsField
    return WormsField()


def start_lake_window():
    from first_island_lake_window import LakeWindow
    return LakeWindow()
