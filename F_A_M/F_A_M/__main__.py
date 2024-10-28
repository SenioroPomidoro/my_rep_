import sys

from PyQt6.QtWidgets import QApplication
from main_window import MainWindow

if __name__ == "__main__":
    game_app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(game_app.exec())
