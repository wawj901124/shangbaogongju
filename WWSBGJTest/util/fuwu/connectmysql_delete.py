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




mn_hao = "chang000000"

#获取设备MN号对应的ID
mysql_yuju = """
        SELECT ID FROM tb_station WHERE MCUSN='%s'
        """ % mn_hao

mn_id = connectDcloudBaseMyDBAndSelect(mysql_yuju)[0][0]
print(mn_id)

#删除dcloud_base库中tb_upload_factor 表中对应设备的数据
sql = """
delete from td_upload_factor WHERE STATION_ID='%s'
""" % mn_id
connectDcloudBaseMyDBAndDelete(sql)



#删除dcloud_base库中td_upload_col 表
mysql_yuju = """
        delete from td_upload_col WHERE STATION_ID='%s'
        """ % mn_id
connectDcloudBaseMyDBAndDelete(mysql_yuju)



#删除对应设备2011表
mysql_yuju = """
        drop table td_raw_2011_%s 
        """ % mn_id
connectDcloudDataMyDBAndDelete(mysql_yuju)

















