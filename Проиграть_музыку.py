'''Файл в mp3 можно воспроизвести через pyqt6 или через 2 закоментированные строчки ниже'''
# from playsound import playsound
# playsound('2.mp3')


import sys
from PyQt6.QtWidgets import QApplication, QPushButton, QMainWindow
from PyQt6.QtCore import QUrl
from PyQt6.QtMultimedia import QAudioOutput, QMediaPlayer

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Пример проигрывания MP3")
        self.setGeometry(100, 100, 200, 100)

        self.button = QPushButton("Воспроизвести", self)
        self.button_2 = QPushButton("Stop", self)
        self.flag = 0  # флаг воспроизведения: 0-не играет, 1- играет
        self.button.clicked.connect(self.play_audio)
        self.button_2.clicked.connect(self.play_stop)
        self.setCentralWidget(self.button)

    def play_audio(self):
        self.file_path = "1.mp3"  # "path/to/your/file.mp3"  # Путь к вашему MP3-файлу
        self.player = QMediaPlayer(self)
        self.audio_output = QAudioOutput(self)
        self.player.setAudioOutput(self.audio_output)
        self.player.setSource(QUrl.fromLocalFile(self.file_path))
        self.audio_output.setVolume(50)
        self.player.play()  # Воспроизведение аудио
        self.flag = 1

    # остановка воспроизведения
    def play_stop(self):
        if self.flag:
            self.player.stop()
            self.flag = 0

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
