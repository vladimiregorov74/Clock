'''PyQt6 предоставляет возможность создания модальных окон, которые блокируют взаимодействие
пользователя с другими окнами, пока модальное окно открыто. Это может быть полезно, когда вам
нужно получить ответ или ввод от пользователя перед продолжением выполнения программы.
    В этом примере у нас есть главное окно MainWindow, которое содержит кнопку "Открыть модальное
окно". При нажатии на эту кнопку создается экземпляр модального окна ModalDialog, и вызывается
его метод exec(), чтобы показать его как модальное окно. Модальное окно содержит метку и кнопку
"Закрыть". При нажатии на кнопку "Закрыть" модальное окно закрывается.В примере мы используем
 app.exec() для запуска цикла обработки событий приложения. Это важно, чтобы гарантировать
 правильное взаимодействие с модальным окном.'''
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QDialog, QVBoxLayout, QLabel, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Пример модального окна")
        self.setGeometry(100, 100, 200, 100)

        self.button = QPushButton("Открыть модальное окно", self)
        self.button.clicked.connect(self.open_modal_dialog)
        self.setCentralWidget(self.button)

    def open_modal_dialog(self):
        dialog = ModalDialog()
        dialog.exec()

class ModalDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Модальное окно")
        self.setLayout(QVBoxLayout())

        label = QLabel("Пример модального окна", self)
        self.layout().addWidget(label)

        button = QPushButton("Закрыть", self)
        button.clicked.connect(self.accept)
        self.layout().addWidget(button)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())