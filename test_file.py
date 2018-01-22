import tkinter
from tkinter import messagebox

import pymssql
import datetime
import matplotlib.pyplot as pl
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
    print(sqlstr)
    myredata=ms.ExecQuery(sqlstr)
    return myredata

def my_fun_displaydata(mygetid2):
    # 从数据库读取数据
    mysql1 = "select * from tb_filename where id= "+str(mygetid2)
    mygetserverdata = my_fun_SQL_readdata(mysql1)
    #print(type(mygetserverdata))
    #print(len(mygetserverdata))
    mystr1 = mygetserverdata[0][4]
    print("mystr1 type=", type(mystr1))
    # print(mystr1)
    mylist3 = mystr1.split('\n')
    # print(mylist3)

    mydtuadd3 = int(mylist3[0])
    ZSQID = int(mylist3[1])
    ZSQTimer = int(mylist3[2])
    mygetdatetime = mylist3[3]

    print(type(mydtuadd3))
    print(mydtuadd3, ZSQID, ZSQTimer)
    print(type(mygetdatetime))
    print(mygetdatetime)

    mygetdata = [float(x) for x in mylist3[4:964]]
    print(type(mygetdata))
    # print(mygetdata)

    # myfont = matplotlib.font_manager.FontProperties(fname=r'C:/Windows/Fonts/msyh.ttf')
    t = mygetdata

    pl.figure(num=2, figsize=(40, 30))
    # pl.subplot(211)
    x0 = []
    x0 = range(0, 960)
    pl.plot(x0, t, label="X0")
    # pl.legend(prop=myfont)
    # pl.xticks(rotation=45)  # 设置时间标签显示格式
    mytitle = "DTU=" + str(mydtuadd3) + "  ZSQ=" + str(ZSQID) + "  Timer=" + str(ZSQTimer) + "  time=" + str(
        mygetdatetime)
    pl.title(mytitle)

    pl.show()





mygetscrolldata='0'
def myprint_item(evet):
    global mygetscrolldata
    #print(mylist1.get(mylist1.curselection()))
    mygetscrolldata=(mylist1.get(mylist1.curselection()))
    #print(mygetscrolldata)

def callback1():
    global mygetscrolldata
    print(mygetscrolldata)
    #print(type(mygetscrolldata))
    mygetid=str(mygetscrolldata).split(",")
    mygetid=int(mygetid[0])
    #print(mygetid)
    try:
        my_fun_displaydata(mygetid)
    except:
        #print("此文件数据没有入库！！")
        messagebox.showwarning("警告","此文件数据没有入库！！")



win=tkinter.Tk()
win.title("波形显示程序")
win.geometry("600x500")



mylb1=tkinter.Label(win,text="文件名称列表")
mylb1.pack

mylb2=tkinter.Label(win,text="使用说明:点击选择左侧列表里面的题目，然后点击“确定”按钮即可")
mylb2.pack(side=tkinter.TOP)

mylb3=tkinter.Label(win,text="       ")
mylb3.pack(side=tkinter.RIGHT)
mylb4=tkinter.Label(win,text="       ")
mylb4.pack(side=tkinter.LEFT)


mybt1=tkinter.Button(win,text="确定")
mybt1.config(command=callback1)
mybt1.pack(side=tkinter.RIGHT)



mylist1=tkinter.Listbox(win)
mylist1.bind('<ButtonRelease-1>',myprint_item)
mylist1.config(width=60)


mysql1="select * from tb_filename order by ID desc "
mygetserverdata=my_fun_SQL_readdata(mysql1)
print(type(mygetserverdata))
print(len(mygetserverdata))
for i in range(0,len(mygetserverdata)):
    mystr0=str(mygetserverdata[i][0])+", "+str(mygetserverdata[i][1])+", "+str(mygetserverdata[i][2])+", "+str(mygetserverdata[i][3])
    #print(mystr0)
    mylist1.insert(i,str(mystr0))

mylist1.pack(side=tkinter.LEFT,fill=tkinter.BOTH)
myscollar=tkinter.Scrollbar(win)
myscollar.pack(side=tkinter.LEFT,fill=tkinter.Y)
myscollar.config(command=mylist1.yview)
mylist1.configure(yscrollcommand=myscollar.set)




win.mainloop()
