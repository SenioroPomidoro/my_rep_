def start_game_main_window(save_name):
    from game_main_window import MainGameWindow
    return MainGameWindow(save_name)


def start_load_window():
    from load_window import LoadWindow
    return LoadWindow()


def start_main_window():
    from main_window import MainWindow
    return MainWindow()


def start_settings_window():
    from settings_window import SettingsWindow
    return SettingsWindow()


def start_create_window():
    from create_window import CreateWindow
    return CreateWindow()
