import datetime
now_time_str = str(datetime.datetime.now().strftime('%Y%m%d%H%M%S%f'))   #格式化到毫秒
print(now_time_str)