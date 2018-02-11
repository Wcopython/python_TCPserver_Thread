# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'myUI1.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1575, 930)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(9, 9, 1551, 841))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1575, 30))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.action_1 = QtWidgets.QAction(MainWindow)
        self.action_1.setObjectName("action_1")
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.action_3 = QtWidgets.QAction(MainWindow)
        self.action_3.setObjectName("action_3")
        self.action_5 = QtWidgets.QAction(MainWindow)
        self.action_5.setObjectName("action_5")
        self.action_6 = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.action_6.setFont(font)
        self.action_6.setObjectName("action_6")
        self.action_4 = QtWidgets.QAction(MainWindow)
        self.action_4.setObjectName("action_4")
        self.toolBar.addAction(self.action_1)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.action_2)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.action_3)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.action_4)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.action_5)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.action_6)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "数据分析软件V20180211V1"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.action_1.setText(_translate("MainWindow", "查询周期数据"))
        self.action_1.setToolTip(_translate("MainWindow", "窗体1"))
        self.action_2.setText(_translate("MainWindow", "查询录波数据"))
        self.action_2.setToolTip(_translate("MainWindow", "窗体2"))
        self.action_3.setText(_translate("MainWindow", "查询信号强度"))
        self.action_3.setToolTip(_translate("MainWindow", "查询信号强度"))
        self.action_5.setText(_translate("MainWindow", "查询报警数据"))
        self.action_6.setText(_translate("MainWindow", "实时监测"))
        self.action_4.setText(_translate("MainWindow", "查询12T数据"))

