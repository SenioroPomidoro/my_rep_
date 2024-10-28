from PyQt6.QtWidgets import QMainWindow, QLabel, QApplication, QPushButton
from PyQt6.QtGui import QMovie
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 1100, 900)

        self.movie = QMovie("game_images/map_images/lava_island/lava.gif")
        self.label = QLabel(self)
        self.label.resize(1100, 900)
        self.label.setMovie(self.movie)
        self.movie.start()

        self.button = QPushButton("ВЫХОД", self)
        self.button.resize(self.button.sizeHint())
        self.button.clicked.connect(self.exit)

    def exit(self):
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())