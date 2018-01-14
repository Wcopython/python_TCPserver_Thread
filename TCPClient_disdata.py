import pymssql
import datetime
import matplotlib.pyplot as pl

#########################3
def my_str_to_hex_display(s):
    # s2 = bytes(s, 'utf-8')
    if s == None:
        return
    print(datetime.datetime.now(), ": ", end='')
    s2 = s
    for i in s2:
        print(hex(i), end='')
        if i != s2[-1]:
            print('-', end='')
    print()

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

def my_fun_SQL_insertdata(sqlstr):
    # ms=MSSQL(host="120.27.48.70:3538",user="saw",pwd="ncist1525",db="DTU_SERVER")  #实例化类对象，连接数据对象
    ms = MSSQL(host="106.14.41.25:3539", user="sa", pwd="NcisT.DKyT_123456", db="ZSQ_TEST")  # 实例化类对象，连接数据对象[ZSQ_TEST]
    # sqlstr = "insert into TB_cycdata (status,timer,temperature) VALUES (10,11,12)"
    print(sqlstr)
    ms.ExecNonQuery(sqlstr)

def my_fun_SQL_readdata(sqlstr):
    # ms=MSSQL(host="120.27.48.70:3538",user="saw",pwd="ncist1525",db="DTU_SERVER")  #实例化类对象，连接数据对象
    ms = MSSQL(host="106.14.41.25:3539", user="sa", pwd="NcisT.DKyT_123456", db="ZSQ_TEST")  # 实例化类对象，连接数据对象[ZSQ_TEST]
    # sqlstr = "insert into TB_cycdata (status,timer,temperature) VALUES (10,11,12)"
    print(sqlstr)
    myredata=ms.ExecQuery(sqlstr)
    return myredata

#从数据库获取数据
mysql1="select * from tb_filename order by ID desc "
mygetserverdata=my_fun_SQL_readdata(mysql1)
print(type(mygetserverdata))
print(len(mygetserverdata))


#对数据进行处理
mystr1=mygetserverdata[0][4]
print("mystr1 type=",type(mystr1))
#print(mystr1)
mylist3=mystr1.split('\n')
#print(mylist3)

mydtuadd3=int(mylist3[0])
ZSQID=int(mylist3[1])
ZSQTimer=int(mylist3[2])
mygetdatetime=mylist3[3]

print(type(mydtuadd3))
print(mydtuadd3,ZSQID,ZSQTimer)
print(type(mygetdatetime))
print(mygetdatetime)

mygetdata=[float(x) for x in mylist3[4:964] ]
print(type(mygetdata))
#print(mygetdata)

#myfont = matplotlib.font_manager.FontProperties(fname=r'C:/Windows/Fonts/msyh.ttf')
t = mygetdata

pl.figure(num=2, figsize=(40, 30))
#pl.subplot(211)
x0=[]
x0=range(0,960)
pl.plot(x0, t, label="X0")
#pl.legend(prop=myfont)
# pl.xticks(rotation=45)  # 设置时间标签显示格式
mytitle="DTU="+str(mydtuadd3)+"  ZSQ="+str(ZSQID)+"  Timer="+str(ZSQTimer)+"  time="+str(mygetdatetime)
pl.title(mytitle)

pl.show()




