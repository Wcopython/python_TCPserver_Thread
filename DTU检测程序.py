import pymssql
import numpy as np
#import pylab as pl
import matplotlib # 注意这个也要import一次
import matplotlib.pyplot as pl
import matplotlib.font_manager as fm
myfont = matplotlib.font_manager.FontProperties(fname=r'C:/Windows/Fonts/msyh.ttf')


print("使用mssqlserver的方法1")
class MSSQL:
    def __init__(self,host,user,pwd,db): #类的构造函数，初始化数据库连接ip或者域名，以及用户名，密码，要连接的数据库名称
        self.host=host
        self.user=user
        self.pwd=pwd
        self.db=db
    def __GetConnect(self):  #得到数据库连接信息函数， 返回: conn.cursor()
        if not self.db:
            rasie(NameError,"没有设置数据库信息")
        self.conn=pymssql.connect(host=self.host,user=self.user,password=self.pwd,database=self.db,charset='utf8')
        cur=self.conn.cursor()  #将数据库连接信息，赋值给cur。
        if not cur:
            raise(NameError,"连接数据库失败")
        else:
            return cur

    #执行查询语句,返回的是一个包含tuple的list，list的元素是记录行，tuple的元素是每行记录的字段
    def ExecQuery(self,sql):  #执行Sql语句函数，返回结果
        cur = self.__GetConnect()   #获得数据库连接信息
        cur.execute(sql)  #执行Sql语句
        resList = cur.fetchall()  #获得所有的查询结果

        #查询完毕后必须关闭连接
        self.conn.close()   #返回查询结果
        return resList
    def ExecNonQuery(self,sql):
        cur = self.__GetConnect()
        cur.execute(sql)
        self.conn.commit()
        self.conn.close()

def main():
    ms=MSSQL(host="120.27.48.70:3538",user="saw",pwd="ncist1525",db="DTU_SERVER")  #实例化类对象，连接数据对象
    timestr='服务器时间'
    str0='太阳能电压'        #'B相电流'  太阳能电压
    str1='电池电压'          #'B相电场' 电池电压
    str11='A相电流'
    str12='A相电场'
    str21 = 'B相电流'
    str22 = 'B相电场'
    str31 = 'C相电流'
    str32 = 'C相电场'
    DTU_add='08001'
    count_num='1000'

    sqlstr="SELECT TOP("+count_num+") "+timestr+','+str0+","+str1 +','+str11+','+str12+','+str21+','+str22+','+str31+','+str32+" FROM DTU_CYCLE_DATA_VIEW2 WHERE DTU编号 = "+DTU_add +" order by id DESC"
    print(sqlstr)
    reslist = ms.ExecQuery(sqlstr)

    #for id in reslist:     #遍历返回结果
        #print(id)        #转换为字符串，打印出来。
    print(type(reslist))
    y=reslist
    x_time=[]
    x0=[]
    x1=[]
    ZSQ11=[]
    ZSQ12=[]
    ZSQ21=[]
    ZSQ22=[]
    ZSQ31=[]
    ZSQ32=[]
    for i in y:
        if i[2]>50 or i[3]==None:
            print(str(i[0])[0:19], i[1], i[2],i[3],i[4],i[5],i[6],i[7],i[8])

        elif i[2]>0:
            x_time.append(str(i[0])[0:19])
            x0.append(float(i[1]))
            x1.append(float(i[2]))

            ZSQ11.append(float(i[3]))
            ZSQ12.append(float(i[4]))
            ZSQ21.append(float(i[5]))
            ZSQ22.append(float(i[6]))
            ZSQ31.append(float(i[7]))
            ZSQ32.append(float(i[8]))



        else:
            print(str(i[0])[0:19], i[1], i[2])

    x0=x0[::-1]
    x1=x1[::-1]
    #print(x0,x1)
    count=len(x0)
    print(count)

    myfont = matplotlib.font_manager.FontProperties(fname=r'C:/Windows/Fonts/msyh.ttf')
    t = np.arange(0, count, 1)
    pl.figure(num=4,figsize=(30,40))
    pl.subplot(411)
    pl.plot(t, x0, label=str0)
    pl.legend(prop=myfont)
    # pl.xticks(rotation=45)  # 设置时间标签显示格式
    pl.title(x_time[-1] + ' 到 ' + x_time[0] + '  DTU=' + DTU_add + ',数量=' + str(len(x0)) + '/' + count_num,fontproperties=myfont)

    pl.subplot(412)
    pl.plot(t, x1, label=str1)

    pl.legend(prop=myfont)
    #pl.xticks(rotation=45)  # 设置时间标签显示格式
    #pl.title(x_time[-1] + ' 到 ' + x_time[0] + '  图形=' + DTU_add + ',数量=' + str(len(x0)) + '/' + count_num,fontproperties=myfont)
    pl.subplot(413)
    pl.plot(t, ZSQ11, label=str11)
    pl.plot(t, ZSQ21, label=str21)
    pl.plot(t, ZSQ31, label=str31)
    pl.legend(prop=myfont)

    pl.subplot(414)
    pl.plot(t, ZSQ12, label=str12)
    pl.plot(t, ZSQ22, label=str22)
    pl.plot(t, ZSQ32, label=str32)
    pl.legend(prop=myfont)

    pl.show()

main()