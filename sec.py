
from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(516, 200)
        
        
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_30 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_30.setObjectName("horizontalLayout_30")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_30.addItem(spacerItem)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        
        self.pushButton_Timer = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton_Timer.setMinimumSize(QtCore.QSize(135, 34))
        self.pushButton_Timer.setStyleSheet("")
        self.pushButton_Timer.setObjectName("pushButton_Timer")
        self.horizontalLayout.addWidget(self.pushButton_Timer)
        
        self.pushButton_Sec = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton_Sec.setMinimumSize(QtCore.QSize(135, 34))
        self.pushButton_Sec.setObjectName("pushButton_Sec")
        self.horizontalLayout.addWidget(self.pushButton_Sec)
        
        spacerItem20= QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem20)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_h = QtWidgets.QLabel(parent=Dialog)
        self.label_h.setMinimumSize(QtCore.QSize(60, 0))
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
        self.label_min.setMinimumSize(QtCore.QSize(60, 0))
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
        self.label_sec.setMinimumSize(QtCore.QSize(60, 0))
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
        self.pushButton_Timer_start_stop = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton_Timer_start_stop.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_Timer_start_stop.setAutoDefault(True)
        self.pushButton_Timer_start_stop.setDefault(False)
        self.pushButton_Timer_start_stop.setObjectName("pushButton_Timer_start_stop")
        self.horizontalLayout_4.addWidget(self.pushButton_Timer_start_stop)
        self.pushButton_Timer_reset = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton_Timer_reset.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_Timer_reset.setDefault(False)
        self.pushButton_Timer_reset.setObjectName("pushButton_Timer_reset")
        self.horizontalLayout_4.addWidget(self.pushButton_Timer_reset)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.pushButton_Timer_setTimer = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton_Timer_setTimer.setMinimumSize(QtCore.QSize(0, 38))
        self.pushButton_Timer_setTimer.setObjectName("pushButton_Timer_setTimer")
        self.verticalLayout.addWidget(self.pushButton_Timer_setTimer)
        
        # add
        self.pushButton_Timer_music = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton_Timer_music.setObjectName("pushButton_Timer_music")
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
        self.pushButton_Sec_start_stop.setMinimumSize(QtCore.QSize(140, 35))
        self.pushButton_Sec_start_stop.setObjectName("pushButton_Sec_start_stop")
        self.horizontalLayout_2.addWidget(self.pushButton_Sec_start_stop)
        spacerItem200 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                            QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem200)
        self.pushButton_Sec_reset = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton_Sec_reset.setMinimumSize(QtCore.QSize(140, 35))
        self.pushButton_Sec_reset.setObjectName("pushButton_Sec_reset")
        self.horizontalLayout_2.addWidget(self.pushButton_Sec_reset)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                            QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_20.addItem(spacerItem3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_30)
        self.pushButton_Sec_round = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton_Sec_round.setMinimumSize(QtCore.QSize(99, 35))
        self.pushButton_Sec_round.setObjectName("pushButton_Sec_round")
        self.horizontalLayout_20.addWidget(self.pushButton_Sec_round)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                            QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_20.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.horizontalLayout_20)
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
        
        # --- ОБЛАСТЬ ПРОКРУТКИ ДЛЯ КРУГОВ ---
        self.scrollArea = QtWidgets.QScrollArea(Dialog)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setMinimumHeight(190)
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        # Слой внутри прокрутки, куда будут падать лейблы
        self.roundsLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.roundsLayout.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)  # Все круги прижимаются к верху
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        # Добавляем label152 без надписи, чтобы после scrollArea оставить пустое место
        # self.label152 = QtWidgets.QLabel(parent=Dialog)
        # self.label152.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        # self.label152.setObjectName("label152")
        # self.label152.setMinimumSize(QtCore.QSize(140, 15))
        # self.verticalLayout.addWidget(self.label152)
        #
        # spacerItem5 = QtWidgets.QSpacerItem(20, 21, QtWidgets.QSizePolicy.Policy.Minimum,
        #                                     QtWidgets.QSizePolicy.Policy.Expanding)
        # self.verticalLayout.addItem(spacerItem5)
        # spacerItem2 = QtWidgets.QSpacerItem(20, 21, QtWidgets.QSizePolicy.Policy.Minimum,
        #                                     QtWidgets.QSizePolicy.Policy.Expanding)
        # self.verticalLayout.addItem(spacerItem2)
        #
        #
        #
        # spacerItem20= QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Policy.Minimum,
        #                                     QtWidgets.QSizePolicy.Policy.Expanding)
        # self.verticalLayout.addItem(spacerItem20)


        self.horizontalLayout_30.addLayout(self.verticalLayout)
        spacerItem_right = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                                 QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_30.addItem(spacerItem_right)
        

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
        self.list_sec_widget = [self.label_Sec_h_2, self.label_Sec_h, self.label_Sec_min_2,
                                self.label_Sec_min, self.label_Sec_sec_2, self.label_Sec_sec,
                                self.pushButton_Sec_start_stop, self.pushButton_Sec_reset,
                                self.pushButton_Sec_round, self.label50,self.label51, self.label52,
                                # self.scrollArea, self.label152]
                                self.scrollArea]
        
        self.list_timer_widget = [self.label_h, self.label_Timer_h, self.label_min,
                                  self.label_Timer_min, self.label_sec, self.label_Timer_sec,
                                  self.pushButton_Timer_start_stop, self.pushButton_Timer_reset,
                                  self.pushButton_Timer_setTimer, self.pushButton_Timer_music]
        
        for i in self.list_sec_widget:
            i.hide()
        
        self.pushButton_Timer.setStyleSheet("background-color: #57e389;")
        self.pushButton_Sec.setStyleSheet("background-color: #f66151;")

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Секундомер/Таймер"))
        self.pushButton_Sec.setText(_translate("Dialog", "Секундомер"))
        self.pushButton_Timer.setText(_translate("Dialog", "Таймер"))
        self.label_h.setText(_translate("Dialog", "0"))
        self.label_Timer_h.setText(_translate("Dialog", "ч."))
        self.label_min.setText(_translate("Dialog", "0"))
        self.label_Timer_min.setText(_translate("Dialog", "мин."))
        self.label_sec.setText(_translate("Dialog", "0"))
        self.label_Timer_sec.setText(_translate("Dialog", "сек."))
        self.pushButton_Timer_start_stop.setText(_translate("Dialog", "Старт"))
        self.pushButton_Timer_reset.setText(_translate("Dialog", "Сброс"))
        self.pushButton_Timer_setTimer.setText(_translate("Dialog", "Задать время и мелодию"))
        self.pushButton_Timer_music.setText(_translate("Dialog", "Остановить музыку"))
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


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
