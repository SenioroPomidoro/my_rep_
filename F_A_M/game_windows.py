import sys

from PyQt6.QtWidgets import QMainWindow, QLabel, QPushButton, QLCDNumber
from PyQt6.QtGui import QPixmap, QIcon
import csv

from main_windows import MainWindow


class MainGameWindow(QMainWindow):
    def __init__(self, session_name):
        super().__init__()

        self.session_name = session_name

        self.setGeometry(50, 50, 1100, 900)
        self.setFixedSize(1100, 900)

        self.setWindowTitle("FISH AND MATH | КАРТА МИРА")
        self.setStyleSheet(F"font-size: 30px;"
                           F"color: black;"
                           F"font-family: Times;")

        self.setWindowIcon(QIcon("game_images/game_icons/256x256.ico"))

        self.grab_data()
        self.initButtons()
        self.initDisplays()

    def grab_data(self):
        with open("data_files/saves.csv") as f:
            reader = csv.DictReader(f, delimiter=';')
            data = [i for i in reader if i["save_name"] == self.session_name][0]

        self.coins = data["coins"]
        self.diamonds = data["diamonds"]
        self.worms = data["worms"]
        self.exp = data["exp"]

    def initButtons(self):
        map_pixmap = QPixmap("game_images/map_images/map.png")

        self.main_label = QLabel(self)
        self.main_label.resize(1100, 900)
        self.main_label.setPixmap(map_pixmap)

        self.back_button = QPushButton("СОХРАНИТЬ И ВЫЙТИ", self)
        self.back_button.resize(self.back_button.sizeHint())
        self.back_button.move(10, 850)
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
        worm_pixmap = QPixmap("game_images/game_icons/worm.png")

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

    def go_to_first(self):
        pass

    def go_to_ice(self):
        pass

    def go_to_air(self):
        pass

    def go_to_volcano(self):
        pass

    def back_action(self):
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

        self.main_window = MainWindow()
        self.main_window.show()

        self.close()
