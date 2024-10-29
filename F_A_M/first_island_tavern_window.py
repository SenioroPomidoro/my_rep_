from PyQt6.QtWidgets import QWidget, QLabel, QPushButton, QLCDNumber
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtCore import QUrl
from PyQt6.QtMultimedia import QSoundEffect


import csv

from chain import start_first_island_window


class TavernWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.effect = QSoundEffect()
        self.effect.setSource(QUrl.fromLocalFile("game_music/click.wav"))
        self.door_effect = QSoundEffect()
        self.door_effect.setSource(QUrl.fromLocalFile("game_music/door.wav"))

        self.setGeometry(50, 50, 1100, 900)
        self.setFixedSize(1100, 900)
        self.setWindowTitle("FISH AND MATH | ДОМ")
        self.setStyleSheet(F"font-size: 40px;"
                           F"color: black;"
                           F"font-family: Times;")

        self.setWindowIcon(QIcon("game_images/game_icons/256x256.ico"))

        self.initUi()

    def initUi(self):
        self.initNature()
        self.grab_data()
        self.initDisplays()
        self.initButtons()

    def initNature(self):
        man_pixmap = QPixmap("game_images/map_images/first_island/man.png")

        self.man_label = QLabel(self)
        self.man_label.resize(1100, 900)
        self.man_label.setPixmap(man_pixmap)

    def initButtons(self):
        self.back_button = QPushButton("ВЫЙТИ ↓", self)
        self.back_button.setStyleSheet(F"font-size: 25px; background: brown")
        self.back_button.resize(self.back_button.sizeHint())
        self.back_button.move(500, 835)
        self.back_button.clicked.connect(self.back_action)

        self.talk_button = QPushButton("ГОВОРИТЬ", self)
        self.talk_button.setStyleSheet(F"font-size: 30px; background: #232c16")
        self.talk_button.move(625, 650)
        self.talk_button.clicked.connect(self.talk_action)

    def grab_data(self):
        with open("data_files/current_session_data.csv") as f:
            reader = csv.DictReader(f, delimiter=";")
            data = [i for i in reader][0]
        self.session_name = data["save_name"]
        self.coins = data["coins"]
        self.diamonds = data["diamonds"]
        self.worms = data["worms"]
        self.exp = data["exp"]
        self.first_start = data["first_start"]

    def initDisplays(self):
        coin_pixmap = QPixmap("game_images/game_icons/coin.png")
        ore_pixmap = QPixmap("game_images/game_icons/ore.png")
        worm_pixmap = QPixmap("game_images/nature_images/worm.png")

        self.money_label = QLabel(self)
        self.money_label.resize(50, 50)
        self.money_label.move(5, 15)
        self.money_label.setPixmap(coin_pixmap)

        self.money_display = QLCDNumber(self)
        self.money_display.resize(50, 40)
        self.money_display.move(60, 20)
        self.money_display.display(self.coins)
        self.money_display.setStyleSheet(F"background: white;")

        self.diamond_label = QLabel(self)
        self.diamond_label.resize(50, 50)
        self.diamond_label.move(5, 75)
        self.diamond_label.setPixmap(ore_pixmap)

        self.diamonds_display = QLCDNumber(self)
        self.diamonds_display.resize(50, 40)
        self.diamonds_display.move(60, 80)
        self.diamonds_display.display(self.diamonds)
        self.diamonds_display.setStyleSheet(F"background: white")

        self.worms_label = QLabel(self)
        self.worms_label.resize(50, 50)
        self.worms_label.move(5, 130)
        self.worms_label.setPixmap(worm_pixmap)

        self.worms_display = QLCDNumber(self)
        self.worms_display.resize(50, 40)
        self.worms_display.move(60, 140)
        self.worms_display.display(self.worms)
        self.worms_display.setStyleSheet(F"background: white")

    def back_action(self):
        self.door_effect.play()

        self.first_island_window = start_first_island_window()
        self.first_island_window.show()

        self.close()

    def talk_action(self):
        self.effect.play()
