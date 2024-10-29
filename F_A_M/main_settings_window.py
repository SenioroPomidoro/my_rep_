from PyQt6.QtWidgets import QWidget, QSlider, QPushButton, QLCDNumber, QLabel
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtCore import Qt, QUrl

from PyQt6.QtMultimedia import QSoundEffect

from chain import start_main_window

import csv


class SettingsWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.effect = QSoundEffect()
        self.effect.setSource(QUrl.fromLocalFile("game_music/click.wav"))

        with open("data_files/settings.csv", "r") as file:
            reader = csv.DictReader(file, delimiter=";")
            data = [i for i in reader]

        self.val_menu = int(data[0]["music_in_menu"])
        self.val_game = int(data[0]["music_in_game"])

        self.setGeometry(50, 50, 800, 800)
        self.setFixedSize(800, 800)
        self.setWindowTitle("FISH AND MATH | ОКНО НАСТРОЕК")
        self.setStyleSheet(F"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0.6 blue, stop: 1 white);"
                           F"font-size: 40px;"
                           F"color: black;"
                           F"font-family: Times;")

        self.setWindowIcon(QIcon("game_images/game_icons/256x256.ico"))

        self.initNature()
        self.initUi()

    def initUi(self):
        self.back_button = QPushButton("НАЗАД", self)
        self.back_button.resize(400, 70)
        self.back_button.move(290, 720)
        self.back_button.clicked.connect(self.back_action)

        self.info_button = QPushButton("info", self)
        self.info_button.resize(90, 60)
        self.info_button.move(700, 730)
        self.info_button.setStyleSheet(F"background: #00008b")
        self.info_button.clicked.connect(self.info_action)

        self.menu_label = QLabel("МУЗЫКА В МЕНЮ: ", self)
        self.menu_label.resize(self.menu_label.sizeHint())
        self.menu_label.move(0, 70)
        self.menu_label.setStyleSheet(F"background: transparent")

        self.menu_lcd = QLCDNumber(self)
        self.menu_lcd.resize(120, 60)
        self.menu_lcd.move(530, 120)
        self.menu_lcd.display(self.val_menu)
        self.menu_lcd.setStyleSheet(F"background: white")

        self.menu_sound_slider = QSlider(self)
        self.menu_sound_slider.setOrientation(Qt.Orientation.Horizontal)
        self.menu_sound_slider.resize(500, 40)
        self.menu_sound_slider.move(0, 130)
        self.menu_sound_slider.setRange(0, 100)
        self.menu_sound_slider.setValue(self.val_menu)
        self.menu_sound_slider.setStyleSheet(F"background: transparent")
        self.menu_sound_slider.valueChanged.connect(self.menu_change)

        self.game_label = QLabel("ЗВУКИ В ИГРЕ: ", self)
        self.game_label.resize(self.menu_label.sizeHint())
        self.game_label.move(0, 190)
        self.game_label.setStyleSheet(F"background: transparent")

        self.game_lcd = QLCDNumber(self)
        self.game_lcd.resize(120, 60)
        self.game_lcd.move(530, 220)
        self.game_lcd.display(self.val_game)
        self.game_lcd.setStyleSheet(F"background: white")

        self.game_sound_slider = QSlider(self)
        self.game_sound_slider.setOrientation(Qt.Orientation.Horizontal)
        self.game_sound_slider.resize(500, 40)
        self.game_sound_slider.move(0, 240)
        self.game_sound_slider.setRange(0, 100)
        self.game_sound_slider.setValue(self.val_game)
        self.game_sound_slider.setStyleSheet(F"background: transparent")
        self.game_sound_slider.valueChanged.connect(self.game_change)

        self.save_button = QPushButton("СОХРАНИТЬ", self)
        self.save_button.resize(self.save_button.sizeHint())
        self.save_button.move(10, 725)
        self.save_button.clicked.connect(self.save_action)

        self.statusbar = QLabel(self)
        self.statusbar.move(150, 0)
        self.statusbar.setStyleSheet("background: transparent")

    def initNature(self):
        town_pixmap = QPixmap("game_images/nature_images/town.png")

        self.town_label = QLabel(self)
        self.town_label.resize(800, 416)
        self.town_label.move(0, 525)
        self.town_label.setPixmap(town_pixmap)
        self.town_label.setStyleSheet("background: transparent")

    def back_action(self):
        self.effect.play()

        self.main_window = start_main_window()
        self.main_window.show()
        self.close()

    def save_action(self):
        self.effect.play()

        with open("data_files/settings.csv", "w") as f:
            writer = csv.writer(f, delimiter=";")
            writer.writerow(["music_in_menu", "music_in_game"])
            writer.writerow([self.menu_sound_slider.value(), self.game_sound_slider.value()])

        self.statusbar.setText("УСПЕШНО СОХРАНЕНО")
        self.statusbar.resize(self.statusbar.sizeHint())

    def info_action(self):
        self.effect.play()

    def menu_change(self):
        self.menu_lcd.display(self.menu_sound_slider.value())

    def game_change(self):
        self.game_lcd.display(self.game_sound_slider.value())
