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
zhigan_name ="支干/断面名称20191231164310"
zhigan_id = "417b73a7f2ba422483d6273478c290a1"
#根据支干/断面查询tb_station表获取对应数据的
mysql_yuju = """
        SELECT * FROM tb_station WHERE NAME='%s'
        """% zhigan_name

mysql_yuju_id = """
        SELECT * FROM tb_station WHERE ID='%s'
        """% zhigan_id
# cursor_dcloud_base.execute(mysql_yuju)
# # 数据库提交命令
# # self.conn.commit()  # 执行update操作时需要写这个，否则就会更新不成功
# rs = cursor_dcloud_base.fetchall()  # 获取执行sql后的结果
# for r in rs:
#     # print(r)
#     mn_id = r[0]
#     break

tbStation = connectDcloudBaseMyDBAndSelect(mysql_yuju)[0]
# tbStation = connectDcloudBaseMyDBAndSelect(mysql_yuju_id)[0]
# print(tbStation)
print("ID:%s" % tbStation[0])
print("AREA_ID（所属省ID）:%s" % tbStation[1])
print("CITY_ID（所属流域ID）:%s" % tbStation[2])
print("MCUSN（MN号）:%s" % tbStation[3])
print("NAME(支干/断面):%s" % tbStation[4])
print("UPLOAD_INTERVAL:%s" % tbStation[5])
print("ADDRESS（站点地址）:%s" % tbStation[6])

print("STANDARD_ID:%s" % tbStation[7])
print("STANDARD_FILE_NAME（执行标准）:%s" % tbStation[8])
print("STANDARD_FILE_RUL（执行标准URL路径）:%s" % tbStation[9])
print("STANDARD_FILE_NEW_NAME:%s" % tbStation[10])
print("OPERTOR（联系人）:%s" % tbStation[11])
print("TELEPHONE（联系方式）:%s" % tbStation[12])
print("file_id（站点图片ID）:%s" % tbStation[13])

print("remarks（备注）:%s" % tbStation[14])
print("CREATETIME:%s" % tbStation[15])
print("LONGITUDE:%s" % tbStation[16])
print("LATITUDE:%s" % tbStation[17])

mn_id = tbStation[0]
area_id = tbStation[1]
cityid = tbStation[2]

fileid = tbStation[13]

#根据所属省ID查询所属省域名称
mysql_yuju = """
        SELECT AREA_NAME FROM tb_area WHERE ID='%s'
        """% area_id

areaname = connectDcloudBaseMyDBAndSelect(mysql_yuju)[0]
print("CITY_NAME（所属省名称）:%s" % areaname)



#根据所属流域ID查询所属流域名称
mysql_yuju = """
        SELECT CITY_NAME FROM tb_city WHERE ID='%s'
        """% cityid

cityname = connectDcloudBaseMyDBAndSelect(mysql_yuju)[0]
print("CITY_NAME（所属流域名称）:%s" % cityname)


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
offline_time = tdstationstate[3]
print(water_type)




print("--------------------------------------------------------------")
print("支干/断面对应的省：%s"% areaname)
print("支干/断面对应的流域：%s"% cityname)
print("支干/断面对应的支干/断面：%s"% tbStation[4])
print("支干/断面对应的最后在线时间：%s"% offline_time)
print("--------------------------------------------------------------")



























