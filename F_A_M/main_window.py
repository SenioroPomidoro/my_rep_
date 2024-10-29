import csv
import sys

from PyQt6.QtWidgets import QMainWindow, QPushButton, QLabel
from PyQt6.QtGui import QPixmap, QIcon

from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput, QSoundEffect
from PyQt6.QtCore import QUrl

from chain import start_settings_window, start_load_window, start_create_window


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.effect = QSoundEffect()
        self.effect.setSource(QUrl.fromLocalFile("game_music/click.wav"))

        self.setGeometry(50, 50, 800, 800)
        self.setFixedSize(800, 800)
        self.setWindowTitle("FISH AND MATH | ГЛАВНОЕ МЕНЮ")
        self.setStyleSheet(F"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0.6 blue, stop: 1 white);"
                           F"font-size: 40px;"
                           F"color: black;"
                           F"font-family: Times;")

        self.setWindowIcon(QIcon("game_images/game_icons/256x256.ico"))

        self.initButtons()
        self.grab_music_data()
        self.initNature()
        self.music()

    def initButtons(self):
        self.player = QMediaPlayer(self)
        self.audioOutput = QAudioOutput()
        self.player.setAudioOutput(self.audioOutput)
        self.player.setSource(QUrl.fromLocalFile("game_music/main_window.mp3"))

        self.load_button = QPushButton("ЗАГРУЗИТЬ ИГРУ", self)
        self.load_button.move(200, 250)
        self.load_button.resize(400, 70)
        self.load_button.clicked.connect(self.load_action)

        self.create_button = QPushButton("НОВАЯ ИГРА", self)
        self.create_button.move(200, 320)
        self.create_button.resize(400, 70)
        self.create_button.clicked.connect(self.create_action)

        self.settings_button = QPushButton("НАСТРОЙКИ", self)
        self.settings_button.move(200, 390)
        self.settings_button.resize(400, 70)
        self.settings_button.clicked.connect(self.settings_action)

        self.exit_button = QPushButton("ВЫХОД", self)
        self.exit_button.move(200, 460)
        self.exit_button.resize(400, 70)
        self.exit_button.clicked.connect(self.exit_action)

        self.info_button = QPushButton("info", self)
        self.info_button.resize(90, 60)
        self.info_button.move(700, 730)
        self.info_button.setStyleSheet(F"background: #00008b")
        self.info_button.clicked.connect(self.info_action)

        self.music_button = QPushButton(self)
        self.music_button.resize(50, 50)
        self.music_button.move(60, 350)
        self.music_button.setStyleSheet(F"background: blue")
        self.music_button.clicked.connect(self.music)

    def initNature(self):
        bubble_pixmap = QPixmap("game_images/nature_images/bubble.png")
        grass1_pixmap = QPixmap("game_images/nature_images/grass.png")
        crabik_pixmap = QPixmap("game_images/nature_images/crab.png")
        octopus_pixmap = QPixmap("game_images/nature_images/octopus.png")
        label_pixmap = QPixmap("game_images/game_icons/game_label.png")

        self.label_for_game_label = QLabel(self)
        self.label_for_game_label.resize(800, 200)
        self.label_for_game_label.move(0, 0)
        self.label_for_game_label.setPixmap(label_pixmap)
        self.label_for_game_label.setStyleSheet(F"background: blue")

        self.bubble1 = QLabel(self)
        self.bubble1.resize(50, 47)
        self.bubble1.move(40, 500)

        self.bubble2 = QLabel(self)
        self.bubble2.resize(50, 47)
        self.bubble2.move(80, 440)

        self.bubble3 = QLabel(self)
        self.bubble3.resize(50, 47)
        self.bubble3.move(100, 540)

        self.bubble4 = QLabel(self)
        self.bubble4.resize(50, 47)
        self.bubble4.move(60, 600)

        self.bubble1.setStyleSheet(F"background: transparent")
        self.bubble2.setStyleSheet(F"background: transparent")
        self.bubble3.setStyleSheet(F"background: transparent")
        self.bubble4.setStyleSheet(F"background: transparent")

        self.bubble1.setPixmap(bubble_pixmap)
        self.bubble2.setPixmap(bubble_pixmap)
        self.bubble3.setPixmap(bubble_pixmap)
        self.bubble4.setPixmap(bubble_pixmap)

        self.crab = QLabel(self)
        self.crab.resize(350, 350)
        self.crab.move(180, 550)
        self.crab.setPixmap(crabik_pixmap)
        self.crab.setStyleSheet(F"background: transparent")

        self.octopus = QLabel(self)
        self.octopus.resize(150, 108)
        self.octopus.move(10, 240)
        self.octopus.setPixmap(octopus_pixmap)
        self.octopus.setStyleSheet(F"background: transparent")

        self.grass1 = QLabel(self)
        self.grass1.resize(300, 187)
        self.grass1.move(-20, 660)

        self.grass2 = QLabel(self)
        self.grass2.resize(300, 187)
        self.grass2.move(420, 660)

        self.grass1.setPixmap(grass1_pixmap)
        self.grass2.setPixmap(grass1_pixmap)

        self.grass1.setStyleSheet(F"background: transparent")
        self.grass2.setStyleSheet(F"background: transparent")

    def music(self):
        if self.player.isPlaying():
            self.player.stop()
            self.music_button.setIcon(QIcon("game_images/sounds_images/sounds_off.ico"))
        else:
            self.player.play()
            self.music_button.setIcon(QIcon("game_images/sounds_images/sound_on.ico"))

    def load_action(self):
        self.effect.play()

        if self.player.isPlaying():
            self.player.stop()

        self.load_window = start_load_window()
        self.load_window.show()
        self.close()

    def create_action(self):
        self.effect.play()

        if self.player.isPlaying():
            self.player.stop()
        self.create_window = start_create_window()
        self.create_window.show()

        self.close()

    def settings_action(self):
        self.effect.play()

        if self.player.isPlaying():
            self.player.stop()

        self.settings_window = start_settings_window()
        self.settings_window.show()
        self.close()

    def grab_music_data(self):
        with open("data_files/settings.csv", "r") as f:
            reader = csv.DictReader(f, delimiter=";")
            data = next(reader)

        self.music_in_menu_val = data["music_in_menu"]
        self.audioOutput.setVolume(int(self.music_in_menu_val) / 100)

    def info_action(self):
        self.effect.play()

    def exit_action(self):
        self.effect.play()
        sys.exit()
