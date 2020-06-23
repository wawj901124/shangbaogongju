import unittest
# ----------------------------------------------------------------------
import os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wanwenyc.settings")
django.setup()
# ----------------------------------------------------------------------
# 独运行某一个py文件时会出现如下错误：django.core.exceptions.AppRegistryNotReady: Apps aren't loaded yet.，以上内容可以解决此问题,加载django中的App

from WWTest.util.getTimeStr import GetTimeStr


from WWQRSTest.util.autoModbus.autoModbus import AutoModbus


class TestShuCaiYiClass(unittest.TestCase):  # 创建测试类

    @classmethod  # 类方法，只执行一次，但必须要加注解@classmethod,且名字固定为setUpClass
    def setUpClass(cls):
        pass

    @classmethod  # 类方法，只执行一次，但必须要加注解@classmethod,且名字固定为tearDownClass
    def tearDownClass(cls):
        # cls.activeweb.closeBrowse()
        pass

    def setUp(self):  # 每条用例执行测试之前都要执行此方法
        pass

    def tearDown(self):  # 每条用例执行测试之后都要执行此方法
        pass

    def defineshucaiyi(self,
                           case_id,
                           depend_config_id
                        ):

        #通过协议配置模块获取配置相关信息
        from shucaiyidate.modelsorder import XieyiConfigDateOrder
        xieyiconfigdateorder = XieyiConfigDateOrder.objects.filter(id=depend_config_id)
        xieyiconfigdateorder_count = xieyiconfigdateorder.count()
        if xieyiconfigdateorder_count == 0:
            print("没有选择相关配置依赖，请选择相关配置依赖")
            assert False
        else:
            #获取配置信息
            for xieyiconfigdateorder_one in xieyiconfigdateorder:
                is_web_modify_xieyi = xieyiconfigdateorder_one.is_web_modify_xieyi
                web_type = xieyiconfigdateorder_one.web_type
                web_xieyi_name = xieyiconfigdateorder_one.web_xieyi_name
                web_xieyi_yinzi = xieyiconfigdateorder_one.web_xieyi_yinzi
                telnet_host_ip = xieyiconfigdateorder_one.telnet_host_ip
                telnet_username = xieyiconfigdateorder_one.telnet_username
                telnet_password = xieyiconfigdateorder_one.telnet_password
                xieyi_bin_dir = xieyiconfigdateorder_one.xieyi_bin_dir
                xieyi_name = xieyiconfigdateorder_one.xieyi_name
                xieyi_test_port = xieyiconfigdateorder_one.xieyi_test_port
                xieyi_device_id = xieyiconfigdateorder_one.xieyi_device_id
                com_port = xieyiconfigdateorder_one.com_port
                com_baudrate = xieyiconfigdateorder_one.com_baudrate
                com_bytesize = xieyiconfigdateorder_one.com_bytesize
                com_parity = xieyiconfigdateorder_one.com_parity
                com_stopbits = xieyiconfigdateorder_one.com_stopbits
                xieyi_db = xieyiconfigdateorder_one.xieyi_db
                xieyi_db_remote_path = xieyiconfigdateorder_one.xieyi_db_remote_path
                xieyi_db_table_name = xieyiconfigdateorder_one.xieyi_db_table_name
                tcp_server_ip = xieyiconfigdateorder_one.tcp_server_ip
                tcp_server_port = xieyiconfigdateorder_one.tcp_server_port
                tcp_receive_delay_min = xieyiconfigdateorder_one.tcp_receive_delay_min
                is_ftp_upload = xieyiconfigdateorder_one.is_ftp_upload
                is_close_xieyi = xieyiconfigdateorder_one.is_close_xieyi
                is_restart_xieyi = xieyiconfigdateorder_one.is_restart_xieyi
                is_com_recive_and_send = xieyiconfigdateorder_one.is_com_recive_and_send
                is_ftp_down_xieyi_file = xieyiconfigdateorder_one.is_ftp_down_xieyi_file
                is_assert_file_success = xieyiconfigdateorder_one.is_assert_file_success
                is_ftp_get_remote_db_file = xieyiconfigdateorder_one.is_ftp_get_remote_db_file
                is_assert_real_db_success = xieyiconfigdateorder_one.is_assert_real_db_success
                is_tcp_server_receive = xieyiconfigdateorder_one.is_tcp_server_receive
                is_assert_tcp_server_receive_success = xieyiconfigdateorder_one.is_assert_tcp_server_receive_success
                break



            #通过发送和接收数据部分获取发送和接收的数据以及预期结果的list
            from depend.shucaiyi.modelorderdepend.senderHexDataOrderDependClass import senderhexdataorderdepend
            sender_hex_data_order_list = senderhexdataorderdepend.makeSenderHexDataOrderList(case_id)

            xieyi_jiexi_expect_result_list = []
            for sender_hex_data_order_list_one in sender_hex_data_order_list:
                is_assert_expect = sender_hex_data_order_list_one[9]
                if is_assert_expect:  #如果进行结果断言
                    expect_one_list = sender_hex_data_order_list_one[3].split(",")
                    for expect_one in expect_one_list:
                        xieyi_jiexi_expect_result_list.append(expect_one)  #添加断言结果到预期校验数据列表中
            print("预期校验数据：")
            print(xieyi_jiexi_expect_result_list)


            xieyi_txt_file_name = '%s_%s.txt'%(xieyi_name,xieyi_test_port)

            # if com_send_date == None:
            #     com_send_hex_list = []
            # else:
            #     com_send_hex_list = com_send_date.split(",")
            #
            # if xieyi_jiexi_expect_result == None:
            #     xieyi_jiexi_expect_result_list = []
            # else:
            #     xieyi_jiexi_expect_result_list = xieyi_jiexi_expect_result.split(",")

            print("web_type:")
            print(web_type)

            #是否通过web修改协议
            if is_web_modify_xieyi:   #如果是，则需要通过web修改协议
                from depend.shucaiyi.dependwebconfig.webConfigClass import WebVSixConfig
                if web_type =="P2":  #如果是V6,则走v6的web程序
                    select_xie_yi = web_xieyi_name
                    select_jian_kong_yin_zi_list = web_xieyi_yinzi.split(",")
                    wc = WebVSixConfig(select_xie_yi, select_jian_kong_yin_zi_list)
                    wc.run()






            am = AutoModbus(
                telnet_host_ip=telnet_host_ip,
                telnet_username=telnet_username,
                telnet_password=telnet_password,
                xieyi_bin_dir=xieyi_bin_dir,
                xieyi_name=xieyi_name,
                xieyi_test_port=xieyi_test_port,
                xieyi_device_id = xieyi_device_id,
                com_port=com_port,
                com_baudrate=com_baudrate,
                com_bytesize=com_bytesize,
                com_parity=com_parity,
                com_stopbits=com_stopbits,
                # com_send_date_list=com_send_hex_list ,
                # com_expect_date=com_expect_date,

                xieyi_jiexi_expect_result_list=xieyi_jiexi_expect_result_list,

                xieyi_db=xieyi_db,
                xieyi_db_remote_path=xieyi_db_remote_path,
                xieyi_db_table_name=xieyi_db_table_name,

                tcp_server_ip=tcp_server_ip,
                tcp_server_port=tcp_server_port,
                tcp_receive_delay_min = tcp_receive_delay_min
            )
            ftp_up_load_file_list = [['/usr/app_install/collect/bin/text.txt','D:/pycharmproject/shangbaogongju/WWQRSTest/util/text.txt'],
                                     ['/usr/app_install/collect/bin/result1.txt','D:/pycharmproject/shangbaogongju/WWQRSTest/util/result1.txt']]
            from depend.shucaiyi.ftpUploadFileDependClass import ftpuploadfiledepend
            ftp_up_load_file_list = ftpuploadfiledepend.makeFtpUpliadFileList(depend_id=case_id)   #传入程序的id，获取上传文件列表
            #1.是否上传配置文件
            #1-1.上传配置文件之前先修改远程文件名称为备份文件名
            #1-2.上传配置文件
            #上传文件进行可执行命令
            #先分离远程文件目录，获取到目录和文件
            if ftp_up_load_file_list == []: #则说明没有填写上传文件路径，不进行文件上传
                pass
            else:
                if is_ftp_upload:   #如果需要上传文件
                    am.run_ftp_up_load_file_list(ftp_up_load_file_list)

            #如果进行web端操作


            #如果需要验证数据库和平台上报数据，需要先删除原数据库中已经存在的内容
            #然后重启，运行后续操作
            # 是否ftp下载实时数据
            # if is_ftp_get_remote_db_file:  #如果需要下载实时数据，那就需要先清除实时数据
            if is_assert_real_db_success:  # 是否验证实时数据，是，则需要先删除远程实时数据库的内容
                am.telnet_client_delete_real_or_rtd_db()  #删除原有实时数据库
            #是否上报平台
            # if is_tcp_server_receive:  #如果上报平台数据：
            if is_assert_tcp_server_receive_success:  # 是否验证平台上报内容，是，则需要清除已经存在的平台数据库
                am.telnet_client_delete_upload_db()   #删除原有上报平台数据

            if is_assert_real_db_success or is_assert_tcp_server_receive_success:  #如果需要验证实时数据库中的数据或需要验证平台上报内容，则需要删除原有数据后，重启
                am.telnet_client_restart_scy()


            #是否关闭默认启动的协议，一定要关闭吗  # 杀死科内特
            # if is_close_xieyi:
            if is_assert_file_success:  # 是否在协议文件中找到相应的解析内容,是，则需要关闭原有协议
                am.telnet_client_close_default_start_xieyi_common()  # 执行关闭协议通用命令
            # #是否关闭默认启动的协议，一定要关闭吗  #杀死科内特
            # from depend.shucaiyi.closeXieYiCommandDependClass import closexieyicommanddepend
            # close_xie_yi_commad_list = closexieyicommanddepend.makeCloseXieYiCommandList(depend_id=case_id)  #传入程序的id，获取关闭协议命令
            # if close_xie_yi_commad_list == []:  #则说明没有关闭命令，不执行关闭命令
            #     am.telnet_client_close_default_start_xieyi_common()  # 执行关闭协议通用命令
            #     pass
            # else:
            #     if is_close_xieyi:
            #
            #         mycommad_list = ['stop_guard','ps aux | grep %s | xargs kill -9 &>/dev/null &' % xieyi_name]
            #         am.telnet_client_close_default_start_xieyi(close_xie_yi_commad_list)  #执行关闭协议命令
            # if is_restart_xieyi:
            if is_assert_file_success:  # 是否在协议文件中找到相应的解析内容,是，则需要重启原有协议，并生成协议解析文件
                am.telnet_client_rstart_xieyi_common()  # 执行重启通用命令

            # #重启协议
            # from depend.shucaiyi.restartXieYiCommandDependClass import restartxieyicommanddepend
            # restart_xie_yi_commad_list = restartxieyicommanddepend.makeRestartXieYiCommandList(depend_id=case_id)
            # if restart_xie_yi_commad_list == []:  #则说明没有重启命令，不执行重启命令
            #     am.telnet_client_rstart_xieyi_common()  # 执行重启通用命令
            #     pass
            # else:
            #     if is_restart_xieyi:
            #         mycommad_list = ['cd /usr/app_install/collect/bin',
            #                          'rm -rf %s'% xieyi_txt_file_name,
            #                          './%s --id=com%s_1 --log_level=develop &>%s &'% (xieyi_name,xieyi_test_port,xieyi_txt_file_name)]
            #         am.telnet_client_rstart_xieyi(restart_xie_yi_commad_list)



            #是否发送数据
            if is_com_recive_and_send:
                send_data_list = []
                # am.com_recive_and_send()
                am.com_recive_and_send_with_params(sender_hex_data_order_list)


            #是否ftp下载获取解析文件
            # if is_ftp_down_xieyi_file:
            if is_assert_file_success:  #是否在协议文件中找到相应的解析内容,是，则需要下载解析文件
                am.ftp_down_xieyi_file_commom()
                # xieyi_remote_file = xieyi_bin_dir+'/'+xieyi_txt_file_name
                # xieyi_local_file = xieyi_txt_file_name
                # am.time_delay(60)
                # am.run_ftp_down(remote_file=xieyi_remote_file, local_file=xieyi_local_file)


            #是否ftp下载实时数据
            # if is_ftp_get_remote_db_file:
            if is_assert_real_db_success: # 是否验证实时数据，是，则需要下载远程实时数据库
                am.ftp_get_remote_db_file()



            #是否上报平台
            # if is_tcp_server_receive:
            if is_assert_tcp_server_receive_success:  #是否验证平台上报内容，是，则需要接收上报平台数据
                am.tcp_server_receive()

            am.end_work()   #善后工作


            #是否在协议文件中找到相应的解析内容
            if is_assert_file_success:
                am.assert_file_success()

            #是否验证实时数据
            if is_assert_real_db_success:
                assert_result_flag = am.assert_real_db_success()
                self.assertTrue(assert_result_flag,msg=u"数据库断言失败")

            #是否验证平台上报内容
            if is_assert_tcp_server_receive_success:
                if is_web_modify_xieyi:  #如果通过web修改协议，则会有监控因子，用监控因子和数据值拼接后断言
                    jiankongyinzi_list = web_xieyi_yinzi.split(",")
                    shuju_list = xieyi_jiexi_expect_result_list
                    tcp_expect_result_list = []
                    #将因子与数据拼接形成断言内容：
                    jiankongyinzi_list_len = len(jiankongyinzi_list)
                    shuju_list_len = len(shuju_list)
                    if jiankongyinzi_list_len ==shuju_list_len:
                        for i in range(0,jiankongyinzi_list_len):
                            tcp_expect_result_one = "%s-Rtd=%s" %(str(jiankongyinzi_list[i]),str(shuju_list[i]))
                            tcp_expect_result_list.append(tcp_expect_result_one)

                        tcp_expect_result_list = ""  # 获取平台断言内容，根据监控因子和断言数据自动拼接而成
                        is_in_tcp = am.assert_tcp_server_receive_success_with_param(
                            expect_result_list=tcp_expect_result_list)  # 带参数的断言
                    else:
                        self.assertTrue(False, "平台上报数据断言失败,监控因子与预期验证数据值个数不同")
                        is_in_tcp = False

                else:  #否则，没有监控因子，只以数据断言
                    is_in_tcp = am.assert_tcp_server_receive_success()  #不带参数的断言

                self.assertTrue(is_in_tcp,"平台上报数据断言失败")


            #如果三个断言中没有一个断言启动，则测试用例断言失败
            if is_assert_file_success or is_assert_real_db_success or is_assert_tcp_server_receive_success:
                self.assertTrue(True)
            else:
                self.assertTrue(False,u"测试用例没有断言，请至少添加一种断言（解析内容断言、实时数据库断言、平台上报内容断言）")


            for sender_hex_data_order_list_one in sender_hex_data_order_list:
                am.outPutMyLog("="*50)
                am.outPutMyLog("接收的数据：%s"% str(sender_hex_data_order_list_one[2]))
                am.outPutMyLog("发送的数据：%s" % str(sender_hex_data_order_list_one[0]))
                if sender_hex_data_order_list_one[9]:  #如果不断言结果，则不写预期结果
                    am.outPutMyLog("预期的解析结果：%s" %str(sender_hex_data_order_list_one[3]))
                am.outPutMyLog("=" * 50)



    @staticmethod  # 根据不同的参数生成测试用例
    def getTestFunc(case_id,depend_config_id):

        def func(self):
            self.defineshucaiyi(case_id,depend_config_id)

        return func


def __generateTestCases():
    from shucaiyidate.modelsorder import XieyiTestCase

    xieyitestcase_all = XieyiTestCase.objects.filter(is_run_case=True).order_by('id')

    for xieyitestcase in xieyitestcase_all:
        forcount = xieyitestcase.case_counts
        starttime = GetTimeStr().getTimeStr()
        if len(str(xieyitestcase.id)) == 1:
            xieyitestcaseid = '0000%s' % xieyitestcase.id
        elif len(str(xieyitestcase.id)) == 2:
            xieyitestcaseid = '000%s' % xieyitestcase.id
        elif len(str(xieyitestcase.id)) == 3:
            xieyitestcaseid = '00%s' % xieyitestcase.id
        elif len(str(xieyitestcase.id)) == 4:
            xieyitestcaseid = '0%s' % xieyitestcase.id
        elif len(str(xieyitestcase.id)) == 5:
            xieyitestcaseid = '%s' % xieyitestcase.id
        else:
            xieyitestcaseid = 'Id已经超过5位数，请重新定义'

        for i in range(1, forcount + 1):  # 循环，从1开始
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

            args = []
            args.append(xieyitestcase.id)
            args.append(xieyitestcase.depend_config_id)

            setattr(TestShuCaiYiClass,
                    'test_func_%s_%s_%s' % (
                    xieyitestcaseid, xieyitestcase.test_case_title, forcount_i),
                    TestShuCaiYiClass.getTestFunc(*args))  # 通过setattr自动为TestCase类添加成员方法，方法以“test_func_”开头


__generateTestCases()

if __name__ == '__main__':
    ts = TestShuCaiYiClass()
    ts.defineshucaiyi()












