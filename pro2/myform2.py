# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'myform2.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_myform2(object):
    def setupUi(self, myform2):
        myform2.setObjectName("myform2")
        myform2.resize(1500, 823)
        self.pushButton_4 = QtWidgets.QPushButton(myform2)
        self.pushButton_4.setGeometry(QtCore.QRect(30, 90, 551, 51))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_2 = QtWidgets.QPushButton(myform2)
        self.pushButton_2.setGeometry(QtCore.QRect(450, 30, 131, 34))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(myform2)
        self.label.setGeometry(QtCore.QRect(30, 720, 711, 81))
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.listWidget1 = QtWidgets.QListWidget(myform2)
        self.listWidget1.setGeometry(QtCore.QRect(30, 230, 731, 461))
        self.listWidget1.setObjectName("listWidget1")
        self.textEdit1 = QtWidgets.QTextEdit(myform2)
        self.textEdit1.setGeometry(QtCore.QRect(30, 180, 731, 41))
        self.textEdit1.setObjectName("textEdit1")
        self.label_2 = QtWidgets.QLabel(myform2)
        self.label_2.setGeometry(QtCore.QRect(30, 150, 211, 18))
        self.label_2.setObjectName("label_2")
        self.tableWidget2 = QtWidgets.QTableWidget(myform2)
        self.tableWidget2.setGeometry(QtCore.QRect(850, 170, 351, 521))
        self.tableWidget2.setObjectName("tableWidget2")
        self.tableWidget2.setColumnCount(0)
        self.tableWidget2.setRowCount(0)
        self.pushButton_3 = QtWidgets.QPushButton(myform2)
        self.pushButton_3.setGeometry(QtCore.QRect(850, 80, 231, 34))
        self.pushButton_3.setObjectName("pushButton_3")
        self.textEdit_2 = QtWidgets.QTextEdit(myform2)
        self.textEdit_2.setGeometry(QtCore.QRect(850, 130, 351, 31))
        self.textEdit_2.setObjectName("textEdit_2")
        self.pushButton_1 = QtWidgets.QPushButton(myform2)
        self.pushButton_1.setGeometry(QtCore.QRect(30, 30, 131, 34))
        self.pushButton_1.setObjectName("pushButton_1")
        self.textEdit_3 = QtWidgets.QTextEdit(myform2)
        self.textEdit_3.setGeometry(QtCore.QRect(240, 30, 71, 31))
        self.textEdit_3.setObjectName("textEdit_3")
        self.label_4 = QtWidgets.QLabel(myform2)
        self.label_4.setGeometry(QtCore.QRect(170, 40, 81, 18))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(myform2)
        self.label_5.setGeometry(QtCore.QRect(320, 30, 51, 31))
        self.label_5.setObjectName("label_5")
        self.textEdit_4 = QtWidgets.QTextEdit(myform2)
        self.textEdit_4.setGeometry(QtCore.QRect(360, 30, 71, 31))
        self.textEdit_4.setObjectName("textEdit_4")

        self.retranslateUi(myform2)
        self.pushButton_2.clicked.connect(myform2.bt2_click)
        self.pushButton_4.clicked.connect(myform2.bt4_click)
        self.listWidget1.itemClicked['QListWidgetItem*'].connect(myform2.LW1_dclick)
        self.pushButton_3.clicked.connect(myform2.bt3_click)
        self.pushButton_1.clicked.connect(myform2.bt1_click)
        QtCore.QMetaObject.connectSlotsByName(myform2)

    def retranslateUi(self, myform2):
        _translate = QtCore.QCoreApplication.translate
        myform2.setWindowTitle(_translate("myform2", "录波数据"))
        self.pushButton_4.setText(_translate("myform2", "确定显示波形"))
        self.pushButton_2.setText(_translate("myform2", "刷新所有DTU"))
        self.label.setText(_translate("myform2", "使用说明："))
        self.textEdit1.setHtml(_translate("myform2", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">条目内容</p></body></html>"))
        self.label_2.setText(_translate("myform2", "选择的条目内容："))
        self.pushButton_3.setText(_translate("myform2", "导出到excel"))
        self.pushButton_1.setText(_translate("myform2", "刷新特定DTU"))
        self.textEdit_3.setHtml(_translate("myform2", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">65104</p></body></html>"))
        self.label_4.setText(_translate("myform2", "DTUID"))
        self.label_5.setText(_translate("myform2", "数量"))
        self.textEdit_4.setHtml(_translate("myform2", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">100</p></body></html>"))

