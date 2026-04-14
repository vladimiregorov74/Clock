import sys
from PyQt6 import QtWidgets, QtCore


class ClickableLabel(QtWidgets.QLabel):
    clicked = QtCore.pyqtSignal(int)  # будем передавать индекс дня

    def __init__(self, index, text, parent=None):
        super().__init__(text, parent)
        self.index = index

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.MouseButton.LeftButton:
            self.clicked.emit(self.index)


class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Days Click Example")

        # состояние дней недели (по умолчанию False)
        self.week = [False] * 7

        main_layout = QtWidgets.QVBoxLayout(self)

        # контейнер информации
        info_layout = QtWidgets.QVBoxLayout()

        self.label_name = QtWidgets.QLabel("Будильник")
        self.btn_time = QtWidgets.QPushButton("07:00")

        # layout дней
        self.days_layout = QtWidgets.QHBoxLayout()
        self.day_labels = []

        days_texts = ["Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс"]

        for i, text in enumerate(days_texts):
            lbl = ClickableLabel(i, text)

            lbl.setFixedSize(24, 24)
            lbl.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

            # подключаем сигнал
            lbl.clicked.connect(self.toggle_day)

            self.day_labels.append(lbl)
            self.days_layout.addWidget(lbl)

        self.days_layout.addStretch()

        # применяем начальные стили
        self.update_styles()

        info_layout.addWidget(self.label_name)
        info_layout.addWidget(self.btn_time)
        info_layout.addLayout(self.days_layout)

        main_layout.addLayout(info_layout)

    def toggle_day(self, index):
        # переключаем состояние
        self.week[index] = not self.week[index]

        # обновляем внешний вид
        self.update_styles()

        # вызываем твою функцию
        self.change_alarm()

    def update_styles(self):
        for i, lbl in enumerate(self.day_labels):
            style = "border-radius: 12px; font-size: 16px; "

            if self.week[i]:
                style += "background-color: #57e389; color: #000;"
            else:
                style += "background-color: #333; color: #666;"

            lbl.setStyleSheet(style)

    def change_alarm(self):
        print("Alarm changed:", self.week)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.resize(300, 150)
    window.show()
    sys.exit(app.exec())