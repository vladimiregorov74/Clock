#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Для отображения иконки делаем cp ~/Рабочий\ стол/Alarm.desktop ~/.local/share/applications/"""
import uuid

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import QUrl, Qt
from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput

from data_in_to_json import data_from_json, data_to_json
from a_t_s import Ui_Dialog  # импорт основного окна
from newsettimer import Ui_Form  # импорт окна задания таймера
from addAlarm import U_Dialog  # импорт окна задания будильника
import os

# Получаем путь к папке скрипта для работы с файлами
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Склеиваем путь к папке с именем файла иконки
ICON_PATH = os.path.join(BASE_DIR, 'icon.png')


def load_stylesheet(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


# класс окна оповещения сработавшего будильника
class AlarmTriggeredDialog(QtWidgets.QDialog):
    stop_alarm = QtCore.pyqtSignal()

    def __init__(self, alarm_name, alarm_time, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Будильник")
        self.setModal(True)
        self.setFixedSize(300, 150)

        layout = QtWidgets.QVBoxLayout(self)

        label_title = QtWidgets.QLabel("⏰ Сработал будильник")
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        label_title.setFont(font)
        label_title.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        label_info = QtWidgets.QLabel(f"{alarm_name}\n{alarm_time}")
        label_info.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        self.stop_button = QtWidgets.QPushButton("Остановить")
        self.stop_button.setFixedHeight(40)
        self.stop_button.clicked.connect(self.on_stop_clicked)

        layout.addWidget(label_title)
        layout.addWidget(label_info)
        layout.addStretch()
        layout.addWidget(self.stop_button)

    def on_stop_clicked(self):
        self.stop_alarm.emit()
        self.accept()


# Класс окна оповещения для таймера
class TimerTriggeredDialog(AlarmTriggeredDialog):
    def __init__(self, timer_name, info_text, parent=None):
        super().__init__(timer_name, info_text, parent)
        self.setWindowTitle("Таймер")
        
        # Находим label с иконкой и меняем текст
        # В родительском классе это первый виджет в layout
        for i in range(self.layout().count()):
            widget = self.layout().itemAt(i).widget()
            if isinstance(widget, QtWidgets.QLabel) and "⏰" in widget.text():
                widget.setText("⏳ Время вышло!")
                break
                
                
#   класс делающий лейбелы будильника кликабельными
class ClickableLabel(QtWidgets.QLabel):
    clicked = QtCore.pyqtSignal(int)  # будем передавать индекс дня

    def __init__(self, index, text, parent=None):
        super().__init__(text, parent)
        self.index = index

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.MouseButton.LeftButton:
            self.clicked.emit(self.index)
            

# класс виджета будильника
class AlarmWidget(QtWidgets.QFrame):
    alarm_updated = QtCore.pyqtSignal()
    # сигнал для уведомления об удалении
    alarm_deleted = QtCore.pyqtSignal(str)

    def __init__(self, value, parent=None):
        super().__init__(parent)
        #  Задаем имя для QSS
        # Для самой карточки
        self.setObjectName("AlarmCard")
        
        self.id = value["id"]
        self.name_alarm = value['name_al']
        self.time_al = value['time_al']
        self.week = value['week_al']
        self.music = value['music']
        self.enabled = value['enabled']
        
        self.last_trigger_date = None
        self.trigger_token = 0
        
        # Указываем, что по вертикали виджет должен занимать
        # фиксированное или минимально необходимое место
        self.setSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred,
                           QtWidgets.QSizePolicy.Policy.Fixed)
        
        # 1. ТОЛЬКО ОДИН основной слой (назначаем на self)
        self.main_layout = QtWidgets.QHBoxLayout(self)
        self.main_layout.setContentsMargins(10, 5, 10, 5)
        
        # 2. Вложенные слои создаем БЕЗ self
        self.verticalLayout_Alarm = QtWidgets.QVBoxLayout()
        self.label_name_2 = ClickableLabel(100, value['name_al']) # 100 - заглушка
        # self.label_name_2 = QtWidgets.QLabel(value['name_al'])
        self.label_name_2.setMinimumSize(QtCore.QSize(355, 0))
        self.label_name_2.setMaximumSize(QtCore.QSize(355, 16777215))
        self.label_name_2.setStyleSheet("""QLabel {
    color: #1a5fb4;
    border: 1px solid #333;
    border-radius: 8px;
    padding: 8px 16px;
    font-size: 16px;
}""")
        self.label_name_2.clicked.connect(self.change_alarm)
        # Для названия (надпись сверху)
        self.label_name_2.setObjectName("AlarmName")
        self.verticalLayout_Alarm.addWidget(self.label_name_2)
        
        self.pushButton_ch_Alarm = QtWidgets.QPushButton(value['time_al'])
        font = QtGui.QFont()
        font.setPointSize(25)
        self.pushButton_ch_Alarm.setFont(font)
        self.verticalLayout_Alarm.addWidget(self.pushButton_ch_Alarm)
        self.pushButton_ch_Alarm.clicked.connect(self.change_alarm)
        # Для кнопки со временем
        self.pushButton_ch_Alarm.setObjectName("AlarmTime")
        
        # Дни недели (компактные кружочки)
        self.horizontalLayout_Alarm2 = QtWidgets.QHBoxLayout()
        self.day_labels_list = []
        days_texts = ["Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс"]
        # Для дней недели (они в цикле)
        
        for i, text in enumerate(days_texts):
            lbl = ClickableLabel(i, text)
            # lbl = QtWidgets.QLabel(text)
            lbl.setFixedSize(24, 24)
            lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
            style = "border-radius: 12px; font-size: 16px; "
            style += "background-color: gold; color: #000;" if self.week[
                i] else "background-color: #333; color: white;"
            lbl.setStyleSheet(style)
            # подключаем сигнал
            lbl.clicked.connect(self.change_alarm)
            self.horizontalLayout_Alarm2.addWidget(lbl)
            self.day_labels_list.append(lbl)
            
        # Пружина (раздвигает дни и кнопку удаления)
        self.horizontalLayout_Alarm2.addStretch()
        
        # Кнопка удалить будильник
        self.pushButton_AlarmDel = QtWidgets.QPushButton("✕")
        self.pushButton_AlarmDel.setFixedSize(30, 30)
        # Для кнопки удаления задаем имя используемое в стилях
        self.pushButton_AlarmDel.setObjectName("AlarmDel")
        self.horizontalLayout_Alarm2.addWidget(self.pushButton_AlarmDel)
        # Сразу подключаем удаление
        self.pushButton_AlarmDel.clicked.connect(self.del_later)
        
        # Собираем все воедино
        self.verticalLayout_Alarm.addLayout(self.horizontalLayout_Alarm2)
        self.main_layout.addLayout(self.verticalLayout_Alarm)
        
        # Отступ перед чекбоксом
        self.main_layout.addSpacing(20)
        
        self.checkBox_2 = QtWidgets.QCheckBox()
        # Для стилей задаем имя чекбокса
        self.checkBox_2.setObjectName("AlarmCheck")
        self.checkBox_2.setChecked(value['enabled'])
       
        
        self.checkBox_2.stateChanged.connect(self.on_enabled_changed)
        if value['enabled']:
            self.checkBox_2.setChecked(True)
            self.checkBox_2.setStyleSheet("background-color: gold; color: red;")
        self.main_layout.addWidget(self.checkBox_2)
    
    # ставим галочку - будильник активирован
    def on_enabled_changed(self, state):
        self.enabled = self.checkBox_2.isChecked()
        self.trigger_token += 1  # Важно сбросывать токен, чтобы можно было включить снова
        self.alarm_updated.emit()
    
    # удаление виджета будильника
    def del_later(self):
        # 1. Сначала скрываем виджет, чтобы он не мешался
        self.hide()
        # Сначала уведомляем главное окно, чтобы оно очистило кэш срабатываний
        self.alarm_deleted.emit(self.id)
        # 2. Удаляем его из компоновщика (Layout) ПРЯМО СЕЙЧАС
        # Это важно: save_all_alarms не увидит его в списке виджетов слоя
        self.setParent(None)
        # 3. Вызываем сигнал обновления (теперь save_all_alarms запишет данные без него)
        self.alarm_updated.emit()
        # 4. Окончательно удаляем объект из памяти
        self.deleteLater()
        
        
    def change_alarm(self):
        self.setEnabled(False)
        dialog = U_Dialog(self.name_alarm, self.week, self.time_al)
        dialog.value_selected.connect(self.handle_value_selected)  # Подключение слота к сигналу
        dialog.exec()
        self.setEnabled(True)
        
    # получение данных из модального окна
    def handle_value_selected(self, value):
        # 1. Распаковываем новые данные
        self.name_alarm, h, m, week, self.music = value
        self.time_al = str(h).rjust(2, "0") + ":" + str(m).rjust(2, "0")
        self.week = week
        self.trigger_token += 1
        
        # 2. Обновляем текстовые значения
        self.label_name_2.setText(self.name_alarm)
        self.pushButton_ch_Alarm.setText(self.time_al)
        
        # 3. Обновляем подсветку дней недели через сохраненный список
        for i, lbl in enumerate(self.day_labels_list):
            if i < len(self.week):
                
                lbl.setFixedSize(24, 24)
                lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
                style = "border-radius: 12px; font-size: 16px; "
                style += "background-color: gold; color: #000;" if self.week[
                    i] else "background-color: #333; color: white;"
                lbl.setStyleSheet(style)
               
        # 4. Сигнализируем окну Window, что пора сохранить изменения в файл
        self.alarm_updated.emit()
       
        
        
        
class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("ClockWindow")
        # Это помогает некоторым менеджерам окон подцепить иконку
        self.setWindowIcon(QtGui.QIcon(ICON_PATH))
        # Загружаем и применяем стиль
        style_path = os.path.join(BASE_DIR, "style.qss")
        if os.path.exists(style_path):
            self.setStyleSheet(load_stylesheet(style_path))
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowType.WindowMaximizeButtonHint)
        
        # Используем BASE_DIR для путей
        self.path_alarm = os.path.join(BASE_DIR, "alarm_data.json")
        self.path_timer = os.path.join(BASE_DIR, "timer_data.json")
        self.default_music = os.path.join(BASE_DIR, "1.mp3")
        
        self.triggered_today = {}
        self.player = QMediaPlayer(self)
        self.audio_output = QAudioOutput(self)
        self.player.setAudioOutput(self.audio_output)
        
        # Загрузка
        try:
            alarms = data_from_json(self.path_alarm)
            for alarm_val in alarms:
                # ВАЖНО: Передаем только именованный аргумент
                self.add_alarm(value=alarm_val)
        except Exception:
            print("Файл будильников не найден или пуст")
        
        # Таймер чтение значений сохраненных
        self.timer_set = 0
        try:
            js = data_from_json(self.path_timer)
            self.timer_set = js.get('save_timer', 0)
            self.path_music = js.get('path_music', self.default_music)
        except:
            self.path_music = self.default_music
        
        # нажатие на кнопку секундомер
        self.ui.pushButton_Sec.clicked.connect(self.window_sec)
        # нажатие на кнопку таймер
        self.ui.pushButton_Timer.clicked.connect(self.window_timer)
        # нажатие на кнопку будильника
        self.ui.pushButton_Alarm.clicked.connect(self.window_alarm)
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
        
        # добавление будильника
        self.ui.pushButton_Alarm_add.clicked.connect(self.add_alarm)
        
        self.spacer = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum,
                                            QtWidgets.QSizePolicy.Policy.Expanding)
        self.ui.verticalLayout_4A.addItem(self.spacer)
       
        self.triggered_today: dict[int, tuple[str, int]] = {} # дата, токен
        
        self.player.setAudioOutput(self.audio_output)
        
        self.alarm_timer = QtCore.QTimer(self)
        self.alarm_timer.timeout.connect(self.check_alarms)
        self.alarm_timer.start(1000)
    
    # переход в окно секундомера
    def window_sec(self):
        
        print("секундомер")
        for i in self.ui.list_timer_widget:
            i.hide()
        self.ui.pushButton_Timer.setStyleSheet("background-color: #d4e040;")
        for i in self.ui.list_alarm_widget:
            i.hide()
        self.ui.pushButton_Alarm.setStyleSheet("background-color: #d4e040;")
        
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
        print("Таймер")
        for i in self.ui.list_sec_widget:
            i.hide()
        self.ui.pushButton_Sec.setStyleSheet("background-color: #d4e040;")
        for i in self.ui.list_alarm_widget:
            i.hide()
        self.ui.pushButton_Alarm.setStyleSheet("background-color: #d4e040;")
        for i in self.ui.list_timer_widget:
            i.show()
        self.ui.pushButton_Timer.setStyleSheet("background-color: #57e389;")
        # # скрыть кнопку останов музыки
        self.ui.pushButton_Timer_music.hide()
        for i in self.label_Secs:
            i.hide()
        # изменяем поведение распорки делаем чтобы она занимала макс значение по вертикали - Expanding
        self.ui.spacerItem4.changeSize(0, 20, QtWidgets.QSizePolicy.Policy.Minimum,
                                       QtWidgets.QSizePolicy.Policy.Expanding)
        self.ui.verticalLayout.invalidate()
    
    # переход в окно будильника
    def window_alarm(self):
        print("Будильник")
        for i in self.ui.list_sec_widget:
            i.hide()
        self.ui.pushButton_Sec.setStyleSheet("background-color: #d4e040;")
        for i in self.ui.list_timer_widget:
            i.hide()
        self.ui.pushButton_Timer.setStyleSheet("background-color: #d4e040;")
        for i in self.ui.list_alarm_widget:
            i.show()
        self.ui.pushButton_Alarm.setStyleSheet("background-color: #57e389;")
        # изменяем поведение распорки делаем чтобы она занимала макс значение по вертикали - Expanding
        self.ui.spacerItem4.changeSize(0, 20, QtWidgets.QSizePolicy.Policy.Minimum,
                                       QtWidgets.QSizePolicy.Policy.Expanding)
        self.ui.verticalLayout.invalidate()
        
        
    def start_stop_timer(self):
        if not self.timer.isActive():
            self.timer.start(1000)
            self.ui.pushButton_Timer_start_stop.setText('Остановить')
            self.ui.pushButton_Timer_reset.setEnabled(False)
            self.ui.pushButton_Timer_setTimer.setEnabled(False)  # Блокируем настройки
        else:
            self.timer.stop()
            self.ui.pushButton_Timer_start_stop.setText('Старт')
            self.ui.pushButton_Timer_reset.setEnabled(True)
            self.ui.pushButton_Timer_setTimer.setEnabled(True)  # Разблокируем настройки
    
    def on_timeout(self):
        # проверяем условие останова таймера
        if self.timer_set == 0:
            self.timer.stop()
            
            # Разблокируем элементы управления
            self.ui.pushButton_Timer_start_stop.setText('Старт')
            self.ui.pushButton_Timer_reset.setEnabled(True)
            self.ui.pushButton_Timer_setTimer.setEnabled(True)  # Кнопка снова доступна
            self.ui.pushButton_Timer_start_stop.setEnabled(False)
            
            # Воспроизводим сигнал
            file_path: str = self.path_music
            self.player.setSource(QUrl.fromLocalFile(file_path))
            self.audio_output.setVolume(50)
            self.player.play()
            
            # Показываем новое окно таймера
            dialog = TimerTriggeredDialog(
                timer_name="Таймер",
                info_text="Заданный интервал времени истек",
                parent=self
            )
            dialog.stop_alarm.connect(self.music_stop)
            dialog.exec()
        
        else:
            self.timer_set = self.timer_set - 1
            self.calc_time()
    
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
        if self.timer_set == 0:
            self.timer.stop()
            
            # Сбрасываем состояние кнопок управления
            self.ui.pushButton_Timer_start_stop.setText('Старт')
            self.ui.pushButton_Timer_reset.setEnabled(True)
            self.ui.pushButton_Timer_setTimer.setEnabled(True)
            self.ui.pushButton_Timer_start_stop.setEnabled(False)
            
            # Воспроизводим музыку
            file_path = self.path_music
            self.player.setSource(QUrl.fromLocalFile(file_path))
            self.audio_output.setVolume(50)
            self.player.play()
            
            # Вызываем окно оповещения (используем тот же класс, что и для будильника)
            # Если хотите другой заголовок, можно создать отдельный класс или добавить аргумент
            dialog = AlarmTriggeredDialog(
                alarm_name="Время вышло!",
                alarm_time="Таймер завершен",
                parent=self
            )
            dialog.setWindowTitle("Таймер")
            # При нажатии "Остановить" в окне — музыка выключается
            dialog.stop_alarm.connect(self.music_stop)
            dialog.exec()
        
        else:
            self.timer_set -= 1
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
    
    # получение данных из модального окна установок таймера
    def handle_value_selected(self, value):
        
        self.h, self.m, self.s, self.path_music = int(value[0]), int(value[1]), int(value[2]), value[3]
        self.ui.label_h.setText(str(self.h))
        self.ui.label_min.setText(str(self.m))
        self.ui.label_sec.setText(str(self.s))
        self.timer_set = 3600 * self.h + 60 * self.m + self.s
        self.fist_timer_set = self.timer_set
        self.ui.pushButton_Timer_start_stop.setEnabled(True)
        # Запись JSON в файл
        data = {"save_timer" : self.timer_set, "path_music": self.path_music}
        try:
            data_to_json(data,self.path_timer)
        except Exception as e:
            print(e)
    
    # Останов музыки
    def music_stop(self):
        self.player.stop()
        # Возвращаем начальное время, если нужно
        if hasattr(self, 'fist_timer_set') and self.fist_timer_set > 0:
            self.timer_set = self.fist_timer_set
            self.calc_time()
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
                # text = f"{self.sec_h:02}:{self.sec_m:02}:{aa:04.1f}  |  {h_r:02}:{m_r:02}:{s_r:04.1f}  |  №{i}"
                text = (
                    f"<pre>"
                    f" {self.sec_h:02}:{self.sec_m:02}:{aa:04.1f}  |  "
                    f" {h_r:02}:{m_r:02}:{s_r:04.1f}  |     №{i}"
                    f"</pre>"
                )
                
                new_label = QtWidgets.QLabel(text)
                new_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)
                new_label.setStyleSheet("border-bottom: 1px solid #ddd; padding: 5px;")  # Добавим разделитель
                font = QtGui.QFont("Monospace")
                font.setStyleHint(QtGui.QFont.StyleHint.Monospace)
                new_label.setFont(font)
                
                # Добавляем в слой ВНУТРИ ScrollArea
                # insertWidget(0, ...) добавит новый круг В НАЧАЛО списка (сверху)
                self.ui.roundsLayout.insertWidget(0, new_label)
                self.label_Secs.append(new_label)
    
    def handle_media_status(self, status):
        # Проверяем, что медиафайл проигран до конца
        if status == QMediaPlayer.MediaStatus.EndOfMedia:
            self.music_stop()
    
    def add_alarm(self, value=None):
        # Если value это False (пришло от нажатия кнопки), создаем новый ID
        if value is None or isinstance(value, bool):
           
            value = {
                'id': uuid.uuid4().hex,
                'time_al': '08:00',
                'name_al': 'Новый будильник',
                'week_al': [False] * 7,
                'music': self.default_music,
                'enabled': False
            }
        
        alarm = AlarmWidget(value)
        alarm.alarm_updated.connect(self.save_all_alarms)
        # Подключаем очистку кэша при удалении
        alarm.alarm_deleted.connect(self.cleanup_triggered_cache)
        # Вставляем перед распоркой (которая в verticalLayout_4A)
        self.ui.verticalLayout_4A.insertWidget(0, alarm)
        # сохраняем будильник
        self.save_all_alarms()
        
    def cleanup_triggered_cache(self, alarm_id):
        """Удаляет данные о срабатывании для удаленного будильника"""
        if alarm_id in self.triggered_today:
            del self.triggered_today[alarm_id]
    
    def save_all_alarms(self):
        all_data = []
        # findChildren надежнее, чем перебор layout.count()
        for widget in self.findChildren(AlarmWidget):
            # Проверяем, не помечен ли виджет на удаление
            if widget:
                all_data.append({
                    'id': widget.id,
                    'name_al': widget.name_alarm,
                    'time_al': widget.time_al,
                    'week_al': widget.week,
                    'music': widget.music,
                    'enabled': widget.checkBox_2.isChecked()
                })
        try:
            data_to_json(all_data, self.path_alarm)
        except Exception as e:
            print(f"Ошибка сохранения: {e}")
    
    def check_alarms(self):
        now = QtCore.QDateTime.currentDateTime()
        current_time = now.time().toString("HH:mm")
        weekday = now.date().dayOfWeek() - 1
        today = now.date().toString("yyyy-MM-dd")
        
        for widget in self.findChildren(AlarmWidget):
            if not widget.checkBox_2.isChecked():
                continue
            
            # Проверяем: если дни недели не выбраны, то считаем это "одноразовым" будильником
            # и пропускаем проверку конкретного дня недели
            has_days = any(widget.week)
            
            if has_days and not widget.week[weekday]:
                continue
            
            if widget.time_al == current_time:
                record = self.triggered_today.get(widget.id)
                if record == (today, widget.trigger_token):
                    continue
                
                # Помечаем как сработавший
                self.triggered_today[widget.id] = (today, widget.trigger_token)
                
                # Если это был одноразовый будильник (дни не выбраны), выключаем его
                if not has_days:
                    widget.checkBox_2.setChecked(False)
                    # Это автоматически вызовет сохранение, так как сигнал
                    # stateChanged подключен к save_all_alarms через alarm_updated
                
                self.trigger_alarm(widget)
    
    def trigger_alarm(self, alarm: AlarmWidget):
        print(f"⏰ Будильник: {alarm.name_alarm}")
        
        self.player.stop()
        self.player.setSource(QUrl.fromLocalFile(alarm.music))
        self.audio_output.setVolume(50)
        self.player.play()
        
        # Показ окна
        dialog = AlarmTriggeredDialog(
            alarm_name=alarm.name_alarm,
            alarm_time=alarm.time_al,
            parent=self
        )
        
        dialog.stop_alarm.connect(self.player.stop)
        dialog.exec()

    
    
if __name__ == '__main__':
    
    import sys
    import os
    
    sys.argv[0] = 'clock_app'  # Подменяем имя программы
    app = QtWidgets.QApplication(sys.argv)
    # Строка, которая помогает Linux связать окно и иконку
    app.setDesktopFileName("clock_app")
    
    # 1. Формируем путь (исправляем проблему путей)
    CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
    ICON_PATH = os.path.join(CURRENT_DIR, 'icon.png')
    
    # 2. Создаем объект иконки
    icon = QtGui.QIcon(ICON_PATH)
    
    # 3. Устанавливаем иконку приложению
    app.setWindowIcon(icon)

    window = Window()
    window.setWindowTitle("Clock App")
    window.show()
    sys.exit(app.exec())