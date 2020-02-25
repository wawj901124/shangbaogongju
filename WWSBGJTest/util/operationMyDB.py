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
                  db_tiaojianziduan=None, db_tiaojianzhi=None,
                  db_paixuziduan=None,db_paixufangshi=None,db_qianjiwei=None):
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
            self.db_password = ''
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
            self.db_ziduan = '*'
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
            self.db_tiaojianziduan = ''
        else:
            self.db_tiaojianziduan = db_tiaojianziduan

        if db_tiaojianzhi == None:
            self.db_tiaojianzhi = ''
        else:
            self.db_tiaojianzhi = db_tiaojianzhi

        if db_paixuziduan == None:
            self.db_paixuziduan = ''
        else:
            self.db_paixuziduan = db_paixuziduan

        if db_paixufangshi == None:
            self.db_paixufangshi = True
        else:
            self.db_paixufangshi = db_paixufangshi

        if db_qianjiwei == None:
            self.db_qianjiwei = ''
        else:
            self.db_qianjiwei = int(db_qianjiwei)


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
            self.outPutMyLog("\t\t" )
            self.outPutMyLog(r)
        return rs

    def connectMyDBAndGetBiaotou(self):
        # 定义要执行的SQL语句
        mysql_biaotou = """
          SELECT COLUMN_NAME FROM information_schema.COLUMNS WHERE TABLE_SCHEMA = '%s' AND TABLE_NAME = '%s'
        """ % (self.db_database,self.db_biao)
        # 执行SQL语句
        rs = self.connectMyDBAndExecute(mysql_biaotou)
        self.outPutMyLog("\t查询的是%s库中%s表的表头：\n" % (self.db_database,self.db_biao))
        for r in rs:
            self.outPutMyLog("\t\t%s" % r)
        biaotou_list = []
        for r_one in rs:
            for r_one_one in r_one:
                if r_one_one != '':
                    print(r_one_one)
                    r_one_one_xiao = r_one_one.lower()
                    print(r_one_one_xiao)
                    biaotou_list.append(r_one_one_xiao)

        print("表头列表：")
        print(biaotou_list)

        return biaotou_list


    def connectMyDBAndSelectAndReturnWithBiaoTou(self):

        # 定义要执行的SQL语句,ASC正序，DESC倒序
        #无条件语句
        if self.db_tiaojianziduan == ""and self.db_tiaojianzhi=="":
            #无排序
            print("self.db_paixuziduan")
            if self.db_paixuziduan == '':
                sql = """
                SELECT %s FROM %s 
                """ % (self.db_ziduan,self.db_biao)
            #有排序
            else:
                #倒序
                if self.db_paixufangshi:
                    #无限制个数
                    if self.db_qianjiwei == '':
                        sql = """
                        SELECT %s FROM %s ORDER BY %s DESC 
                        """ % (self.db_ziduan,self.db_biao,self.db_paixuziduan)
                    #有限制个数
                    else:
                        sql = """
                        SELECT %s FROM %s ORDER BY %s DESC LIMIT %d
                        """ % (self.db_ziduan,self.db_biao,self.db_paixuziduan,self.db_qianjiwei)
                #正序
                else:
                    #无限制个数
                    if self.db_qianjiwei == '':
                        sql = """
                        SELECT %s FROM %s ORDER BY %s ASC
                        """ % (self.db_ziduan,self.db_biao,self.db_paixuziduan)
                    #有限制个数
                    else:
                        sql = """
                        SELECT %s FROM %s ORDER BY %s ASC LIMIT %d
                        """ % (self.db_ziduan,self.db_biao,self.db_paixuziduan,self.db_qianjiwei)
        #有条件语句
        elif self.db_tiaojianziduan != ""and self.db_tiaojianzhi!="":
            if self.db_paixuziduan == '':
                sql = """
                SELECT %s FROM %s WHERE %s=%s
                """ % (self.db_ziduan,self.db_biao, self.db_tiaojianziduan, self.db_tiaojianzhi)
            else:
                if self.db_paixufangshi:
                    if self.db_qianjiwei == '':
                        sql = """
                        SELECT %s FROM %s WHERE %s=%s ORDER BY %s DESC 
                        """ % (self.db_ziduan,self.db_biao, self.db_tiaojianziduan, self.db_tiaojianzhi, self.db_paixuziduan)
                    else:
                        sql = """
                        SELECT %s FROM %s WHERE %s=%s ORDER BY %s DESC LIMIT %d
                        """ % (self.db_ziduan,self.db_biao, self.db_tiaojianziduan, self.db_tiaojianzhi, self.db_paixuziduan,self.db_qianjiwei)

                else:
                    if self.db_qianjiwei == '':
                        sql = """
                        SELECT %s FROM %s WHERE %s=%s ORDER BY %s ASC
                        """ % (self.db_ziduan,self.db_biao,self.db_tiaojianziduan,self.db_tiaojianzhi,self.db_paixuziduan)
                    else:
                        sql = """
                        SELECT %s FROM %s WHERE %s=%s ORDER BY %s ASC LIMIT %d
                        """ % (self.db_ziduan,self.db_biao,self.db_tiaojianziduan,self.db_tiaojianzhi,self.db_paixuziduan,self.db_qianjiwei)
        #条件不全语句
        else:
            sql = "没有执行sql语句"
            print("条件字段与条件值要配对使用，你不能一个用，一个不用，要么都用，要么都不用")

        print("获取表内容开始.......")
        # 执行SQL语句
        rs = self.connectMyDBAndExecute(sql)
        self.outPutMyLog("\t查询的是%s表中的所有字段（筛选条件是字段%s等于%s的结果）的值，查询到的结果是：\n" % (self.db_biao,self.db_tiaojianziduan,self.db_tiaojianzhi))
        biaotou_list = self.connectMyDBAndGetBiaotou()

        biao_content_list = []
        for r_one in rs:
            biao_content_one_list = []
            for r_one_one in r_one:
                biao_content_one_list.append(r_one_one)
            print("列表一条内容：")
            print(biao_content_one_list)
            biao_content_one_dict = dict(zip(biaotou_list, biao_content_one_list))
            print("列表一条数据内容字典：")
            print(biao_content_one_dict)
            biao_content_list.append(biao_content_one_dict)

        print("列表内容：")
        print(biao_content_list)
        return biao_content_list


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
    db_host = '127.0.0.1'
    db_port = 3306
    db_user = 'root'
    db_password = ''
    db_database = 'wanwen'
    db_charset = 'utf8'
    db_biao = "wanwen"
    db_ziduan = "current_page_click_ele_find_value"
    db_xiugaiqiandezhi = "修改后的油烟餐饮"
    db_xiugaihoudezhi = "/html/body/"
    db_tiaojianziduan = "id"
    db_tiaojianzhi = "10"




    ob = OperationMyDB(db_tiaojianzhi="all")
    # ob.run()
    # ob.connectMyDBAndSelect()
    # ob.connectMyDBAndUpdate("testdatas_clickandback","current_page_click_ele_find_value","/html/body/","修改后的油烟餐饮","id","10")
    # ob.connectMyDBAndSelect()


