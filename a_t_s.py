# Основное окно программы


from PyQt6 import QtCore, QtGui, QtWidgets
from config import load_config


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(516, 650)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_20.addItem(spacerItem)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButton_Alarm = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton_Alarm.setMinimumSize(QtCore.QSize(128, 36))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_Alarm.setFont(font)
        self.pushButton_Alarm.setStyleSheet("")
        self.pushButton_Alarm.setObjectName("pushButton_Alarm")
        self.horizontalLayout.addWidget(self.pushButton_Alarm)
        self.pushButton_Timer = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton_Timer.setMinimumSize(QtCore.QSize(128, 36))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_Timer.setFont(font)
        self.pushButton_Timer.setStyleSheet("")
        self.pushButton_Timer.setObjectName("pushButton_Timer")
        self.horizontalLayout.addWidget(self.pushButton_Timer)
        self.pushButton_Sec = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton_Sec.setMinimumSize(QtCore.QSize(128, 36))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_Sec.setFont(font)
        self.pushButton_Sec.setObjectName("pushButton_Sec")
        self.horizontalLayout.addWidget(self.pushButton_Sec)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        # --- ЧАСЫ ---
        self.label_clock = QtWidgets.QLabel(parent=Dialog)
        self.label_clock.setObjectName("label_clock")
        font_clock = QtGui.QFont()
        font_clock.setPointSize(48)
        font_clock.setBold(True)
        self.label_clock.setFont(font_clock)
        self.label_clock.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_clock.setText("00:00:00")
        self.verticalLayout.addWidget(self.label_clock)
        self.label_clock.setStyleSheet("""
            #label_clock {
                border-image: url(pic.jpg);
                background-repeat: no-repeat;
                background-position: center;
                border: 1px solid #333;
                border-radius: 12px;
            }
        """)
        # --- конец часов ---
        self.verticalLayout.addLayout(self.horizontalLayout)
        
        # Будильник
        
        self.pushButton_Alarm_add = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton_Alarm_add.setMinimumSize(QtCore.QSize(99, 35))
        self.pushButton_Alarm_add.setObjectName("pushButton_Alarm_add")
        self.verticalLayout.addWidget(self.pushButton_Alarm_add)
        self.scrollArea_Alarm = QtWidgets.QScrollArea(parent=Dialog)
        self.scrollArea_Alarm.setMinimumSize(QtCore.QSize(0, 520))
        self.scrollArea_Alarm.setWidgetResizable(True)
        self.scrollArea_Alarm.setObjectName("scrollArea_Alarm")
        self.scrollArea_Alarm.setStyleSheet("""
            /* Сама рамка скролла */
            QScrollArea {
                border: 2px solid #57e389;
                border-radius: 8px;
                background-color: transparent; /* Делаем основу прозрачной */
            }

            /* Внутреннее пространство, где лежат виджеты */
            QScrollArea QWidget#qt_scrollarea_viewport {
                background-image: url(pic.jpg);
                background-position: center;
                background-repeat: no-repeat;
                /* Если картинка маленькая и нужно растянуть, используйте border-image: */
                /* border-image: url(pic.jpg) 0 0 0 0 stretch stretch; */
            }

            /* Контейнер для виджетов тоже должен быть прозрачным */
            #scrollAreaWidgetContents_Alarm {
                background: transparent;
            }
        """)
        self.scrollAreaWidgetContents_Alarm = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_Alarm.setGeometry(QtCore.QRect(0, 0, 442, 514))
        self.scrollAreaWidgetContents_Alarm.setObjectName("scrollAreaWidgetContents_Alarm")
        self.verticalLayout_4A = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_Alarm)
        self.verticalLayout_4A.setObjectName("verticalLayout_4A")
        
        
        self.scrollArea_Alarm.setWidget(self.scrollAreaWidgetContents_Alarm)
        self.verticalLayout.addWidget(self.scrollArea_Alarm)
        self.horizontalLayout_20.addLayout(self.verticalLayout)
        spacerItem6A = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                            QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_20.addItem(spacerItem6A)
        
        
        # Таймер
        
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_h = QtWidgets.QLabel(parent=Dialog)
        self.label_h.setMinimumSize(QtCore.QSize(60, 45))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label_h.setFont(font)
        self.label_h.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_h.setObjectName("label_h")
        self.horizontalLayout_2.addWidget(self.label_h)
        self.label_Timer_h = QtWidgets.QLabel(parent=Dialog)
        self.label_Timer_h.setObjectName("label_Timer_h")
        self.horizontalLayout_2.addWidget(self.label_Timer_h)
        self.label_min = QtWidgets.QLabel(parent=Dialog)
        self.label_min.setMinimumSize(QtCore.QSize(60, 45))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label_min.setFont(font)
        self.label_min.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_min.setObjectName("label_min")
        self.horizontalLayout_2.addWidget(self.label_min)
        self.label_Timer_min = QtWidgets.QLabel(parent=Dialog)
        self.label_Timer_min.setObjectName("label_Timer_min")
        self.horizontalLayout_2.addWidget(self.label_Timer_min)
        self.label_sec = QtWidgets.QLabel(parent=Dialog)
        self.label_sec.setMinimumSize(QtCore.QSize(60, 45))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label_sec.setFont(font)
        self.label_sec.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_sec.setObjectName("label_sec")
        self.horizontalLayout_2.addWidget(self.label_sec)
        self.label_Timer_sec = QtWidgets.QLabel(parent=Dialog)
        self.label_Timer_sec.setObjectName("label_Timer_sec")
        self.horizontalLayout_2.addWidget(self.label_Timer_sec)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        # self.pushButton_Timer_start_stop = QtWidgets.QPushButton(parent=Dialog)
        # self.pushButton_Timer_start_stop.setMinimumSize(QtCore.QSize(0, 40))
        # self.pushButton_Timer_start_stop.setAutoDefault(True)
        # self.pushButton_Timer_start_stop.setDefault(False)
        # self.pushButton_Timer_start_stop.setObjectName("pushButton_Timer_start_stop")
        # self.horizontalLayout_4.addWidget(self.pushButton_Timer_start_stop)
        self.pushButton_Timer_setTimer = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton_Timer_setTimer.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_Timer_setTimer.setObjectName("pushButton_Timer_setTimer")
        self.horizontalLayout_4.addWidget(self.pushButton_Timer_setTimer)
        self.pushButton_Timer_reset = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton_Timer_reset.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_Timer_reset.setDefault(False)
        self.pushButton_Timer_reset.setObjectName("pushButton_Timer_reset")
        self.horizontalLayout_4.addWidget(self.pushButton_Timer_reset)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        # self.pushButton_Timer_setTimer = QtWidgets.QPushButton(parent=Dialog)
        # self.pushButton_Timer_setTimer.setMinimumSize(QtCore.QSize(99, 35))
        # self.pushButton_Timer_setTimer.setObjectName("pushButton_Timer_setTimer")
        # self.verticalLayout.addWidget(self.pushButton_Timer_setTimer)
        self.pushButton_Timer_start_stop = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton_Timer_start_stop.setMinimumSize(QtCore.QSize(99, 35))
        self.pushButton_Timer_start_stop.setAutoDefault(True)
        self.pushButton_Timer_start_stop.setDefault(False)
        self.pushButton_Timer_start_stop.setObjectName("pushButton_Timer_start_stop")
        self.verticalLayout.addWidget(self.pushButton_Timer_start_stop)
        self.horizontalLayout_20.addLayout(self.verticalLayout)
        
        # добавляем кнопку останов музыки на таймере
        self.pushButton_Timer_music = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton_Timer_music.setObjectName("pushButton_Timer_music")
        self.pushButton_Timer_music.setMinimumSize(QtCore.QSize(99, 35))
        self.verticalLayout.addWidget(self.pushButton_Timer_music)
        self.pushButton_Timer_music.hide()
        
        
        # Секундомер
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_Sec_h_2 = QtWidgets.QLabel(parent=Dialog)
        self.label_Sec_h_2.setMinimumSize(QtCore.QSize(60, 45))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label_Sec_h_2.setFont(font)
        self.label_Sec_h_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_Sec_h_2.setObjectName("label_Sec_h_2")
        self.horizontalLayout_3.addWidget(self.label_Sec_h_2)
        self.label_Sec_h = QtWidgets.QLabel(parent=Dialog)
        self.label_Sec_h.setObjectName("label_Sec_h")
        self.horizontalLayout_3.addWidget(self.label_Sec_h)
        self.label_Sec_min_2 = QtWidgets.QLabel(parent=Dialog)
        self.label_Sec_min_2.setMinimumSize(QtCore.QSize(60, 0))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label_Sec_min_2.setFont(font)
        self.label_Sec_min_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_Sec_min_2.setObjectName("label_Sec_min_2")
        self.horizontalLayout_3.addWidget(self.label_Sec_min_2)
        self.label_Sec_min = QtWidgets.QLabel(parent=Dialog)
        self.label_Sec_min.setObjectName("label_Sec_min")
        self.horizontalLayout_3.addWidget(self.label_Sec_min)
        self.label_Sec_sec_2 = QtWidgets.QLabel(parent=Dialog)
        self.label_Sec_sec_2.setMinimumSize(QtCore.QSize(60, 0))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label_Sec_sec_2.setFont(font)
        self.label_Sec_sec_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_Sec_sec_2.setObjectName("label_Sec_sec_2")
        self.horizontalLayout_3.addWidget(self.label_Sec_sec_2)
        self.label_Sec_sec = QtWidgets.QLabel(parent=Dialog)
        self.label_Sec_sec.setObjectName("label_Sec_sec")
        self.horizontalLayout_3.addWidget(self.label_Sec_sec)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_Sec_start_stop = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton_Sec_start_stop.setMinimumSize(QtCore.QSize(140, 40))
        self.pushButton_Sec_start_stop.setObjectName("pushButton_Sec_start_stop")
        self.horizontalLayout_2.addWidget(self.pushButton_Sec_start_stop)
        self.pushButton_Sec_reset = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton_Sec_reset.setMinimumSize(QtCore.QSize(140, 40))
        self.pushButton_Sec_reset.setObjectName("pushButton_Sec_reset")
        self.horizontalLayout_2.addWidget(self.pushButton_Sec_reset)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.pushButton_Sec_round = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton_Sec_round.setMinimumSize(QtCore.QSize(99, 35))
        self.pushButton_Sec_round.setObjectName("pushButton_Sec_round")
        self.verticalLayout.addWidget(self.pushButton_Sec_round)
        self.horizontalLayout_50 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_50.setObjectName("horizontalLayout_50")
        self.label50 = QtWidgets.QLabel(parent=Dialog)
        self.label50.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label50.setObjectName("label50")
        self.horizontalLayout_50.addWidget(self.label50)
        self.label51 = QtWidgets.QLabel(parent=Dialog)
        self.label51.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label51.setObjectName("label51")
        self.horizontalLayout_50.addWidget(self.label51)
        self.label52 = QtWidgets.QLabel(parent=Dialog)
        self.label52.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label52.setObjectName("label52")
        self.horizontalLayout_50.addWidget(self.label52)
        self.verticalLayout.addLayout(self.horizontalLayout_50)
        self.scrollArea = QtWidgets.QScrollArea(parent=Dialog)
        self.scrollArea.setMinimumSize(QtCore.QSize(0, 250))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollArea.setStyleSheet("""
            QScrollArea {
                border: 1px solid #d4e040;
                border-radius: 12px;
                background-color: transparent;
            }
            #scrollArea QWidget#qt_scrollarea_viewport {
                border-image: url(pic.jpg) 0 0 0 0 stretch stretch;
            }
        """)
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 354, 248))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        
        # Слой внутри прокрутки, куда будут падать лейблы
        self.roundsLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.roundsLayout.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)  # Все круги прижимаются к верху
        self.verticalLayout.addWidget(self.scrollArea)
        self.horizontalLayout_20.addLayout(self.verticalLayout)
        
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_20.addItem(spacerItem3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_20)
        # Для обращения к этой распорке делаем ее через self
        self.spacerItem4 = QtWidgets.QSpacerItem(0, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_2.addItem(self.spacerItem4)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
        self.list_alarm_widget = [self.pushButton_Alarm_add, self.scrollArea_Alarm, self.scrollAreaWidgetContents_Alarm]
        
        
        self.list_sec_widget = [self.label_Sec_h_2, self.label_Sec_h, self.label_Sec_min_2,
                                self.label_Sec_min, self.label_Sec_sec_2, self.label_Sec_sec,
                                self.pushButton_Sec_start_stop, self.pushButton_Sec_reset,
                                self.pushButton_Sec_round, self.label50, self.label51, self.label52,
                                self.scrollArea]
        
        self.list_timer_widget = [self.label_h, self.label_Timer_h, self.label_min,
                                  self.label_Timer_min, self.label_sec, self.label_Timer_sec,
                                  self.pushButton_Timer_start_stop, self.pushButton_Timer_reset,
                                  self.pushButton_Timer_setTimer, self.pushButton_Timer_music]
        
        for i in self.list_timer_widget:
            i.hide()
        
        for i in self.list_sec_widget:
            i.hide()
        
        self.pushButton_Alarm.setStyleSheet("background-color: #57e389;")
        self.pushButton_Timer.setStyleSheet("background-color: #d4e040;")
        self.pushButton_Sec.setStyleSheet("background-color: #d4e040;")
        
        

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Будильник/Таймер/Секндомер"))
        
        # Инициализация часов, минут, секунд
        path_env_timer = ".env_newsettimer"
        default_value_h = str(load_config(path_env_timer).N_C.default_value_h)
        default_value_min = str(load_config(path_env_timer).N_C.default_value_min)
        default_value_s = str(load_config(path_env_timer).N_C.default_value_s)
        
        self.pushButton_Alarm.setText(_translate("Dialog", "Будильник"))
        self.pushButton_Timer.setText(_translate("Dialog", "Таймер"))
        self.pushButton_Sec.setText(_translate("Dialog", "Секундомер"))
        self.label_h.setText(_translate("Dialog", default_value_h))
        self.label_Timer_h.setText(_translate("Dialog", "ч."))
        self.label_min.setText(_translate("Dialog", default_value_min))
        self.label_Timer_min.setText(_translate("Dialog", "мин."))
        self.label_sec.setText(_translate("Dialog", default_value_s))
        self.label_Timer_sec.setText(_translate("Dialog", "сек."))
        self.pushButton_Timer_start_stop.setText(_translate("Dialog", "Старт"))
        self.pushButton_Timer_reset.setText(_translate("Dialog", "Сброс"))
        self.pushButton_Timer_setTimer.setText(_translate("Dialog", "Задать время и мелодию"))
        self.label_Sec_h_2.setText(_translate("Dialog", "0"))
        self.label_Sec_h.setText(_translate("Dialog", "ч."))
        self.label_Sec_min_2.setText(_translate("Dialog", "0"))
        self.label_Sec_min.setText(_translate("Dialog", "мин."))
        self.label_Sec_sec_2.setText(_translate("Dialog", "0"))
        self.label_Sec_sec.setText(_translate("Dialog", "сек."))
        self.pushButton_Sec_start_stop.setText(_translate("Dialog", "Старт"))
        self.pushButton_Sec_reset.setText(_translate("Dialog", "Сброс"))
        self.pushButton_Sec_round.setText(_translate("Dialog", "Круг"))
        self.label50.setText(_translate("Dialog", "Общее время"))
        self.label51.setText(_translate("Dialog", "Время круга"))
        self.label52.setText(_translate("Dialog", "Круги"))
        self.pushButton_Timer_music.setText(_translate("Dialog", "Остановить музыку"))
        self.pushButton_Alarm_add.setText(_translate("Dialog", "Добавить будильник"))
        
    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
