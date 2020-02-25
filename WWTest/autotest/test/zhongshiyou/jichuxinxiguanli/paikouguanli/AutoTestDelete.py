import unittest
# ----------------------------------------------------------------------
import os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wanwenyc.settings")
django.setup()
# ----------------------------------------------------------------------
# 独运行某一个py文件时会出现如下错误：django.core.exceptions.AppRegistryNotReady: Apps aren't loaded yet.，以上内容可以解决此问题,加载django中的App
import ddt

#from WWTest.autotest.config.wanwei.globalconfig.globalConfig import GlobalConfig, gc  # 导入全局变量
#from WWTest.base.activeBrowser import ActiveBrowser
from WWTest.util.getTimeStr import GetTimeStr
from WWTest.autotest.config.zhongshiyou.page.loginPage import *  # 导入登录页
from WWTest.autotest.config.zhongshiyou.depend.clickAndBackDepend import ClickAndBackDepend, clickandbackdepend
# 导入 ClickAndBack依赖
from WWTest.autotest.config.zhongshiyou.depend.inputTapInputText import InputTapInputText, inputtapinputtext
from WWTest.autotest.config.zhongshiyou.depend.selectTapSelectOption import SelectTapSelectOption, selecttapselectoption
from WWTest.autotest.config.zhongshiyou.depend.selectTapSelectText import SelectTapSelectText, selecttapselecttext
from WWTest.autotest.config.zhongshiyou.depend.inputTapInputFile import InputTapInputFile, inputtapinputfile
from WWTest.autotest.config.zhongshiyou.depend.assertTipText import AssertTipText, asserttiptext
from WWTest.autotest.config.zhongshiyou.depend.inputTapInputDateTime import inputtapinputdatetime, InputTapInputDateTime
from WWTest.autotest.config.zhongshiyou.depend.radioAndReelectionLabel import RadioAndReelectionLabel, \
    radioandreelectionlabel
from WWTest.autotest.config.zhongshiyou.depend.iframeBodyInputText import iframebodyinputtext


class TestDeleteClass(unittest.TestCase):  # 创建测试类

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
        self.activebrowser = ActiveBrowser()  # 实例化
        # lpf.login(self.activebrowser)
        lpf.loginwithcookiesauto(self.activebrowser)
        pass

    def tearDown(self):  # 每条用例执行测试之后都要执行此方法
        self.activebrowser.closeBrowse()
        pass

    def definedepend(self, dependid):
        clickandbackdepend.clickandbackdepend(self.activebrowser, dependid)

    # 定义删除函数
    def definedelete(self, num, depend_click_case_id,
                     delete_ele_find,delete_ele_find_value,
                     delete_button_find,delete_button_find_value,
                     is_cancel,
                     confirm_ele_find, confirm_ele_find_value,
                     click_confirm_delay_time,
                     cancel_ele_find, cancel_ele_find_value,
                     popup_ele_find,popup_ele_find_value,popup_text,
                     is_signel_page,
                     page_number_xpath,
                     result_table_ele_find, result_table_ele_find_value,
                     table_colnum_counts
                     ):

        # 如果有依赖ID，则执行依赖函数，达到执行当前用例的前提条件
        if depend_click_case_id != None:
            print("depend_click_case_id：%s" % depend_click_case_id)
            self.definedepend(depend_click_case_id)
            self.activebrowser.outPutMyLog("依赖函数执行完毕！！！")

        self.activebrowser.outPutMyLog("开始正式执行测试用例")

        #获取被删除元素的文本信息
        delete_ele_text = self.activebrowser.findEleAndReturnText(num,delete_ele_find,delete_ele_find_value)

        #删除前，验证元素存在
        delete_before_reault_check = self.activebrowser. \
            findEleAndCheckTableWithColnumCounts(num, result_table_ele_find,
                                                 result_table_ele_find_value, delete_ele_text,
                                                 table_colnum_counts)
        self.assertTrue(delete_before_reault_check)

        #点击删除按钮
        self.activebrowser.findEleAndClick(num,delete_button_find,delete_button_find_value)

        #开始删除弹框逻辑判断
        # 判断是否点击取消按钮
        if is_cancel:
            # 如果点击取消按钮，则点击取消按钮
            self.activebrowser.findEleAndClick(num, cancel_ele_find, cancel_ele_find_value)
            self.activebrowser.outPutMyLog("点击【取消】按钮")

            if is_signel_page:
                self.activebrowser.outPutMyLog("页面不需要分页")
            else:
                son_ele_s = self.activebrowser.getFatherSonElesList("xpath", page_number_xpath, "tag_name", "li")
                son_count = len(son_ele_s)
                son_last_xpath = "%s/%s[%s]" % (page_number_xpath, "li", son_count)
                self.activebrowser.findEleAndClick(num, "xpath", son_last_xpath)

            #点击取消按钮后，元素依然存在
            reault_check = self.activebrowser.findEleAndCheckTableWithColnumCounts(num, result_table_ele_find,
                                                                                   result_table_ele_find_value, delete_ele_text,table_colnum_counts)
            self.assertTrue(reault_check)

        else:
            # 否则点击确定按钮
            # self.activebrowser.findEleAndClick(num,confirm_ele_find,confirm_ele_find_value)
            self.activebrowser.findEleAndClickConfigDelayTime(num, confirm_ele_find, confirm_ele_find_value,
                                                              click_confirm_delay_time)
            self.activebrowser.outPutMyLog("点击【确定】按钮")
            self.activebrowser.getPageSource()
            # self.activebrowser.delayTime(30000)

            #验证删除弹框内容
            if popup_ele_find!=None and popup_ele_find_value!=None and popup_text!=None:
                popup_except_text = popup_text
                popup_actual_text = self.activebrowser.findEleAndReturnText(num, popup_ele_find,popup_ele_find_value)

                self.assertEqual(popup_except_text,popup_actual_text)


            # 是否单页面判断
            if is_signel_page:
                self.activebrowser.outPutMyLog("页面不需要分页")
            else:
                son_ele_s = self.activebrowser.getFatherSonElesList("xpath", page_number_xpath, "tag_name", "li")
                son_count = len(son_ele_s)
                son_last_xpath = "%s/%s[%s]" % (page_number_xpath, "li", son_count)
                self.activebrowser.findEleAndClick(num, "xpath", son_last_xpath)

            # 验证表格内容
            #点击取消按钮后，元素不应该存在
            reault_check = self.activebrowser.findEleAndCheckTableWithColnumCounts(num, result_table_ele_find,
                                                                                   result_table_ele_find_value, delete_ele_text,table_colnum_counts)
            self.assertFalse(reault_check)


    # def test001(self):
    #     print("第一条测试用例")
    #     self.definedepend(self.dependid)

    @staticmethod  # 根据不同的参数生成测试用例
    def getTestFunc(num, depend_click_case_id,
                     delete_ele_find,delete_ele_find_value,
                     delete_button_find,delete_button_find_value,
                     is_cancel,
                     confirm_ele_find, confirm_ele_find_value,
                     click_confirm_delay_time,
                     cancel_ele_find, cancel_ele_find_value,
                     popup_ele_find,popup_ele_find_value,popup_text,
                     is_signel_page,
                     page_number_xpath,
                     result_table_ele_find, result_table_ele_find_value,
                     table_colnum_counts):

        def func(self):
            self.definedelete(num, depend_click_case_id,
                     delete_ele_find,delete_ele_find_value,
                     delete_button_find,delete_button_find_value,
                     is_cancel,
                     confirm_ele_find, confirm_ele_find_value,
                     click_confirm_delay_time,
                     cancel_ele_find, cancel_ele_find_value,
                     popup_ele_find,popup_ele_find_value,popup_text,
                     is_signel_page,
                     page_number_xpath,
                     result_table_ele_find, result_table_ele_find_value,
                     table_colnum_counts)

        return func


def __generateTestCases():
    from testdatas.models import DeleteAndCheck

    deleteandchecktestcase_all = DeleteAndCheck.objects.filter(test_project="中石油_迭代一").\
        filter(test_module="排口管理").filter(is_run_case=True).order_by('id')

    for deleteandchecktestcase in deleteandchecktestcase_all:
        forcount = deleteandchecktestcase.case_counts
        starttime = GetTimeStr().getTimeStr()
        if len(str(deleteandchecktestcase.id)) == 1:
            deleteandchecktestcaseid = '0000%s' % deleteandchecktestcase.id
        elif len(str(deleteandchecktestcase.id)) == 2:
            deleteandchecktestcaseid = '000%s' % deleteandchecktestcase.id
        elif len(str(deleteandchecktestcase.id)) == 3:
            deleteandchecktestcaseid = '00%s' % deleteandchecktestcase.id
        elif len(str(deleteandchecktestcase.id)) == 4:
            deleteandchecktestcaseid = '0%s' % deleteandchecktestcase.id
        elif len(str(deleteandchecktestcase.id)) == 5:
            deleteandchecktestcaseid = '%s' % deleteandchecktestcase.id
        else:
            deleteandchecktestcaseid = 'Id已经超过5位数，请重新定义'

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
            args.append(deleteandchecktestcaseid)
            # args.append(i)
            args.append(deleteandchecktestcase.depend_click_case_id)

            args.append(deleteandchecktestcase.delete_ele_find)
            args.append(deleteandchecktestcase.delete_ele_find_value)
            args.append(deleteandchecktestcase.delete_button_find)
            args.append(deleteandchecktestcase.delete_button_find_value)


            args.append(deleteandchecktestcase.is_click_cancel)
            args.append(deleteandchecktestcase.confirm_ele_find)
            args.append(deleteandchecktestcase.confirm_ele_find_value)
            args.append(deleteandchecktestcase.click_confirm_delay_time)
            args.append(deleteandchecktestcase.cancel_ele_find)
            args.append(deleteandchecktestcase.cancel_ele_find_value)

            args.append(deleteandchecktestcase.popup_ele_find)
            args.append(deleteandchecktestcase.popup_ele_find_value)
            args.append(deleteandchecktestcase.popup_text)

            args.append(deleteandchecktestcase.is_signel_page)
            args.append(deleteandchecktestcase.page_number_xpath)
            args.append(deleteandchecktestcase.result_table_ele_find)
            args.append(deleteandchecktestcase.result_table_ele_find_value)
            args.append(deleteandchecktestcase.table_colnum_counts)

            setattr(TestDeleteClass,
                    'test_func_%s_%s_%s_%s' % (
                    deleteandchecktestcaseid,deleteandchecktestcase.test_page,deleteandchecktestcase.test_case_title, forcount_i),
                    TestDeleteClass.getTestFunc(*args))  # 通过setattr自动为TestCase类添加成员方法，方法以“test_func_”开头


__generateTestCases()

if __name__ == '__main__':
    print("hello world")
    unittest.main()












