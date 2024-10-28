from chain import start_main_window, start_game_main_window

from PyQt6.QtWidgets import QWidget, QPushButton, QLabel, QLineEdit
from PyQt6.QtGui import QPixmap, QIcon

import csv


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
        self.main_window = start_main_window()
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
        self.game_window = start_game_main_window(save_name)
        self.game_window.show()

        self.close()
