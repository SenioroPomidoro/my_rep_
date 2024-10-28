from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
from PyQt6.QtCore import Qt
import sys


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # Настройка основного окна
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Пример диалога выхода')

        # Кнопка для вызова диалога выхода
        btn = QPushButton('Выйти', self)
        btn.move(50, 50)
        btn.clicked.connect(self.show_dialog)

        self.show()

    def show_dialog(self):
        # Создание сообщения для диалога
        msg_box = QMessageBox(self)
        msg_box.setStyleSheet("background: red")
        msg_box.setText("Вы действительно хотите выйти?")
        msg_box.setInformativeText("Все несохраненные данные будут потеряны.")
        msg_box.setWindowTitle("Подтверждение выхода")
        msg_box.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        msg_box.buttonClicked.connect(self.on_button_clicked)

        # Отображение диалога
        msg_box.exec()

    def on_button_clicked(self, button):
        if button.text() == '&Yes':
            QApplication.quit()
        else:
            pass  # Ничего не делать, если пользователь нажал 'Нет'


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    sys.exit(app.exec())