import pymysql

class SQLite():

    def __init__(self,dict1={},dict2={}):
        self.dict1 = dict1
        self.dict2 = dict2
        self.connect_sql()


    def connect_sql(self):
        # 创建mysql连接
        global cursor,db
        db = pymysql.connect(host='1.117.156.220',
                            port=5006,
                            user='admin',
                            passwd='pass12345',
                            db='pic',
                            charset='utf8',
                            autocommit=True)

        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()
        print("数据库连接成功！")

    def create_table(self):
        # 删除已经存在的表
        sqla = """DROP TABLE IF EXISTS main"""
        cursor.execute(sqla)

        # 创建表
        sql="""CREATE TABLE IF NOT EXISTS main (
                  ID  INT,
                  SIM  FLOAT )"""
        # 运行sql语句
        cursor.execute(sql)
        print("数据库表创建成功！")

    def insert_data(self):
        for i in self.dict1:
            sql = """INSERT INTO main (ID,SIM) VALUES ({},{})""".format(i,self.dict1[i])
            cursor.execute(sql)
        print("数据创建成功！")


    def open_data(self):
        result2 = {}
        sql = """SELECT  *  FROM main order by SIM desc """
        cursor.execute(sql)
        data = cursor.fetchall()
        for i in data[0:6]:
            result2[str(i[0])] = round(i[1]*100,4)
        print(result2)
        return result2

    def close_sql(self):
        # 关闭数据库连接
        db.close()