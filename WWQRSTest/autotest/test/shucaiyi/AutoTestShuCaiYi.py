import unittest
# ----------------------------------------------------------------------
import os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wanwenyc.settings")
django.setup()
# ----------------------------------------------------------------------
# 独运行某一个py文件时会出现如下错误：django.core.exceptions.AppRegistryNotReady: Apps aren't loaded yet.，以上内容可以解决此问题,加载django中的App
import ddt

from WWTest.autotest.config.wanwei.globalconfig.globalConfig import GlobalConfig, gc  # 导入全局变量
from WWTest.base.activeBrowser import ActiveBrowser
from WWTest.util.getTimeStr import GetTimeStr
from WWTest.autotest.config.lina.zhonghuanxie.page.loginPage import *  # 导入登录页
from WWTest.autotest.config.wanwei.depend.clickAndBackDepend import ClickAndBackDepend, clickandbackdepend
# 导入 ClickAndBack依赖
from WWTest.autotest.config.wanwei.depend.inputTapInputText import InputTapInputText, inputtapinputtext
from WWTest.autotest.config.wanwei.depend.selectTapSelectOption import SelectTapSelectOption, selecttapselectoption
from WWTest.autotest.config.wanwei.depend.selectTapSelectText import SelectTapSelectText, selecttapselecttext
from WWTest.autotest.config.wanwei.depend.inputTapInputFile import InputTapInputFile, inputtapinputfile
from WWTest.autotest.config.wanwei.depend.assertTipText import AssertTipText, asserttiptext
from WWTest.autotest.config.wanwei.depend.inputTapInputDateTime import inputtapinputdatetime, InputTapInputDateTime
from WWTest.autotest.config.wanwei.depend.radioAndReelectionLabel import RadioAndReelectionLabel, \
    radioandreelectionlabel
from WWTest.autotest.config.wanwei.depend.iframeBodyInputText import iframebodyinputtext

from WWQRSTest.util.autoModbus.autoModbus import AutoModbus


class TestShuCaiYiClass(unittest.TestCase):  # 创建测试类

    @classmethod  # 类方法，只执行一次，但必须要加注解@classmethod,且名字固定为setUpClass
    def setUpClass(cls):
        # cls.activeweb = ActiveBrowser()  # 实例化
        # cls.loginurl = LoginPage().pageurl
        # cls.activeweb.getUrl(indexpage.pageurl)  # 打开网址
        # cls.activeweb.findElementByXpathAndInput(LoginPage().account,AGENT_LOGIN_ACCOUNT)
        # cls.activeweb.findElementByXpathAndInput(LoginPage().password,AGENT_LOGIN_PASSWORD)
        # cls.activeweb.findElementByXpathAndClick(LoginPage().loginbutton)
        # cls.activeweb.delayTime(3)
        # cls.testpage = DetailsPage()
        # cls.testpageurl =cls.testpage.pageurl   #测试页面url
        # cls.activeweb.getUrl(cls.testpageurl)
        # cls.activeweb.delayTime(3)
        pass

    @classmethod  # 类方法，只执行一次，但必须要加注解@classmethod,且名字固定为tearDownClass
    def tearDownClass(cls):
        # cls.activeweb.closeBrowse()
        pass

    def setUp(self):  # 每条用例执行测试之前都要执行此方法
        # self.activebrowser = ActiveBrowser()  # 实例化
        # # lpf.login(self.activebrowser)
        # lpf.loginwithcookiesauto(self.activebrowser)
        pass

    def tearDown(self):  # 每条用例执行测试之后都要执行此方法
        # self.activebrowser.closeBrowse()
        pass

    def testdefineshucaiyi(self,telnet_host_ip ,
                                telnet_username ,
                                telnet_password ,
                                xieyi_bin_dir ,
                                xieyi_name ,
                                xieyi_test_port  ,
                                xieyi_db ,
                                xieyi_db_remote_path ,
                                xieyi_db_table_name ,
                                com_port ,
                                com_baudrate ,
                                com_bytesize ,
                                com_parity ,
                                com_stopbits ,
                                com_send_date ,
                                com_expect_date ,
                                xieyi_jiexi_expect_result_list ,
                                tcp_server_ip ,
                                tcp_server_port ,
                                is_ftp_upload ,
                                is_close_xieyi ,
                                is_restart_xieyi ,
                                is_com_recive_and_send ,
                                is_ftp_down_xieyi_file ,
                                is_assert_file_success ,
                                is_ftp_get_remote_db_file ,
                                is_assert_real_db_success ,
                                is_tcp_server_receive ,
                                is_assert_tcp_server_receive_success):

        xieyi_txt_file_name = '%s_%s.txt'%(xieyi_name,xieyi_test_port)


        am = AutoModbus(
            telnet_host_ip=None,
            telnet_username=None,
            telnet_password=None,
            telnet_clicent_object=None,
            ftp_client_object=None,
            xieyi_name=None,
            xieyi_test_port=None,
            xieyi_txt_file_name=None,
            xieyi_db=None,
            xieyi_db_remote_path=None,
            xieyi_db_table_name=None,
            com_port=None,
            com_baudrate=None,
            com_bytesize=None,
            com_parity=None,
            com_stopbits=None,
            com_timeout=None,
            com_send_date_yinzi_num=None,
            com_send_date_yinzi_num_is_auto_make=None,
            com_send_date_yinzi_hex_str_is_auto_make=None,
            com_send_date_yinzi_hex_str_list=None,
            com_send_date=None,
            com_expect_date=None,
            com_expect_date_bytes=None,
            com_send_date_list=None,
            com_send_date_bytes=None,
            com_send_date_list_bytes=None,
            xieyi_jiexi_expect_result=None,
            xieyi_jiexi_expect_result_list=None,
            xieyi_cfg_protocol=None,
            xieyi_cfg_idNum=None,
            xieyi_cfg_startAddress=None,
            xieyi_cfg_functionCode=None,
            xieyi_cfg_registerNum=None,
            xieyi_cfg_DataLen=None,
            xieyi_cfg_dataLen=None,
            xieyi_cfg_dataType=None,
            tcp_server_ip=None,
            tcp_server_port=None,
            tcp_server_file_name=None,
            tcp_server_object=None,
            is_ftp_get_modbus_cfg=None,
            is_check_modbus_xieyi_cfg=None,
            is_get_modbus_cfg_main=None,
            is_set_com_send_date=None,
            is_write_device=None,
            write_device_reatart_time=None,
            is_telnet_client_close_default_start_xieyi=None,
            is_telnet_client_rstart_xieyi=None,
            is_com_recive_and_send=None,
            is_ftp_get_file=None,
            is_assert_file_success=None,
            is_ftp_get_remote_db_file=None,
            is_assert_real_db_success=None,
            is_tcp_server_receive=None,
            is_assert_tcp_server_receive_success=None
        )
        ftp_up_load_file_list = [['/usr/app_install/collect/bin/text.txt','D:/pycharmproject/shangbaogongju/WWQRSTest/util/text.txt'],
                                 ['/usr/app_install/collect/bin/result1.txt','D:/pycharmproject/shangbaogongju/WWQRSTest/util/result1.txt']]
        #1.是否上传配置文件
        #1-1.上传配置文件之前先修改远程文件名称为备份文件名
        #1-2.上传配置文件
        #上传文件进行可执行命令
        #先分离远程文件目录，获取到目录和文件
        if is_ftp_upload:   #如果需要上传文件
            am.run_ftp_up_load_file_list(ftp_up_load_file_list)

        #如果进行web端操作

        #如果关闭和重启协议
        #是否关闭默认启动的协议，一定要关闭吗  #杀死科内特
        if is_close_xieyi:
            mycommad_list = ['stop_guard','ps aux | grep %s | xargs kill -9 &>/dev/null &' % xieyi_name]
            am.telnet_client_close_default_start_xieyi(mycommad_list)

        #重启协议
        if is_restart_xieyi:
            mycommad_list = ['cd /usr/app_install/collect/bin',
                             'rm -rf %s'% xieyi_txt_file_name,
                             './%s --id=com%s_1 --log_level=develop &>%s &'% (xieyi_name,xieyi_test_port,xieyi_txt_file_name)]
            am.telnet_client_rstart_xieyi(mycommad_list)

        #是否发送数据
        if is_com_recive_and_send:
            send_data_list = []
            am.com_recive_and_send()

        #是否ftp下载获取解析文件
        if is_ftp_down_xieyi_file:
            xieyi_remote_file = xieyi_bin_dir+'/'+xieyi_txt_file_name
            xieyi_local_file = xieyi_txt_file_name
            am.run_ftp_down(remote_file=xieyi_remote_file, local_file=xieyi_local_file)

        #是否对在协议文件中找到相应的解析内容
        if is_assert_file_success:
            am.assert_file_success()

        #是否ftp下载实时数据
        if is_ftp_get_remote_db_file:
            am.ftp_get_remote_db_file()

        #是否验证实时数据
        if is_assert_real_db_success:
            am.assert_real_db_success()

        #是否上报平台
        if is_tcp_server_receive:
            am.tcp_server_receive()

        if is_assert_tcp_server_receive_success:
            am.assert_tcp_server_receive_success()






    @staticmethod  # 根据不同的参数生成测试用例
    def getTestFunc(num, depend_click_case_id,
                    is_cancel,
                    addnew_id,
                    confirm_ele_find, confirm_ele_find_value,
                    click_confirm_delay_time,
                    cancel_ele_find, cancel_ele_find_value,
                    is_submit_success,
                    is_signel_page,
                    page_number_xpath,
                    result_table_ele_find, result_table_ele_find_value,
                    table_colnum_counts):

        def func(self):
            self.definenewadd(num, depend_click_case_id,
                              is_cancel,
                              addnew_id,
                              confirm_ele_find, confirm_ele_find_value,
                              click_confirm_delay_time,
                              cancel_ele_find, cancel_ele_find_value,
                              is_submit_success,
                              is_signel_page,
                              page_number_xpath,
                              result_table_ele_find, result_table_ele_find_value,
                              table_colnum_counts)

        return func


def __generateTestCases():
    from shucaiyidate.models import XieyiConfigDate

    xieyiconfigdatetestcase_all = XieyiConfigDate.objects.filter(id=1).order_by('id')

    for xieyiconfigdatetestcase in xieyiconfigdatetestcase_all:
        forcount = xieyiconfigdatetestcase.case_counts
        starttime = GetTimeStr().getTimeStr()
        if len(str(xieyiconfigdatetestcase.id)) == 1:
            xieyiconfigdatetestcaseid = '0000%s' % xieyiconfigdatetestcase.id
        elif len(str(xieyiconfigdatetestcase.id)) == 2:
            xieyiconfigdatetestcaseid = '000%s' % xieyiconfigdatetestcase.id
        elif len(str(xieyiconfigdatetestcase.id)) == 3:
            xieyiconfigdatetestcaseid = '00%s' % xieyiconfigdatetestcase.id
        elif len(str(xieyiconfigdatetestcase.id)) == 4:
            xieyiconfigdatetestcaseid = '0%s' % xieyiconfigdatetestcase.id
        elif len(str(xieyiconfigdatetestcase.id)) == 5:
            xieyiconfigdatetestcaseid = '%s' % xieyiconfigdatetestcase.id
        else:
            xieyiconfigdatetestcaseid = 'Id已经超过5位数，请重新定义'

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
            args.append(xieyiconfigdatetestcaseid)
            # args.append(i)
            args.append(xieyiconfigdatetestcase.depend_click_case_id)
            args.append(xieyiconfigdatetestcase.is_click_cancel)
            args.append(xieyiconfigdatetestcase.id)
            args.append(xieyiconfigdatetestcase.confirm_ele_find)
            args.append(xieyiconfigdatetestcase.confirm_ele_find_value)
            args.append(xieyiconfigdatetestcase.click_confirm_delay_time)
            args.append(xieyiconfigdatetestcase.cancel_ele_find)
            args.append(xieyiconfigdatetestcase.cancel_ele_find_value)
            args.append(xieyiconfigdatetestcase.is_submit_success)
            args.append(xieyiconfigdatetestcase.is_signel_page)
            args.append(xieyiconfigdatetestcase.page_number_xpath)
            args.append(xieyiconfigdatetestcase.result_table_ele_find)
            args.append(xieyiconfigdatetestcase.result_table_ele_find_value)
            args.append(xieyiconfigdatetestcase.table_colnum_counts)

            setattr(TestShuCaiYiClass,
                    'test_func_%s_%s_%s' % (
                    xieyiconfigdatetestcaseid, xieyiconfigdatetestcase.test_case_title, forcount_i),
                    TestShuCaiYiClass.getTestFunc(*args))  # 通过setattr自动为TestCase类添加成员方法，方法以“test_func_”开头


__generateTestCases()

if __name__ == '__main__':
    # print("hello world")
    # unittest.main()
    ts = TestShuCaiYiClass()
    ts.testdefineshucaiyi()












