import time
import datetime


class TongXinXieYi(object):
    def __init__(self,ST,CN,PW,MN,Flag,invert,CPtime,CPyinzi):
        self.ST = ST
        self.CN = CN
        self.PW = PW
        self.MN = MN
        self.Flag = Flag
        self.invert = invert
        self.CPtime = CPtime
        self.CPyinzi = CPyinzi


    #包头
    def baotou(self):
        return "##"

    # 数据段_请求编码 QN
    def shujuduanQN(self):
        """
        精确到毫秒的时间戳:QN=YYYYMMDDhhmmsszzz，用来唯一标识一次命令交互
        :return:
        """
        t = time.time()
        timestamp = int(round(t * 1000))    #毫秒级时间戳,微妙到毫秒转换位四舍五入
        d = datetime.datetime.fromtimestamp(timestamp / 1000)
        # 精确到毫秒
        qn = d.strftime("%Y%m%d%H%M%S%f")
        qn = qn[0:17]
        print(qn)
        print(len(qn))
        return qn

    # 数据段_系统编码ST
    def shujuduanST(self):
        """
        地表水ST=21系统编码, 系统编码取值详见《系统编码表》
        :return:
        """
        if self.ST !=None:
            st_str = str(self.ST)
            st_str_wei = len(st_str)
            if st_str_wei > 5:
                print("系统编码不能超过5位，而实际超过5位")
                st_str = None
            return st_str
        else:
            return self.ST

    # 数据段_命令编码CN
    def shujuduanCN(self):
        """
        CN=命令编码,详见《命令编码表》
        :return:
        """
        if self.CN !=None:
            st_str = str(self.CN)
            st_str_wei = len(st_str)
            if st_str_wei > 7:
                print("命令编码不能超过7位，而实际超过7位")
                st_str = None
            return st_str
        else:
            return self.CN

    # 数据段_访问密码PW
    def shujuduanPW(self):
        """
        PW=访问密码
        :return:
        """
        if self.PW !=None:
            st_str = str(self.PW)
            st_str_wei = len(st_str)
            if st_str_wei > 9:
                print("命令编码不能超过7位，而实际超过7位")
                st_str = None
            return st_str
        else:
            return self.PW

    # 数据段_站点唯一标识 MN
    def shujuduanMN(self):
        """
        MN=地表水用于站点编码唯一标识，编码规则：“A”+6位行政区域代码+ “_”+4位序列编号，见附录E
        :return:
        """
        if self.MN !=None:
            st_str = str(self.MN)
            st_str_wei = len(st_str)
            if st_str_wei > 12:
                print("命令编码不能超过12位，而实际超过12位")
                st_str = None
            return st_str
        else:
            return self.MN

    # 数据段_应答标志Flag
    def shujuduanFlag(self):
        """
        目前只用两个Bit；
        V5	V4	V3	V2	V1	V0	D	A
        V5~V0：标准版本号；Bit：000000 表示标准HJ/T 212-2005，000001表示标准HJ/T 212-2017,000010表示本次标准修订版本号
        A：数据是否应答；Bit：1-应答，0-不应答

        :return:
        """
        flag_int = int(self.Flag)
        return flag_int

    # 数据段_指令参数 CP
    def shujuduanCPdatatime(self):
        """
        CPdatatime
        :return:
        """
        if self.CPtime == "shishi":   #实时数据
            CPdatatime = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
            CPdatatime_str= str(CPdatatime)
            print("实时数据时间串：")
            print(CPdatatime_str)
        elif self.CPtime == "fenzhong":  #1分钟数据
            CPdatatime = datetime.datetime.now().strftime('%Y%m%d%H%M')
            CPdatatime_str= str(CPdatatime)
            CPdatatime_str = "%s00" % CPdatatime_str
            print("1分钟数据时间串：")
            print(CPdatatime_str)
        elif self.CPtime == "fivefenzhong":   #5分钟数据
            CPdatatime_hour = datetime.datetime.now().strftime('%Y%m%d%H')
            CPdatatime_hour_str= str(CPdatatime_hour)
            CPdatatime_fen = datetime.datetime.now().strftime('%M')
            CPdatatime_fen_int = int(str(CPdatatime_fen))
            if CPdatatime_fen_int == 0:  #如果是0分，则输出“00”
                CPdatatime_fen_str = "00"
            else:
                CPdatatime_fen_int_str = str((CPdatatime_fen_int // 5) * 5)   #获取5分钟字符串
                CPdatatime_fen_int_str_len = len(CPdatatime_fen_int_str)
                if CPdatatime_fen_int_str_len == 1:
                    CPdatatime_fen_str = "0%s"% CPdatatime_fen_int_str
                else:
                    CPdatatime_fen_str = CPdatatime_fen_int_str
            CPdatatime_str = "%s%s00"%(CPdatatime_hour_str,CPdatatime_fen_str)
            print("5分钟数据时间串：")
            print(CPdatatime_str)

        elif self.CPtime == "tenfenzhong": #10分钟数据
            CPdatatime_hour = datetime.datetime.now().strftime('%Y%m%d%H')
            CPdatatime_hour_str= str(CPdatatime_hour)
            CPdatatime_fen = datetime.datetime.now().strftime('%M')
            CPdatatime_fen_int = int(str(CPdatatime_fen))
            if CPdatatime_fen_int == 0:  #如果是0分，则输出“00”
                CPdatatime_fen_str = "00"
            else:
                CPdatatime_fen_int_str = str((CPdatatime_fen_int // 10) * 10)   #获取10分钟字符串
                CPdatatime_fen_int_str_len = len(CPdatatime_fen_int_str)
                if CPdatatime_fen_int_str_len == 1:
                    CPdatatime_fen_str = "0%s"% CPdatatime_fen_int_str
                else:
                    CPdatatime_fen_str = CPdatatime_fen_int_str
            CPdatatime_str = "%s%s00"%(CPdatatime_hour_str,CPdatatime_fen_str)
            print("10分钟数据时间串：")
            print(CPdatatime_str)

        elif self.CPtime == "xiaoshi":
            CPdatatime = datetime.datetime.now().strftime('%Y%m%d%H')
            CPdatatime_str= str(CPdatatime)
            CPdatatime_str = "%s0000" % CPdatatime_str
            print("小时数据时间串：")
            print(CPdatatime_str)

        return CPdatatime_str

    def shujuduanCPyinzi(self):
        """
        CPyinzi
        :return:
        """
        CPyinzi = "w01001-Rtd=63.0, w01001-Flag=N; w01003-Rtd =63.0,w01003-Flag=N; w01009-Rtd =63.0,w01009-Flag=N; w01010-Rtd =63.0,w01010-Flag=N;"
        CPyinzi = self.CPyinzi
        return CPyinzi


    # 数据段_指令参数 CP
    def shujuduanCP(self):
        """
        CP=&&数据区&&，数据区定义见 6.6 章节
        :return:
        """
        cp = """&&DataTime=20160801085857;w01001-Rtd=63.0, w01001-Flag=N; w01003-Rtd =63.0,w01003-Flag=N; w01009-Rtd =63.0,w01009-Flag=N; w01010-Rtd =63.0,w01010-Flag=N;&&"""

        cp = """&&DataTime=%s;%s&&"""\
             %(self.shujuduanCPdatatime(),self.shujuduanCPyinzi())

        return cp



    #数据段
    def shujuduan(self):
        shujuduan= "QN=20160801085857223;ST=21;CN=1062;PW=123456;MN=A220582_0001;Flag=9;CP=&&RtdInterval=10&&"
        return shujuduan

    def shujuduanMain(self):
        shujuduan = """QN=%s;ST=%s;CN=%s;PW=%s;MN=%s;Flag=%s;CP=%s"""\
                      %(self.shujuduanQN(),self.shujuduanST(),self.shujuduanCN(),
                        self.shujuduanPW(),self.shujuduanMN(),self.shujuduanFlag(),
                        self.shujuduanCP()
                        )
        # shujuduan = "QN=20160801085857223;ST=21;CN=1062;PW=123456;MN=A220582_0001;Flag=9;CP=&&RtdInterval=10&&"

        print(shujuduan)
        return shujuduan

    #数据段长度
    def shujuduanchangdu(self):
        shujuduan = self.shujuduanMain()
        shujuduan_ascii_count = 0  # 用来记录ascii个数
        for ch in shujuduan:
            if ord(ch) <= 127:
                shujuduan_ascii_count += 1
        print("ascii字符个数是：",shujuduan_ascii_count)
        shujuduanchandu_str = str(shujuduan_ascii_count)
        shujuduanchandu_str_wei = len( shujuduanchandu_str)

        if shujuduanchandu_str_wei == 1:
            shujuduanchandu_str = "000%s" % shujuduanchandu_str
        elif shujuduanchandu_str_wei == 2:
            shujuduanchandu_str = "00%s" % shujuduanchandu_str
        elif shujuduanchandu_str_wei == 3:
            shujuduanchandu_str = "0%s" % shujuduanchandu_str
        elif shujuduanchandu_str_wei == 4:
            shujuduanchandu_str = "%s" % shujuduanchandu_str
        else:
            shujuduanchandu_str = None
            print("错误：数据段的ASCII字符个数值最大应该为9999，而实际超过9999")
        print(shujuduanchandu_str)
        return shujuduanchandu_str


    #数据段CRC校验
    def shujuduancrc16(self):  #进行crc校验，invert为True表示校验码按照先高字节后低字节的顺序存放， False表示校验码按照先低字节后高字节的顺序存放
        x = self.shujuduanMain()
        print(x)
        crc_reg = 0xFFFF
        b = 0xA001
        for x_byte in x:
            # print("x_byte:"+x_byte)
            # time.sleep(30000)
            crc_reg >>=8
            crc_reg ^= ord(x_byte)

            for i in range(8):
                last = crc_reg  % 2
                crc_reg >>= 1
                if last == 1:
                    crc_reg ^= b
        s = hex(crc_reg).upper()
        print(s)
        s_list = s.split("X")
        print(s_list)
        s_list_two = s_list[1]
        s_list_two_str = str(s_list_two)
        print(s_list_two_str)
        s_list_two_str_wei = len(s_list_two_str)
        if s_list_two_str_wei == 1:
            s_two = "000%s" % s_list_two_str
        elif s_list_two_str_wei == 2:
            s_two = "00%s" % s_list_two_str
        elif s_list_two_str_wei == 3:
            s_two = "0%s" % s_list_two_str
        elif s_list_two_str_wei == 4:
            s_two = "%s" % s_list_two_str
        else:
            s_two = None
            print("错误：数据段的CRC校验值最大应该为4位，而实际超过4位")
        s = "0X%s" % s_two
        print(s)
        result = s[4:6] + s[2:4] if self.invert == False else s[2:4] + s[4:6]
        print("--------------------------------")
        print("CRCjiaoyanjieguo")
        print(result)
        print("--------------------------------")
        return  result


    #包尾
    def baowei(self):
        return "\\r\\n"  #固定为<CR><LF>（回车，换行）

    def shujuMain(self):
        shujuduan = """%s%s%s%s%s"""\
                      %(self.baotou(),self.shujuduanchangdu(),self.shujuduanMain(),
                        self.shujuduancrc16(),self.baowei())
        print(shujuduan)
        return shujuduan


if __name__ == '__main__':
    ST="21"
    CN="2011"
    PW="123456"
    MN="A220582_0001"
    Flag="9"
    inver = True
    CPtime = "xiaoshi"
    CPyinzi = "w01001-Rtd=63.0, w01001-Flag=N; w01003-Rtd =63.0,w01003-Flag=N; w01009-Rtd =63.0,w01009-Flag=N; w01010-Rtd =63.0,w01010-Flag=N;"

    tx =  TongXinXieYi(ST,CN,PW,MN,Flag,inver,CPtime,CPyinzi)
    print(tx.shujuMain())
    shujuduan = "QN=20160801085857223;ST=21;CN=1062;PW=123456;MN=A220582_0001;Flag=9;CP=&&RtdInterval=10&&"

    print(len(shujuduan))
    #
    # print(tx.baotou())
    # print(tx.shujuduanchangdu())
    # print(tx.shujuduancrc16(True))
    # print(tx.shujuduancrc16(False))
    # print(tx.baowei())
    # print(tx.shujuduanQN())
    # print(tx.shujuduanQN())
    # crc_reg = 0xFFFF
    # crc_reg >>= 8
    # # for i in range(8):
    # #     crc_reg >>= 1
    # print(crc_reg)
    # a=1
    # a_type = type(a)
    # print(a_type)
    # print(type(a_type))
    # if str(a_type) == "<class 'int'>":
    #     print("deng")
    # else:
    #     print("gun")