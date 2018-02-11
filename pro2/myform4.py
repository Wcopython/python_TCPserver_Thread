# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'myform4.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_myform4(object):
    def setupUi(self, myform4):
        myform4.setObjectName("myform4")
        myform4.resize(1500, 830)
        self.tableWidget1 = QtWidgets.QTableWidget(myform4)
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
        self.pushButton = QtWidgets.QPushButton(myform4)
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 201, 34))
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setObjectName("pushButton")
        self.textEdit = QtWidgets.QTextEdit(myform4)
        self.textEdit.setGeometry(QtCore.QRect(280, 10, 81, 31))
        self.textEdit.setObjectName("textEdit")
        self.label_3 = QtWidgets.QLabel(myform4)
        self.label_3.setGeometry(QtCore.QRect(220, 20, 61, 18))
        self.label_3.setObjectName("label_3")
        self.textEdit_2 = QtWidgets.QTextEdit(myform4)
        self.textEdit_2.setGeometry(QtCore.QRect(440, 10, 81, 31))
        self.textEdit_2.setObjectName("textEdit_2")
        self.label_4 = QtWidgets.QLabel(myform4)
        self.label_4.setGeometry(QtCore.QRect(380, 20, 51, 18))
        self.label_4.setObjectName("label_4")
        self.pushButton_2 = QtWidgets.QPushButton(myform4)
        self.pushButton_2.setGeometry(QtCore.QRect(790, 10, 211, 34))
        self.pushButton_2.setAutoFillBackground(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_5 = QtWidgets.QLabel(myform4)
        self.label_5.setGeometry(QtCore.QRect(540, 20, 51, 18))
        self.label_5.setObjectName("label_5")
        self.textEdit_3 = QtWidgets.QTextEdit(myform4)
        self.textEdit_3.setGeometry(QtCore.QRect(590, 10, 81, 31))
        self.textEdit_3.setObjectName("textEdit_3")

        self.retranslateUi(myform4)
        self.pushButton.clicked.connect(myform4.bt1_click)
        self.pushButton_2.clicked.connect(myform4.bt2_click)
        QtCore.QMetaObject.connectSlotsByName(myform4)

    def retranslateUi(self, myform4):
        _translate = QtCore.QCoreApplication.translate
        myform4.setWindowTitle(_translate("myform4", "查询12T"))
        self.pushButton.setText(_translate("myform4", "刷新特定DTU-12T数据"))
        self.textEdit.setHtml(_translate("myform4", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">65104</p></body></html>"))
        self.label_3.setText(_translate("myform4", "DTUID"))
        self.textEdit_2.setHtml(_translate("myform4", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">100</p></body></html>"))
        self.label_4.setText(_translate("myform4", "数量："))
        self.pushButton_2.setText(_translate("myform4", "刷新所有DTU-12T数据"))
        self.label_5.setText(_translate("myform4", "状态："))
        self.textEdit_3.setHtml(_translate("myform4", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1</p></body></html>"))

