from chain import start_main_window, start_game_main_window

from PyQt6.QtWidgets import QWidget, QPushButton, QListWidget, QListWidgetItem, QLabel, QMessageBox
from PyQt6.QtGui import QPixmap, QIcon

import csv


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
        self.delete_button.clicked.connect(self.delete_click)

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
        self.main_window = start_main_window()
        self.main_window.show()
        self.close()

    def delete_click(self):
        try:
            self.list_widget.currentItem().text()
        except AttributeError:
            return
        # исключается возможность удаления невыбранного элемента

        ask_box = QMessageBox(self)
        ask_box.setWindowTitle("ПОДТВЕРЖДЕНИЕ УДАЛЕНИЯ")
        ask_box.setText("Вы точно хотите удалить сохранение?")
        ask_box.setInformativeText("Вернуть его будет невозможно.")

        ask_box.setStyleSheet("background: blue")

        ask_box.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        ask_box.buttonClicked.connect(self.delete_action)

        ask_box.exec()

    def delete_action(self, button):
        if button.text() == '&Yes':
            to_delete = self.list_widget.currentItem().text()

            with open("data_files/saves.csv", "r") as f:
                reader = csv.DictReader(f, delimiter=";")
                data = [i for i in reader]
                head = list(data[0].keys())

            with open("data_files/saves.csv", "w") as f:
                writer = csv.writer(f, delimiter=";")
                writer.writerow(head)
                for item in data:
                    if item["save_name"] != to_delete:
                        writer.writerow(list(item.values()))

            self.new_load = LoadWindow()
            self.new_load.show()
            self.close()

        else:
            pass

    def info_action(self):
        pass

    def start_game(self):
        save_name = self.list_widget.currentItem().text()
        self.game_window = start_game_main_window(save_name)
        self.game_window.show()

        self.close()