import csv

import sys

import importlib

from PyQt6.QtWidgets import QMainWindow, QWidget, QPushButton, QLineEdit, QLabel, QListWidget, QListWidgetItem, QSlider
from PyQt6.QtWidgets import QLCDNumber, QMessageBox
from PyQt6.QtGui import QPixmap, QIcon

from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput
from PyQt6.QtCore import QUrl, Qt

from chain import my_function

# !!!!!!!!!!!! ПОТОМ РАСКИДАЮ ОКНА ПО ОТДЕЛЬНЫМ ФАЙЛАМ !!!!!!!!!!!!!!!!


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(50, 50, 800, 800)
        self.setFixedSize(800, 800)
        self.setWindowTitle("FISH AND MATH | ГЛАВНОЕ МЕНЮ")
        self.setStyleSheet(F"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0.6 blue, stop: 1 white);"
                           F"font-size: 40px;"
                           F"color: black;"
                           F"font-family: Times;")

        self.setWindowIcon(QIcon("game_images/game_icons/256x256.ico"))

        self.initNature()
        self.initUi()
        self.music()

    def initUi(self):
        self.player = QMediaPlayer()
        self.audioOutput = QAudioOutput()
        self.player.setAudioOutput(self.audioOutput)
        self.player.setSource(QUrl.fromLocalFile("game_music/main_window.mp3"))

        self.label_for_game_label = QLabel(self)
        self.label_for_game_label.resize(800, 200)
        self.label_for_game_label.move(0, 0)
        self.label_for_game_label.setPixmap(QPixmap("game_images/game_icons/game_label.png"))
        self.label_for_game_label.setStyleSheet(F"background: blue")

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
        if self.player.isPlaying():
            self.player.stop()

        self.load_window = LoadWindow()
        self.load_window.show()
        self.close()

    def create_action(self):
        if self.player.isPlaying():
            self.player.stop()

        self.create_window = CreateWindow()
        self.create_window.show()
        self.close()

    def settings_action(self):
        if self.player.isPlaying():
            self.player.stop()

        self.settings_window = SettingsWindow()
        self.settings_window.show()
        self.close()

    def info_action(self):
        pass

    def exit_action(self):
        sys.exit()


class LoadWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(50, 50, 800, 800)
        self.setFixedSize(800, 800)
        self.setWindowTitle("FISH AND MATH | ОКНО ЗАГРУЗКИ")
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

        self.delete_button = QPushButton("УДАЛИТЬ СОХРАНЕНИЕ", self)
        self.delete_button.resize(500, 70)
        self.delete_button.move(20, 610)
        self.delete_button.clicked.connect(self.delete_action)

        self.info_button = QPushButton("info", self)
        self.info_button.resize(90, 60)
        self.info_button.move(700, 730)
        self.info_button.setStyleSheet(F"background: #00008b")
        self.info_button.clicked.connect(self.info_action)

        self.list_widget = QListWidget(self)
        self.list_widget.resize(590, 590)
        self.list_widget.move(10, 10)
        self.list_widget.setStyleSheet("background: white")

        with open("data_files/saves.csv", "r") as f:
            reader = csv.DictReader(f, delimiter=";")
            for item in reader:
                self.list_widget.addItem(QListWidgetItem(item["save_name"]))

        self.list_widget.doubleClicked.connect(self.start_game)

    def initNature(self):
        grass_pixmap = QPixmap("game_images/nature_images/grass.png")
        bubble_pixmap = QPixmap("game_images/nature_images/bubble.png")
        dolphin_pixmap = QPixmap("game_images/nature_images/dolphin.png")

        self.grass = QLabel(self)
        self.grass.setPixmap(grass_pixmap)
        self.grass.resize(300, 187)
        self.grass.move(0, 660)
        self.grass.setStyleSheet(F"background: transparent")

        self.dolphin = QLabel(self)
        self.dolphin.setPixmap(dolphin_pixmap)
        self.dolphin.resize(350, 213)
        self.dolphin.move(520, 490)
        self.dolphin.setStyleSheet(F"background: transparent")

    def back_action(self):
        self.main_window = MainWindow()
        self.main_window.show()
        self.close()

    def delete_action(self):
        pass

    def info_action(self):
        pass

    def start_game(self):
        save_name = self.list_widget.currentItem().text()
        self.game_window = my_function(save_name)
        self.game_window.show()

        self.close()


class CreateWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(50, 50, 800, 800)
        self.setFixedSize(800, 800)
        self.setWindowTitle("FISH AND MATH | ОКНО НОВОЙ ИГРЫ")
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

        self.save_label = QLabel("НАЗВАНИЕ МИРА: ", self)
        self.save_label.resize(self.save_label.sizeHint())
        self.save_label.setStyleSheet(F"background: transparent")
        self.save_label.move(230, 250)

        self.get_save_name = QLineEdit(self)
        self.get_save_name.resize(700, 100)
        self.get_save_name.move(50, 300)
        self.get_save_name.setStyleSheet(F"background: white")

        self.save_button = QPushButton("СОЗДАТЬ МИР", self)
        self.save_button.resize(self.save_button.sizeHint())
        self.save_button.move(250, 450)
        self.save_button.clicked.connect(self.save_action)

        self.statusbar = QLabel(self)
        self.statusbar.resize(700, 50)
        self.statusbar.move(100, 400)
        self.statusbar.setStyleSheet("color: red; background: transparent")

    def initNature(self):
        seledka_pixmap = QPixmap("game_images/nature_images/seledka.png")
        grass_pixmap = QPixmap("game_images/nature_images/grass.png")

        self.seledka_label = QLabel(self)
        self.seledka_label.setPixmap(seledka_pixmap)
        self.seledka_label.resize(self.seledka_label.sizeHint())
        self.seledka_label.setStyleSheet(F"background: transparent")

        self.grass_label = QLabel(self)
        self.grass_label.setPixmap(grass_pixmap)
        self.grass_label.resize(self.grass_label.sizeHint())
        self.grass_label.move(0, 660)
        self.grass_label.setStyleSheet(F"background: transparent")

    def back_action(self):
        self.main_window = MainWindow()
        self.main_window.show()
        self.close()

    def save_action(self):
        save_name = self.get_save_name.text()

        if not save_name:
            self.statusbar.setText("ошибка: введите непустое название.")
            return

        try:
            with open("data_files/saves.csv", "r") as f:
                reader = csv.DictReader(f, delimiter=";")
                data = [i for i in reader]
        except Exception:
            self.statusbar.setText("ошибка чтения файла: обратитесь к админу")
            return

        names_data = list(map(lambda x: x["save_name"].split(".")[0], data))

        if save_name in names_data:
            self.statusbar.setText("ошибка: такой мир уже существует.")
            return

        with open("data_files/saves.csv", "a") as f:
            writer = csv.writer(f, delimiter=";")
            writer.writerow([save_name, "0", "0", "0", "0", "1"])

        self.start_game(save_name)

    def info_action(self):
        pass

    def start_game(self, save_name):
        self.game_window = my_function(save_name)
        self.game_window.show()

        self.close()


class SettingsWindow(QWidget):
    def __init__(self):
        super().__init__()

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
        self.main_window = MainWindow()
        self.main_window.show()
        self.close()

    def save_action(self):
        with open("data_files/settings.csv", "w") as f:
            writer = csv.writer(f, delimiter=";")
            writer.writerow(["music_in_menu", "music_in_game"])
            writer.writerow([self.menu_sound_slider.value(), self.game_sound_slider.value()])
        self.statusbar.setText("УСПЕШНО СОХРАНЕНО")
        self.statusbar.resize(self.statusbar.sizeHint())

    def info_action(self):
        pass

    def menu_change(self):
        self.menu_lcd.display(self.menu_sound_slider.value())

    def game_change(self):
        self.game_lcd.display(self.game_sound_slider.value())
