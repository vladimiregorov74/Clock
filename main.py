#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import QUrl
from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput
# from sec import Ui_Dialog  # импорт основного окна
from s_t_21 import Ui_Dialog  # импорт основного окна
from sec2 import Ui_Form
import os



class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        # Получаем текущие флаги окна и убираем из них кнопку развертывания
        self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowType.WindowMaximizeButtonHint)
        
        # устанавливаем первоначальное значение таймера
        try:
            with open('timer_data.json', 'r') as f:
                js = json.load(f)
                self.timer_set = js.get('save_timer')
                self.fist_timer_set = self.timer_set
                # устанавливаем первоначальные значения времени и файла музыки
                self.calc_time()
                self.path_music = js.get('path_music')
                if not os.path.exists(self.path_music):
                    raise Exception("не найден файл")
        except:
            self.timer_set = 0
            # устанавливаем первоначальные значения времени и файла музыки
            self.h, self.m, self.s = 0, 0, 0
            self.path_music = '1.mp3'
        
        # нажатие на кнопку секундомер
        self.ui.pushButton_Sec.clicked.connect(self.window_sec)
        # нажатие на кнопку таймер
        self.ui.pushButton_Timer.clicked.connect(self.window_timer)
        # до установки времени таймер заблокирован
        if self.timer_set == 0:
            self.ui.pushButton_Timer_start_stop.setEnabled(False)
        # Установка таймера
        self.ui.pushButton_Timer_setTimer.clicked.connect(self.open_modal_dialog)
        # Запуск\остановка таймера
        self.flag_start = 0  # флаг работы таймера: 1-работает, 0-остановлен
        self.ui.pushButton_Timer_start_stop.clicked.connect(self.start_stop_timer)
        # Сброс таймера
        self.ui.pushButton_Timer_reset.clicked.connect(self.reset_timer)
        # Останов музыки
        self.ui.pushButton_Timer_music.clicked.connect(self.music_stop)
        
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.on_timeout)
        
        # инициализация значений для секундомера
        self.sec_go = 0  # флаг работы\приостановки секундомера
        self.sec, self.sec_0 = 0, 0  # начальное значение секундомера
        self.flag_start_sec = 1
        # создаем список для круга
        self.rounds = []
        # добавляем в круг первое значение 0
        self.rounds.append(0)
        # список строчек в виджете куда выводится значения времени, времени круга и номер круга
        self.label_Secs = []
        
        # Запуск\остановка секундомера
        self.ui.pushButton_Sec_start_stop.clicked.connect(self.start_sec)
        # Сброс секундомера
        self.ui.pushButton_Sec_reset.clicked.connect(self.reset_sec)
        # Запись круга
        self.ui.pushButton_Sec_round.clicked.connect(self.round)
        self.timer_sec = QtCore.QTimer()
        self.timer_sec.timeout.connect(self.on_timer_sec)
        
        self.player = QMediaPlayer(self)
        self.audio_output = QAudioOutput(self)
        
        # проверка статуса медиаплеера
        self.player.mediaStatusChanged.connect(self.handle_media_status)
    
    # переход в окно секундомера
    def window_sec(self):
        
        print(11111111111111111111111111111)
        for i in self.ui.list_timer_widget:
            i.hide()
            self.ui.pushButton_Timer.setStyleSheet("background-color: #f66151;")
            for i in self.ui.list_sec_widget:
                i.show()
            self.ui.pushButton_Sec.setStyleSheet("background-color: #57e389;")
            for i in self.label_Secs:
                i.show()
        #
        self.ui.spacerItem4.changeSize(0, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        self.ui.verticalLayout.invalidate()
        
        # self.adjustSize()
    
    # переход в окно таймера
    def window_timer(self):
        
        for i in self.ui.list_sec_widget:
            i.hide()
        self.ui.pushButton_Sec.setStyleSheet("background-color: #f66151;")
        for i in self.ui.list_timer_widget:
            i.show()
        self.ui.pushButton_Timer.setStyleSheet("background-color: #57e389;")
        # скрыть кнопку останов музыки
        self.ui.pushButton_Timer_music.hide()
        for i in self.label_Secs:
            i.hide()
        # изменяем поведение распорки делаем чтобы она занимала макс значение по вертикали - Expanding
        self.ui.spacerItem4.changeSize(0, 20, QtWidgets.QSizePolicy.Policy.Minimum,
                                       QtWidgets.QSizePolicy.Policy.Expanding)
        self.ui.verticalLayout.invalidate()
    
    # реализация таймера, с изменением надписей кнопок и их заморозки
    def start_stop_timer(self):
        if not self.timer.isActive():
            self.timer.start(1000)
            self.ui.pushButton_Timer_start_stop.setText('Остановить')
            self.ui.pushButton_Timer_reset.setEnabled(False)
            self.ui.pushButton_Timer_setTimer.setEnabled(False)
        else:
            self.timer.stop()
            self.ui.pushButton_Timer_start_stop.setText('Старт')
            self.ui.pushButton_Timer_reset.setEnabled(True)
            self.ui.pushButton_Timer_setTimer.setEnabled(True)
    #
    def calc_time(self):
        # вычисляем часы, минути, секунды
        self.h = self.timer_set // 3600
        self.m = (self.timer_set - 3600 * self.h) // 60
        self.s = self.timer_set - 3600 * self.h - 60 * self.m
        #  записываем значения в окно таймера
        self.ui.label_h.setText(str(self.h))
        self.ui.label_min.setText(str(self.m))
        self.ui.label_sec.setText(str(self.s))
    
    
    # реализация отображения значений таймера и проверки условия останова
    def on_timeout(self):
        
        # проверяем условие останова таймер
        if self.timer_set == 0:
            self.timer.stop()
            self.ui.pushButton_Timer.click()  # нажатием на кнопку переходим в окно таймера
            self.ui.pushButton_Timer_start_stop.setText('Старт')
            self.ui.pushButton_Timer_reset.setEnabled(True)
            self.ui.pushButton_Timer_setTimer.setEnabled(True)
            self.ui.pushButton_Timer_setTimer.hide()  # скрываем кнопку настроек, для вывода кнопки останова сигнала
            self.ui.pushButton_Timer_music.show()
            self.ui.pushButton_Timer_start_stop.setEnabled(False)
            # воспроизводим сигнал (при достижении таймером 0)
            file_path: str = self.path_music
            self.player.setAudioOutput(self.audio_output)
            self.player.setSource(QUrl.fromLocalFile(file_path))
            self.audio_output.setVolume(50)
            self.player.play()  # Воспроизведение аудио
        
        else:
            self.timer_set = self.timer_set - 1  # уменьшаем таймер на 1
            self.calc_time()
            
    
    # реализация сброса таймера
    def reset_timer(self):
        self.timer_set = 0
        # устанавливаем часы, минути, секунды
        self.h = 0
        self.m = 0
        self.s = 0
        #  записываем значения в окно таймера
        self.ui.label_h.setText(str(self.h))
        self.ui.label_min.setText(str(self.m))
        self.ui.label_sec.setText(str(self.s))
    
    # открываем модальное окно настроек таймера
    def open_modal_dialog(self):
        self.setEnabled(False)
        dialog = Ui_Form()
        dialog.value_selected.connect(self.handle_value_selected)  # Подключение слота к сигналу
        dialog.exec()
        self.setEnabled(True)
    
    # получение данных из модального окна
    def handle_value_selected(self, value):
        
        self.h, self.m, self.s, self.path_music = value
        self.ui.label_h.setText(str(self.h))
        self.ui.label_min.setText(str(self.m))
        self.ui.label_sec.setText(str(self.s))
        self.timer_set = 3600 * self.h + 60 * self.m + self.s
        self.fist_timer_set = self.timer_set
        self.ui.pushButton_Timer_start_stop.setEnabled(True)
        # Запись JSON в файл
        data = {"save_timer" : self.timer_set, "path_music": self.path_music}
        try:
            with open("timer_data.json", "w") as file:
                json.dump(data, file)
        except Exception as e:
            print(e)
    
    # Останов музыки
    def music_stop(self):
        self.player.stop()
        self.ui.pushButton_Timer_setTimer.show()  # скрываем кнопку настроек, для вывода кнопки останова сигнала
        self.ui.pushButton_Timer_music.hide()
        if self.fist_timer_set > 0:
            self.timer_set = self.fist_timer_set
            self.calc_time()
            # Делаем кнопку активной
            self.ui.pushButton_Timer_start_stop.setEnabled(True)
    
    # реализация секундомера, с изменением надписей кнопок и их заморозки
    def start_sec(self):
        self.timer_sec.start(100)  # 1c -1000 (в этой строчке я сделал чтобы между сменой показаний проходило 1.0 сек)
        if self.flag_start_sec == 1:
            self.flag_start_sec = 0
            self.sec_go = 1
            self.ui.pushButton_Sec_start_stop.setText('Остановить')
            self.ui.pushButton_Sec_reset.setEnabled(False)
        
        else:
            self.flag_start_sec = 1
            self.ui.pushButton_Sec_start_stop.setText('Старт')
            self.ui.pushButton_Sec_reset.setEnabled(True)
            self.timer_sec.stop()
    
    # реализация отображения значений секундомера
    def on_timer_sec(self):
        self.sec_0 = self.sec_0 + 1  # увеличиваем секундомер на 0,1
        if self.sec_0 == 10:
            self.sec_0 = 0
            self.sec += 1  # увеличиваем секунды на 1
        # вычисляем часы, минуты, секунды
        self.sec_h = self.sec // 3600
        self.sec_m = (self.sec - 3600 * self.sec_h) // 60
        self.sec_s = self.sec - 3600 * self.sec_h - 60 * self.sec_m
        #  записываем значения в окно секундомера
        self.ui.label_Sec_h_2.setText(str(self.sec_h))
        self.ui.label_Sec_min_2.setText(str(self.sec_m))
        str_sec = f'{self.sec_s}.{self.sec_0}'
        self.ui.label_Sec_sec_2.setText(str_sec)
    
    # сброс значений секундомера к 0
    def reset_sec(self):
        self.sec = 0
        self.sec_0 = 0
        self.sec_go = 0
        # устанавливаем часы, минуты, секунды
        self.sec_h = 0
        self.sec_m = 0
        self.sec_s = 0
        #  записываем значения в окно таймера
        self.ui.label_Sec_h_2.setText(str(self.sec_h))
        self.ui.label_Sec_min_2.setText(str(self.sec_m))
        self.ui.label_Sec_sec_2.setText(str(self.sec_s))
        # for i in range(len(self.rounds) - 1):
        for i in range(len(self.label_Secs) - 1):
            try:
                self.label_Secs[i].hide()
            except Exception as e:
                print(i, len(self.label_Secs))
       
        # self.resize(516, 200)
        # self.adjustSize()
        self.label_Secs = []
        self.rounds = []
        self.rounds.append(0)
        for i in reversed(range(self.ui.roundsLayout.count())):
            self.ui.roundsLayout.itemAt(i).widget().setParent(None)
        self.label_Secs = []
        self.rounds = [0]
    
    def round(self):
        if self.sec_go:
            a = self.sec + self.sec_0 / 10
            self.rounds.append(a)
            r = self.rounds[-1] - self.rounds[-2]
            
            if r != 0:
                h_r = int(r // 3600)
                m_r = int((r - 3600 * h_r) // 60)
                s_r = round(r - 3600 * h_r - 60 * m_r, 1)
                
                i = len(self.rounds) - 1
                
                # Создаем строку круга
                aa = self.sec_s + self.sec_0 / 10
                text = f"{self.sec_h:02}:{self.sec_m:02}:{aa:04.1f}  |  {h_r:02}:{m_r:02}:{s_r:04.1f}  |  №{i}"
                
                new_label = QtWidgets.QLabel(text)
                new_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                new_label.setStyleSheet("border-bottom: 1px solid #ddd; padding: 5px;")  # Добавим разделитель
                
                # Добавляем в слой ВНУТРИ ScrollArea
                # insertWidget(0, ...) добавит новый круг В НАЧАЛО списка (сверху)
                self.ui.roundsLayout.insertWidget(0, new_label)
                self.label_Secs.append(new_label)
    
    def handle_media_status(self, status):
        # Проверяем, что медиафайл проигран до конца
        if status == QMediaPlayer.MediaStatus.EndOfMedia:
            self.music_stop()

if __name__ == '__main__':
    import sys
    
    os.environ['QT_MULTIMEDIA_PREFERRED_PLUGINS'] = 'windowsmediafoundation'
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())