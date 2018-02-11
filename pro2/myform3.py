# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'myform3.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_myform3(object):
    def setupUi(self, myform3):
        myform3.setObjectName("myform3")
        myform3.resize(1500, 830)
        self.tableWidget1 = QtWidgets.QTableWidget(myform3)
        self.tableWidget1.setGeometry(QtCore.QRect(10, 60, 1500, 730))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget1.sizePolicy().hasHeightForWidth())
        self.tableWidget1.setSizePolicy(sizePolicy)
        self.tableWidget1.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tableWidget1.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tableWidget1.setSelectionMode(QtWidgets.QAbstractItemView.ContiguousSelection)
        self.tableWidget1.setObjectName("tableWidget1")
        self.tableWidget1.setColumnCount(0)
        self.tableWidget1.setRowCount(0)
        self.pushButton = QtWidgets.QPushButton(myform3)
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 201, 34))
        self.pushButton.setObjectName("pushButton")
        self.textEdit = QtWidgets.QTextEdit(myform3)
        self.textEdit.setGeometry(QtCore.QRect(280, 10, 81, 31))
        self.textEdit.setObjectName("textEdit")
        self.label_3 = QtWidgets.QLabel(myform3)
        self.label_3.setGeometry(QtCore.QRect(220, 20, 61, 18))
        self.label_3.setObjectName("label_3")
        self.textEdit_2 = QtWidgets.QTextEdit(myform3)
        self.textEdit_2.setGeometry(QtCore.QRect(440, 10, 81, 31))
        self.textEdit_2.setObjectName("textEdit_2")
        self.label_4 = QtWidgets.QLabel(myform3)
        self.label_4.setGeometry(QtCore.QRect(380, 20, 51, 18))
        self.label_4.setObjectName("label_4")
        self.pushButton_2 = QtWidgets.QPushButton(myform3)
        self.pushButton_2.setGeometry(QtCore.QRect(600, 10, 211, 34))
        self.pushButton_2.setAutoFillBackground(False)
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(myform3)
        self.pushButton.clicked.connect(myform3.bt1_click)
        self.pushButton_2.clicked.connect(myform3.bt2_click)
        QtCore.QMetaObject.connectSlotsByName(myform3)

    def retranslateUi(self, myform3):
        _translate = QtCore.QCoreApplication.translate
        myform3.setWindowTitle(_translate("myform3", "查询信号强度"))
        self.pushButton.setText(_translate("myform3", "刷新特定DTU信号强度"))
        self.textEdit.setHtml(_translate("myform3", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">65104</p></body></html>"))
        self.label_3.setText(_translate("myform3", "DTUID"))
        self.textEdit_2.setHtml(_translate("myform3", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">100</p></body></html>"))
        self.label_4.setText(_translate("myform3", "数量："))
        self.pushButton_2.setText(_translate("myform3", "刷新所有DTU信号强度"))

