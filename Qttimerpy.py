'''Программа представляет собой обратный таймер с возможностью подкорректировать длину одной секунды(смену между двумя
 показаниями таймера) '''
import sys

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QWidget
import time


class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__()


        self.setWindowTitle('Timer')
        self.resize(250, 150)
        self.label = QtWidgets.QLabel('')

        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label.setFont(font)
        self.label.setStyleSheet("font: 75 36pt \"MS Shell Dlg 2\";background-color: rgb(85, 170, 255);")
        self.label.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setIndent(0)
        self.label.setObjectName("label")

        #self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.button1 = QtWidgets.QPushButton('ЗАПУСТИТЬ')
        #  self.button2 = QtWidgets.QPushButton('ОСТАНОВИТЬ')
        self.button2 = QtWidgets.QPushButton('Restart')
        self.button2.setEnabled(False)
        vbox = QtWidgets.QVBoxLayout()
        vbox.addWidget(self.label)
        vbox.addWidget(self.button1)
        vbox.addWidget(self.button2)
        self.setLayout(vbox)
        # функция запуска таймера кнопкой Запустить\Остановить
        self.button1.clicked.connect(self.on_clicked_button1)
        self.flag_start = 1  # флаг работы таймера: 1-работает, 0-остановлен
        # функция рестарта таймера кнопкой Restart
        self.button2.clicked.connect(self.on_clicked_button2)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.on_timeout)
        # устанавливаем длительность таймера
        self.c = 5
        # записываем значение таймера в окно
        self.label.setText(str(self.c))
    def on_clicked_button1(self):
        self.timer.start(1260)  # 1c -1000 (в этой строчке я сделал чтобы между сменой показаний проходило 1.26 сек)
        if self.flag_start == 1:
            self.flag_start = 0
            self.button1.setText('ОСТАНОВИТЬ')
            self.button2.setEnabled(False)

        else:
            self.flag_start = 1
            self.button1.setText('ЗАПУСТИТЬ')
            self.button2.setEnabled(True)
            self.timer.stop()

    # реализация функции рестарт
    def on_clicked_button2(self):
        self.c = 5
        self.label.setText(str(self.c))
        self.button1.setEnabled(True)
        self.button2.setEnabled(False)

    # реализация хода таймера
    def on_timeout(self):
        #self.label.setText(time.strftime('%H:%M:%S'))
        self.c = self.c-1
        self.label.setText(str(self.c))
        if self.c == 0:
            self.label.setText('Time Over')
            self.c = 5  # для перезапуска таймера
            self.timer.stop()










if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()

    window.show()
    sys.exit(app.exec())