import pymssql

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


def my_fun1():
    ms = MSSQL(host="106.14.41.25:3539", user="sa", pwd="NcisT.DKyT_123456", db="DTU_SERVER_NEW")  # 实例化类对象，连接数据对象
    reslist = ms.ExecQuery("SELECT TOP(3) * FROM DTU_CYCLE_DATA_VIEW2 WHERE DTU编号 = '65001' order by id DESC")

    #for id in reslist:  # 遍历返回结果
        #print(id)  # 转换为字符串，打印出来。
    print(str(reslist[0]))
    return str(reslist[0])







from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    s1=my_fun1()
    return s1

if __name__ == '__main__':
    app.run(host="127.0.0.1",port=9000)