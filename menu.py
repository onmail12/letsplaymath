# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menu.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(972, 521)
        icon = QtGui.QIcon.fromTheme("add")
        Form.setWindowIcon(icon)
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(30, 140, 571, 281))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.btn_quiz_subtract = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_quiz_subtract.setMinimumSize(QtCore.QSize(0, 80))
        self.btn_quiz_subtract.setObjectName("btn_quiz_subtract")
        self.gridLayout.addWidget(self.btn_quiz_subtract, 0, 1, 1, 1)
        self.btn_quiz_divide = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_quiz_divide.setMinimumSize(QtCore.QSize(0, 80))
        self.btn_quiz_divide.setObjectName("btn_quiz_divide")
        self.gridLayout.addWidget(self.btn_quiz_divide, 1, 1, 1, 1)
        self.btn_quiz_multiply = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_quiz_multiply.setMinimumSize(QtCore.QSize(0, 80))
        self.btn_quiz_multiply.setObjectName("btn_quiz_multiply")
        self.gridLayout.addWidget(self.btn_quiz_multiply, 1, 0, 1, 1)
        self.btn_quiz_add = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_quiz_add.setMinimumSize(QtCore.QSize(0, 80))
        self.btn_quiz_add.setObjectName("btn_quiz_add")
        self.gridLayout.addWidget(self.btn_quiz_add, 0, 0, 1, 1)
        self.label_title = QtWidgets.QLabel(Form)
        self.label_title.setGeometry(QtCore.QRect(30, 30, 371, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_title.setFont(font)
        self.label_title.setObjectName("label_title")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(670, 10, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.table_scores = QtWidgets.QTableWidget(Form)
        self.table_scores.setGeometry(QtCore.QRect(670, 50, 256, 411))
        self.table_scores.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.table_scores.setColumnCount(2)
        self.table_scores.setObjectName("table_scores")
        self.table_scores.setRowCount(0)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Let\'s Play Math"))
        self.btn_quiz_subtract.setText(_translate("Form", "Pengurangan (-)"))
        self.btn_quiz_divide.setText(_translate("Form", "Pembagian (/)"))
        self.btn_quiz_multiply.setText(_translate("Form", "Perkalian (x)"))
        self.btn_quiz_add.setText(_translate("Form", "Pertambahan (+)"))
        self.label_title.setText(_translate("Form", "Let\'s Play Math"))
        self.label_2.setText(_translate("Form", "Histori Skor"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
