

from PyQt6 import QtCore, QtGui, QtWidgets
import os

from PyQt6.QtCore import QUrl, pyqtSignal
from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput
from PyQt6.QtWidgets import QDialog, QFileDialog
from config import load_config
# Инициализация часов, минут, секунд
path_env_timer = ".env_newsettimer"
default_value_h = load_config(path_env_timer).N_C.default_value_h
default_value_min = load_config(path_env_timer).N_C.default_value_min
default_value_s = load_config(path_env_timer).N_C.default_value_s
default_value_music = load_config(path_env_timer).N_C.default_value_music

# Получаем путь к папке скрипта для работы с файлами
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# переопределяем клас QtWidgets.QSpinBox для вывода занчений типа 01, 02, ...
class ZeroPaddedSpinBox(QtWidgets.QSpinBox):
    def textFromValue(self, value: int) -> str:
        return f"{value:02d}"

class Ui_Form(QDialog):
    value_selected = pyqtSignal(tuple)
    def __init__(self):
        super().__init__()
        self.setObjectName("Dialog")
        self.setWindowTitle("Установка таймера")
        self.resize(500, 590)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setMinimumSize(QtCore.QSize(500, 590))
        self.setMaximumSize(QtCore.QSize(500, 590))
        self.setSizeGripEnabled(False)
        self.setModal(True)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem = QtWidgets.QSpacerItem(16, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_2 = QtWidgets.QLabel()
        self.label_2.setStyleSheet("color: rgb(26, 95, 180);")
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_4.addWidget(self.label_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_5 = QtWidgets.QPushButton()
        self.pushButton_5.setStyleSheet("""QPushButton {
    background-color: #bad49d;
    border: 1px solid #333;
    border-radius: 8px;
    padding: 8px 16px;
    font-size: 16px;
}
QPushButton:hover {
    background-color: #9a9996;
    border-color: #57e389;
    color: black;
}""")
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_2.addWidget(self.pushButton_5)
        self.pushButton_6 = QtWidgets.QPushButton()
        self.pushButton_6.setStyleSheet("""QPushButton {
    background-color: #bad49d;
    border: 1px solid #333;
    border-radius: 8px;
    padding: 8px 16px;
    font-size: 16px;
}
QPushButton:hover {
    background-color: #9a9996;
    border-color: #57e389;
    color: black;
}""")
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_2.addWidget(self.pushButton_6)
        self.pushButton_7 = QtWidgets.QPushButton()
        self.pushButton_7.setStyleSheet("""QPushButton {
    background-color: #bad49d;
    border: 1px solid #333;
    border-radius: 8px;
    padding: 8px 16px;
    font-size: 16px;
}
QPushButton:hover {
    background-color: #9a9996;
    border-color: #57e389;
    color: black;
}""")
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout_2.addWidget(self.pushButton_7)
        self.pushButton_8 = QtWidgets.QPushButton()
        self.pushButton_8.setStyleSheet("""QPushButton {
    background-color: #bad49d;
    border: 1px solid #333;
    border-radius: 8px;
    padding: 8px 16px;
    font-size: 16px;
}
QPushButton:hover {
    background-color: #9a9996;
    border-color: #57e389;
    color: black;
}""")
        self.pushButton_8.setObjectName("pushButton_8")
        self.horizontalLayout_2.addWidget(self.pushButton_8)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.verticalLayout_4.addItem(spacerItem1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton()
        self.pushButton.setStyleSheet("""QPushButton {
    background-color: #bad49d;
    border: 1px solid #333;
    border-radius: 8px;
    padding: 8px 16px;
    font-size: 16px;
}
QPushButton:hover {
    background-color: #9a9996;
    border-color: #57e389;
    color: black;
}""")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton()
        self.pushButton_2.setStyleSheet("""QPushButton {
    background-color: #bad49d;
    border: 1px solid #333;
    border-radius: 8px;
    padding: 8px 16px;
    font-size: 16px;
}
QPushButton:hover {
    background-color: #9a9996;
    border-color: #57e389;
    color: black;
}""")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton()
        self.pushButton_3.setStyleSheet("""QPushButton {
    background-color: #bad49d;
    border: 1px solid #333;
    border-radius: 8px;
    padding: 8px 16px;
    font-size: 16px;
}
QPushButton:hover {
    background-color: #9a9996;
    border-color: #57e389;
    color: black;
}""")
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton()
        self.pushButton_4.setStyleSheet("""QPushButton {
    background-color: #bad49d;
    border: 1px solid #333;
    border-radius: 8px;
    padding: 8px 16px;
    font-size: 16px;
}
QPushButton:hover {
    background-color: #9a9996;
    border-color: #57e389;
    color: black;
}""")
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.verticalLayout_4.addItem(spacerItem2)
        self.label = QtWidgets.QLabel()
        self.label.setStyleSheet("color: rgb(28, 113, 216);")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.verticalLayout_4.addItem(spacerItem3)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_9 = QtWidgets.QPushButton()
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet("""QPushButton {
    background-color: #bad49d;
    border: 1px solid #333;
    border-radius: 8px;
    padding: 8px 16px;
    font-size: 16px;
}
QPushButton:hover {
    background-color: #9a9996;
    border-color: #57e389;
    color: #9141ac;
    font: bold;
}""")
        self.pushButton_9.setObjectName("pushButton_9")
        self.verticalLayout.addWidget(self.pushButton_9)
        self.spinBox = QtWidgets.QSpinBox()
        self.spinBox.setMinimumSize(QtCore.QSize(90, 0))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.spinBox.setFont(font)
        self.spinBox.setWrapping(True)
        self.spinBox.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.spinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.spinBox.setMaximum(23)
        self.spinBox.setObjectName("spinBox")
        self.spinBox.setValue(default_value_h)
        self.verticalLayout.addWidget(self.spinBox)
        
        # подмена старого spinBox на новый определенный в классе ZeroPaddedSpinBox
        old = self.spinBox
        layout = self.verticalLayout  # ← ВАЖНО
        
        new = ZeroPaddedSpinBox(self)
        new.setRange(old.minimum(), old.maximum())
        new.setValue(old.value())
        new.setFont(old.font())
        new.setAlignment(old.alignment())
        new.setButtonSymbols(old.buttonSymbols())
        new.setMaximum(old.maximum())
        new.setMinimum(old.minimum())
        new.setFrame(old.hasFrame())
        new.setWrapping(True)
        
        layout.replaceWidget(old, new)
        old.deleteLater()
        
        self.spinBox = new  # ← обязательно!
        
        self.pushButton_10 = QtWidgets.QPushButton()
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setStyleSheet("""QPushButton {
    background-color: #cdab8f;
    border: 1px solid #333;
    border-radius: 8px;
    padding: 8px 16px;
    font-size: 16px;
}
QPushButton:hover {
    background-color: #9a9996;
    border-color: #57e389;
    color: #9141ac;
    font: bold;
}""")
        self.pushButton_10.setObjectName("pushButton_10")
        self.verticalLayout.addWidget(self.pushButton_10)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.label_4 = QtWidgets.QLabel()
        self.label_4.setMaximumSize(QtCore.QSize(49, 16777215))
        font = QtGui.QFont()
        font.setPointSize(35)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_11 = QtWidgets.QPushButton()
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setStyleSheet("""QPushButton {
    background-color: #bad49d;
    border: 1px solid #333;
    border-radius: 8px;
    padding: 8px 16px;
    font-size: 16px;
}
QPushButton:hover {
    background-color: #9a9996;
    border-color: #57e389;
    color: #9141ac;
    font: bold;
}""")
        self.pushButton_11.setObjectName("pushButton_11")
        self.verticalLayout_2.addWidget(self.pushButton_11)
        self.spinBox_2 = QtWidgets.QSpinBox()
        self.spinBox_2.setMinimumSize(QtCore.QSize(90, 0))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.spinBox_2.setFont(font)
        self.spinBox_2.setWrapping(True)
        self.spinBox_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.spinBox_2.setButtonSymbols(QtWidgets.QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.spinBox_2.setMaximum(59)
        self.spinBox_2.setObjectName("spinBox_2")
        self.spinBox_2.setValue(default_value_min)
        self.verticalLayout_2.addWidget(self.spinBox_2)
        
        # подмена старого spinBox на новый определенный в классе ZeroPaddedSpinBox
        old = self.spinBox_2
        layout = self.verticalLayout_2  # ← ВАЖНО
        
        new_2 = ZeroPaddedSpinBox(self)
        new_2.setRange(old.minimum(), old.maximum())
        new_2.setValue(old.value())
        new_2.setFont(old.font())
        new_2.setAlignment(old.alignment())
        new_2.setButtonSymbols(old.buttonSymbols())
        new_2.setMaximum(old.maximum())
        new_2.setMinimum(old.minimum())
        new_2.setFrame(old.hasFrame())
        new_2.setWrapping(True)
        
        layout.replaceWidget(old, new_2)
        old.deleteLater()
        
        self.spinBox_2 = new_2  # ← обязательно!
        
        self.pushButton_12 = QtWidgets.QPushButton()
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setStyleSheet("""QPushButton {
    background-color: #cdab8f;
    border: 1px solid #333;
    border-radius: 8px;
    padding: 8px 16px;
    font-size: 16px;
}
QPushButton:hover {
    background-color: #9a9996;
    border-color: #57e389;
    color: #9141ac;
    font: bold;
}""")
        self.pushButton_12.setObjectName("pushButton_12")
        self.verticalLayout_2.addWidget(self.pushButton_12)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.label_7 = QtWidgets.QLabel()
        self.label_7.setMaximumSize(QtCore.QSize(49, 16777215))
        font = QtGui.QFont()
        font.setPointSize(35)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_3.addWidget(self.label_7)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pushButton_13 = QtWidgets.QPushButton()
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_13.setFont(font)
        self.pushButton_13.setStyleSheet("""QPushButton {
    background-color: #bad49d;
    border: 1px solid #333;
    border-radius: 8px;
    padding: 8px 16px;
    font-size: 16px;
}
QPushButton:hover {
    background-color: #9a9996;
    border-color: #57e389;
    color: #9141ac;
    font: bold;
}""")
        self.pushButton_13.setObjectName("pushButton_13")
        self.verticalLayout_3.addWidget(self.pushButton_13)
        self.spinBox_3 = QtWidgets.QSpinBox()
        self.spinBox_3.setMinimumSize(QtCore.QSize(90, 0))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.spinBox_3.setFont(font)
        self.spinBox_3.setWrapping(True)
        self.spinBox_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.spinBox_3.setButtonSymbols(QtWidgets.QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.spinBox_3.setMaximum(59)
        self.spinBox_3.setObjectName("spinBox_3")
        self.spinBox_3.setValue(default_value_s)
        self.verticalLayout_3.addWidget(self.spinBox_3)
        
        # подмена старого spinBox на новый определенный в классе ZeroPaddedSpinBox
        old = self.spinBox_3
        layout = self.verticalLayout_3  # ← ВАЖНО
        
        new_3 = ZeroPaddedSpinBox(self)
        new_3.setRange(old.minimum(), old.maximum())
        new_3.setValue(old.value())
        new_3.setFont(old.font())
        new_3.setAlignment(old.alignment())
        new_3.setButtonSymbols(old.buttonSymbols())
        new_3.setMaximum(old.maximum())
        new_3.setMinimum(old.minimum())
        new_3.setFrame(old.hasFrame())
        new_3.setWrapping(True)
        
        layout.replaceWidget(old, new_3)
        old.deleteLater()
        
        self.spinBox_3 = new_3  # ← обязательно!
        
        self.pushButton_14 = QtWidgets.QPushButton()
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_14.setFont(font)
        self.pushButton_14.setStyleSheet("""QPushButton {
    background-color: #cdab8f;
    border: 1px solid #333;
    border-radius: 8px;
    padding: 8px 16px;
    font-size: 16px;
}
QPushButton:hover {
    background-color: #9a9996;
    border-color: #57e389;
    color: #9141ac;
    font: bold;
}""")
        self.pushButton_14.setObjectName("pushButton_14")
        self.verticalLayout_3.addWidget(self.pushButton_14)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        spacerItem6 = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.verticalLayout_4.addItem(spacerItem6)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.input_play_Button = QtWidgets.QPushButton()
        self.input_play_Button.setStyleSheet("""QPushButton {
    background-color: #989C0E;
    border: 1px solid #333;
    border-radius: 8px;
    padding: 8px 16px;
    font-size: 16px;
}
QPushButton:hover {
    background-color: #9a9996;
    border-color: #57e389;
    color: black;
}""")
        self.input_play_Button.setObjectName("input_play_Button")
        self.horizontalLayout_4.addWidget(self.input_play_Button)
        self.stop_play_Button = QtWidgets.QPushButton()
        self.stop_play_Button.setStyleSheet("""QPushButton {
    background-color: #989C0E;
    border: 1px solid #333;
    border-radius: 8px;
    padding: 8px 16px;
    font-size: 16px;
}
QPushButton:hover {
    background-color: #9a9996;
    border-color: #57e389;
    color: black;

}
QPushButton:disabled {
    background-color: #4F5208; /* Делаем фон темнее */
    color: black;            /* Делаем текст тусклым */
    border: 1px solid #222222; /* Едва заметная рамка */
}
""")
        self.stop_play_Button.setObjectName("stop_play_Button")
        self.horizontalLayout_4.addWidget(self.stop_play_Button)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        spacerItem7 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.verticalLayout_4.addItem(spacerItem7)
        self.ok_Button = QtWidgets.QPushButton()
        self.ok_Button.setStyleSheet("""QPushButton {
    background-color: #d4e040;
    border: 1px solid #333;
    border-radius: 8px;
    padding: 8px 16px;
    font-size: 16px;
}
QPushButton:hover {
    background-color: #9a9996;
    border-color: #57e389;
    color: black;
}""")
        self.ok_Button.setObjectName("ok_Button")
        self.verticalLayout_4.addWidget(self.ok_Button)
        spacerItem8 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.verticalLayout_4.addItem(spacerItem8)
        self.horizontalLayout_5.addLayout(self.verticalLayout_4)
        spacerItem9 = QtWidgets.QSpacerItem(16, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem9)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)
        
        # предустановленная мелодия
        self.music = os.path.join(BASE_DIR, default_value_music)
        # если предустановленной мелодии не существует не позволяем ее оставить без выбора
        if not os.path.exists(self.music):
            self.ok_Button.setEnabled(False)
        
        # задаем клики кнопок
        self.pushButton_9.clicked.connect(self.add_h)
        self.pushButton_10.clicked.connect(self.del_h)
        self.pushButton_11.clicked.connect(self.add_m)
        self.pushButton_12.clicked.connect(self.del_m)
        self.pushButton_13.clicked.connect(self.add_s)
        self.pushButton_14.clicked.connect(self.del_s)
        self.input_play_Button.clicked.connect(self.open_modal)
        self.stop_play_Button.clicked.connect(self.music_stop)
        self.ok_Button.clicked.connect(self.handle_button_click)
        self.pushButton.clicked.connect(self.m1)
        self.pushButton_2.clicked.connect(self.m2)
        self.pushButton_3.clicked.connect(self.m3)
        self.pushButton_4.clicked.connect(self.m5)
        self.pushButton_5.clicked.connect(self.m15)
        self.pushButton_6.clicked.connect(self.m30)
        self.pushButton_7.clicked.connect(self.m45)
        self.pushButton_8.clicked.connect(self.h1)
        
        
        
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Установка таймера"))
        self.label_2.setText(_translate("Dialog", "Быстрая установка по нажатию"))
        self.pushButton_5.setText(_translate("Dialog", "15 мин"))
        self.pushButton_6.setText(_translate("Dialog", "30 мин"))
        self.pushButton_7.setText(_translate("Dialog", "45 мин"))
        self.pushButton_8.setText(_translate("Dialog", "1 час"))
        self.pushButton.setText(_translate("Dialog", "1 мин"))
        self.pushButton_2.setText(_translate("Dialog", "2 мин"))
        self.pushButton_3.setText(_translate("Dialog", "3 мин"))
        self.pushButton_4.setText(_translate("Dialog", "5 мин"))
        self.label.setText(_translate("Dialog", "Установить таймер в ручную"))
        self.pushButton_9.setText(_translate("Dialog", "+"))
        self.pushButton_10.setText(_translate("Dialog", "-"))
        self.label_4.setText(_translate("Dialog", ":"))
        self.pushButton_11.setText(_translate("Dialog", "+"))
        self.pushButton_12.setText(_translate("Dialog", "-"))
        self.label_7.setText(_translate("Dialog", ":"))
        self.pushButton_13.setText(_translate("Dialog", "+"))
        self.pushButton_14.setText(_translate("Dialog", "-"))
        self.input_play_Button.setText(_translate("Dialog", "Задать музыку и воспроизвести"))
        self.stop_play_Button.setText(_translate("Dialog", "Остановить музыку"))
        self.ok_Button.setText(_translate("Dialog", "Подтвердить"))
        
    def add_h(self):
        self.spinBox.stepUp()
    def del_h(self):
        self.spinBox.stepDown()
    def add_m(self):
        self.spinBox_2.stepUp()
    def del_m(self):
        self.spinBox_2.stepDown()
    def add_s(self):
        self.spinBox_3.stepUp()
    def del_s(self):
        self.spinBox_3.stepDown()
        
    def m1(self):
        self.spinBox.setValue(0)
        self.spinBox_2.setValue(1)
        self.spinBox_3.setValue(0)
        
    def m2(self):
        self.spinBox.setValue(0)
        self.spinBox_2.setValue(2)
        self.spinBox_3.setValue(0)
        
    def m3(self):
        self.spinBox.setValue(0)
        self.spinBox_2.setValue(3)
        self.spinBox_3.setValue(0)
        
    def m5(self):
        self.spinBox.setValue(0)
        self.spinBox_2.setValue(5)
        self.spinBox_3.setValue(0)
        
    def m15(self):
        self.spinBox.setValue(0)
        self.spinBox_2.setValue(15)
        self.spinBox_3.setValue(0)
        
    def m30(self):
        self.spinBox.setValue(0)
        self.spinBox_2.setValue(30)
        self.spinBox_3.setValue(0)
    
    def m45(self):
        self.spinBox.setValue(0)
        self.spinBox_2.setValue(45)
        self.spinBox_3.setValue(0)
    
    def h1(self):
        self.spinBox.setValue(1)
        self.spinBox_2.setValue(0)
        self.spinBox_3.setValue(0)
    # Вызов модального окна проигрования музыки с передачей имени проигруемого файла
    
    def open_modal(self):
        self.music = QFileDialog.getOpenFileName(self, 'Open File', './', 'JPG File (*.mp3);;MP3 File (*.mp3)')[0]
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
        # Ваше выбранное значение
        selected_value = (self.spinBox.text(), self.spinBox_2.text(), self.spinBox_3.text(), self.music)
        self.value_selected.emit(selected_value)  # Испускание сигнала с передачей значения
        with open(".env_newsettimer", "w") as f:
            f.write(f"DEF_VALUE_H={self.spinBox.text()}\nDEF_VALUE_MIN={self.spinBox_2.text()}\nDEF_VALUE_S={self.spinBox_3.text()}\nMUSIC={self.music}")
        self.accept()  # Закрываем окно
    # останавливаем воспроизведение музыки
    
    def music_stop(self):
        self.player.stop()
        self.ok_Button.setEnabled(True)
        
        # Проверяем статус воспроизведения музыки(если музыка закончилась - разблокируем кнопки)
    
    def handle_media_status(self, status):
        if status == QMediaPlayer.MediaStatus.EndOfMedia:
            self.ok_Button.setEnabled(True)
    
if __name__ == "__main__":
    import sys    
    app = QtWidgets.QApplication(sys.argv)
    window = Ui_Form()
    window.show()
    sys.exit(app.exec())
