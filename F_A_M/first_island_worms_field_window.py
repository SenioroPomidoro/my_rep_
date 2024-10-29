from PyQt6.QtWidgets import QWidget, QLabel, QLCDNumber, QPushButton
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtCore import QTimer, QUrl
from PyQt6.QtMultimedia import QSoundEffect

from random import randint

import csv

from chain import start_first_island_window


class WormsField(QWidget):
    def __init__(self):
        super().__init__()

        self.effect = QSoundEffect()
        self.effect.setSource(QUrl.fromLocalFile("game_music/click.wav"))

        self.worm_effect = QSoundEffect()
        self.worm_effect.setSource(QUrl.fromLocalFile("game_music/worm.wav"))

        self.setGeometry(50, 50, 1100, 900)
        self.setFixedSize(1100, 900)
        self.setWindowTitle("FISH AND MATH | МИРНЫЙ ОСТРОВ")
        self.setStyleSheet(F"font-size: 40px;"
                           F"color: black;"
                           F"font-family: Times;")

        self.setWindowIcon(QIcon("game_images/game_icons/256x256.ico"))
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_field)

        self.worms_left = 20
        self.score = 0

        self.initUi()

    def initUi(self):
        self.initNature()
        self.grab_data()
        self.initDisplays()
        self.initButtons()

    def initNature(self):
        field_pixmap = QPixmap("game_images/map_images/first_island/worms_field.png")

        self.worms_label = QLabel(self)
        self.worms_label.resize(1100, 900)
        self.worms_label.setPixmap(field_pixmap)

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

        self.worms_counter = QLabel(self)
        self.worms_counter.setText("Червячков осталось: 0")
        self.worms_counter.resize(450, 100)
        self.worms_counter.move(650, 0)

        self.worms_hatched = QLabel(self)
        self.worms_hatched.setText("Червячков поймано: 0")
        self.worms_hatched.resize(450, 100)
        self.worms_hatched.move(650, 100)

    def initButtons(self):
        self.back_button = QPushButton("К ДОМУ →", self)
        self.back_button.resize(self.back_button.sizeHint())
        self.back_button.move(895, 835)
        self.back_button.setStyleSheet(F"background: #232c16")
        self.back_button.clicked.connect(self.back_action)

        self.start_event_button = QPushButton("КОПАТЬ ЧЕРВЯЧКОВ!", self)
        self.start_event_button.resize(self.start_event_button.sizeHint())
        self.start_event_button.move(300, 820)
        self.start_event_button.setStyleSheet(F"background: #2fc22f")
        self.start_event_button.clicked.connect(self.start_worms_event)

        self.worm = QPushButton(self)
        self.worm.setGeometry(randint(60, 1040), randint(475, 670), 60, 60)
        self.worm.setStyleSheet(F"background: #3d001e; border-radius: 30px")
        self.worm.setVisible(False)
        self.worm.clicked.connect(self.worm_clicked)

    def back_action(self):
        self.effect.play()

        self.game_main_window = start_first_island_window()
        self.game_main_window.show()

        self.close()

    def start_worms_event(self):
        self.effect.play()

        self.timer.start(700)
        self.worm.setEnabled(True)

    def update_field(self):
        self.worms_left -= 1
        self.worms_counter.setText(F"Червячков осталось: {self.worms_left}")

        if self.worms_left <= 0:
            self.worm.setVisible(False)
            self.worm.setEnabled(False)
            self.end_worms_event()

        x, y = randint(60, 1040), randint(460, 670)
        self.worm.move(x, y)
        self.worm.setVisible(True)

    def worm_clicked(self):
        self.worm_effect.play()

        self.score += 1
        self.worms_hatched.setText(F"Червячков поймано: {self.score}")
        self.worm.setVisible(False)

    def end_worms_event(self):
        self.timer.stop()
        self.worms_hatched.setText(F"Червячков осталось: 0")
        self.worms_counter.setText(F"Червячков поймано: 0")

        self.worms = int(self.worms) + self.score
        self.worms_display.display(self.worms)

        with open("data_files/current_session_data.csv", "w") as f:
            writer = csv.writer(f, delimiter=";")
            writer.writerow(["save_name", "coins", "diamonds", "worms", "exp", "first_start"])
            writer.writerow([self.session_name, self.coins, self.diamonds, self.worms, self.exp, self.first_start])

        self.worms_left = 20
        self.score = 0

