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




#获取设备MN号对应的ID
mysql_yuju = """
        SELECT ID FROM tb_station WHERE MCUSN='chang000265'
        """
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

#查询dcloud_base库中tb_upload_factor 表
mysql_yuju = """
        SELECT * FROM td_upload_factor WHERE STATION_ID='%s' ORDER BY ID ASC 
        """ % mn_id

td_upload_factor_contents_yinzi_list = []
td_upload_factor_contents = connectDcloudBaseMyDBAndSelect(mysql_yuju)
# print(td_upload_factor_content)
print(len(td_upload_factor_contents))
for td_upload_factor_content in td_upload_factor_contents:
    # print(td_upload_factor_content)
    #获取因子代码
    yinzi_list = []
    yinzi_list.append(td_upload_factor_content[2])
    yinzi_list.append(td_upload_factor_content[3])
    td_upload_factor_contents_yinzi_list.append(yinzi_list)
    print(yinzi_list)

print("td_upload_factor表中对应设备的因子编码与因子名称:%s"%td_upload_factor_contents_yinzi_list)



#查询dcloud_base库中td_upload_col 表
mysql_yuju = """
        SELECT * FROM td_upload_col WHERE STATION_ID='%s' ORDER BY ID ASC 
        """ % mn_id
td_upload_col_contents_yinzi_list = []
td_upload_col_contents = connectDcloudBaseMyDBAndSelect(mysql_yuju)
# print(td_upload_factor_content)
print(len(td_upload_col_contents))
for td_upload_col_content in td_upload_col_contents:
    # print(td_upload_col_content)
    if td_upload_col_content[6] == '2011':
        # 获取因子代码
        yinzi_list = []
        yinzi_list.append(td_upload_col_content[2])
        # yinzi_list.append(td_upload_col_content[3])
        # yinzi_list.append(td_upload_col_content[4])
        # yinzi_list.append(td_upload_col_content[5])
        # yinzi_list.append(td_upload_col_content[6])
        td_upload_col_contents_yinzi_list.append(yinzi_list)
        print(yinzi_list)
print(len(td_upload_col_contents_yinzi_list))
# print("td_upload_col表中对应设备的因子编码、因子代码、标志位、因子名称、上报CN码、:%s"%td_upload_factor_contents_yinzi_list)
print("td_upload_col表中对应设备的因子编码:%s"%td_upload_col_contents_yinzi_list)



#查询对应设备2011表
mysql_yuju = """
        SELECT * FROM td_raw_2011_%s  ORDER BY DT DESC 
        """ % mn_id

td_raw_2011_contents = connectDcloudDataMyDBAndSelect(mysql_yuju)
print(len(td_raw_2011_contents))
for td_raw_2011_content in td_raw_2011_contents:
    print(td_raw_2011_content)
    print("__________一条开始____________")
    print(len(td_raw_2011_content))
    for con in td_raw_2011_content:
        print(con)
    print("__________一条结束____________")

#获取表的表头字段名
mysql_biaotou = """
  SELECT COLUMN_NAME FROM information_schema.COLUMNS WHERE TABLE_SCHEMA = 'dcloud_data' AND TABLE_NAME = 'td_raw_2011_%s'
""" % mn_id
td_raw_2011_contents = connectDcloudDataMyDBAndSelect(mysql_biaotou)
td_raw_2011_contents_len = len(td_raw_2011_contents)
print(td_raw_2011_contents)
print(td_raw_2011_contents_len)
td_raw_2011_contents_yinzi_biaotou_list = []
for i in range(5,td_raw_2011_contents_len):
    biaotou = td_raw_2011_contents[i][0]
    print(biaotou)
    td_raw_2011_contents_yinzi_biaotou_list.append(biaotou)

td_raw_2011_contents_yinzi_biaotou_list_sort = sorted(td_raw_2011_contents_yinzi_biaotou_list)
print(td_raw_2011_contents_yinzi_biaotou_list_sort)

biaotou_flag_list = []
biaotou_rtd_list = []
biaotou_tag_list = []
for td_raw_2011_contents_yinzi_biaotou in td_raw_2011_contents_yinzi_biaotou_list_sort:
    if "FLAG" in td_raw_2011_contents_yinzi_biaotou:
        biaotou_flag_list.append(td_raw_2011_contents_yinzi_biaotou)
    if "RTD" in td_raw_2011_contents_yinzi_biaotou:
        biaotou_rtd_list.append(td_raw_2011_contents_yinzi_biaotou)
    if "TAG" in td_raw_2011_contents_yinzi_biaotou:
        biaotou_tag_list.append(td_raw_2011_contents_yinzi_biaotou)

# print(biaotou_flag_list)
# print(biaotou_rtd_list)
# print(biaotou_tag_list)
# print(td_upload_col_contents_yinzi_list)
td_upload_col_contents_yinzi_list_rtd_list = []
td_upload_col_contents_yinzi_list_flag_list = []
for td_upload_col_contents_yinzi in td_upload_col_contents_yinzi_list:
    yizibianli = td_upload_col_contents_yinzi[0]
    if "FLAG" in yizibianli:
        td_upload_col_contents_yinzi_list_flag_list.append(yizibianli)
    if "RTD" in yizibianli:
        td_upload_col_contents_yinzi_list_rtd_list.append(yizibianli)



td_upload_col_contents_yinzi_list_rtd_list_sort = sorted(td_upload_col_contents_yinzi_list_rtd_list)
td_upload_col_contents_yinzi_list_flag_list_sort = sorted(td_upload_col_contents_yinzi_list_flag_list)
print("----------------------------------------------------------")
print("2011表表头因子flag列表长度  :%s"% len(biaotou_flag_list))
print("2011表表头因子flag         :%s"% biaotou_flag_list)
print("td_upload_col表因子flag    :%s"% td_upload_col_contents_yinzi_list_flag_list_sort)
print("2011表表头因子rtd列表长度   :%s"% len(biaotou_rtd_list))
print("2011表表头因子rtd          :%s"% biaotou_rtd_list)
print("td_upload_col表因子rtd     :%s"%  td_upload_col_contents_yinzi_list_rtd_list_sort)
print("2011表表头因子tag列表长度   :%s"% len(biaotou_tag_list))
print("2011表表头因子tag          :%s"% biaotou_tag_list)
print("----------------------------------------------------------")






















