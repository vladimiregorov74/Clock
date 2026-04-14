'''Чтобы передать значение из модального окна в основное окно, вы можете добавить сигналы и слоты в ваши классы окон
В этом примере добавлен сигнал value_selected в класс ModalDialog, который оповещает о выбранном значении. Затем в
основном окне MainWindow создается слот handle_value_selected, который будет вызван, когда сигнал будет испущен. В
слоте handle_value_selected вы можете обработать полученное значение, например, вывести его на консоль.
    В модальном окне, когда пользователь нажимает кнопку "Закрыть", выбранное значение передается через сигнал
value_selected с использованием метода emit. Затем модальное окно закрывается с помощью self.accept(). Таким образом,
вы можете передать выбранное значение из модального окна в основное окно и выполнять нужные действия с этим значением
в слоте handle_value_selected.

    Обрати вмимание, что тип данных для испускаемого сигнала необходимо задавать во втором модальном окне(в данном
случае это сделано сразу после задания класса второго окна)'''


import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
from Модальные_окна_2 import ModalDialog

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Пример модального окна")
        self.setGeometry(100, 100, 400, 300)

        self.button = QPushButton("Открыть модальное окно", self)
        self.button.clicked.connect(self.open_modal_dialog)
        self.setCentralWidget(self.button)

        self.dat1 = 123456

    def open_modal_dialog(self):

        dialog = ModalDialog()
        dialog.set_data(self.dat1)
        dialog.value_selected.connect(self.handle_value_selected)  # Подключение слота к сигналу
        dialog.exec()

    def handle_value_selected(self, value):
        print("Переданное значение из модального окна:", value)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
