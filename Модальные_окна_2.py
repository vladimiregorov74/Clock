from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton

class ModalDialog(QDialog):
    value_selected = pyqtSignal(tuple)  # Определение сигнала

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Модальное окно")
        self.setLayout(QVBoxLayout())

        label = QLabel("Пример модального окна", self)
        self.layout().addWidget(label)

        # self.label_1 = QLabel("Данные из основного окна:")
        self.data_label = QLabel()

        button = QPushButton("Закрыть", self)
        button.clicked.connect(self.handle_button_click)
        self.layout().addWidget(self.data_label)
        self.layout().addWidget(button)

    def handle_button_click(self):
        selected_value = (2,2)  # Ваше выбранное значение
        self.value_selected.emit(selected_value)  # Испускание сигнала с передачей значения
        self.accept()

    def set_data(self, data):
        self.data_label.setText(str(data))
        print(f'Переданное из основного окна:{data}')
