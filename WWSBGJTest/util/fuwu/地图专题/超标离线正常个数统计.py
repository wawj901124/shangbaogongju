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


#根据支干/断面的ID查询td_station_state表获取对应STATION_ID为mn_id数据的 WATER_TYPE字段
mysql_count_zhengchang = """
        SELECT COUNT(*) FROM td_station_state WHERE STATE='1' 
        """
# mysql_yuju = """
#         SELECT COUNT(*) FROM td_station_state
#         SELECT * FROM td_station_state WHERE STATION_ID='%s' ORDER BY ID ASC
#         """
# cursor_dcloud_base.execute(mysql_yuju)
# # 数据库提交命令
# # self.conn.commit()  # 执行update操作时需要写这个，否则就会更新不成功
# rs = cursor_dcloud_base.fetchall()  # 获取执行sql后的结果
# for r in rs:
#     # print(r)
#     mn_id = r[0]
#     break
tdstationstatecount_zhengchang = connectDcloudBaseMyDBAndSelect(mysql_count_zhengchang)[0][0]
print(tdstationstatecount_zhengchang)

mysql_count_chaobiao = """
        SELECT COUNT(*) FROM td_station_state WHERE STATE='3' 
        """
tdstationstatecount_chaobiao = connectDcloudBaseMyDBAndSelect(mysql_count_chaobiao)[0][0]
print(tdstationstatecount_chaobiao)

mysql_count_lixian = """
        SELECT COUNT(*) FROM td_station_state WHERE STATE='6' 
        """
tdstationstatecount_lixian = connectDcloudBaseMyDBAndSelect(mysql_count_lixian)[0][0]
print(tdstationstatecount_lixian)

mysql_count_zong = """
        SELECT COUNT(*) FROM td_station_state 
        """
tdstationstatecount_zong = connectDcloudBaseMyDBAndSelect(mysql_count_zong)[0][0]
print(tdstationstatecount_zong)

if int(tdstationstatecount_zong) == int(tdstationstatecount_zhengchang)+int(tdstationstatecount_chaobiao)+int(tdstationstatecount_lixian):
    print("-----------------------------------------------------" )
    print("总个数：%s"% tdstationstatecount_zong)
    print("在线正常个数：%s" % tdstationstatecount_zhengchang)
    print("在线超标个数：%s" % tdstationstatecount_chaobiao)
    print("离线个数：%s" % tdstationstatecount_lixian)
    print("-----------------------------------------------------")































