# 导入pymysql模块
import pymysql
from datetime import datetime,timedelta
from dateutil.relativedelta import relativedelta

from WWDBTest.util.myLogs import MyLogs   #导入日志


class GetBeforeTime():
    def getNowTime(self):
        now_time = datetime.now()
        print("当前时间：%s" % now_time)
        return now_time

    def getBeforeTime(self,time_str, years=0, months=0, days=0, hours=0, minutes=0, seconds=0):
        if type(time_str) == str:
            time_str = datetime.strptime(time_str, '%Y-%m-%d %H:%M:%S')

        ret = time_str + relativedelta(years=years, months=months, days=days, hours=hours, minutes=minutes,
                                       seconds=seconds)
        return ret

    def run(self,years=0, months=0, days=0, hours=0, minutes=0, seconds=0):
        now_time = self.getNowTime()
        ret2 = self.getBeforeTime(now_time,years=years, months=months, days=days, hours=hours, minutes=minutes,
                                       seconds=seconds)
        print("结果时间:%s" % ret2)
        return  ret2

    def runGetBeforeOneWeekTime(self):
        before_two_weeks = self.run(days=-7)
        before_two_weeks_str = str(before_two_weeks)
        before_two_weeks_str_list = before_two_weeks_str.split(" ")
        before_two_weeks_str_day = before_two_weeks_str_list[0]
        print("before_one_week_str_day:%s" % before_two_weeks_str_day)
        return before_two_weeks_str_day


class OperationMyDB(object):
    def  __init__(self,db_host=None,db_port=None,db_user=None,db_password=None,db_database=None,db_charset=None,
                  db_biao=None, db_ziduan=None, db_xiugaiqiandezhi=None, db_xiugaihoudezhi=None,
                  db_tiaojianziduan=None, db_tiaojianzhi=None):
        if db_host == None:
            self.db_host = '192.168.100.198'
        else:
            self.db_host = db_host

        if db_port == None:
            self.db_port = int("3306")
        else:
            self.db_port = int(db_port)

        if db_user == None:
            self.db_user = 'lepus_user'
        else:
            self.db_user = db_user

        if db_password == None:
            self.db_password = '123456'
        else:
            self.db_password = db_password

        if db_database == None:
            self.db_database = 'testconn'
        else:
            self.db_database = db_database

        if db_charset == None:
            self.db_charset = 'utf8'
        else:
            self.db_charset = db_charset

        if db_biao == None:
            self.db_biao = 'testdatas_clickandback'
        else:
            self.db_biao = db_biao

        if db_ziduan == None:
            self.db_ziduan = 'current_page_click_ele_find_value'
        else:
            self.db_ziduan = db_ziduan

        if db_xiugaiqiandezhi == None:
            self.db_xiugaiqiandezhi = '修改后的油烟餐饮'
        else:
            self.db_xiugaiqiandezhi = db_xiugaiqiandezhi

        if db_xiugaihoudezhi == None:
            self.db_xiugaihoudezhi = '/html/body/'
        else:
            self.db_xiugaihoudezhi = db_xiugaihoudezhi

        if db_tiaojianziduan == None:
            self.db_tiaojianziduan = 'id'
        else:
            self.db_tiaojianziduan = db_tiaojianziduan

        if db_tiaojianzhi == None:
            self.db_tiaojianzhi = '10'
        else:
            self.db_tiaojianzhi = db_tiaojianzhi

        self.conn = self.connectMyDB()
        self.cursor = self.connectMyDBAndCursor()

    def outPutMyLog(self,context):
        mylog = MyLogs(context)
        mylog.runMyLog()


    def outPutErrorMyLog(self,context):
        mylog = MyLogs(context)
        mylog.runErrorLog()

    def connectMyDB(self):
        # 连接database
        try:
            conn = pymysql.connect(host=self.db_host, port=self.db_port, user=self.db_user, password=self.db_password,
                                   database=self.db_database, charset=self.db_charset)
            self.outPutMyLog("\n成功连接数据库:%s_%s\n" % (self.db_host,self.db_database))
            return conn
        except Exception as e:
            self.outPutErrorMyLog("\n数据库%s_%s连接失败，失败原因：\n\t%s\n" % (self.db_host,self.db_database,e))
            return None


    def connectMyDBAndCursor(self):
        # 得到一个可以执行SQL语句的光标对象
        cursor = self.conn.cursor()
        self.outPutMyLog("成功创建执行SQL语句的光标对象\n")
        return cursor

    def connectMyDBAndExecute(self,mySqlSentence):
        #执行SQL语句
        self.outPutMyLog("\t执行的sql语句：\n\t\t%s\n" % mySqlSentence)
        self.cursor.execute(mySqlSentence)
        #数据库提交命令
        self.conn.commit()  # 执行update操作时需要写这个，否则就会更新不成功
        rs = self.cursor.fetchall()  # 获取执行sql后的结果
        return rs   # 返回执行sql后的结果

    def connectMyDBAndSelect(self):
        # 定义要执行的SQL语句
        sql = """
        SELECT %s FROM %s WHERE %s=%s
        """ % (self.db_ziduan,self.db_biao,self.db_tiaojianziduan,self.db_tiaojianzhi)

        if self.db_tiaojianzhi == "all":
            sql = """
            SELECT %s FROM %s 
            """ % (self.db_ziduan, self.db_biao)
        # 执行SQL语句
        rs = self.connectMyDBAndExecute(sql)
        self.outPutMyLog("\t查询的是%s表中的%s字段（筛选条件是字段%s等于%s的结果）的值，查询到的结果是：\n" % (self.db_biao,self.db_ziduan,self.db_tiaojianziduan,self.db_tiaojianzhi))
        for r in rs:
            self.outPutMyLog("\t\t%s" % r)

    def connectMyDBAndSelectAndReturn(self):
        # 定义要执行的SQL语句
        sql = """
        SELECT %s FROM %s WHERE %s=%s
        """ % (self.db_ziduan,self.db_biao,self.db_tiaojianziduan,self.db_tiaojianzhi)

        if self.db_tiaojianzhi == "all":
            sql = """
            SELECT %s FROM %s 
            """ % (self.db_ziduan, self.db_biao)
        # 执行SQL语句
        rs = self.connectMyDBAndExecute(sql)
        self.outPutMyLog("\t查询的是%s表中的%s字段（筛选条件是字段%s等于%s的结果）的值，查询到的结果是：\n" % (self.db_biao,self.db_ziduan,self.db_tiaojianziduan,self.db_tiaojianzhi))
        for r in rs:
            self.outPutMyLog("\t\t%s" % r)
        return rs

    def connectMyDBAndUpdate(self):
        # 定义要执行的SQL语句
        sql = """
        UPDATE %s SET %s = REPLACE(%s, "%s", "%s") WHERE %s = %s
        """ % (self.db_biao,self.db_ziduan,self.db_ziduan,self.db_xiugaiqiandezhi,self.db_xiugaihoudezhi,self.db_tiaojianziduan,self.db_tiaojianzhi)

        if self.db_tiaojianzhi == "all":
            sql = """
            UPDATE %s SET %s = REPLACE(%s, "%s", "%s")
            """ % (self.db_biao, self.db_ziduan, self.db_ziduan, self.db_xiugaiqiandezhi, self.db_xiugaihoudezhi)
        # 执行SQL语句
        # 执行SQL语句
        rs = self.connectMyDBAndExecute(sql)
        self.outPutMyLog("\t替换的是%s表中的%s字段（筛选条件是字段%s等于%s的结果）的值：\n\t\t要替换的内容：%s\n\t\t替换后的内容：%s\n" % (self.db_biao,self.db_ziduan,self.db_tiaojianziduan,self.db_tiaojianzhi,self.db_xiugaiqiandezhi,self.db_xiugaihoudezhi))

    def connectMyDBAndDelete(self):
        gbt = GetBeforeTime()
        btwd = gbt.runGetBeforeOneWeekTime()
        print("btwd:%s" % btwd)
        # 定义要执行的SQL语句
        sql = """
        delete from %s  where %s<'%s 00:00:00'
        """ % (self.db_biao,self.db_tiaojianziduan,btwd)
        # 执行SQL语句
        rs = self.connectMyDBAndExecute(sql)
        self.outPutMyLog("\t删除的是%s表中的%s字段小于%s的数据\n" % (self.db_biao,self.db_tiaojianziduan,btwd))


    def closeCursorAndConnect(self):
        # 关闭光标对象
        self.cursor.close()
        self.outPutMyLog("\n关闭执行SQL语句的光标对象\n")
        # 关闭数据库连接
        self.conn.close()
        self.outPutMyLog("断开数据库连接\n")

    def run(self):
        self.outPutMyLog("替换前查询到的结果：\n" )

        self.connectMyDBAndSelect()
        self.outPutMyLog("执行替换:\n")
        self.connectMyDBAndUpdate()
        self.outPutMyLog("替换后查询到的结果：\n" )
        self.connectMyDBAndSelect()
        self.closeCursorAndConnect()



if __name__ == '__main__':
    db_host = '192.168.100.198'
    db_port = 3306
    db_user = 'lepus_user'
    db_password = '123456'
    db_database = 'testconn'
    db_charset = 'utf8'
    db_biao = "testdatas_clickandback"
    db_ziduan = "current_page_click_ele_find_value"
    db_xiugaiqiandezhi = "修改后的油烟餐饮"
    db_xiugaihoudezhi = "/html/body/"
    db_tiaojianziduan = "id"
    db_tiaojianzhi = "10"



    ob = OperationMyDB(db_tiaojianzhi="all")
    ob.run()
    # ob.connectMyDBAndSelect()
    # ob.connectMyDBAndUpdate("testdatas_clickandback","current_page_click_ele_find_value","/html/body/","修改后的油烟餐饮","id","10")
    # ob.connectMyDBAndSelect()


