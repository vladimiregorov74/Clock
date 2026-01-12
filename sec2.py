# окно выбора времени и музыки
import os

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import pyqtSignal, QUrl
from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput
from PyQt6.QtWidgets import QFileDialog, QDialog


class Ui_Form(QDialog):
    value_selected = pyqtSignal(tuple)  # Определение сигнала
    
    def __init__(self):
        super().__init__()
        
        self.resize(428, 166)
        self.setWindowTitle("")
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.timeEdit = QtWidgets.QTimeEdit(self)
        font = QtGui.QFont()
        font.setPointSize(29)
        self.timeEdit.setFont(font)
        self.timeEdit.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.timeEdit.setMinimumDate(QtCore.QDate(2000, 1, 5))
        self.timeEdit.setObjectName("timeEdit")
        self.verticalLayout.addWidget(self.timeEdit)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.input_play_Button = QtWidgets.QPushButton(self)
        self.input_play_Button.setObjectName("input_play_Button")
        self.horizontalLayout.addWidget(self.input_play_Button)
        self.stop_play_Button = QtWidgets.QPushButton(self)
        self.stop_play_Button.setObjectName("stop_play_Button")
        self.horizontalLayout.addWidget(self.stop_play_Button)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.ok_Button = QtWidgets.QPushButton(self)
        self.ok_Button.setObjectName("ok_Button")
        self.verticalLayout.addWidget(self.ok_Button)
        
        self.media_player = QMediaPlayer(self)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)
        
        
        
        # предустановленная мелодия
        self.music = '1.mp3'
        # если предустановленной мелодии не существует не позволяем ее оставить без выбора
        if not os.path.exists(self.music):
            self.ok_Button.setEnabled(False)
        # вызовы на кнопки
        self.input_play_Button.clicked.connect(self.open_modal)  # выбор музыки
        self.stop_play_Button.clicked.connect(self.music_stop)  # останов музыки
        self.stop_play_Button.setEnabled(False)  # пока не произошел выбор и не начала играть музыка, то не можем ее остановить
        self.ok_Button.clicked.connect(self.handle_button_click)  # выход в основное окно
       

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Настройки"))
        self.label.setText(_translate("Form", "Задайте время таймера"))
        self.timeEdit.setDisplayFormat(_translate("Form", "HH:mm:ss"))
        self.input_play_Button.setText(_translate("Form", "Задать музыку и восроизвести"))
        self.stop_play_Button.setText(_translate("Form", "Остановить музыку"))
        self.ok_Button.setText(_translate("Form", "Подтвердить"))
        
    # Вызов модального окна проигрования музыки с передачей имени проигруемого файла
    def open_modal(self):
        self.music= QFileDialog.getOpenFileName(self, 'Open File', './', 'JPG File (*.mp3);;MP3 File (*.mp3)')[0]
        print(self.music)
        file_path = self.music  # "path/to/your/file.mp3"  # Путь к вашему MP3-файлу
        self.player = QMediaPlayer(self)
        self.audio_output = QAudioOutput(self)
        self.player.setAudioOutput(self.audio_output)
        self.player.setSource(QUrl.fromLocalFile(file_path))
        self.audio_output.setVolume(50)
        self.player.play()  # Воспроизведение аудио
        self.player.mediaStatusChanged.connect(self.handle_media_status)
        # делаеам активные и неактивные кнопки
        self.stop_play_Button.setEnabled(True)
        self.ok_Button.setEnabled(False)
       
    # подтверждаем значения и выходим
    def handle_button_click(self):
        selected_value = (self.timeEdit.time().hour(), self.timeEdit.time().minute(), self.timeEdit.time().second(),
                          self.music)  # Ваше выбранное значение
        self.value_selected.emit(selected_value)  # Испускание сигнала с передачей значения
        self.accept()  # Закрываем окно
    
    # останавливаем воспроизведение музыки
    def music_stop(self):
        self.player.stop()
        self.ok_Button.setEnabled(True)
        
    # Проверяем статус воспроизведения музыки(если музыка закончилась - разблокируем кнопки)
    def handle_media_status(self, status):
        if status == QMediaPlayer.MediaStatus.EndOfMedia:
            self.ok_Button.setEnabled(True)
        
if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Ui_Form()
    window.show()
    sys.exit(app.exec())
