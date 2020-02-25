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
zhigan_name ="支干/断面名称20200108110645"
zhigan_id = "cf3c3593720646b0ad8cde4dc7b9fdae"
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

cityid = tbStation[2]
fileid = tbStation[13]


#根据所属流域ID查询所属流域名称
mysql_yuju = """
        SELECT CITY_NAME FROM tb_city WHERE ID='%s'
        """% cityid
# cursor_dcloud_base.execute(mysql_yuju)
# # 数据库提交命令
# # self.conn.commit()  # 执行update操作时需要写这个，否则就会更新不成功
# rs = cursor_dcloud_base.fetchall()  # 获取执行sql后的结果
# for r in rs:
#     # print(r)
#     mn_id = r[0]
#     break

cityname = connectDcloudBaseMyDBAndSelect(mysql_yuju)[0]
print("CITY_NAME（所属流域名称）:%s" % cityname)

fileid_list = fileid.split(";")
print(fileid_list)
file_path_list = []
for fileid_list_one in fileid_list:
    if fileid_list_one != '':
        #根据file_id查询文件路径
        mysql_yuju = """
                SELECT FILE_PATH FROM tb_upload_file WHERE ID='%s'
                """% fileid_list_one
        # cursor_dcloud_base.execute(mysql_yuju)
        # # 数据库提交命令
        # # self.conn.commit()  # 执行update操作时需要写这个，否则就会更新不成功
        # rs = cursor_dcloud_base.fetchall()  # 获取执行sql后的结果
        # for r in rs:
        #     # print(r)
        #     mn_id = r[0]
        #     break

        filepath = connectDcloudBaseMyDBAndSelect(mysql_yuju)[0]
        file_path_list.append(filepath)
        print("FILE_PATH（站点图片路径）:%s" % filepath)

print("站点图片路径：%s" % file_path_list)










# #根据支干/断面查询tb_station表获取对应数据的
# mysql_yuju = """
#         SELECT MCUSN FROM tb_station WHERE NAME='%s'
#         """% zhigan_name
# # cursor_dcloud_base.execute(mysql_yuju)
# # # 数据库提交命令
# # # self.conn.commit()  # 执行update操作时需要写这个，否则就会更新不成功
# # rs = cursor_dcloud_base.fetchall()  # 获取执行sql后的结果
# # for r in rs:
# #     # print(r)
# #     mn_id = r[0]
# #     break
# MN_hao = connectDcloudBaseMyDBAndSelect(mysql_yuju)[0][0]
# print(MN_hao)
#
#
# #根据支干/断面的ID查询td_station_state表获取对应STATION_ID为mn_id数据的 WATER_TYPE字段
# mysql_yuju = """
#         SELECT * FROM td_station_state WHERE STATION_ID='%s' ORDER BY ID ASC
#         """ % mn_id
# # cursor_dcloud_base.execute(mysql_yuju)
# # # 数据库提交命令
# # # self.conn.commit()  # 执行update操作时需要写这个，否则就会更新不成功
# # rs = cursor_dcloud_base.fetchall()  # 获取执行sql后的结果
# # for r in rs:
# #     # print(r)
# #     mn_id = r[0]
# #     break
# tdstationstate = connectDcloudBaseMyDBAndSelect(mysql_yuju)[0]
# print(tdstationstate)
# water_type = tdstationstate[5]
# print(water_type)
#
# shouyaowuranwu = tdstationstate[4]
# print(shouyaowuranwu)
#
#
# #根据支干/断面查询tb_station表获取对应数据的 CITY_ID
# mysql_yuju = """
#         SELECT CITY_ID FROM tb_station WHERE NAME='%s'
#         """% zhigan_name
# # cursor_dcloud_base.execute(mysql_yuju)
# # # 数据库提交命令
# # # self.conn.commit()  # 执行update操作时需要写这个，否则就会更新不成功
# # rs = cursor_dcloud_base.fetchall()  # 获取执行sql后的结果
# # for r in rs:
# #     # print(r)
# #     mn_id = r[0]
# #     break
#
# city_id = connectDcloudBaseMyDBAndSelect(mysql_yuju)[0][0]
# print(city_id)
#
# #根据支干/断面查询tb_station表获取对应数据的 CITY_ID后，查询tb_city表中对应的ID对应的CITY_NAME
# mysql_yuju = """
#         SELECT CITY_NAME FROM tb_city WHERE ID='%s'
#         """% city_id
# # cursor_dcloud_base.execute(mysql_yuju)
# # # 数据库提交命令
# # # self.conn.commit()  # 执行update操作时需要写这个，否则就会更新不成功
# # rs = cursor_dcloud_base.fetchall()  # 获取执行sql后的结果
# # for r in rs:
# #     # print(r)
# #     mn_id = r[0]
# #     break
#
# city_name = connectDcloudBaseMyDBAndSelect(mysql_yuju)[0][0]
# print(city_name)
#
#
#
# # print("%s（支干/断面）的水质等级为%s" % (zhigan_name,water_type))
# #
# print("--------------------------------------------------------------")
# print("支干/断面名称：%s"% zhigan_name)
# print("支干/断面水质等级：%s"% water_type)
# print("支干/断面对应的流域名称：%s"% city_name)
# print("支干/断面对应的首要污染物：%s"% shouyaowuranwu)
# print("支干/断面对应设备MN号：%s"% MN_hao)
# print("--------------------------------------------------------------")
#
#
#
#
#
#
#
#
#
#
#
















