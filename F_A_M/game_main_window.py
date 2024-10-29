from PyQt6.QtWidgets import QMainWindow, QLabel, QPushButton, QLCDNumber
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtMultimedia import QSoundEffect
from PyQt6.QtCore import QUrl

import csv

from chain import start_main_window, start_first_island_window


class MainGameWindow(QMainWindow):
    def __init__(self, session_name, from_menu=0):
        super().__init__()

        self.effect = QSoundEffect()
        self.effect.setSource(QUrl.fromLocalFile("game_music/click.wav"))

        if from_menu:
            self.file = "saves.csv"
        else:
            self.file = "current_session_data.csv"

        self.session_name = session_name

        self.setGeometry(50, 50, 1100, 900)
        self.setFixedSize(1100, 900)

        self.setWindowTitle("FISH AND MATH | КАРТА МИРА")
        self.setStyleSheet(F"font-size: 30px;"
                           F"color: black;"
                           F"font-family: Times;")

        self.setWindowIcon(QIcon("game_images/game_icons/256x256.ico"))

        self.grab_data()
        self.start_current_session()
        self.initButtons()
        self.initDisplays()
        self.lock_islands()

    def grab_data(self):
        with open(F"data_files/{self.file}") as f:
            reader = csv.DictReader(f, delimiter=';')
            data = [i for i in reader if i["save_name"] == self.session_name][0]

        self.coins = data["coins"]
        self.diamonds = data["diamonds"]
        self.worms = data["worms"]
        self.exp = data["exp"]
        self.first_start = data["first_start"]

    def start_current_session(self):
        with open("data_files/current_session_data.csv", "w") as f:
            writer = csv.writer(f, delimiter=";")
            writer.writerow(["save_name", "coins", "diamonds", "worms", "exp", "first_start"])
            writer.writerow([self.session_name, self.coins, self.diamonds, self.worms, self.exp, self.first_start])

    def initButtons(self):
        map_pixmap = QPixmap("game_images/map_images/map.png")

        self.main_label = QLabel(self)
        self.main_label.resize(1100, 900)
        self.main_label.setPixmap(map_pixmap)

        self.back_button = QPushButton("СОХРАНИТЬ И ВЫЙТИ", self)
        self.back_button.resize(self.back_button.sizeHint())
        self.back_button.move(10, 845)
        self.back_button.setStyleSheet(F"background: red")
        self.back_button.clicked.connect(self.back_action)

        self.first_island_button = QPushButton("Мирный остров", self)
        self.first_island_button.resize(self.first_island_button.sizeHint())
        self.first_island_button.move(130, 450)
        self.first_island_button.setStyleSheet(F"background: green;")
        self.first_island_button.clicked.connect(self.go_to_first)

        self.ice_island_button = QPushButton("Ледяной остров", self)
        self.ice_island_button.resize(self.ice_island_button.sizeHint())
        self.ice_island_button.move(410, 335)
        self.ice_island_button.setStyleSheet(F"background: #0000cd")
        self.ice_island_button.clicked.connect(self.go_to_ice)

        self.air_island_button = QPushButton("Воздушный остров", self)
        self.air_island_button.resize(self.air_island_button.sizeHint())
        self.air_island_button.move(735, 320)
        self.air_island_button.setStyleSheet(F"background: #87cefa")
        self.air_island_button.clicked.connect(self.go_to_air)

        self.volcano_island_button = QPushButton("Вулканический остров", self)
        self.volcano_island_button.resize(self.volcano_island_button.sizeHint())
        self.volcano_island_button.move(500, 650)
        self.volcano_island_button.setStyleSheet(F"background: #c10020")
        self.volcano_island_button.clicked.connect(self.go_to_volcano)

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

    def lock_islands(self):
        lock_pixmap = QPixmap("game_images/map_images/lock.png")

        if int(self.exp) < 100:
            self.ice_lock_label = QLabel(self)
            self.ice_lock_label.resize(150, 109)
            self.ice_lock_label.setPixmap(lock_pixmap)
            self.ice_lock_label.move(430, 260)
            self.ice_island_button.setEnabled(False)

        self.air_lock_label = QLabel(self)
        self.air_lock_label.resize(150, 109)
        self.air_lock_label.setPixmap(lock_pixmap)
        self.air_lock_label.move(785, 240)
        self.air_island_button.setEnabled(False)

        self.volcano_lock_label = QLabel(self)
        self.volcano_lock_label.resize(150, 109)
        self.volcano_lock_label.setPixmap(lock_pixmap)
        self.volcano_lock_label.move(575, 560)
        self.volcano_island_button.setEnabled(False)

    def go_to_first(self):
        self.effect.play()

        with open("data_files/current_session_data.csv", "w") as f:
            writer = csv.writer(f, delimiter=';')
            writer.writerow(["save_name", "coins", "diamonds", "worms", "exp", "first_start"])
            writer.writerow([self.session_name, self.coins, self.diamonds, self.worms, self.exp, self.first_start])

        self.first_island = start_first_island_window()
        self.first_island.show()

        self.close()

    def go_to_ice(self):
        pass

    def go_to_air(self):
        pass

    def go_to_volcano(self):
        pass

    def back_action(self):
        self.effect.play()

        with open("data_files/saves.csv", "r") as f:
            reader = csv.DictReader(f, delimiter=";")
            data = [i for i in reader]
        heads = list(data[0].keys())

        for item in range(len(data)):
            if data[item]["save_name"] == self.session_name:
                data[item]["coins"] = self.coins
                data[item]["diamonds"] = self.diamonds
                data[item]["worms"] = self.worms
                data[item]["exp"] = self.exp
                data[item]["first_start"] = 0

        with open("data_files/saves.csv", "w") as f:
            writer = csv.writer(f, delimiter=";")
            writer.writerow(heads)
            for item in data:
                writer.writerow(list(item.values()))

        self.main_window = start_main_window()
        self.main_window.show()

        self.close()
