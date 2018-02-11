import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QWidget,QFileDialog
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from  PyQt5 import QtCore
from PyQt5.QtGui import QColor,QFont
from PyQt5.QtCore import QTimer,QDateTime

from myUI1 import Ui_MainWindow

from myform1 import Ui_myform1
from myform2 import Ui_myform2
from myform3 import Ui_myform3
from myform4 import Ui_myform4
from myform5 import Ui_myform5

import pymssql
import _mssql
import uuid
import decimal
import matplotlib.pyplot as pl
import xlwt
from datetime import time,datetime

####基础业务逻辑部分=============
class MSSQL:
    def __init__(self, host, user, pwd, db):  # 类的构造函数，初始化数据库连接ip或者域名，以及用户名，密码，要连接的数据库名称
        self.host = host
        self.user = user
        self.pwd = pwd
        self.db = db

    def __GetConnect(self):  # 得到数据库连接信息函数， 返回: conn.cursor()
        if not self.db:
            raise (NameError, "没有设置数据库信息")
        self.conn = pymssql.connect(host=self.host, user=self.user, password=self.pwd, database=self.db, charset='utf8')
        cur = self.conn.cursor()  # 将数据库连接信息，赋值给cur。
        if not cur:
            raise (NameError, "连接数据库失败")
        else:
            return cur

    # 执行查询语句,返回的是一个包含tuple的list，list的元素是记录行，tuple的元素是每行记录的字段
    def ExecQuery(self, sql):  # 执行Sql语句函数，返回结果
        cur = self.__GetConnect()  # 获得数据库连接信息
        cur.execute(sql)  # 执行Sql语句
        resList = cur.fetchall()  # 获得所有的查询结果

        # 查询完毕后必须关闭连接
        self.conn.close()  # 返回查询结果
        return resList

    def ExecNonQuery(self, sql):
        cur = self.__GetConnect()
        cur.execute(sql)
        self.conn.commit()
        self.conn.close()
def my_fun_SQL_readdata(sqlstr):
    # ms=MSSQL(host="120.27.48.70:3538",user="saw",pwd="ncist1525",db="DTU_SERVER")  #实例化类对象，连接数据对象
    ms = MSSQL(host="106.14.41.25:3539", user="sa", pwd="NcisT.DKyT_123456", db="ZSQ_TEST")  # 实例化类对象，连接数据对象[ZSQ_TEST]
    # sqlstr = "insert into TB_cycdata (status,timer,temperature) VALUES (10,11,12)"
    #print(sqlstr)
    myredata=ms.ExecQuery(sqlstr)
    return myredata

myfilename_GL=''
mygetdata_GL=[]
mygetscrolldata='0'
def write_data_to_excel(self,name,data):

    result = data
    # 实例化一个Workbook()对象(即excel文件)
    wbk = xlwt.Workbook()
    # 新建一个名为Sheet1的excel sheet。此处的cell_overwrite_ok =True是为了能对同一个单元格重复操作。
    sheet = wbk.add_sheet('Sheet1',cell_overwrite_ok=True)
    #sheet.write("相序波形")
    sheet.write(0,0,str(result[0]))
    # 遍历result中的每个个元素。
    for i in range(1,len(result)):
        #将每一行的每个元素按行号i,列号j,写入到excel中。
        sheet.write(i,0,result[i])
        # 以传递的name+当前日期作为excel名称保存。
    wbk.save(name+'.xls')
    QMessageBox.information( self,"恭喜！！", name+': '+"文件导出成功")


def my_fun_displaydata(self,mygetid2,myfilename):
    # 从数据库读取数据
    global myfilename_GL
    global mygetdata_GL
    myfilename_GL=myfilename
    mysql1 = "select * from tb_filename where id= "+str(mygetid2)
    mygetserverdata = my_fun_SQL_readdata(mysql1)
    mystr1 = mygetserverdata[0][4]
    mylist3 = mystr1.split('\n')
    mydtuadd3 = int(mylist3[0])
    ZSQID = int(mylist3[1])
    ZSQTimer = int(mylist3[2])
    mygetdatetime = mylist3[3]
    mygetdata = [float(x) for x in mylist3[4:964]]
    if ZSQID == 1 or ZSQID == 2 or ZSQID == 3:
        myaver=float(sum(mygetdata))/len(mygetdata)
        for x in range(0,len(mygetdata)):
            mygetdata[x]=mygetdata[x]-myaver

    mygetdata_GL=mygetdata

    ##数据展示
    self.textEdit_2.setPlainText(
        "ID=" + str(mygetid2) + ' ' + str(mydtuadd3) + ' ' + str(ZSQID) + ' ' + str(mygetdatetime))
    myrow_count = len(mygetdata)
    myclomn_count = 1
    self.tableWidget2.setRowCount(myrow_count)
    self.tableWidget2.setColumnCount(myclomn_count)
    if ZSQID == 1:
        myhead = "A相电流"
    elif ZSQID == 11:
        myhead = "A相电场"
    elif ZSQID == 2:
        myhead = "B相电流"
    elif ZSQID == 12:
        myhead = "B相电场"
    elif ZSQID == 3:
        myhead = "C相电流"
    elif ZSQID == 13:
        myhead = "C相电场"
    else:
        myhead = "未知相"

    mystr0 = [str(myhead)]
    self.tableWidget2.setHorizontalHeaderLabels(mystr0)
    for xx in range(0, myrow_count):
        newitem = QTableWidgetItem(str(mygetdata[xx]))
        self.tableWidget2.setItem(xx, 0, newitem)


    ##########plot画图部分
    t = mygetdata
    pl.figure(num=2, figsize=(6, 4))
    x0 = []
    x0 = range(0, 960)
    pl.plot(x0, t, label="X0")
    mytitle ="ID="+str(mygetid2)+ "  DTU=" + str(mydtuadd3) + "  ZSQ=" + str(ZSQID) + "\nTimer=" + str(ZSQTimer) + "  time=" + str(
        mygetdatetime)
    pl.title(mytitle)
    pl.show()
    #数据保存
    mygetdata_GL.insert(0, str(myhead))












#==界面部分==================

class MainForm(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(MainForm, self).__init__()
        self.setupUi(self)
        self.child1=myform1()
        self.child2 = myform2()
        self.child3 = myform3()
        self.child4 = myform4()
        self.child5 = myform5()
        #按钮对应的动作
        self.action_1.triggered.connect(self.child1show)
        self.action_2.triggered.connect(self.child2show)
        self.action_3.triggered.connect(self.child3show)
        self.action_4.triggered.connect(self.child4show)
        self.action_5.triggered.connect(self.child5show)




    def child1show(self):
        self.gridLayout.addWidget(self.child1)

        #self.setCentralWidget(self.child1)
        self.child1.show()
        self.child2.close()
        self.child3.close()
        self.child4.close()
        self.child5.close()
    def child2show(self):
        self.gridLayout.addWidget(self.child2)
        #self.setCentralWidget(self.child2)
        self.child1.close()
        self.child2.show()
        self.child3.close()
        self.child4.close()
        self.child5.close()

    def child3show(self):
        self.gridLayout.addWidget(self.child3)
        #self.setCentralWidget(self.child2)

        self.child1.close()
        self.child2.close()
        self.child3.show()
        self.child4.close()
        self.child5.close()
    def child4show(self):
        self.gridLayout.addWidget(self.child4)
        #self.setCentralWidget(self.child2)
        self.child1.close()
        self.child2.close()
        self.child3.close()
        self.child4.show()
        self.child5.close()
    def child5show(self):
        self.gridLayout.addWidget(self.child5)
        #self.setCentralWidget(self.child2)
        self.child1.close()
        self.child2.close()
        self.child3.close()
        self.child4.close()
        self.child5.show()



#子窗体1的函数--周期
class myform1(QMainWindow,Ui_myform1):
    def __init__(self):
        super(myform1, self).__init__()
        self.setupUi(self)


        self.timer=QTimer(self)
        self.timer.timeout.connect(self.showTime)
    def showTime(self):
        pass
        time=QDateTime.currentDateTime()
        timeDisplay=time.toString("yyyy-MM-dd hh:mm:ss dddd")
        self.label.setText(timeDisplay)
        self.pushButton.click()

    def bt1_click(self):
        pass
        myid = self.textEdit.toPlainText()
        mynum=self.textEdit_2.toPlainText()
        mysql1 = "select top "+str(mynum)+" * from TB_View_cycdata where dtuid=" + str(myid) + " order by ID DESC "
        mygetserverdata = my_fun_SQL_readdata(mysql1)
        # print(type(mygetserverdata))
        myrow_count = len(mygetserverdata)
        myclomn_count = len(mygetserverdata[0])
        self.tableWidget1.setRowCount(myrow_count)
        self.tableWidget1.setColumnCount(myclomn_count)
        mystr0 = ['ID', 'DTUID', 'status', '服务器时间', 'DTU\n时标', 'A相\n时标', 'B相\n时标', 'C相\n时标', 'A电流', 'B电流', 'C电流', 'A电场', 'B电场',
                  'C电场',
                  'A半波', 'B半波', 'C半波', 'A短路', 'B短路', 'C短路', 'A接地', 'B接地', 'C接地', '报警\n相序', '报警\n时间', 'A\n锂电池', 'B\n锂电池', 'C\n锂电池',
                  'A\n太阳能', 'B\n太阳能', 'C\n太阳能', 'A\n线上电', 'B\n线上电', 'C\n线上电', 'A温度', 'B温度', 'C温度', 'A_timer', 'B_timer', 'C_timer',
                  'DTU\ndatetime', 'DTU\n电池', 'DTU\n太阳能', 'DTU\n温度', 'DTU\n湿度']
        self.tableWidget1.setHorizontalHeaderLabels(mystr0)
        for xx in range(0, myclomn_count):
            self.tableWidget1.setColumnWidth(xx, 80)

        self.tableWidget1.setColumnWidth(3, 200)
        self.tableWidget1.setColumnWidth(40, 200)
        for xx in range(0, myrow_count):
            for yy in range(0, myclomn_count):
                pass
                newitem = QTableWidgetItem(str(mygetserverdata[xx][yy]))
                # newitem.setfont(QFont("Times",8,QFont.Black))
                self.tableWidget1.setItem(xx, yy, newitem)

    def bt2_click(self):
        pass
        myid = self.textEdit.toPlainText()
        mynum = self.textEdit_2.toPlainText()
        mysql1 = "select top " + str(mynum) + " * from TB_View_cycdata  order by ID DESC "
        mygetserverdata = my_fun_SQL_readdata(mysql1)
        # print(type(mygetserverdata))
        myrow_count = len(mygetserverdata)
        myclomn_count = len(mygetserverdata[0])
        self.tableWidget1.setRowCount(myrow_count)
        self.tableWidget1.setColumnCount(myclomn_count)
        mystr0 = ['ID', 'DTUID', 'status', '服务器时间', 'DTU\n时标', 'A相\n时标', 'B相\n时标', 'C相\n时标', 'A电流', 'B电流', 'C电流', 'A电场',
                  'B电场',
                  'C电场',
                  'A半波', 'B半波', 'C半波', 'A短路', 'B短路', 'C短路', 'A接地', 'B接地', 'C接地', '报警\n相序', '报警\n时间', 'A\n锂电池', 'B\n锂电池',
                  'C\n锂电池',
                  'A\n太阳能', 'B\n太阳能', 'C\n太阳能', 'A\n线上电', 'B\n线上电', 'C\n线上电', 'A温度', 'B温度', 'C温度', 'A_timer', 'B_timer',
                  'C_timer',
                  'DTU\ndatetime', 'DTU\n电池', 'DTU\n太阳能', 'DTU\n温度', 'DTU\n湿度']
        self.tableWidget1.setHorizontalHeaderLabels(mystr0)
        for xx in range(0, myrow_count):
            self.tableWidget1.setColumnWidth(xx, 80)

        self.tableWidget1.setColumnWidth(3, 200)
        self.tableWidget1.setColumnWidth(40, 200)
        for xx in range(0, myrow_count):
            for yy in range(0, myclomn_count):
                pass
                newitem = QTableWidgetItem(str(mygetserverdata[xx][yy]))
                # newitem.setfont(QFont("Times",8,QFont.Black))
                self.tableWidget1.setItem(xx, yy, newitem)


    def bt3_click(self):
        pass
        self.timer.start(1000*int(self.textEdit_4.toPlainText()))
        self.pushButton_3.setEnabled(False)
        self.pushButton_4.setEnabled(True)

    def bt4_click(self):  # excel导出
        pass
        self.timer.stop()
        self.pushButton_3.setEnabled(True)
        self.pushButton_4.setEnabled(False)
    def bt5_click(self): #查询特点DTU波形
        pass

    def LW1_dclick(self):
        pass

#子窗体2的函数--录波
class myform2(QMainWindow,Ui_myform2):
    def __init__(self):
        super(myform2, self).__init__()
        self.setupUi(self)
        self.label.setText("（1）点击 《刷新XX》 按钮获得最新的100条数据\n"+
                           "（2）然后单击条目\n"+
                            "(3)最后点击 《确定显示波形》 按钮显示图形\n"+
                           "(4)点击《导出到excel》可以把波形数据导出到excel")
    def bt1_click(self):
        pass
        mysql1 = "select top "+str(self.textEdit_4.toPlainText())+" * from tb_filename where DTUID=" + str(
            self.textEdit_3.toPlainText()) + "order by ID desc "
        mygetserverdata = my_fun_SQL_readdata(mysql1)
        self.listWidget1.clear()
        for i in range(0, len(mygetserverdata)):
            mystr0 = str(mygetserverdata[i][0]) + ", " + str(mygetserverdata[i][1]) + ", " + str(
                mygetserverdata[i][2]) + ", " + str(mygetserverdata[i][3])
            self.listWidget1.addItem(str(mystr0))

    def bt2_click(self):
        pass
        mysql1 = "select top "+str(self.textEdit_4.toPlainText())+" * from tb_filename order by ID desc "
        mygetserverdata = my_fun_SQL_readdata(mysql1)
        self.listWidget1.clear()
        for i in range(0, len(mygetserverdata)):
            mystr0 = str(mygetserverdata[i][0]) + ", " + str(mygetserverdata[i][1]) + ", " + str(
                mygetserverdata[i][2]) + ", " + str(mygetserverdata[i][3])
            self.listWidget1.addItem(str(mystr0))
    def bt3_click(self):
        pass
        global myfilename_GL
        global mygetdata_GL
        try:
            write_data_to_excel(self, myfilename_GL, mygetdata_GL)
        except:
            QMessageBox.information(self, "警告", "没有选择波形文件")
    def bt4_click(self):
        pass
        global mygetscrolldata
        try:
            # self.label.setText("显示曲线")
            mygetdata = str(mygetscrolldata).split(",")
            mygetid = int(mygetdata[0])
            myfilename = str(mygetdata[3])
            # print(mygetid)
            my_fun_displaydata(self, mygetid, myfilename)
        except:
            # print("此文件数据没有入库！！")
            pass
            QMessageBox.information(self, "警告", "没选取波形文件数据")
    def bt5_click(self):
        pass

    def LW1_dclick(self):
        pass
        global mygetscrolldata
        # mygetstr1=self.listWidget1.item(self.listWidget1.currentRow()).text()
        mygetscrolldata = self.listWidget1.currentItem().text()
        self.textEdit1.setText(str(mygetscrolldata))
#子窗体3的函数--信号强度
class myform3(QMainWindow,Ui_myform3):
    def __init__(self):
        super(myform3, self).__init__()
        self.setupUi(self)
    def bt1_click(self):
        pass
        myid = self.textEdit.toPlainText()
        mynum=self.textEdit_2.toPlainText()
        mysql1 = "select top "+str(mynum)+" * from TB_dbm where dtuid=" + str(myid) + " order by ID DESC "
        mygetserverdata = my_fun_SQL_readdata(mysql1)
        # print(type(mygetserverdata))
        myrow_count = len(mygetserverdata)
        myclomn_count = len(mygetserverdata[0])
        self.tableWidget1.setRowCount(myrow_count)
        self.tableWidget1.setColumnCount(myclomn_count)
        mystr0 = ['ID', 'DTUID', '服务器时间', 'GPRS\n信号强度', 'A相\n信号强度', 'B相\n信号强度', 'C相\n信号强度']
        self.tableWidget1.setHorizontalHeaderLabels(mystr0)
        for xx in range(0, myrow_count):
            self.tableWidget1.setColumnWidth(xx, 80)

        self.tableWidget1.setColumnWidth(2, 280)

        for xx in range(0, myrow_count):
            for yy in range(0, myclomn_count):
                pass
                newitem = QTableWidgetItem(str(mygetserverdata[xx][yy]))
                # newitem.setfont(QFont("Times",8,QFont.Black))
                self.tableWidget1.setItem(xx, yy, newitem)

    def bt2_click(self):
        pass
        myid = self.textEdit.toPlainText()
        mynum = self.textEdit_2.toPlainText()
        mysql1 = "select top " + str(mynum) + " * from TB_dbm  order by ID DESC "
        mygetserverdata = my_fun_SQL_readdata(mysql1)
        # print(type(mygetserverdata))
        myrow_count = len(mygetserverdata)
        myclomn_count = len(mygetserverdata[0])
        self.tableWidget1.setRowCount(myrow_count)
        self.tableWidget1.setColumnCount(myclomn_count)
        mystr0 = ['ID', 'DTUID', '服务器时间', 'GPRS\n信号强度', 'A相\n信号强度', 'B相\n信号强度', 'C相\n信号强度']
        self.tableWidget1.setHorizontalHeaderLabels(mystr0)
        for xx in range(0, myrow_count):
            self.tableWidget1.setColumnWidth(xx, 80)

        self.tableWidget1.setColumnWidth(2, 280)

        for xx in range(0, myrow_count):
            for yy in range(0, myclomn_count):
                pass
                newitem = QTableWidgetItem(str(mygetserverdata[xx][yy]))
                # newitem.setfont(QFont("Times",8,QFont.Black))
                self.tableWidget1.setItem(xx, yy, newitem)
#子窗体4函数--12T
class myform4(QMainWindow,Ui_myform4):
    def __init__(self):
        super(myform4, self).__init__()
        self.setupUi(self)
    def bt1_click(self):
        pass
        myid = self.textEdit.toPlainText()
        mynum = self.textEdit_2.toPlainText()
        mystatus=self.textEdit_3.toPlainText()
        if int(mystatus)==1 or int(mystatus)==2:
            mysql1 = "select top " + str(mynum) + " * from TB_AC12T where dtuid=" + str(myid) + " and status="+str(mystatus)+" order by ID DESC "
        else:
            mysql1 = "select top " + str(mynum) + " * from TB_AC12T where dtuid=" + str(myid) + " order by ID DESC "
        mygetserverdata = my_fun_SQL_readdata(mysql1)



        # print(type(mygetserverdata))
        myrow_count = len(mygetserverdata)
        myclomn_count = len(mygetserverdata[0])
        self.tableWidget1.setRowCount(myrow_count)
        self.tableWidget1.setColumnCount(myclomn_count)
        mystr0 = ['ID', 'DTUID','状态', 'ZSQ\nID', '服务器时间','DTU时间','T1', 'T2', 'T3', 'T4', 'T5', 'T6', 'T7', 'T8', 'T9', 'T10', 'T11', 'T12']
        self.tableWidget1.setHorizontalHeaderLabels(mystr0)
        for xx in range(0, myrow_count):
            self.tableWidget1.setColumnWidth(xx, 80)
        self.tableWidget1.setColumnWidth(2, 60)
        self.tableWidget1.setColumnWidth(4, 200)
        self.tableWidget1.setColumnWidth(5, 180)

        for xx in range(0, myrow_count):
            pass
            mystr1=''
            if mygetserverdata[xx][3]//10==1:
                mystr1='A'
            elif mygetserverdata[xx][3]//10==2:
                mystr1 = 'B'
            elif mygetserverdata[xx][3]// 10 == 3:
                mystr1 = 'C'
            else:
                mystr1 = 'X'

            if mygetserverdata[xx][3]%10==1:
                mystr1=mystr1+'电流'
            elif mygetserverdata[xx][3]%10==2:
                mystr1 =mystr1+'电场'
            else:
                mystr1 =mystr1+ '未知'
            mygetserverdata[xx]=list(mygetserverdata[xx])
            mygetserverdata[xx][3] = mystr1


        for xx in range(0, myrow_count):
            for yy in range(0, myclomn_count):
                pass
                newitem = QTableWidgetItem(str(mygetserverdata[xx][yy]))
                # newitem.setfont(QFont("Times",8,QFont.Black))
                self.tableWidget1.setItem(xx, yy, newitem)
    def bt2_click(self):
        pass
        myid = self.textEdit.toPlainText()
        mynum = self.textEdit_2.toPlainText()
        mystatus = self.textEdit_3.toPlainText()
        mysql1 = "select top " + str(mynum) + " * from TB_AC12T  "+" where status="+str(mystatus)+"order by ID DESC "
        mygetserverdata = my_fun_SQL_readdata(mysql1)
        # print(type(mygetserverdata))
        myrow_count = len(mygetserverdata)
        myclomn_count = len(mygetserverdata[0])
        self.tableWidget1.setRowCount(myrow_count)
        self.tableWidget1.setColumnCount(myclomn_count)
        mystr0 = ['ID', 'DTUID', '状态', 'ZSQ\nID', '服务器时间', 'DTU时间', 'T1', 'T2', 'T3', 'T4', 'T5', 'T6', 'T7', 'T8',
                  'T9', 'T10', 'T11', 'T12']
        self.tableWidget1.setHorizontalHeaderLabels(mystr0)
        for xx in range(0, myrow_count):
            self.tableWidget1.setColumnWidth(xx, 80)

        self.tableWidget1.setColumnWidth(2, 60)
        self.tableWidget1.setColumnWidth(4, 200)
        self.tableWidget1.setColumnWidth(5, 180)

        for xx in range(0, myrow_count):
            pass
            mystr1=''
            if mygetserverdata[xx][3]//10==1:
                mystr1='A'
            elif mygetserverdata[xx][3]//10==2:
                mystr1 = 'B'
            elif mygetserverdata[xx][3]// 10 == 3:
                mystr1 = 'C'
            else:
                mystr1 = 'X'

            if mygetserverdata[xx][3]%10==1:
                mystr1=mystr1+'电流'
            elif mygetserverdata[xx][3]%10==2:
                mystr1 =mystr1+'电场'
            else:
                mystr1 =mystr1+ '未知'
            mygetserverdata[xx]=list(mygetserverdata[xx])
            mygetserverdata[xx][3] = mystr1

        for xx in range(0, myrow_count):
            for yy in range(0, myclomn_count):
                pass
                newitem = QTableWidgetItem(str(mygetserverdata[xx][yy]))
                # newitem.setfont(QFont("Times",8,QFont.Black))
                self.tableWidget1.setItem(xx, yy, newitem)
#子船体5函数--报警

class myform5(QMainWindow,Ui_myform5):
    def __init__(self):
        super(myform5, self).__init__()
        self.setupUi(self)
        self.timer=QTimer(self)
        self.timer.timeout.connect(self.showTime)
        self.dateTimeEdit_1.setDateTime(QDateTime.currentDateTime().addDays(-1))
        self.dateTimeEdit_2.setDateTime(QDateTime.currentDateTime())
    def showTime(self):
        pass
        time=QDateTime.currentDateTime()
        timeDisplay=time.toString("yyyy-MM-dd hh:mm:ss dddd")
        self.label.setText(timeDisplay)
        self.pushButton.click()
    def bt1_click(self):
        pass
        myid = self.textEdit.toPlainText()
        mynum=self.textEdit_2.toPlainText()
        mystatus=self.textEdit_3.toPlainText()
        #######周期部分##########
        mysql1 = "select top "+str(mynum)+" * from TB_View_cycdata where dtuid=" + str(myid) +" and status="+str(mystatus) +" order by ID DESC "
        mygetserverdata = my_fun_SQL_readdata(mysql1)
        # print(type(mygetserverdata))
        myrow_count = len(mygetserverdata)
        myclomn_count = len(mygetserverdata[0])
        self.tableWidget1.setRowCount(myrow_count)
        self.tableWidget1.setColumnCount(myclomn_count)
        mystr0 = ['ID', 'DTUID', 'status', '服务器时间', 'DTU\n时标', 'A相\n时标', 'B相\n时标', 'C相\n时标', 'A电流', 'B电流', 'C电流', 'A电场', 'B电场',
                  'C电场',
                  'A半波', 'B半波', 'C半波', 'A短路', 'B短路', 'C短路', 'A接地', 'B接地', 'C接地', '报警\n相序', '报警\n时间', 'A\n锂电池', 'B\n锂电池', 'C\n锂电池',
                  'A\n太阳能', 'B\n太阳能', 'C\n太阳能', 'A\n线上电', 'B\n线上电', 'C\n线上电', 'A温度', 'B温度', 'C温度', 'A_timer', 'B_timer', 'C_timer',
                  'DTU\ndatetime', 'DTU\n电池', 'DTU\n太阳能', 'DTU\n温度', 'DTU\n湿度']
        self.tableWidget1.setHorizontalHeaderLabels(mystr0)
        for xx in range(0, myclomn_count):
            self.tableWidget1.setColumnWidth(xx, 80)

        self.tableWidget1.setColumnWidth(3, 200)
        self.tableWidget1.setColumnWidth(40, 200)
        for xx in range(0, myrow_count):
            for yy in range(0, myclomn_count):
                pass
                newitem = QTableWidgetItem(str(mygetserverdata[xx][yy]))
                # newitem.setfont(QFont("Times",8,QFont.Black))
                self.tableWidget1.setItem(xx, yy, newitem)
        ############12T部分#############
        if int(mystatus)==1 or int(mystatus)==2:
            mysql1 = "select top " + str(int(mynum)*6) + " * from TB_AC12T where dtuid=" + str(myid) + " and status="+str(mystatus)+" order by ID DESC "
        else:
            mysql1 = "select top " + str(int(mynum)*6) + " * from TB_AC12T where dtuid=" + str(myid) + " order by ID DESC "
        mygetserverdata = my_fun_SQL_readdata(mysql1)

        myrow_count = len(mygetserverdata)
        myclomn_count = len(mygetserverdata[0])
        self.tableWidget1_2.setRowCount(myrow_count)
        self.tableWidget1_2.setColumnCount(myclomn_count)
        mystr0 = ['ID', 'DTUID','状态', 'ZSQ\nID', '服务器时间','DTU时间','T1', 'T2', 'T3', 'T4', 'T5', 'T6', 'T7', 'T8', 'T9', 'T10', 'T11', 'T12']
        self.tableWidget1_2.setHorizontalHeaderLabels(mystr0)
        for xx in range(0, myrow_count):
            self.tableWidget1_2.setColumnWidth(xx, 80)
        self.tableWidget1_2.setColumnWidth(2, 60)
        self.tableWidget1_2.setColumnWidth(4, 200)
        self.tableWidget1_2.setColumnWidth(5, 180)

        for xx in range(0, myrow_count):
            pass
            mystr1=''
            if mygetserverdata[xx][3]//10==1:
                mystr1='A'
            elif mygetserverdata[xx][3]//10==2:
                mystr1 = 'B'
            elif mygetserverdata[xx][3]// 10 == 3:
                mystr1 = 'C'
            else:
                mystr1 = 'X'

            if mygetserverdata[xx][3]%10==1:
                mystr1=mystr1+'电流'
            elif mygetserverdata[xx][3]%10==2:
                mystr1 =mystr1+'电场'
            else:
                mystr1 =mystr1+ '未知'
            mygetserverdata[xx]=list(mygetserverdata[xx])
            mygetserverdata[xx][3] = mystr1


        for xx in range(0, myrow_count):
            for yy in range(0, myclomn_count):
                pass
                newitem = QTableWidgetItem(str(mygetserverdata[xx][yy]))
                # newitem.setfont(QFont("Times",8,QFont.Black))
                self.tableWidget1_2.setItem(xx, yy, newitem)

    def bt2_click(self):
        pass
        myid = self.textEdit.toPlainText()
        mynum = self.textEdit_2.toPlainText()
        mystatus = self.textEdit_3.toPlainText()

        mysql1 = "select top " + str(mynum) + " * from TB_View_cycdata "+ " where status="+str(mystatus) +" order by ID DESC "
        mygetserverdata = my_fun_SQL_readdata(mysql1)
        # print(type(mygetserverdata))
        myrow_count = len(mygetserverdata)
        myclomn_count = len(mygetserverdata[0])
        self.tableWidget1.setRowCount(myrow_count)
        self.tableWidget1.setColumnCount(myclomn_count)
        mystr0 = ['ID', 'DTUID', 'status', '服务器时间', 'DTU\n时标', 'A相\n时标', 'B相\n时标', 'C相\n时标', 'A电流', 'B电流', 'C电流', 'A电场',
                  'B电场',
                  'C电场',
                  'A半波', 'B半波', 'C半波', 'A短路', 'B短路', 'C短路', 'A接地', 'B接地', 'C接地', '报警\n相序', '报警\n时间', 'A\n锂电池', 'B\n锂电池',
                  'C\n锂电池',
                  'A\n太阳能', 'B\n太阳能', 'C\n太阳能', 'A\n线上电', 'B\n线上电', 'C\n线上电', 'A温度', 'B温度', 'C温度', 'A_timer', 'B_timer',
                  'C_timer',
                  'DTU\ndatetime', 'DTU\n电池', 'DTU\n太阳能', 'DTU\n温度', 'DTU\n湿度']
        self.tableWidget1.setHorizontalHeaderLabels(mystr0)
        for xx in range(0, myrow_count):
            self.tableWidget1.setColumnWidth(xx, 80)

        self.tableWidget1.setColumnWidth(3, 200)
        self.tableWidget1.setColumnWidth(40, 200)
        for xx in range(0, myrow_count):
            for yy in range(0, myclomn_count):
                pass
                newitem = QTableWidgetItem(str(mygetserverdata[xx][yy]))
                # newitem.setfont(QFont("Times",8,QFont.Black))
                self.tableWidget1.setItem(xx, yy, newitem)
####################12T##########
        mysql1 = "select top " + str(int(mynum)*6) + " * from TB_AC12T  " + " where status=" + str(
            mystatus) + "order by ID DESC "
        mygetserverdata = my_fun_SQL_readdata(mysql1)
        # print(type(mygetserverdata))
        myrow_count = len(mygetserverdata)
        myclomn_count = len(mygetserverdata[0])
        self.tableWidget1_2.setRowCount(myrow_count)
        self.tableWidget1_2.setColumnCount(myclomn_count)
        mystr0 = ['ID', 'DTUID', '状态', 'ZSQ\nID', '服务器时间', 'DTU时间', 'T1', 'T2', 'T3', 'T4', 'T5', 'T6', 'T7', 'T8',
                  'T9', 'T10', 'T11', 'T12']
        self.tableWidget1_2.setHorizontalHeaderLabels(mystr0)
        for xx in range(0, myrow_count):
            self.tableWidget1_2.setColumnWidth(xx, 80)

        self.tableWidget1_2.setColumnWidth(2, 60)
        self.tableWidget1_2.setColumnWidth(4, 200)
        self.tableWidget1_2.setColumnWidth(5, 180)

        for xx in range(0, myrow_count):
            pass
            mystr1 = ''
            if mygetserverdata[xx][3] // 10 == 1:
                mystr1 = 'A'
            elif mygetserverdata[xx][3] // 10 == 2:
                mystr1 = 'B'
            elif mygetserverdata[xx][3] // 10 == 3:
                mystr1 = 'C'
            else:
                mystr1 = 'X'

            if mygetserverdata[xx][3] % 10 == 1:
                mystr1 = mystr1 + '电流'
            elif mygetserverdata[xx][3] % 10 == 2:
                mystr1 = mystr1 + '电场'
            else:
                mystr1 = mystr1 + '未知'
            mygetserverdata[xx] = list(mygetserverdata[xx])
            mygetserverdata[xx][3] = mystr1

        for xx in range(0, myrow_count):
            for yy in range(0, myclomn_count):
                pass
                newitem = QTableWidgetItem(str(mygetserverdata[xx][yy]))
                # newitem.setfont(QFont("Times",8,QFont.Black))
                self.tableWidget1_2.setItem(xx, yy, newitem)

    def bt3_click(self):
        pass
        self.timer.start(1000*int(self.textEdit_4.toPlainText()))
        self.pushButton_3.setEnabled(False)
        self.pushButton_4.setEnabled(True)

    def bt4_click(self):  #
        pass
        self.timer.stop()
        self.pushButton_3.setEnabled(True)
        self.pushButton_4.setEnabled(False)
    def bt5_click(self):
        pass
        myid = self.textEdit.toPlainText()
        mynum = self.textEdit_2.toPlainText()
        mystatus = self.textEdit_3.toPlainText()
        mydatetime1=self.dateTimeEdit_1.dateTime()
        mydatetime2 = self.dateTimeEdit_2.dateTime()
        mydatetime1=QDateTime(mydatetime1).toString("yyyy-MM-dd hh:mm:ss")
        mydatetime2 = QDateTime(mydatetime2).toString("yyyy-MM-dd hh:mm:ss")
        #######周期部分##########
        mysql1 = "select * from TB_View_cycdata where  CONVERT(varchar(16), 服务器时间, 20)>=\'"+\
                str(mydatetime1) +\
                "\' and CONVERT(varchar(16), 服务器时间, 20)<=\'"+ \
                 str(mydatetime2) +\
                 "\' and DTUID="+str(myid)+" and status="+str(mystatus)+" order by id desc "
        print(mysql1)
        mygetserverdata = my_fun_SQL_readdata(mysql1)
        # print(type(mygetserverdata))
        myrow_count = len(mygetserverdata)
        if myrow_count==0:
            QMessageBox.information(self, "警告！！", "当前查询条件没有数据！")
            return
        myclomn_count = len(mygetserverdata[0])


        self.tableWidget1.setRowCount(myrow_count)
        self.tableWidget1.setColumnCount(myclomn_count)
        mystr0 = ['ID', 'DTUID', 'status', '服务器时间', 'DTU\n时标', 'A相\n时标', 'B相\n时标', 'C相\n时标', 'A电流', 'B电流', 'C电流', 'A电场',
                  'B电场',
                  'C电场',
                  'A半波', 'B半波', 'C半波', 'A短路', 'B短路', 'C短路', 'A接地', 'B接地', 'C接地', '报警\n相序', '报警\n时间', 'A\n锂电池', 'B\n锂电池',
                  'C\n锂电池',
                  'A\n太阳能', 'B\n太阳能', 'C\n太阳能', 'A\n线上电', 'B\n线上电', 'C\n线上电', 'A温度', 'B温度', 'C温度', 'A_timer', 'B_timer',
                  'C_timer',
                  'DTU\ndatetime', 'DTU\n电池', 'DTU\n太阳能', 'DTU\n温度', 'DTU\n湿度']
        self.tableWidget1.setHorizontalHeaderLabels(mystr0)
        for xx in range(0, myclomn_count):
            self.tableWidget1.setColumnWidth(xx, 80)

        self.tableWidget1.setColumnWidth(3, 200)
        self.tableWidget1.setColumnWidth(40, 200)
        for xx in range(0, myrow_count):
            for yy in range(0, myclomn_count):
                pass
                newitem = QTableWidgetItem(str(mygetserverdata[xx][yy]))
                # newitem.setfont(QFont("Times",8,QFont.Black))
                self.tableWidget1.setItem(xx, yy, newitem)
        ############12T部分#############


        if int(mystatus) == 1 or int(mystatus) == 2:
            mysql1 = "select * from TB_AC12T where dtuid=" + str(myid) + " and status=" + str(mystatus) + \
                     "and CONVERT(varchar(16), serverdatetime, 20)>=\'"+\
                    str(mydatetime1) +\
                    "\' and CONVERT(varchar(16), serverdatetime, 20)<=\'"+ \
                    str(mydatetime2) +\
                     "\' order by ID DESC "
        else:
            mysql1 = "select top " + str(int(mynum) * 6) + " * from TB_AC12T where dtuid=" + str(
                myid) + " order by ID DESC "
        print(mysql1)
        mygetserverdata = my_fun_SQL_readdata(mysql1)

        myrow_count = len(mygetserverdata)
        myclomn_count = len(mygetserverdata[0])
        self.tableWidget1_2.setRowCount(myrow_count)
        self.tableWidget1_2.setColumnCount(myclomn_count)
        mystr0 = ['ID', 'DTUID', '状态', 'ZSQ\nID', '服务器时间', 'DTU时间', 'T1', 'T2', 'T3', 'T4', 'T5', 'T6', 'T7', 'T8',
                  'T9', 'T10', 'T11', 'T12']
        self.tableWidget1_2.setHorizontalHeaderLabels(mystr0)
        for xx in range(0, myrow_count):
            self.tableWidget1_2.setColumnWidth(xx, 80)
        self.tableWidget1_2.setColumnWidth(2, 60)
        self.tableWidget1_2.setColumnWidth(4, 200)
        self.tableWidget1_2.setColumnWidth(5, 180)

        for xx in range(0, myrow_count):
            pass
            mystr1 = ''
            if mygetserverdata[xx][3] // 10 == 1:
                mystr1 = 'A'
            elif mygetserverdata[xx][3] // 10 == 2:
                mystr1 = 'B'
            elif mygetserverdata[xx][3] // 10 == 3:
                mystr1 = 'C'
            else:
                mystr1 = 'X'

            if mygetserverdata[xx][3] % 10 == 1:
                mystr1 = mystr1 + '电流'
            elif mygetserverdata[xx][3] % 10 == 2:
                mystr1 = mystr1 + '电场'
            else:
                mystr1 = mystr1 + '未知'
            mygetserverdata[xx] = list(mygetserverdata[xx])
            mygetserverdata[xx][3] = mystr1

        for xx in range(0, myrow_count):
            for yy in range(0, myclomn_count):
                pass
                newitem = QTableWidgetItem(str(mygetserverdata[xx][yy]))
                # newitem.setfont(QFont("Times",8,QFont.Black))
                self.tableWidget1_2.setItem(xx, yy, newitem)





if __name__=="__main__":
    app=QApplication(sys.argv)
    win=MainForm()
    #win=myform1()
    win.show()
    sys.exit(app.exec_())