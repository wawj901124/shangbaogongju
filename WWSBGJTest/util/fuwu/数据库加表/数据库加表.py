import pymysql

conn_dcloud_base = pymysql.connect(host="192.168.8.205", port=3306, user="root", password="admin123!@#qwe",
                       database="dcloud_base", charset="utf8")
conn_dcloud_data = pymysql.connect(host="192.168.8.205", port=3306, user="root", password="admin123!@#qwe",
                       database="dcloud_data", charset="utf8")

cursor_dcloud_base = conn_dcloud_base.cursor()

cursor_dcloud_data = conn_dcloud_data.cursor()


def connectDcloudBaseMyDBAndSelect(sql):
    cursor_dcloud_base.execute(sql)
    # 数据库提交命令
    # self.conn.commit()  # 执行update操作时需要写这个，否则就会更新不成功
    rs = cursor_dcloud_base.fetchall()  # 获取执行sql后的结果
    # for r in rs:
    #     # print(r)
    #     mn_id = r[0]
    #     break
    # print(mn_id)
    return rs

def connectDcloudDataMyDBAndSelect(sql):
    cursor_dcloud_data.execute(sql)
    # 数据库提交命令
    # self.conn.commit()  # 执行update操作时需要写这个，否则就会更新不成功
    rs = cursor_dcloud_data.fetchall()  # 获取执行sql后的结果
    # for r in rs:
    #     # print(r)
    #     mn_id = r[0]
    #     break
    # print(mn_id)
    return rs

def connectDcloudBaseMyDBAndDelete(sql):
    print("执行语句:%s" % sql)
    cursor_dcloud_base.execute(sql)
    conn_dcloud_base.commit()

def connectDcloudDataMyDBAndDelete(sql):
    print("执行语句:%s" % sql)
    cursor_dcloud_data.execute(sql)
    conn_dcloud_data.commit()


#数据库加表
sql_create = """
CREATE TABLE `td_station_state`(
`ID` int(11) NOT NULL AUTO_INCREMENT,
`STATION_ID` varchar(50) DEFAULT NULL COMMENT '站点ID',
`STATE` int(11) DEFAULT NULL COMMENT '排放口总状态1正常;3超标;6.离线',
`OFFLINE_TIME`
  
)

"""




















