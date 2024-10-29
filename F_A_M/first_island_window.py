from PyQt6.QtWidgets import QWidget, QLabel, QLCDNumber, QPushButton
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtMultimedia import QSoundEffect
from PyQt6.QtCore import QUrl


from chain import start_game_main_window, start_tavern_window, start_worm_field_window, start_lake_window

import csv


class FirstIsland(QWidget):
    def __init__(self):
        super().__init__()

        self.effect = QSoundEffect()
        self.effect.setSource(QUrl.fromLocalFile("game_music/click.wav"))

        self.door_effect = QSoundEffect()
        self.door_effect.setSource(QUrl.fromLocalFile("game_music/door.wav"))

        self.setGeometry(50, 50, 1100, 900)
        self.setFixedSize(1100, 900)
        self.setWindowTitle("FISH AND MATH | МИРНЫЙ ОСТРОВ")
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
        background_pixmap = QPixmap("game_images/map_images/first_island/man_house.png")

        self.background_label = QLabel(self)
        self.background_label.resize(1100, 900)
        self.background_label.setPixmap(background_pixmap)

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

    def initButtons(self):
        self.back_button = QPushButton("К КАРТЕ МИРА", self)
        self.back_button.setStyleSheet(F"font-size: 20px; background: #232c16")
        self.back_button.resize(self.back_button.sizeHint())
        self.back_button.move(940, 0)
        self.back_button.clicked.connect(self.back_action)

        self.to_worms_field = QPushButton("← НА ПОЛЕ", self)
        self.to_worms_field.setStyleSheet(F"background: #232c16")
        self.to_worms_field.resize(self.to_worms_field.sizeHint())
        self.to_worms_field.move(0, 835)
        self.to_worms_field.clicked.connect(self.to_worms_action)

        self.to_lake_button = QPushButton("К ОЗЕРУ →", self)
        self.to_lake_button.setStyleSheet(F"background: #232c16")
        self.to_lake_button.resize(self.to_lake_button.sizeHint())
        self.to_lake_button.move(890, 835)
        self.to_lake_button.clicked.connect(self.to_lake_action)

        self.to_tavern_button = QPushButton("ВОЙТИ ↑", self)
        self.to_tavern_button.setStyleSheet(F"font-size: 25px; background: brown")
        self.to_tavern_button.resize(self.to_tavern_button.sizeHint())
        self.to_tavern_button.move(525, 650)
        self.to_tavern_button.clicked.connect(self.enter_action)

    def back_action(self):
        self.effect.play()

        self.game_main_window = start_game_main_window(self.session_name)
        self.game_main_window.show()

        self.close()

    def to_worms_action(self):
        self.effect.play()

        self.worms_field = start_worm_field_window()
        self.worms_field.show()

        self.close()

    def to_lake_action(self):
        self.effect.play()

        self.lake_window = start_lake_window()
        self.lake_window.show()

        self.close()

    def enter_action(self):
        self.door_effect.play()

        self.tavern_window = start_tavern_window()
        self.tavern_window.show()

        self.close()
