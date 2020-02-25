import unittest
# ----------------------------------------------------------------------
import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wanwenyc.settings")
django.setup()
# ----------------------------------------------------------------------
#独运行某一个py文件时会出现如下错误：django.core.exceptions.AppRegistryNotReady: Apps aren't loaded yet.，以上内容可以解决此问题,加载django中的App
import json
import socket
import sys

from threading import Thread,Lock
import time


from WWSBGJTest.util.getTimeStr import GetTimeStr
from WWSBGJTest.util.shangBaoGongju import TongXinXieYi
from depend.shangbaogongjudepend.shangbaoyinzi import ShangBaoYinZi,shangbaoyinzi
from depend.shangbaogongjudepend.getmnfromsjk import getNM
from WWSBGJTest.util.operationMyDB import OperationMyDB


# 去掉首位的0的递归
def delelezoro(shuzhi):
    if shuzhi[0] == '0':
        shuzhi = shuzhi[1:]
        delelezoro(shuzhi)
    print(shuzhi)
    return shuzhi


class ShangBaoShuJuThread(Thread):
    def __init__(self,shujuduan_st,shujuduan_cn,shujuduan_pw,
                 shujuduan_mn,shujuduan_flag,is_check_crc,
                 shujuduan_cp_datatime_type,sbyzid,
                 forcount,time_delay,mn_counts):
        Thread.__init__(self)
        self.shujuduan_st = shujuduan_st
        self.shujuduan_cn = shujuduan_cn
        self.shujuduan_pw = shujuduan_pw
        self.shujuduan_mn = shujuduan_mn
        self.shujuduan_flag = shujuduan_flag
        self.is_check_crc = is_check_crc
        self.shujuduan_cp_datatime_type = shujuduan_cp_datatime_type
        self.sbyzid = sbyzid
        self.forcount = forcount
        self.time_delay = time_delay
        self.mn_counts = mn_counts
        self.mysql_lock = Lock()





    #定义点击返回函数
    def run(self):
        print("开始线程：%s" % self.name)
        for i in range(0,int(self.forcount)):
            #获取因子串
            sbyz = ShangBaoYinZi()
            yinzi_list = sbyz.shangbaoyinzi(self.sbyzid)
            CPyinzi = ''.join(yinzi_list)
            print("上报因子：")
            print(CPyinzi)
            # CPyinzi ="w01001-Rtd=63.0, w01001-Flag=N; w01003-Rtd =63.0,w01003-Flag=N;"
            txxy = TongXinXieYi(ST=self.shujuduan_st,CN=self.shujuduan_cn,PW=self.shujuduan_pw,
                                MN=self.shujuduan_mn,Flag=self.shujuduan_flag,invert=self.is_check_crc,
                                CPtime=self.shujuduan_cp_datatime_type,CPyinzi=CPyinzi)

            shangbaoshuju = txxy.shujuMain()
            print("上报数据：")
            print(shangbaoshuju)

            #tcp上报数据
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect(("192.168.8.205", 57001))
                senddata = shangbaoshuju   #上报数据
                s.send(senddata)  #进行上报
                reposedata = s.recv(1024)   #获取返回值
                s.close()
            except  Exception as e:
                reposedata = e

            #存储上报的因子，源数据及返回结果,多数据上报时不用，设备数小于10时，保存数据库，测试流程时用，超过10个设备，数据不进行数据库保存
            if self.mn_counts < 10:
                from shangbaoshuju.models import StoreSBShuJu
                ssbsj = StoreSBShuJu()
                ssbsj.shujuduan_mn = self.shujuduan_mn
                ssbsj.sb_yinzi = CPyinzi
                ssbsj.sb_shuju = shangbaoshuju
                ssbsj.sb_ret = reposedata
                ssbsj.save()

                #后续数据对比
                #通过数据库获取上传的因子
                #获取目标数据库中上传的因子数值：
                #获取表的表头及字段内容组成一个list
                #获取表因子值，以CPyinzi形式显示

            #存储上报的因子，源数据及返回结果,多数据上报时不用，设备数小于10时，保存数据库，测试流程时用，超过10个设备，数据不进行数据库保存

            print("等待%s秒" % self.time_delay)
            time.sleep(int(self.time_delay))


        print("退出线程：%s" % self.name)



    # def test001(self):
    #     print("第一条测试用例")
    #     self.definedepend(self.dependid)

    # @staticmethod    #根据不同的参数生成测试用例
    # def getTestFunc(shujuduan_st,shujuduan_cn,shujuduan_pw,
    #                         shujuduan_mn,shujuduan_flag,is_check_crc,
    #                         shujuduan_cp_datatime_type,sbyzid):
    #
    #     def func(self):
    #         self.defineshangbaoshuju(shujuduan_st,shujuduan_cn,shujuduan_pw,
    #                         shujuduan_mn,shujuduan_flag,is_check_crc,
    #                         shujuduan_cp_datatime_type,sbyzid)
    #     return func

# def __generateTestCases():
#     from shangbaoshuju.models import ShangBaoShuJu
#
#     shangbaoshujutestcase_all = ShangBaoShuJu.objects.filter(id=2).order_by('id')
#
#     for shangbaoshujutestcase in shangbaoshujutestcase_all:
#         forcount = shangbaoshujutestcase.forcount
#         print(forcount)
#         starttime = GetTimeStr().getTimeStr()
#         if len(str(shangbaoshujutestcase.id)) == 1:
#             shangbaoshujutestcaseid = '0000%s' % shangbaoshujutestcase.id
#         elif len(str(shangbaoshujutestcase.id)) == 2:
#             shangbaoshujutestcaseid = '000%s' % shangbaoshujutestcase.id
#         elif len(str(shangbaoshujutestcase.id)) == 3:
#             shangbaoshujutestcaseid = '00%s' % shangbaoshujutestcase.id
#         elif len(str(shangbaoshujutestcase.id)) == 4:
#             shangbaoshujutestcaseid = '0%s' % shangbaoshujutestcase.id
#         elif len(str(shangbaoshujutestcase.id)) == 5:
#             shangbaoshujutestcaseid = '%s' % shangbaoshujutestcase.id
#         else:
#             shangbaoshujutestcaseid = 'Id已经超过5位数，请重新定义'
#
#         for i in range(1, int(forcount) + 1):  # 循环，从1开始
#             if len(str(i)) == 1:
#                 forcount_i = '0000%s' % i
#             elif len(str(i)) == 2:
#                 forcount_i = '000%s' % i
#             elif len(str(i)) == 3:
#                 forcount_i = '00%s' % i
#             elif len(str(i)) == 4:
#                 forcount_i = '0%s' % i
#             elif len(str(i)) == 5:
#                 forcount_i = '%s' % i
#             else:
#                 forcount_i = 'Id已经超过5位数，请重新定义'
#
#             args = []
#             args.append(shangbaoshujutestcase.shujuduan_st)
#             args.append(shangbaoshujutestcase.shujuduan_cn)
#             args.append(shangbaoshujutestcase.shujuduan_pw)
#             args.append(shangbaoshujutestcase.shujuduan_mn)
#             args.append(shangbaoshujutestcase.shujuduan_flag)
#             args.append(shangbaoshujutestcase.is_check_crc)
#             args.append(shangbaoshujutestcase.shujuduan_cp_datatime_type)
#             args.append(shangbaoshujutestcase.id)
#             setattr(TestShangBaoShuJuClass,
#                     'test_func_%s_%s' % (shangbaoshujutestcaseid,forcount_i),
#                     TestShangBaoShuJuClass.getTestFunc(*args))  # 通过setattr自动为TestCase类添加成员方法，方法以“test_func_”开头
#
#
# __generateTestCases()

if __name__ == '__main__':
    print("hello world")
    # unittest.main()
    args_list = []
    from shangbaoshuju.models import ShangBaoShuJu

    shangbaoshujutestcase_all = ShangBaoShuJu.objects.filter(id=1).order_by('id')

    for shangbaoshujutestcase in shangbaoshujutestcase_all:
        forcount = shangbaoshujutestcase.forcount
        print(forcount)
        starttime = GetTimeStr().getTimeStr()
        if len(str(shangbaoshujutestcase.id)) == 1:
            shangbaoshujutestcaseid = '0000%s' % shangbaoshujutestcase.id
        elif len(str(shangbaoshujutestcase.id)) == 2:
            shangbaoshujutestcaseid = '000%s' % shangbaoshujutestcase.id
        elif len(str(shangbaoshujutestcase.id)) == 3:
            shangbaoshujutestcaseid = '00%s' % shangbaoshujutestcase.id
        elif len(str(shangbaoshujutestcase.id)) == 4:
            shangbaoshujutestcaseid = '0%s' % shangbaoshujutestcase.id
        elif len(str(shangbaoshujutestcase.id)) == 5:
            shangbaoshujutestcaseid = '%s' % shangbaoshujutestcase.id
        else:
            shangbaoshujutestcaseid = 'Id已经超过5位数，请重新定义'

        # 对mn进行分离从操作
        nmtype = shangbaoshujutestcase.mn_type
        print("mn类型")
        print(nmtype)
        if nmtype == "P0":
            shujuduan_mn_content = shangbaoshujutestcase.shujuduan_mn
            shujuduan_mn_list = shujuduan_mn_content.split(',')
        elif nmtype == "P1":
            print("通过SQL语句从数据库中获取nm")
            # shujuduan_mn_list = []
            opdbarg_list = getNM(shangbaoshujutestcase.mn_sql_id)
            opdb = OperationMyDB(*opdbarg_list)
            getmn_result = opdb.connectMyDBAndSelectAndReturn()
            opdb.closeCursorAndConnect()
            print("通过数据库获取到的数MN：")
            print(getmn_result)
            shujuduan_mn_list = []
            for getmnone in getmn_result:
                for getmnone_one in getmnone:
                    if getmnone_one != '':
                        shujuduan_mn_list.append(getmnone_one)

            print("数据库获取转化生成的MN数列：")
            print(shujuduan_mn_list)
            # shujuduan_mn_list = ['1212313','132ds1231']
        elif nmtype == "P2":
            print("通过输入上下限值自动生成nm")
            mn_auto_make_base = shangbaoshujutestcase.mn_auto_make_base
            mn_auto_make_up = shangbaoshujutestcase.mn_auto_make_up
            mn_auto_make_down = shangbaoshujutestcase.mn_auto_make_down
            mn_auto_make_interval = shangbaoshujutestcase.mn_auto_make_interval
            #根据上下限自动生成MN
            #1.先去掉0判断大小，上下限的字符串位数需要一致
            mn_auto_make_down_len = len(mn_auto_make_down)
            mn_auto_make_down = delelezoro(mn_auto_make_down)
            mn_auto_make_down_int = int(mn_auto_make_down)

            mn_auto_make_up_len = len(mn_auto_make_up)
            mn_auto_make_up = delelezoro(mn_auto_make_up)
            mn_auto_make_up_int = int(mn_auto_make_up)

            mn_auto_make_interval_int = int(mn_auto_make_interval)

            if mn_auto_make_down_len == mn_auto_make_up_len:
                #进行数字比较
                if mn_auto_make_down_int <= mn_auto_make_up_int:
                    #根据间隔生成数据
                    if mn_auto_make_interval_int ==0 or mn_auto_make_down_int==mn_auto_make_up_int:
                        #间隔为0处理
                        shujuduan_mn_list = []
                        shujuduan_mn_list.append("%s%s"%(mn_auto_make_base,mn_auto_make_up))
                    else:
                        shujuduan_mn_list = []
                        #获取第一项
                        shujuduan_mn_list.append("%s%s"%(mn_auto_make_base,mn_auto_make_down))
                        #获取中间项
                        for i in range(mn_auto_make_down_int+1,mn_auto_make_up_int,mn_auto_make_interval_int):
                            nm_auto_zhongjian = i
                            nm_auto_zhongjian_str = str(nm_auto_zhongjian)
                            nm_auto_zhongjian_str_withzero = nm_auto_zhongjian_str.zfill(mn_auto_make_down_len)
                            shujuduan_mn_list.append("%s%s"%(mn_auto_make_base,nm_auto_zhongjian_str_withzero))

                        #获取最后一项
                        shujuduan_mn_list.append("%s%s"%(mn_auto_make_base,mn_auto_make_up))
                else:
                    print("上限值不得小于下限值")
                    shujuduan_mn_list = []
            else:
                print("上下限位数必须一致")
                shujuduan_mn_list = []

        print("MN数列：")
        print(shujuduan_mn_list)
        shujuduan_mn_list_len = len(shujuduan_mn_list)
        print("shujuduan_mn_list_len:%s" % shujuduan_mn_list_len)
        for j in range(1, shujuduan_mn_list_len + 1):
            print("MN:%s" % shujuduan_mn_list[j-1])
            if len(str(j)) == 1:
                shujuduan_mn_j = '0000%s' % j
            elif len(str(j)) == 2:
                shujuduan_mn_j = '000%s' % j
            elif len(str(j)) == 3:
                shujuduan_mn_j = '00%s' % j
            elif len(str(j)) == 4:
                shujuduan_mn_j = '0%s' % j
            elif len(str(j)) == 5:
                shujuduan_mn_j = '%s' % j
            else:
                shujuduan_mn_j = 'Id已经超过5位数，请重新定义'

            args = []
            args.append(shangbaoshujutestcase.shujuduan_st)
            args.append(shangbaoshujutestcase.shujuduan_cn)
            args.append(shangbaoshujutestcase.shujuduan_pw)
            args.append(shujuduan_mn_list[j-1])
            args.append(shangbaoshujutestcase.shujuduan_flag)
            args.append(shangbaoshujutestcase.is_check_crc)
            args.append(shangbaoshujutestcase.shujuduan_cp_datatime_type)
            args.append(shangbaoshujutestcase.id)
            args.append(shangbaoshujutestcase.forcount)
            args.append(shangbaoshujutestcase.time_delay)
            args.append(shujuduan_mn_list_len)
            args_list.append(args)

    print(args_list)
    args_list_len = len(args_list)

    #设置数据库最大连接数
    import pymysql
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root')
    cur = conn.cursor()
    # 通常，mysql的最大连接数默认是100, 最大可以达到16384。
    cur.execute(" show variables like '%max_connections%';")
    for r in cur.fetchall():
        print(r)
    cur.execute(" set GLOBAL max_connections = 10000;")
    for r in cur.fetchall():
        print(r)
    cur.execute(" flush privileges;")
    for r in cur.fetchall():
        print(r)
    cur.execute(" show variables like '%max_connections%';")
    for r in cur.fetchall():
        print(r)
    cur.close()
    conn.close()

    threads = []
    for i in range(0,args_list_len):
        ShangBaoShuJuThread(*args_list[i]).start()













