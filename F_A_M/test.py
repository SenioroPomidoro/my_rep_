from PyQt6.QtWidgets import QApplication, QPushButton, QMainWindow
from PyQt6.QtMultimedia import QSoundEffect
from PyQt6.QtCore import QUrl

import sys


class Example(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(300, 300, 300, 300)
        self.button = QPushButton("Нажми", self)
        self.button.clicked.connect(self.click)

        self.effect = QSoundEffect()
        self.effect.setSource(QUrl.fromLocalFile("click.wav"))

    def click(self):
        self.effect.play()

# app = QApplication([])
#
# button = QPushButton('Нажми меня')
# button.show()
#
# sound_effect = QSoundEffect()
# sound_effect.setSource(QUrl.fromLocalFile('click_sound.wav'))
#
# def on_button_click():
#     if sound_effect.status() == QSoundEffect.Status.StoppedState:
#         sound_effect.play()
#
# button.clicked.connect(on_button_click)
#
# sys.exit(app.exec())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())