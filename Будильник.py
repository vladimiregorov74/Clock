import datetime
import time
import os
import pyglet

from playsound import playsound
playsound('System.mp3')


# Запрос веремени для установки будильника
hour = int(input('Введите часы (от 0 до 23): '))
minute = int(input('Введите минуты (от 0 до 59): '))

# Проверка корректности введенного времени
if hour < 0 or hour > 23 or minute < 0 or minute > 59:
	print('Время введено некорректно')
	exit()

# Ожидание до указанного времени

while True:
	now = datetime.datetime.now()
	if now.hour == hour and now.minute == minute:
		print('Будильник сработал')
		# Проигрываем звуковой файл
		# для macOS -'afplay alarm_sound.mp3'; для Windows:
		os.system('afplay alarm_sound.mp3')
		# song = pyglet.media.load('alarm_sound.mp3')
		# song.play()
		# pyglet.app.run()
		break
	time.sleep(60)

# import sys
# from PyQt6.QtCore import Qt, pyqtSignal
# from PyQt6.QtWidgets import QApplication, QMainWindow, QDialog, QLabel, QVBoxLayout, QPushButton, QLineEdit
#
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Пример передачи данных")
#         self.setGeometry(100, 100, 400, 300)
#
#         self.button = QPushButton("Открыть модальное окно", self)
#         self.button.clicked.connect(self.open_modal)
#         self.setCentralWidget(self.button)
#
#     def open_modal(self):
#         dialog = ModalDialog(self)
#         dialog.data_signal.connect(self.receive_data)
#         dialog.exec()
#
#     def receive_data(self, data):
#         print("Получены данные из модального окна:", data)
#
# class ModalDialog(QDialog):
#     data_signal = pyqtSignal(str)
#
#     def __init__(self, parent=None):
#         super().__init__(parent, Qt.WindowType.Dialog)
#         self.setWindowModality(Qt.WindowModality.WindowModal)
#         self.setWindowTitle("Модальное окно")
#
#         layout = QVBoxLayout()
#         label = QLabel("Введите данные:")
#         self.lineEdit = QLineEdit()
#         button = QPushButton("Отправить")
#         button.clicked.connect(self.send_data)
#
#         layout.addWidget(label)
#         layout.addWidget(self.lineEdit)
#         layout.addWidget(button)
#         self.setLayout(layout)
#
#     def send_data(self):
#         data = self.lineEdit.text()
#         self.data_signal.emit(data)
#         self.close()
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec())

# import sys
# from PyQt6.QtCore import Qt, pyqtSignal
# from PyQt6.QtWidgets import QApplication, QMainWindow, QDialog, QLabel, QVBoxLayout, QPushButton, QLineEdit
#
# class MainWindow(QMainWindow):
# 	def __init__(self):
# 		super().__init__()
# 		self.setWindowTitle("Пример передачи данных")
# 		self.setGeometry(100, 100, 400, 300)
# 		self.dat1 = 123456
# 		self.button = QPushButton("Открыть модальное окно", self)
# 		self.button.clicked.connect(self.open_modal)
# 		self.setCentralWidget(self.button)
#
#
# 	def open_modal(self):
#
# 		dialog = ModalDialog(self)
# 		dialog.set_data(self.dat1)
# 		dialog.exec()
#
# class ModalDialog(QDialog):
# 	def __init__(self, parent=None):
# 		super().__init__(parent, Qt.WindowType.Dialog)
# 		self.setWindowModality(Qt.WindowModality.WindowModal)
# 		self.setWindowTitle("Модальное окно")
#
# 		self.label = QLabel("Данные из основного окна:")
# 		self.data_label = QLabel()
#
# 		layout = QVBoxLayout()
# 		layout.addWidget(self.label)
# 		layout.addWidget(self.data_label)
# 		self.setLayout(layout)
#
# 	def set_data(self, data):
# 		self.data_label.setText(str(data))
# 		print(data)
#
# if __name__ == '__main__':
# 	app = QApplication(sys.argv)
# 	window = MainWindow()
# 	window.show()
# 	sys.exit(app.exec())
