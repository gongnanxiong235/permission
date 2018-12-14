import pymysql
# from config import ConfigUtil as c
from src.util.config import ConfigUtil


class MysqldbHelper(object):
    conf = ConfigUtil()
    host_name = conf.read_config_database('host')
    username_name = conf.read_config_database('username')
    password_name = conf.read_config_database('password')
    port_name = int(conf.read_config_database('port'))
    database_name = conf.read_config_database('database')
    def __init__(self, host=host_name, username=username_name, password=password_name, port=port_name,
                 database=database_name):
        self.host = host
        self.username = username
        self.password = password
        self.database = database
        self.port = port
        self.con = None
        self.cur = None
        try:
            self.con = pymysql.connect(host=self.host, user=self.username, passwd=self.password, port=self.port,
                                       db=self.database)
            # 所有的查询，都在连接 con 的一个模块 cursor 上面运行的
            self.cur = self.con.cursor()
        except:
            raise Exception("DataBase connect error,please check the db config.")

    def close(self):
        """关闭数据库连接

        """
        if  self.con:
            self.con.close()
        else:
            raise Exception("DataBase doesn't connect,close connectiong error;please check the db config.")

    def getVersion(self):
        """获取数据库的版本号

        """
        self.cur.execute("SELECT VERSION()")
        return self.getOneData()

    '''
    返回值：
    1.返回值是元祖:表明查询到了结果
    2.返回值是None：表明没有查询到结果
    3.rtype:返回类型，如果etype=dict 以字典的形式返回查询到的数据，相反则以二维元祖的形式返回数据
    4.type=all  返回全部结果，type=one 只返回第一条结果
    '''

    def executeSelect(self, sql='', args=(), type='all', rtype=''):
        # 执行sql语句，针对读操作返回结果集
        records=""
        if rtype == 'dict':
            self.cur = self.con.cursor(cursor=pymysql.cursors.DictCursor)
        self.cur.execute(sql, args=args)
        print('执行sql语句:', self.cur._last_executed)  # 打印sql语句
        if type == 'one':
            records = self.cur.fetchone()
            print("records:", records)
        else:
            records = self.cur.fetchall()
            print("records:",records)
        return  records


    '''
    针对删改 等操作失败会自动回滚   
    返回值:
    1.None：表明已经执行成功
    '''
    def executeUpDe(self, sql='', args=()):
        try:
            self.cur.execute(sql, args)
            print(self.cur._last_executed)  # 打印sql语句
            self.con.commit()
        except pymysql.Error as e:
            self.con.rollback()
            error = 'MySQL execute failed! ERROR (%s): %s' % (e.args[0], e.args[1])
            print("error:", error)
            raise Exception(error)


    '''
    针对insert 返回主键
    '''
    def executeInsert(self,sql='', args=()):
        self.executeUpDe(sql,args)
        return self.cur.lastrowid



if __name__ == '__main__':
    a=MysqldbHelper().executeSelect("select *from user")
    print(a)