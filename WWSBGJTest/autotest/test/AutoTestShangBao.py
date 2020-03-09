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
import time

from WWSBGJTest.util.getTimeStr import GetTimeStr
from WWSBGJTest.util.shangBaoGongju import TongXinXieYi
from depend.shangbaogongjudepend.shangbaoyinzi import ShangBaoYinZi,shangbaoyinzi
from depend.shangbaogongjudepend.getmnfromsjk import getNM
from depend.shangbaogongjudepend.getsqlyinzi import getSQLYinZi
from WWSBGJTest.util.operationMyDB import OperationMyDB


# 去掉首位的0的递归
def delelezoro(shuzhi):
    if shuzhi[0] == '0':
        shuzhi = shuzhi[1:]
        delelezoro(shuzhi)
    print(shuzhi)
    return shuzhi

#字典中的键值对大写转为小写
def capital_to_lower(dict_info):
    new_dict = {}
    for i,j in dict_info.items():
        new_dict[str(i).lower()] = str(j).lower()
    return new_dict



class TestShangBaoShuJuClass(unittest.TestCase):  # 创建测试类

    @classmethod  # 类方法，只执行一次，但必须要加注解@classmethod,且名字固定为setUpClass
    def setUpClass(cls):
        pass

    @classmethod  # 类方法，只执行一次，但必须要加注解@classmethod,且名字固定为tearDownClass
    def tearDownClass(cls):
        pass




    def setUp(self):  # 每条用例执行测试之前都要执行此方法
        pass

    def tearDown(self):  # 每条用例执行测试之后都要执行此方法
        pass



    #定义点击返回函数
    def defineshangbaoshuju(self,shujuduan_st,shujuduan_cn,shujuduan_pw,
                            shujuduan_mn,shujuduan_flag,is_check_crc,
                            shujuduan_cp_datatime_type,sbyzid,
                            forcount, time_delay, mn_counts,actual_data_sql_id,
                            dele_ziduan,actual_data_count,actual_data_delay_time,
                            tcp_host,tcp_port):
        actual_data_count_int = int(actual_data_count)
        #获取因子串
        #第一次上报数据
        sbyz = ShangBaoYinZi()
        yinzi_list = sbyz.shangbaoyinzi(sbyzid)
        CPyinzi = ''.join(yinzi_list)
        print(CPyinzi)
        # CPyinzi ="w01001-Rtd=63.0, w01001-Flag=N; w01003-Rtd =63.0,w01003-Flag=N;"
        txxy = TongXinXieYi(ST=shujuduan_st,CN=shujuduan_cn,PW=shujuduan_pw,
                            MN=shujuduan_mn,Flag=shujuduan_flag,invert=is_check_crc,
                            CPtime=shujuduan_cp_datatime_type,CPyinzi=CPyinzi)


        shangbaoshuju = txxy.shujuMain()
        print("上报数据：")
        print(shangbaoshuju)

        # tcp上报数据
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((str(tcp_host),int(tcp_port)))
            senddata = shangbaoshuju  # 上报数据
            s.send(senddata)  # 进行上报
            reposedata = s.recv(1024)  # 获取返回值
            s.close()
        except  Exception as e:
            reposedata = e

        # 存储上报的因子，源数据及返回结果,多数据上报时不用，设备数小于10时，保存数据库，测试流程时用，超过10个设备，数据不进行数据库保存
        if mn_counts < 10:
            from shangbaoshuju.models import StoreSBShuJu
            ssbsj = StoreSBShuJu()
            ssbsj.shujuduan_mn = shujuduan_mn
            ssbsj.sb_yinzi = CPyinzi
            ssbsj.sb_shuju = shangbaoshuju
            ssbsj.sb_ret = reposedata
            ssbsj.save()

            # 后续数据对比
            #获取输入因子值为字典
            #将因子list遍历并输入成字典
            yinzi_list_len = len(yinzi_list)
            pre_yinzi_dict = {}
            if yinzi_list_len>0:
                for i in range(yinzi_list_len):
                    yinzi_list_one_list = yinzi_list[i].split(",")
                    yinzi_list_one_list_len = len(yinzi_list_one_list)
                    if yinzi_list_one_list_len > 1:
                        #将最后一项的分号去掉
                        yinzi_list_one_list[yinzi_list_one_list_len - 1] = yinzi_list_one_list[yinzi_list_one_list_len-1].strip(";")

                        #将所有项的中的字母转为小写
                        for i in range(yinzi_list_one_list_len):
                            yinzi_list_one_list[i] = yinzi_list_one_list[i].lower()
                        print("因子一项列表数据：")
                        print(yinzi_list_one_list)

                        #将每一项转化为字典保存
                        for i in range(yinzi_list_one_list_len):
                            yinzi_list_one_list_dict_list = yinzi_list_one_list[i].split("=")
                            dict_key = yinzi_list_one_list_dict_list[0]
                            dick_value = yinzi_list_one_list_dict_list[1]
                            pre_yinzi_dict[dict_key]=dick_value

                    else:
                        print("因子参数为无")
            else:
                print("因子参数为无")

            print("等待%s秒" % time_delay)
            time.sleep(int(time_delay))

            #进行第二次或者更多次数据上报
            if actual_data_count_int > 1:
                for i in range(1,actual_data_count_int):
                    sbyz_for = ShangBaoYinZi()
                    yinzi_list_for = sbyz_for.shangbaoyinzi(sbyzid)
                    CPyinzi_for = ''.join(yinzi_list_for)
                    print(CPyinzi_for)
                    # CPyinzi ="w01001-Rtd=63.0, w01001-Flag=N; w01003-Rtd =63.0,w01003-Flag=N;"
                    txxy = TongXinXieYi(ST=shujuduan_st, CN=shujuduan_cn, PW=shujuduan_pw,
                                        MN=shujuduan_mn, Flag=shujuduan_flag, invert=is_check_crc,
                                        CPtime=shujuduan_cp_datatime_type, CPyinzi=CPyinzi_for)

                    shangbaoshuju_for = txxy.shujuMain()
                    print("第%s次上报数据："% str(i+1))
                    print(shangbaoshuju_for)

                    # tcp上报数据
                    try:
                        s_for = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        s_for.connect((str(tcp_host),int(tcp_port)))
                        senddata_for = shangbaoshuju_for  # 上报数据
                        s_for.send(senddata_for)  # 进行上报
                        reposedata_for = s_for.recv(1024)  # 获取返回值
                        s_for.close()
                    except  Exception as e_for:
                        reposedata_for = e_for

                    # 存储上报的因子，源数据及返回结果,多数据上报时不用，设备数小于10时，保存数据库，测试流程时用，超过10个设备，数据不进行数据库保存
                    if mn_counts < 10:
                        from shangbaoshuju.models import StoreSBShuJu
                        ssbsj = StoreSBShuJu()
                        ssbsj.shujuduan_mn = shujuduan_mn
                        ssbsj.sb_yinzi = CPyinzi_for
                        ssbsj.sb_shuju = shangbaoshuju_for
                        ssbsj.sb_ret = reposedata_for
                        ssbsj.save()

                        # 后续数据对比
                        # 获取输入因子值为字典
                        # 将因子list遍历并输入成字典
                        yinzi_list_len_for = len(yinzi_list_for)
                        pre_yinzi_dict_for = {}
                        if yinzi_list_len_for > 0:
                            for i in range(yinzi_list_len_for):
                                yinzi_list_one_list_for = yinzi_list_for[i].split(",")
                                yinzi_list_one_list_len_for = len(yinzi_list_one_list_for)
                                if yinzi_list_one_list_len_for > 1:
                                    # 将最后一项的分号去掉
                                    yinzi_list_one_list_for[yinzi_list_one_list_len_for - 1] = yinzi_list_one_list_for[
                                        yinzi_list_one_list_len_for - 1].strip(";")

                                    # 将所有项的中的字母转为小写
                                    for i in range(yinzi_list_one_list_len_for):
                                        yinzi_list_one_list_for[i] = yinzi_list_one_list_for[i].lower()
                                    print("因子一项列表数据：")
                                    print(yinzi_list_one_list_for)

                                    # 将每一项转化为字典保存
                                    for i in range(yinzi_list_one_list_len_for):
                                        yinzi_list_one_list_dict_list_for = yinzi_list_one_list_for[i].split("=")
                                        dict_key_for = yinzi_list_one_list_dict_list_for[0]
                                        dick_value_for = yinzi_list_one_list_dict_list_for[1]
                                        pre_yinzi_dict_for[dict_key_for] = dick_value_for

                                else:
                                    print("因子参数为无")
                        else:
                            print("因子参数为无")
                            print("等待%s秒" % time_delay)
                            time.sleep(int(time_delay))

            #循环终止



            print("预期因子字典")
            print(pre_yinzi_dict)
            print(type(pre_yinzi_dict))

            pre_yinzi_dict_order_list = sorted(pre_yinzi_dict.items(), key=lambda x: x[0], reverse=False)  # 按字典集合中，每一个元组的第一个元素（即键排序，第二个元素为值，即值排序）排列
            print("预期因子字典按照键排序后的字典列表")
            print(pre_yinzi_dict_order_list)
            print(type(pre_yinzi_dict_order_list))

            #从上报数据到数据库录入数据预估耗时
            if actual_data_count_int > 0:
                for i in range(0,actual_data_count_int):
                    print("等待%s秒" % actual_data_delay_time)
                    time.sleep(int(actual_data_delay_time))

            # 通过数据库获取上传的因子
            # 获取目标数据库中上传的因子数值：
            # 获取表的表头及字段内容组成一个list
            # 获取表因子值，并转换字典
            biao_content_arg_list = getSQLYinZi(actual_data_sql_id)
            op = OperationMyDB(*biao_content_arg_list)
            biao_content = op.connectMyDBAndSelectAndReturnWithBiaoTou()
            print("表的内容：")
            print(biao_content)
            #将获取一条数据
            actural_yinzi_dict = biao_content[0]
            print("actural_yinzi_dict:")
            print(actural_yinzi_dict)
            print(type(actural_yinzi_dict))
            #去掉字典中某些键
            print("dele_ziduan:")
            print(dele_ziduan)
            if dele_ziduan != "":
                dele_ziduan_list = dele_ziduan.split(",")
                for dele_ziduan_one in dele_ziduan_list:
                    actural_yinzi_dict.pop(dele_ziduan_one)
                    print("删除%s字段"%dele_ziduan_one)
                print("删除某些字段后的actural_yinzi_dict:")
                print(actural_yinzi_dict)
                print(type(actural_yinzi_dict))
            #字典键值变为小写
            actural_yinzi_dict = capital_to_lower(actural_yinzi_dict)
            print("键值对变为小写后的actural_yinzi_dict:")
            print(actural_yinzi_dict)

            #字典按照键排序
            actural_yinzi_dict_order_list = sorted(actural_yinzi_dict.items(), key=lambda x: x[0], reverse=False)  # 按字典集合中，每一个元组的第一个元素（即键排序，第二个元素为值，即值排序）排列
            print("实际因子字典按照键排序后的字典列表")
            print(actural_yinzi_dict_order_list)
            print(type(actural_yinzi_dict_order_list))

            # actural_yinzi_dict_list = [('94102-flag', '1'), ('94102-rtd', '1.0'), ('w01001-flag', 'n'), ('w01001-rtd', '200.9'), ('w01003-flag', 'd'), ('w01003-rtd', '99.4')]

            # actural_yinzi_dict_list = pre_yinzi_dict_order_list

            #对比两个字典列表的值
            # list_diff= list(pre_yinzi_dict_order_list-actural_yinzi_dict_list)
            print("对比结果")
            print(pre_yinzi_dict_order_list==actural_yinzi_dict_order_list)
            # self.assertTrue(pre_yinzi_dict_order_list==actural_yinzi_dict_list,msg="实际与预期不一致")
            self.assertEqual(pre_yinzi_dict_order_list,actural_yinzi_dict_order_list,msg="实际与预期不一致")
            #使用对比

        # 存储上报的因子，源数据及返回结果,多数据上报时不用，设备数小于10时，保存数据库，测试流程时用，超过10个设备，数据不进行数据库保存


    # def test001(self):
    #     print("第一条测试用例")
    #     self.definedepend(self.dependid)

    @staticmethod    #根据不同的参数生成测试用例
    def getTestFunc(shujuduan_st,shujuduan_cn,shujuduan_pw,
                            shujuduan_mn,shujuduan_flag,is_check_crc,
                            shujuduan_cp_datatime_type,sbyzid,
                            forcount, time_delay, mn_counts,
                    actual_data_sql_id,dele_ziduan,
                    actual_data_count,actual_data_delay_time,
                    tcp_host,tcp_port):

        def func(self):
            self.defineshangbaoshuju(shujuduan_st,shujuduan_cn,shujuduan_pw,
                            shujuduan_mn,shujuduan_flag,is_check_crc,
                            shujuduan_cp_datatime_type,sbyzid,
                            forcount, time_delay, mn_counts,actual_data_sql_id,dele_ziduan,
                                     actual_data_count,actual_data_delay_time,
                                     tcp_host,tcp_port)
        return func

def __generateTestCases():
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

        for i in range(1, int(forcount) + 1):  # 循环，从1开始
            if len(str(i)) == 1:
                forcount_i = '0000%s' % i
            elif len(str(i)) == 2:
                forcount_i = '000%s' % i
            elif len(str(i)) == 3:
                forcount_i = '00%s' % i
            elif len(str(i)) == 4:
                forcount_i = '0%s' % i
            elif len(str(i)) == 5:
                forcount_i = '%s' % i
            else:
                forcount_i = 'Id已经超过5位数，请重新定义'

            # 对mn进行分离从操作
            nmtype = shangbaoshujutestcase.mn_type
            print("mn类型")
            print(nmtype)
            if nmtype == "P0":
                shujuduan_mn_content = shangbaoshujutestcase.shujuduan_mn
                shujuduan_mn_list = shujuduan_mn_content.split(',')
            elif nmtype == "P1":
                print("通过SQL语句从数据库中获取nm")
                opdbarg_list = getNM(shangbaoshujutestcase.mn_sql_id)
                opdb = OperationMyDB(*opdbarg_list)
                getmn_result = opdb.connectMyDBAndSelectAndReturnQuan()
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
                # 根据上下限自动生成MN
                # 1.先去掉0判断大小，上下限的字符串位数需要一致
                mn_auto_make_down_len = len(mn_auto_make_down)
                mn_auto_make_down = delelezoro(mn_auto_make_down)
                mn_auto_make_down_int = int(mn_auto_make_down)

                mn_auto_make_up_len = len(mn_auto_make_up)
                mn_auto_make_up = delelezoro(mn_auto_make_up)
                mn_auto_make_up_int = int(mn_auto_make_up)

                mn_auto_make_interval_int = int(mn_auto_make_interval)

                if mn_auto_make_down_len == mn_auto_make_up_len:
                    # 进行数字比较
                    if mn_auto_make_down_int <= mn_auto_make_up_int:
                        # 根据间隔生成数据
                        if mn_auto_make_interval_int == 0 or mn_auto_make_down_int == mn_auto_make_up_int:
                            # 间隔为0处理
                            shujuduan_mn_list = []
                            shujuduan_mn_list.append("%s%s" % (mn_auto_make_base, mn_auto_make_up))
                        else:
                            shujuduan_mn_list = []
                            # 获取第一项
                            shujuduan_mn_list.append("%s%s" % (mn_auto_make_base, mn_auto_make_down))
                            # 获取中间项
                            for i in range(mn_auto_make_down_int + 1, mn_auto_make_up_int, mn_auto_make_interval_int):
                                nm_auto_zhongjian = i
                                nm_auto_zhongjian_str = str(nm_auto_zhongjian)
                                nm_auto_zhongjian_str_withzero = nm_auto_zhongjian_str.zfill(mn_auto_make_down_len)
                                shujuduan_mn_list.append("%s%s" % (mn_auto_make_base, nm_auto_zhongjian_str_withzero))

                            # 获取最后一项
                            shujuduan_mn_list.append("%s%s" % (mn_auto_make_base, mn_auto_make_up))
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
                print("MN:%s" % shujuduan_mn_list[j - 1])
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
                args.append(shujuduan_mn_list[j - 1])
                args.append(shangbaoshujutestcase.shujuduan_flag)
                args.append(shangbaoshujutestcase.is_check_crc)
                args.append(shangbaoshujutestcase.shujuduan_cp_datatime_type)
                args.append(shangbaoshujutestcase.id)
                args.append(i)
                args.append(shangbaoshujutestcase.time_delay)
                args.append(shujuduan_mn_list_len)
                args.append(shangbaoshujutestcase.actual_data_sql_id)
                args.append(shangbaoshujutestcase.dele_zidian)
                args.append(shangbaoshujutestcase.actual_data_count)
                args.append(shangbaoshujutestcase.actual_data_delay_time)
                args.append(shangbaoshujutestcase.tcp_host)
                args.append(shangbaoshujutestcase.tcp_port)
                setattr(TestShangBaoShuJuClass,
                        'test_func_%s%s_%s-%s_%s-%s' % ("caseid",shangbaoshujutestcaseid,shujuduan_mn_list[j - 1],shujuduan_mn_j,"count",forcount_i),
                        TestShangBaoShuJuClass.getTestFunc(*args))  # 通过setattr自动为TestCase类添加成员方法，方法以“test_func_”开头


__generateTestCases()

if __name__ == '__main__':
    print("hello world")
    unittest.main()












