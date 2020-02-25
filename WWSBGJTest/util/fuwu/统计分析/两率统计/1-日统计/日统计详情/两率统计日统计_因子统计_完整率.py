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
zhigan_name ="支干/断面名称20200108104853"
#根据支干/断面查询tb_station表获取对应数据的
mysql_yuju = """
        SELECT * FROM tb_station WHERE NAME='%s'
        """% zhigan_name
# cursor_dcloud_base.execute(mysql_yuju)
# # 数据库提交命令
# # self.conn.commit()  # 执行update操作时需要写这个，否则就会更新不成功
# rs = cursor_dcloud_base.fetchall()  # 获取执行sql后的结果
# for r in rs:
#     # print(r)
#     mn_id = r[0]
#     break

tbStation = connectDcloudBaseMyDBAndSelect(mysql_yuju)[0]
# print(tbStation)
# print("ID:%s" % tbStation[0])
# print("AREA_ID（所属省ID）:%s" % tbStation[1])
# print("CITY_ID（所属流域ID）:%s" % tbStation[2])
# print("MCUSN（MN号）:%s" % tbStation[3])
# print("NAME(支干/断面):%s" % tbStation[4])
# print("UPLOAD_INTERVAL:%s" % tbStation[5])
# print("ADDRESS（站点地址）:%s" % tbStation[6])
#
# print("STANDARD_ID:%s" % tbStation[7])
# print("STANDARD_FILE_NAME（执行标准）:%s" % tbStation[8])
# print("STANDARD_FILE_RUL（执行标准URL路径）:%s" % tbStation[9])
# print("STANDARD_FILE_NEW_NAME:%s" % tbStation[10])
# print("OPERTOR（联系人）:%s" % tbStation[11])
# print("TELEPHONE（联系方式）:%s" % tbStation[12])
# print("file_id（站点图片ID）:%s" % tbStation[13])
#
# print("remarks（备注）:%s" % tbStation[14])
# print("CREATETIME:%s" % tbStation[15])
# print("LONGITUDE:%s" % tbStation[16])
# print("LATITUDE:%s" % tbStation[17])

cityid = tbStation[2]
fileid = tbStation[13]

tbStationid = tbStation[0]
print(tbStationid )



#根据站点ID查询2011中的数据（实时曲线数据（2011表））获取数据表表头
#查询dcloud_base库中tb_upload_factor 表
mysql_biaotou = """
  SELECT COLUMN_NAME FROM information_schema.COLUMNS WHERE TABLE_SCHEMA = 'dcloud_base' AND TABLE_NAME = 'tb_full_rate_day_factor'
"""
# cursor_dcloud_base.execute(mysql_yuju)
# # 数据库提交命令
# # self.conn.commit()  # 执行update操作时需要写这个，否则就会更新不成功
# rs = cursor_dcloud_base.fetchall()  # 获取执行sql后的结果
# for r in rs:
#     # print(r)
#     mn_id = r[0]
#     break

shishiquxian_biaotou = connectDcloudDataMyDBAndSelect(mysql_biaotou)

shishiquxian_biaotou_len = len(shishiquxian_biaotou)
# print(shishiquxian_biaotou)
# print(shishiquxian_biaotou)
shishiquxian_biaotou_list = []
for i in range(0,shishiquxian_biaotou_len):
    biaotou = shishiquxian_biaotou[i][0]
    # print(biaotou)
    shishiquxian_biaotou_list.append(biaotou)

print(shishiquxian_biaotou_list)

shishiquxian_biaotou_list_len = len(shishiquxian_biaotou_list)



# 处理RTD显示因子
for i in range(0, shishiquxian_biaotou_list_len):
    if "AVG" in shishiquxian_biaotou_list[i]:
        biaotou_list_yinzi_code = shishiquxian_biaotou_list[i].split("_")[1]
        print(biaotou_list_yinzi_code)
        # 根据因子code查询tb_factor得到因子名称
        mysql_yuju = """
                SELECT * FROM tb_factor WHERE FACTOR_CODE='%s'
                """ % biaotou_list_yinzi_code
        tbfactor = connectDcloudBaseMyDBAndSelect(mysql_yuju)
        print(tbfactor)
        if len(tbfactor)>0:
            biaotou_list_yinzi_name = tbfactor[0][2]
            biaotou_list_yinzi_danwei = tbfactor[0][4]
            print(biaotou_list_yinzi_name)
            shishiquxian_biaotou_list[i] = "%s(%s(%s（%s）))"%(shishiquxian_biaotou_list[i],biaotou_list_yinzi_name,biaotou_list_yinzi_danwei,"平均值")
            print("-----------------")
    elif "COU" in shishiquxian_biaotou_list[i]:
        biaotou_list_yinzi_code = shishiquxian_biaotou_list[i].split("_")[1]
        print(biaotou_list_yinzi_code)
        # 根据因子code查询tb_factor得到因子名称
        mysql_yuju = """
                SELECT * FROM tb_factor WHERE FACTOR_CODE='%s'
                """ % biaotou_list_yinzi_code
        tbfactor = connectDcloudBaseMyDBAndSelect(mysql_yuju)
        print(tbfactor)
        if len(tbfactor)>0:
            biaotou_list_yinzi_name = tbfactor[0][2]
            biaotou_list_yinzi_danwei = tbfactor[0][4]
            print(biaotou_list_yinzi_name)
            shishiquxian_biaotou_list[i] = "%s(%s(%s(%s)))"%(shishiquxian_biaotou_list[i],biaotou_list_yinzi_name,biaotou_list_yinzi_danwei,"累计值")
            print("-----------------")





#根据站点ID查询2011中的数据（实时曲线数据（2011表））最近一条数据
mysql_yuju = """
        SELECT * FROM tb_full_rate_day_factor WHERE STATION_ID='%s' ORDER by DT DESC limit 131
        """% (tbStationid)
# cursor_dcloud_base.execute(mysql_yuju)
# # 数据库提交命令
# # self.conn.commit()  # 执行update操作时需要写这个，否则就会更新不成功
# rs = cursor_dcloud_base.fetchall()  # 获取执行sql后的结果
# for r in rs:
#     # print(r)
#     mn_id = r[0]
#     break

shishiquxian = connectDcloudBaseMyDBAndSelect(mysql_yuju)

num = 1
for shishiquxian_one in shishiquxian:
    print("第%s条——————————————————————————————————"% num)
    # print(shishiquxian_one)
    shishiquxian_one_len = len(shishiquxian_one)
    shishiquxian_one_list = []
    for i in range(0, shishiquxian_one_len):
        shishiquxian_one_list.append(shishiquxian_one[i])
    # print(shishiquxian_one_list)


    shishiquxian_one_dict =dict(zip(shishiquxian_biaotou_list,shishiquxian_one_list))
    # print(shishiquxian_one_dict)

    for key, value in shishiquxian_one_dict.items():
        print("%s:%s" %(key,value))

    print("一条结束")
    num = num+1;



















#