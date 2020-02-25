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




#根据支干/断面名称查询水质类别
#支干/断面名称
# zhigan_name = "昌平区测试设备1号"
zhigan_name ="北京测试1号流域"
#根据支干/断面查询tb_station表获取对应数据的 ID
mysql_yuju = """
        SELECT ID FROM tb_station WHERE NAME='%s'
        """% zhigan_name
# cursor_dcloud_base.execute(mysql_yuju)
# # 数据库提交命令
# # self.conn.commit()  # 执行update操作时需要写这个，否则就会更新不成功
# rs = cursor_dcloud_base.fetchall()  # 获取执行sql后的结果
# for r in rs:
#     # print(r)
#     mn_id = r[0]
#     break

mn_id = connectDcloudBaseMyDBAndSelect(mysql_yuju)[0][0]
print(mn_id)

#根据支干/断面查询tb_station表获取对应数据的
mysql_yuju = """
        SELECT MCUSN FROM tb_station WHERE NAME='%s'
        """% zhigan_name
# cursor_dcloud_base.execute(mysql_yuju)
# # 数据库提交命令
# # self.conn.commit()  # 执行update操作时需要写这个，否则就会更新不成功
# rs = cursor_dcloud_base.fetchall()  # 获取执行sql后的结果
# for r in rs:
#     # print(r)
#     mn_id = r[0]
#     break
MN_hao = connectDcloudBaseMyDBAndSelect(mysql_yuju)[0][0]
print(MN_hao)


#根据支干/断面的ID查询td_station_state表获取对应STATION_ID为mn_id数据的 WATER_TYPE字段
mysql_yuju = """
        SELECT * FROM td_station_state WHERE STATION_ID='%s' ORDER BY ID ASC
        """ % mn_id
# cursor_dcloud_base.execute(mysql_yuju)
# # 数据库提交命令
# # self.conn.commit()  # 执行update操作时需要写这个，否则就会更新不成功
# rs = cursor_dcloud_base.fetchall()  # 获取执行sql后的结果
# for r in rs:
#     # print(r)
#     mn_id = r[0]
#     break
tdstationstate = connectDcloudBaseMyDBAndSelect(mysql_yuju)[0]
print(tdstationstate)
water_type = tdstationstate[5]
print(water_type)

shouyaowuranwu = tdstationstate[4]
print(shouyaowuranwu)


#根据支干/断面查询tb_station表获取对应数据的 CITY_ID
mysql_yuju = """
        SELECT CITY_ID FROM tb_station WHERE NAME='%s'
        """% zhigan_name
# cursor_dcloud_base.execute(mysql_yuju)
# # 数据库提交命令
# # self.conn.commit()  # 执行update操作时需要写这个，否则就会更新不成功
# rs = cursor_dcloud_base.fetchall()  # 获取执行sql后的结果
# for r in rs:
#     # print(r)
#     mn_id = r[0]
#     break

city_id = connectDcloudBaseMyDBAndSelect(mysql_yuju)[0][0]
print(city_id)

#根据支干/断面查询tb_station表获取对应数据的 CITY_ID后，查询tb_city表中对应的ID对应的CITY_NAME
mysql_yuju = """
        SELECT CITY_NAME FROM tb_city WHERE ID='%s'
        """% city_id
# cursor_dcloud_base.execute(mysql_yuju)
# # 数据库提交命令
# # self.conn.commit()  # 执行update操作时需要写这个，否则就会更新不成功
# rs = cursor_dcloud_base.fetchall()  # 获取执行sql后的结果
# for r in rs:
#     # print(r)
#     mn_id = r[0]
#     break

city_name = connectDcloudBaseMyDBAndSelect(mysql_yuju)[0][0]
print(city_name)



# print("%s（支干/断面）的水质等级为%s" % (zhigan_name,water_type))
#
print("--------------------------------------------------------------")
print("支干/断面名称：%s"% zhigan_name)
print("支干/断面水质等级：%s"% water_type)
print("支干/断面对应的流域名称：%s"% city_name)
print("支干/断面对应的首要污染物：%s"% shouyaowuranwu)
print("支干/断面对应设备MN号：%s"% MN_hao)
print("--------------------------------------------------------------")



























