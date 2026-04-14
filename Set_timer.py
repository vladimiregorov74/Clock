from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(193, 102)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.timeEdit = QtWidgets.QTimeEdit(parent=Form)
        self.timeEdit.setMinimumDate(QtCore.QDate(2000, 1, 5))
        self.timeEdit.setObjectName("timeEdit")
        self.verticalLayout.addWidget(self.timeEdit)
        self.pushButton = QtWidgets.QPushButton(parent=Form)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Задайте время таймера"))
        self.timeEdit.setDisplayFormat(_translate("Form", "HH:mm:ss"))
        self.pushButton.setText(_translate("Form", "Подтвердить"))
