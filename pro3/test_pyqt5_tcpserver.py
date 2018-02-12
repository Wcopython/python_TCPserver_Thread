#!/usr/bin/env python3
import bisect
import collections
import sys
from PyQt5.QtCore import (QByteArray, QDataStream, QDate, QReadWriteLock, QThread,QIODevice, Qt)
from PyQt5.QtWidgets import (QApplication, QMessageBox, QPushButton)
from PyQt5.QtNetwork import (QAbstractSocket,QHostAddress, QTcpServer, QTcpSocket)

from PyQt5.QtWidgets import QApplication,QMainWindow,QWidget,QFileDialog,QListWidget
from myUI1 import Ui_myUI1
from PyQt5.QtCore import *

PORT = 9407








#################3333
class Thread(QThread):

    lock = QReadWriteLock()
    sinOut1 = pyqtSignal(str) #信号量变量
    sinOut2 = pyqtSignal(str)  # 信号量变量
    sinOut3 = pyqtSignal(str)

    #socket = QTcpSocket()
    def __init__(self, socketId, parent):
        super(Thread, self).__init__(parent)
        self.socketId = socketId


    def run(self):
        self.socket = QTcpSocket()
        self.myclientid1=0
        if not self.socket.setSocketDescriptor(self.socketId):
            self.error.connect(self.socket.error)
            return
        self.sinOut1.emit(str(self.socketId)+"#"+QDateTime.currentDateTime().toString("yyyy-MM-dd HH:mm:ss"))#发送信号量 //建立连接

        while self.socket.state() == QAbstractSocket.ConnectedState:
            if (self.socket.waitForReadyRead(1000*60*10) and self.socket.bytesAvailable() > 0):
                #waitForReadyRead(1000*60*10)说明，单位为毫秒，时间内等待接收数据，超时为假
                mygetdata=self.socket.readAll()
                mygetdata=bytes(mygetdata)
                #print(mygetdata)
                self.sinOut2.emit("get data:" + str(mygetdata)) #client发送来的数据
                #分析客户端数据中的ID值
                myclientid=self.myanalyseframe(mygetdata)

                if myclientid!=0 and myclientid!=self.myclientid1:
                    self.myclientid1=myclientid
                    # 利用client数据，标识处TCP连接的对象ID值，指令中的值
                    self.sinOut1.emit(str(self.socketId)+"#"+QDateTime.currentDateTime().toString("yyyy-MM-dd HH:mm:ss")+"#"+str(myclientid))

            else:
                self.senddata(self.socket,'TCP time out')
                self.sinOut3.emit(str(self.socketId))#超时，线程结束,删除前台listw中的条目

                return #超时，线程结束





    def sendStr(self, socket, msg):
        mysentdata=msg.encode('utf-8')
        socket.write(mysentdata)

    def senddata(self, socket, data):
        if isinstance(data,str)==True:
            mysentdata = data.encode('utf-8')
        elif isinstance(data,list)==True:
            mysentdata=bytes(data)
        elif isinstance(data,int)==True or isinstance(data,float)==True:
            mysentdata=str(data)
            mysentdata = mysentdata.encode('utf-8')
        else:
            mysentdata=data
        #print(mysentdata)
        socket.write(mysentdata)
        self.sinOut2.emit("send data:"+str(mysentdata))

    def getUIsenddata(self,data):
        pass
        mystr1=data.split(',')
        mystr1= [int(x)//10*16+int(x)%10 for x in mystr1]
        mystr1=bytes(mystr1)
        self.senddata(self.socket, mystr1)
##########################################
    ##############业务逻辑部分#############
    def myanalyseframe(self,mydata):
        pass
        if isinstance(mydata, str) == True:
            mygetdata = mydata.encode('utf-8')
        elif isinstance(mydata, list) == True:
            mygetdata = bytes(mydata)
        elif isinstance(mydata, int) == True or isinstance(mydata, float) == True:
            mygetdata = str(mydata)
            mygetdata = mygetdata.encode('utf-8')
        else:
            mygetdata=mydata
        mydata1 = mygetdata
        if len(mydata1) != 6:
            pass
            return 0
        if mydata1[0] == 0x10 and mydata1[5] == 0x16:
            myclientid = int(mydata1[2]) + int(mydata1[3]) * 256
            pass
            return myclientid
        else:
            pass
            return 0


mythread=[]
class TcpServer(QTcpServer):#TCPserver服务器端代码

    mytcpsingal1=pyqtSignal(str)
    mytcpsingal2 = pyqtSignal(str)
    mytcpsingal3 = pyqtSignal(str)
    global mythread
    def __init__(self, parent=None):
        super(TcpServer, self).__init__(parent)
        #print('1' )

    def outtext1(self,msg):
        pass
        self.mytcpsingal1.emit(msg)
        #print(msg)
    def outtext2(self,msg):
        pass
        self.mytcpsingal2.emit(msg)
    def outtext3(self,msg):
        pass
        #print("len1={}".format(len(mythread)))
        for xx in range(0,len(mythread))[::-1]:
            if (str(msg) == str(mythread[xx].socketId)):
                del mythread[xx]
                print("del thread1:" + str(xx))
        #print("len1={}".format(len(mythread)))
        self.mytcpsingal3.emit(msg)
    def incomingConnection(self, socketId):

        thread = Thread(socketId, self)
        thread.finished.connect(thread.deleteLater)
        thread.sinOut1.connect(self.outtext1)
        thread.sinOut2.connect(self.outtext2)
        thread.sinOut3.connect(self.outtext3)
        thread.start()
        #print(len(mythread))
        for xx in range(0,len(mythread)):
            pass
            #print(str(thread.socketId))
            #print(str(mythread[xx].socketId))
            if(str(thread.socketId)==str(mythread[xx].socketId)):
                del mythread[xx]
                #print("del thread2:"+str(xx))

        #print(len(mythread))
        mythread.append(thread)


    def getUIdata(self,data):
        pass
        #print(data)
        #thread.getUIsenddata('bcd')
        mystr1=data.split('#')
        for xx in range(0,len(mythread)):
            if str(mystr1[0])==str(mythread[xx].socketId):
                print("T:"+str(mythread[xx].socketId))
                mythread[xx].getUIsenddata(mystr1[1])
            else:
                print("F:" + str(mythread[xx].socketId))




class myUI1(QMainWindow,Ui_myUI1):
    #global mylistWiget
    def __init__(self):
        super(myUI1, self).__init__()
        self.setupUi(self)

        self.LWgetdata=''
        ########################
        self.tcpServer = TcpServer(self)
        self.tcpServer.mytcpsingal1.connect(self.callbacklog1)
        self.tcpServer.mytcpsingal2.connect(self.callbacklog2)
        self.tcpServer.mytcpsingal3.connect(self.callbacklog3)
        if not self.tcpServer.listen(QHostAddress("127.0.0.1"), PORT):
            QMessageBox.critical(self, "Building Services Server",
                                 "Failed to start server: {0}".format(self.tcpServer.errorString()))
            self.close()
            return
    ###########################
    # 在列表中添加连接条目
    def callbacklog1(self, msg):
        #print(msg)
        #print("LWlen01={}".format(len(self.listWidget)))
        mystr2 = msg.split('#')
        for xx in range(0, len(self.listWidget))[::-1]:
            mystr1 = self.listWidget.item(xx).text().split('#')
            if mystr2[0] == mystr1[0]:
                self.listWidget.takeItem(xx)
        self.listWidget.addItem(str(msg))

    #在列表中添加指令
    def callbacklog2(self, msg):
        self.listWidget_2.addItem(str(msg))

    #超时，或者断开连接，删除列表中连接条目
    def callbacklog3(self, msg):
        #print(msg)
        #print("LWlen3={}".format(len(self.listWidget)))
        for xx in range(0,len(self.listWidget))[::-1]:
            mystr1=self.listWidget.item(xx).text().split('#')
            if str(msg)==mystr1[0]:
                self.listWidget.takeItem(xx)
                #print("del item={}".format(xx))
                #print("LWlen4={}".format(len(self.listWidget)))
        self.listWidget_2.addItem(str(msg))#添加指令

    ######################33333
    def bt1_click(self):
        pass
    def bt2_click(self):
        pass
    def bt3_click(self):
        pass
    def bt4_click(self):
        self.tcpServer.getUIdata(self.LWgetdata)
        pass

    def bt5_click(self):#   TCP STOP
        pass
        self.close()
    def bt6_click(self):
        pass
    def LW1_dclick(self):
        pass
        mystr1=self.listWidget.currentItem().text().split('#')
        self.LWgetdata=str(mystr1[0])
        print("LWgetdata:"+self.LWgetdata)

    def bt11_click(self):
        if len(self.LWgetdata)==0:
            QMessageBox.critical(self, "警告","先选取连接条目")
        mysendata1=str(self.LWgetdata)+'#'+self.textEdit_5.toPlainText()
        #print(mysendata1)
        self.tcpServer.getUIdata(mysendata1)
        pass

    def bt12_click(self):
        pass

app = QApplication(sys.argv)
#form = BuildingServicesDlg()
form = myUI1()
form.show()
form.move(0, 0)
app.exec_()