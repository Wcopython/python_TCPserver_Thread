# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'myform1.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_myform1(object):
    def setupUi(self, myform1):
        myform1.setObjectName("myform1")
        myform1.resize(1500, 830)
        self.tableWidget1 = QtWidgets.QTableWidget(myform1)
        self.tableWidget1.setGeometry(QtCore.QRect(0, 90, 1500, 730))
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
        self.pushButton = QtWidgets.QPushButton(myform1)
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 201, 34))
        self.pushButton.setObjectName("pushButton")
        self.textEdit = QtWidgets.QTextEdit(myform1)
        self.textEdit.setGeometry(QtCore.QRect(280, 10, 81, 31))
        self.textEdit.setObjectName("textEdit")
        self.label_3 = QtWidgets.QLabel(myform1)
        self.label_3.setGeometry(QtCore.QRect(220, 20, 61, 18))
        self.label_3.setObjectName("label_3")
        self.textEdit_2 = QtWidgets.QTextEdit(myform1)
        self.textEdit_2.setGeometry(QtCore.QRect(440, 10, 81, 31))
        self.textEdit_2.setObjectName("textEdit_2")
        self.label_4 = QtWidgets.QLabel(myform1)
        self.label_4.setGeometry(QtCore.QRect(380, 20, 51, 18))
        self.label_4.setObjectName("label_4")
        self.pushButton_2 = QtWidgets.QPushButton(myform1)
        self.pushButton_2.setGeometry(QtCore.QRect(600, 10, 211, 34))
        self.pushButton_2.setAutoFillBackground(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(myform1)
        self.pushButton_3.setGeometry(QtCore.QRect(1030, 10, 121, 34))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(myform1)
        self.pushButton_4.setGeometry(QtCore.QRect(1030, 50, 121, 34))
        self.pushButton_4.setObjectName("pushButton_4")
        self.label = QtWidgets.QLabel(myform1)
        self.label.setGeometry(QtCore.QRect(1180, 50, 271, 31))
        self.label.setObjectName("label")
        self.label_8 = QtWidgets.QLabel(myform1)
        self.label_8.setGeometry(QtCore.QRect(1370, 10, 41, 31))
        self.label_8.setObjectName("label_8")
        self.textEdit_4 = QtWidgets.QTextEdit(myform1)
        self.textEdit_4.setGeometry(QtCore.QRect(1280, 10, 81, 31))
        self.textEdit_4.setObjectName("textEdit_4")
        self.label_2 = QtWidgets.QLabel(myform1)
        self.label_2.setGeometry(QtCore.QRect(1180, 10, 91, 31))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(myform1)
        self.pushButton.clicked.connect(myform1.bt1_click)
        self.pushButton_2.clicked.connect(myform1.bt2_click)
        self.pushButton_3.clicked.connect(myform1.bt3_click)
        self.pushButton_4.clicked.connect(myform1.bt4_click)
        QtCore.QMetaObject.connectSlotsByName(myform1)

    def retranslateUi(self, myform1):
        _translate = QtCore.QCoreApplication.translate
        myform1.setWindowTitle(_translate("myform1", "Form"))
        self.pushButton.setText(_translate("myform1", "刷新特定DTU周期数据"))
        self.textEdit.setHtml(_translate("myform1", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">65104</p></body></html>"))
        self.label_3.setText(_translate("myform1", "DTUID"))
        self.textEdit_2.setHtml(_translate("myform1", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">100</p></body></html>"))
        self.label_4.setText(_translate("myform1", "数量："))
        self.pushButton_2.setText(_translate("myform1", "刷新所有DTU周期数据"))
        self.pushButton_3.setText(_translate("myform1", "开启自动刷新"))
        self.pushButton_4.setText(_translate("myform1", "关闭自动刷新"))
        self.label.setText(_translate("myform1", "当前刷新时间"))
        self.label_8.setText(_translate("myform1", "秒"))
        self.textEdit_4.setHtml(_translate("myform1", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">10</p></body></html>"))
        self.label_2.setText(_translate("myform1", "刷新间隔："))

