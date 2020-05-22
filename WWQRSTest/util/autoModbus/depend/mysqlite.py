#导入SQLite驱动：
import sqlite3 #连接到SQlite数据库

class MySqlite(object):
    def __init__(self,sql_name,table_name):
        self.sql_name = sql_name
        self.sql_table_name = table_name
        self.conn = self.conn_sqlite()
        self.cursor = self.cursor_sqlite()

    #连接数据库
    def conn_sqlite(self):
        conn = sqlite3.connect(self.sql_name)  # 数据库文件是test.db，不存在，则自动创建
        return conn

    #游标
    def cursor_sqlite(self):
        cursor = self.conn.cursor()
        return cursor

    def run_sql_commad(self,sql_commad):
        cursor = self.cursor
        cursor.execute(sql_commad)
        sql_result = cursor.fetchall()
        return sql_result


    def cursor_close(self):
        self.cursor.close()  #关闭Cursor:

    def conn_commit(self):
        self.conn.commit()  #提交事务：

    def conn_close(self):  #关闭连接
        self.conn.close()

    def get_table_title(self):
        sql_commad_one = "PRAGMA table_info(%s)" % self.sql_table_name
        r = self.run_sql_commad(sql_commad_one)
        r_list = r
        table_title = []
        for i in r_list:
            t_name = i[1]
            # print(t_name)
            table_title.append(t_name)
        return table_title

    def get_table_content(self):
        sql_commad_two = 'select * from %s;' % self.sql_table_name
        r_list = self.run_sql_commad(sql_commad_two)
        # print(r_list)
        table_content_list = []
        for r_list_one in r_list:
            t_name = r_list_one
            table_content_one_dict = {}
            table_content_one = []
            for one in t_name:
                # print(one)
                table_content_one.append(one)
            table_content_list.append(table_content_one)
        return table_content_list


    def get_table_title_and_content(self):
        table_title = self.get_table_title()
        table_content_list = self.get_table_content()
        table_title_and_content_list = []
        for table_content_one in table_content_list:
            table_content_one_dict = dict(zip(table_title, table_content_one))
            table_title_and_content_list.append(table_content_one_dict)
            print(table_content_one_dict)
        # print(table_title_and_content_list)
        return table_title_and_content_list









if __name__ == '__main__':
    sql_name = 'rtd.db'
    table_name = 'tb_rtd'
    ms = MySqlite(sql_name,table_name)
    print(ms.get_table_title())
    print(ms.get_table_content())
    print(ms.get_table_title_and_content())

    # sql_commad_one = "PRAGMA table_info(rttable)"
    # r = ms.run_sql_commad(sql_commad_one)
    # r_list = r
    # table_title = []
    # for i in r_list:
    #     t_name = i[1]
    #     # print(t_name)
    #     table_title.append(t_name)
    # # print(table_title)
    #
    # sql_commad_two ='select * from rttable;'
    # r_list = ms.run_sql_commad(sql_commad_two)
    # table_content = []
    # for i in r_list:
    #     t_name = i
    #     table_content_one_dict={}
    #     table_content_one = []
    #     for one in t_name:
    #         # print(one)
    #         table_content_one.append(one)
    #     # print(table_content_one)
    #     table_content_one_dict = dict(zip(table_title, table_content_one))
    #     print(table_content_one_dict)
    #
    #
    #
    # print(r_list[0][1])
    # print(r_list[0][3])


