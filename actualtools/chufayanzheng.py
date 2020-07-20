# a = 5
# b= (a//5)*5
# print(b)
import datetime
def shujuduanCPdatatime(CPtime):
    """
    CPdatatime
    :return:
    """
    if CPtime == "shishi":  # 实时数据
        CPdatatime = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        CPdatatime_str = str(CPdatatime)
        print("实时数据时间串：")
        print(CPdatatime_str)
    elif CPtime == "fenzhong":  # 1分钟数据
        CPdatatime = datetime.datetime.now().strftime('%Y%m%d%H%M')
        CPdatatime_str = str(CPdatatime)
        CPdatatime_str = "%s00" % CPdatatime_str
        print("1分钟数据时间串：")
        print(CPdatatime_str)
    elif CPtime == "fivefenzhong":  # 5分钟数据
        CPdatatime_hour = datetime.datetime.now().strftime('%Y%m%d%H')
        CPdatatime_hour_str = str(CPdatatime_hour)
        CPdatatime_fen = datetime.datetime.now().strftime('%M')
        CPdatatime_fen_int = int(str(CPdatatime_fen))
        if CPdatatime_fen_int == 0:  # 如果是0分，则输出“00”
            CPdatatime_fen_str = "00"
        else:
            CPdatatime_fen_int_str = str((CPdatatime_fen_int // 5) * 5)  # 获取5分钟字符串
            CPdatatime_fen_int_str_len = len(CPdatatime_fen_int_str)
            if CPdatatime_fen_int_str_len == 1:
                CPdatatime_fen_str = "0%s" % CPdatatime_fen_int_str
            else:
                CPdatatime_fen_str = CPdatatime_fen_int_str
        CPdatatime_str = "%s%s00" % (CPdatatime_hour_str, CPdatatime_fen_str)
        print("5分钟数据时间串：")
        print(CPdatatime_str)

    elif CPtime == "tenfenzhong":  # 10分钟数据
        CPdatatime_hour = datetime.datetime.now().strftime('%Y%m%d%H')
        CPdatatime_hour_str = str(CPdatatime_hour)
        CPdatatime_fen = datetime.datetime.now().strftime('%M')
        CPdatatime_fen_int = int(str(CPdatatime_fen))
        if CPdatatime_fen_int == 0:  # 如果是0分，则输出“00”
            CPdatatime_fen_str = "00"
        else:
            CPdatatime_fen_int_str = str((CPdatatime_fen_int // 10) * 10)  # 获取10分钟字符串
            CPdatatime_fen_int_str_len = len(CPdatatime_fen_int_str)
            if CPdatatime_fen_int_str_len == 1:
                CPdatatime_fen_str = "0%s" % CPdatatime_fen_int_str
            else:
                CPdatatime_fen_str = CPdatatime_fen_int_str
        CPdatatime_str = "%s%s00" % (CPdatatime_hour_str, CPdatatime_fen_str)
        print("10分钟数据时间串：")
        print(CPdatatime_str)

    elif CPtime == "xiaoshi":
        CPdatatime = datetime.datetime.now().strftime('%Y%m%d%H')
        CPdatatime_str = str(CPdatatime)
        CPdatatime_str = "%s0000" % CPdatatime_str
        print("小时数据时间串：")
        print(CPdatatime_str)

    return CPdatatime_str

if __name__ == '__main__':
    CPtime = "shishi"
    shujuduanCPdatatime(CPtime)
    CPtime = "fenzhong"
    shujuduanCPdatatime(CPtime)
    CPtime = "fivefenzhong"
    shujuduanCPdatatime(CPtime)
    CPtime = "tenfenzhong"
    shujuduanCPdatatime(CPtime)
    CPtime = "xiaoshi"
    shujuduanCPdatatime(CPtime)
