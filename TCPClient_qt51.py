from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from  PyQt5 import QtCore
from PyQt5.QtGui import QColor,QFont
from demo3 import Ui_Form
import pymssql
import _mssql
import uuid
import decimal
import matplotlib.pyplot as pl
import xlwt

#############excel############

myfilename_GL=''
mygetdata_GL=[]


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


########################
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
        myhead = "A相电电场"
    elif ZSQID == 2:
        myhead = "B相电电场"
    elif ZSQID == 12:
        myhead = "B相电电场"
    elif ZSQID == 3:
        myhead = "C相电电场"
    elif ZSQID == 13:
        myhead = "C相电电场"
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












##########################33
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



class mywindow(QtWidgets.QWidget,Ui_Form):
    def __init__(self):
        super(mywindow,self).__init__()
        self.setupUi(self)

    def bt1_click(self):  # 定义槽函数btn_click(),也可以理解为重载类Ui_MainWindow中的槽函数btn_click()
        #self.label.setText("点击 刷新 按钮获得最新的100条数据，然后单击条目，最后后点击 确定 按钮显示图形")
        mysql1 = "select top 100 * from tb_filename order by ID desc "
        mygetserverdata = my_fun_SQL_readdata(mysql1)
        self.listWidget1.clear()
        for i in range(0, len(mygetserverdata)):
            mystr0 = str(mygetserverdata[i][0]) + ", " + str(mygetserverdata[i][1]) + ", " + str(
                mygetserverdata[i][2]) + ", " + str(mygetserverdata[i][3])
            self.listWidget1.addItem(str(mystr0))
            #mylist1.insert(i, str(mystr0))
    def bt2_click(self):  # 定义槽函数btn_click(),也可以理解为重载类Ui_MainWindow中的槽函数btn_click()
        global mygetscrolldata
        try:
            #self.label.setText("显示曲线")
            mygetdata= str(mygetscrolldata).split(",")
            mygetid = int(mygetdata[0])
            myfilename=str(mygetdata[3])
            # print(mygetid)
            my_fun_displaydata(self,mygetid,myfilename)
        except:
            # print("此文件数据没有入库！！")
            pass
            QMessageBox.information(self, "警告", "没选取波形文件数据")

    def LW1_dclick(self):
        global mygetscrolldata
        #mygetstr1=self.listWidget1.item(self.listWidget1.currentRow()).text()
        mygetscrolldata=self.listWidget1.currentItem().text()
        self.textEdit1.setText(str(mygetscrolldata))
    def bt3_click(self):
        pass
        myid=self.textEdit.toPlainText()


        print(myid)

        mysql1 = "select top 100 * from TB_View_cycdata where dtuid="+str(myid)+" order by ID DESC "
        mygetserverdata = my_fun_SQL_readdata(mysql1)
        #print(type(mygetserverdata))
        myrow_count=len(mygetserverdata)
        myclomn_count=len(mygetserverdata[0])
        self.tableWidget1.setRowCount(myrow_count)
        self.tableWidget1.setColumnCount(myclomn_count)
        mystr0 = ['ID','DTUID', 'status', '服务器时间', 'DTU时标', 'A相时标', 'B相时标', 'C相时标', 'A电流', 'B电流', 'C电流', 'A电场', 'B电场', 'C电场',
                  'A半波', 'B半波', 'C半波', 'A短路', 'B短路', 'C短路', 'A接地', 'B接地', 'C接地', '报警相序', '报警时间', 'A锂电池', 'B锂电池', 'C锂电池',
                  'A太阳能', 'B太阳能', 'C太阳能', 'A线上电', 'B线上电', 'C线上电', 'A温度', 'B温度', 'C温度', 'A_timer', 'B_timer', 'C_timer',
                  'DTUdatetime', 'DTU电池', 'DTU太阳能', 'DTU温度', 'DTU湿度']
        self.tableWidget1.setHorizontalHeaderLabels(mystr0)
        for xx in range(0,myrow_count):
            self.tableWidget1.setColumnWidth(xx,100)
        #self.tableWidget1.setHorizontalHeaderLabels(['姓名','性别','体重'])
        for xx in range(0,myrow_count):
            for yy in range(0,myclomn_count):
                pass
                newitem=QTableWidgetItem(str(mygetserverdata[xx][yy]))
                #newitem.setfont(QFont("Times",8,QFont.Black))
                self.tableWidget1.setItem(xx,yy,newitem)


    def bt4_click(self): #excel导出

        pass
        global myfilename_GL
        global mygetdata_GL
        try:
            write_data_to_excel(self,myfilename_GL,mygetdata_GL)
        except:
            QMessageBox.information(self, "警告", "没有选择波形文件")

    def bt5_click(self): #查询特点DTU波形
        pass
        mysql1 = "select top 100 * from tb_filename where DTUID="+str(self.textEdit_3.toPlainText())+"order by ID desc "
        mygetserverdata = my_fun_SQL_readdata(mysql1)
        self.listWidget1.clear()
        for i in range(0, len(mygetserverdata)):
            mystr0 = str(mygetserverdata[i][0]) + ", " + str(mygetserverdata[i][1]) + ", " + str(
                mygetserverdata[i][2]) + ", " + str(mygetserverdata[i][3])
            self.listWidget1.addItem(str(mystr0))




if __name__=="__main__":
    import sys

    app=QtWidgets.QApplication(sys.argv)
    myshow=mywindow()
    myshow.label.setText("（1）点击 《刷新XX》 按钮获得最新的100条数据,（2）然后单击条目,(3)最后点击 《确定显示波形》 按钮显示图形。(4)点击《导出到excel》可以把波形数据导出到excel")
    myshow.setWindowTitle("波形显示软件20180130V3")

    myshow.show()
    sys.exit(app.exec_())
