import pymssql
import re
import pandas


class MSSQL:
    def __init__(self,host,user,pwd,db): #类的构造函数，初始化数据库连接ip或者域名，以及用户名，密码，要连接的数据库名称
        self.host=host
        self.user=user
        self.pwd=pwd
        self.db=db
    def __GetConnect(self):  #得到数据库连接信息函数， 返回: conn.cursor()
        if not self.db:
            print(NameError,"没有设置数据库信息")
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
    ms=MSSQL(host="127.0.0.1",user="sa",pwd="ncist123456",db="istudy_p03")  #实例化类对象，连接数据对象
    getdata =ms.ExecQuery("select  * from TB_examescore")
    myrow=len(getdata)
    mycolomn=len(getdata[0])
    print(myrow,mycolomn)
    xx_select1=[]
    xx_word10=[]
    xx_word20 = []
    xx_excel1=[]
    xx_ppt1=[]
    xx_windows1=[]
    for i in range(0,myrow):
        xx1=str(getdata[i][8])
        xx_select1.append(re.findall(r"单项选择题，第\d+套，第\d+题\D+总分\D+\d+\D+得分\D+\d+",xx1))
        xx_word10.append(re.findall(r"Word表格操作，第\d+套，第\d+题\D+总分\D+\d+\D+得分\D+\d+",xx1))
        xx_word20.append(re.findall(r"Word编辑操作，第\d+套，第\d+题\D+总分\D+\d+\D+得分\D+\d+", xx1))
        xx_excel1.append(re.findall(r"Excel题，第\d+套，第\d+题\D+总分\D+\d+\D+得分\D+\d+", xx1))
        xx_ppt1.append(re.findall(r"PowerPoint题，第\d+套，第\d+题\D+总分\D+\d+\D+得分\D+\d+", xx1))
        xx_windows1.append(re.findall(r"Windows题，第\d+套，第\d+题\D+总分\D+\d+\D+得分\D+\d+", xx1))
    print(len(xx_select1),len(xx_select1[0]))
    print(len(xx_word10), len(xx_word10[0]))
    print(len(xx_word20), len(xx_word20[0]))
    print(len(xx_excel1), len(xx_excel1[0]))
    print(len(xx_ppt1), len(xx_ppt1[0]))
    print(len(xx_windows1), len(xx_windows1[0]))
    print("###################")
    print(xx_excel1[100])
    print("###################")


    xx_select2=[]
    xx_word12=[]
    xx_word22=[]
    xx_excel2=[]
    xx_ppt2=[]
    xx_windows2=[]
    for yy in range(0,len(xx_select1)):
        for kk in range(0,len(xx_select1[yy])):
            pass

            t1=re.findall(r"第\d+套",str(xx_select1[yy][kk]))[0]
            t2=re.findall(r"第\d+题",str(xx_select1[yy][kk]))[0]
            t3=re.findall(r"得分\D+\d+",str(xx_select1[yy][kk]))
            t3=t3[0][-1]
            #print(t1,t2,t3)
            t0=[]
            t0.append(t1)
            t0.append(t2)
            t0.append(int(t3))
            #print(t0)
            xx_select2.append(t0)
    for yy in range(0,len(xx_word10)):
        t1 = re.findall(r"第\d+套",str(xx_word10[yy]))
        t2 = re.findall(r"第\d+题", str(xx_word10[yy]))
        t3 = re.findall(r"得分\D+\d+", str(xx_word10[yy]))

        if len(t1)!=0:

            t1=t1[0]
            t2=t2[0]
            t3 = t3[0][-2:]
            t3=int(t3)
            t0 = []
            t0.append(t1)
            #t0.append(t2)
            t0.append(t3)

            xx_word12.append(t0)

##################################
    for yy in range(0,len(xx_word20)):
        t1 = re.findall(r"第\d+套",str(xx_word20[yy]))
        t2 = re.findall(r"第\d+题", str(xx_word20[yy]))
        t3 = re.findall(r"得分\D+\d+", str(xx_word20[yy]))

        if len(t1)!=0:

            t1=t1[0]
            t2=t2[0]
            t3 = t3[0][-2:]
            t3=int(t3)
            t0 = []
            t0.append(t1)
            #t0.append(t2)
            t0.append(t3)
            xx_word22.append(t0)


    for yy in range(0,len(xx_excel1)):

        t1 = re.findall(r"第\d+套",str(xx_excel1[yy]))
        t2 = re.findall(r"第\d+题", str(xx_excel1[yy]))
        t3 = re.findall(r"得分\D+\d+", str(xx_excel1[yy]))

        if len(t1)!=0:

            t1=t1[0]
            t2=t2[0]
            t3 = t3[0][-2:]
            t3=int(t3)
            t0 = []
            t0.append(t1)
            #t0.append(t2)
            t0.append(t3)
            xx_excel2.append(t0)
            #print(t0)
    for yy in range(0,len(xx_ppt1)):

        t1 = re.findall(r"第\d+套",str(xx_ppt1[yy]))
        t2 = re.findall(r"第\d+题", str(xx_ppt1[yy]))
        t3 = re.findall(r"得分\D+\d+", str(xx_ppt1[yy]))

        if len(t1)!=0:

            t1=t1[0]
            t2=t2[0]
            t3 = t3[0][-2:]
            t3=int(t3)
            t0 = []
            t0.append(t1)
            #t0.append(t2)
            t0.append(t3)
            xx_ppt2.append(t0)

    for yy in range(0,len(xx_windows1)):

        t1 = re.findall(r"第\d+套",str(xx_windows1[yy]))
        t2 = re.findall(r"第\d+题", str(xx_windows1[yy]))
        t3 = re.findall(r"得分\D+\d+", str(xx_windows1[yy]))

        if len(t1)!=0:

            t1=t1[0]
            t2=t2[0]
            t3 = t3[0][-2:]
            t3=int(t3)
            t0 = []
            t0.append(t1)
            #t0.append(t2)
            t0.append(t3)
            xx_windows2.append(t0)

    print(xx_select2[100])
    print(xx_word12[100])
    print(xx_word22[100])
    print(xx_excel2[100])
    print(xx_ppt2[100])
    print(xx_windows2[100])

############################
    print("#########################")
    print(xx_word12)




main()