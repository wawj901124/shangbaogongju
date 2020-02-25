import redis

conn_host = "192.168.8.205"
conn_port = 17328
conn_password = "admin123!@#qwe"
# 连接池
pool = redis.ConnectionPool(host=conn_host, port=17328,password=conn_password)
conn = redis.Redis(connection_pool=pool)
# conn.execute_command("flushall")
# print("已经将%s主机的redis数据清空" %conn_host)
rs = conn.execute_command("keys *")
change_realdata_list = []
for rs_one in rs:
    rs_one_str = str(rs_one, encoding="utf-8")
    print("字节：%s,字符串：%s"%(rs_one,rs_one_str ))
    if "chang" in  rs_one_str:
        change_realdata_list.append(rs_one_str)
        conn.execute_command("DEL %s" % rs_one_str)
        print("已经将%s键值的数据"% rs_one_str)

print(change_realdata_list)

# conn.execute_command("DEL resvdata:HJ212")
# print("已经将resvdata:HJ212键值的数据")
conn.close()

# # str to bytes 字符串转字节
# bytes(str, encoding="utf8")
#
# # bytes to str  字节转字符串
# str(bytes, encoding="utf-8")