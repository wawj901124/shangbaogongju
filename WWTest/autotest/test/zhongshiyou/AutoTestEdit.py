import unittest
# ----------------------------------------------------------------------
import os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wanwenyc.settings")
django.setup()
# ----------------------------------------------------------------------
# 独运行某一个py文件时会出现如下错误：django.core.exceptions.AppRegistryNotReady: Apps aren't loaded yet.，以上内容可以解决此问题,加载django中的App
import ddt

from WWTest.util.getTimeStr import GetTimeStr
from WWTest.autotest.config.zhongshiyou.page.loginPage import *  # 导入登录页
from WWTest.autotest.config.zhongshiyou.depend.clickAndBackDepend import ClickAndBackDepend, clickandbackdepend
# 导入 ClickAndBack依赖
from WWTest.autotest.config.zhongshiyou.depend.editdepend.inputTapInputText import InputTapInputText, inputtapinputtext
from WWTest.autotest.config.zhongshiyou.depend.editdepend.selectTapSelectOption import SelectTapSelectOption, selecttapselectoption
from WWTest.autotest.config.zhongshiyou.depend.editdepend.inputTapInputFile import InputTapInputFile, inputtapinputfile
from WWTest.autotest.config.zhongshiyou.depend.editdepend.assertTipText import AssertTipText, asserttiptext
from WWTest.autotest.config.zhongshiyou.depend.editdepend.inputTapInputDateTime import inputtapinputdatetime, InputTapInputDateTime
from WWTest.autotest.config.zhongshiyou.depend.editdepend.radioAndReelectionLabel import RadioAndReelectionLabel, \
    radioandreelectionlabel
from WWTest.autotest.config.zhongshiyou.depend.editdepend.iframeBodyInputText import iframebodyinputtext


class TestEditClass(unittest.TestCase):  # 创建测试类

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

    # 定义新增函数
    def definenewadd(self, num, depend_click_case_id,
                     edit_ele_find,edit_ele_find_value,
                     edit_button_find,edit_button_find_value,
                     is_cancel,
                     edit_id,
                     confirm_ele_find, confirm_ele_find_value,
                     click_confirm_delay_time,
                     cancel_ele_find, cancel_ele_find_value,
                     is_submit_success,
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

        #获取要修改的元素的text
        edit_ele_text = self.activebrowser.findEleAndReturnText(num,edit_ele_find,edit_ele_find_value)

        #修改前，验证元素存在
        edit_before_reault_check = self.activebrowser. \
            findEleAndCheckTableWithColnumCounts(num, result_table_ele_find,
                                                 result_table_ele_find_value, edit_ele_text,
                                                 table_colnum_counts)
        self.assertTrue(edit_before_reault_check)

        #点击修改按钮
        self.activebrowser.findEleAndClick(num,edit_button_find,edit_button_find_value)


        # in_xpath = "/html/body/div[1]/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[3]/div/div[2]/div/div[1]/form/div[1]/div/div/div/input"
        # self.activebrowser.findEleAndInputNum(num, "xpath", in_xpath,"wert")
        # self.activebrowser.getPageSource()
        # self.activebrowser.delayTime(30000)

        # 文本输入框添加内容
        inputtext_list = inputtapinputtext.inputtapinputtext(self.activebrowser, edit_id)

        # self.activebrowser.delayTime(30000)

        # 文件输入框添加内容
        inputtapinputfile.inputtapinputfile(self.activebrowser, edit_id)

        # 选项框添加内容
        selecttapselectoption.selecttapselectoption(self.activebrowser, edit_id)

        # self.activebrowser.delayTime(30000)

        # 单选项与复选项添加内容
        radioandreelectionlabel.radioandreelectionlabel(self.activebrowser, edit_id)

        # 日期添加内容
        inputtapinputdatetime.inputtapinputdatetime(self.activebrowser, edit_id)

        #富文本添加内容
        iframe_inputtext_list = iframebodyinputtext.iframebodyinputtext(self.activebrowser, edit_id)

        # 判断是否点击取消按钮
        if is_cancel:
            # 如果点击取消按钮，则点击取消按钮
            self.activebrowser.findEleAndClick(num, cancel_ele_find, cancel_ele_find_value)
            self.activebrowser.outPutMyLog("点击【取消】按钮")

            #判断取消按钮不存在
            self.activebrowser.assertEleNotExist(cancel_ele_find, cancel_ele_find_value)



            if is_signel_page:
                self.activebrowser.outPutMyLog("页面不需要分页")
            else:
                son_ele_s = self.activebrowser.getFatherSonElesList("xpath", page_number_xpath, "tag_name", "li")
                son_count = len(son_ele_s)
                son_last_xpath = "%s/%s[%s]" % (page_number_xpath, "li", son_count)
                self.activebrowser.findEleAndClick(num, "xpath", son_last_xpath)

            # 修改后，点击取消，验证元素存在
            edit_after_reault_check = self.activebrowser. \
                findEleAndCheckTableWithColnumCounts(num, result_table_ele_find,
                                                     result_table_ele_find_value, edit_ele_text,
                                                     table_colnum_counts)
            self.assertTrue(edit_after_reault_check)

            inputtext_list_len = len(inputtext_list)
            for i in range(0, inputtext_list_len):
                reault_check = self.activebrowser. \
                    findEleAndCheckTableWithColnumCounts(num, result_table_ele_find,
                                                         result_table_ele_find_value, inputtext_list[i],
                                                         table_colnum_counts)
                self.assertFalse(reault_check)

            asserttest_list_all = asserttiptext.assertiptext(self.activebrowser, edit_id)
            asserttest_list_all_long = len(asserttest_list_all)
            if asserttest_list_all_long == 0 and inputtext_list_len == 0:
                self.activebrowser.outPutErrorMyLog("【异常提示】：本用例为验证点击取消按钮的用例，"
                                                    "但没有添加要输入的测试数据或者验证文本信息，"
                                                    "请检查用例测试数据，将测试数据补充完整！")
                self.assertTrue(False)


        else:
            # 否则点击确定按钮
            # self.activebrowser.findEleAndClick(num,confirm_ele_find,confirm_ele_find_value)
            self.activebrowser.findEleAndClickConfigDelayTime(num, confirm_ele_find, confirm_ele_find_value,
                                                              click_confirm_delay_time)
            self.activebrowser.outPutMyLog("点击【确定】按钮")
            self.activebrowser.getPageSource()
            # self.activebrowser.delayTime(30000)



            if not is_submit_success:  # 如果不是添加成功，需要验证某些文本信息
                self.activebrowser.outPutMyLog("提交不成功时的提示信息验证")
                asserttest_list_all = asserttiptext.assertiptext(self.activebrowser, edit_id)
                asserttest_list_all_long = len(asserttest_list_all)
                if asserttest_list_all_long != 0:
                    for i in range(0, asserttest_list_all_long):
                        self.assertEqual(asserttest_list_all[i][0], asserttest_list_all[i][1])
                else:
                    self.activebrowser.outPutErrorMyLog("【异常提示】：本用例为验证提示信息用例，"
                                                        "但是却没有添加相应的提示信息测试数据"
                                                        "请检查用例测试数据，将测试数据补充完整！")
                    self.assertTrue(False)
            else:
                self.activebrowser.outPutMyLog("添加成功后的添加数据的验证")
                # 判断确定按钮不存在
                self.activebrowser.assertEleNotExist(confirm_ele_find, confirm_ele_find_value)

                # 验证弹框或文本信息
                asserttest_list_all = asserttiptext.assertiptext(self.activebrowser, edit_id)
                asserttest_list_all_long = len(asserttest_list_all)
                if asserttest_list_all_long != 0:
                    for i in range(0, asserttest_list_all_long):
                        self.assertEqual(asserttest_list_all[i][0], asserttest_list_all[i][1])


                # 是否单页面判断
                if is_signel_page:
                    self.activebrowser.outPutMyLog("页面不需要分页")
                else:
                    son_ele_s = self.activebrowser.getFatherSonElesList("xpath", page_number_xpath, "tag_name", "li")
                    son_count = len(son_ele_s)
                    son_last_xpath = "%s/%s[%s]" % (page_number_xpath, "li", son_count)
                    self.activebrowser.findEleAndClick(num, "xpath", son_last_xpath)

                # 修改后，点击确定，验证元素不存在
                edit_after_reault_check = self.activebrowser. \
                    findEleAndCheckTableWithColnumCounts(num, result_table_ele_find,
                                                         result_table_ele_find_value, edit_ele_text,
                                                         table_colnum_counts)
                self.assertFalse(edit_after_reault_check)

                # 验证表格内容
                inputtext_list_len = len(inputtext_list)
                iframe_inputtext_list_len = len(iframe_inputtext_list)
                if inputtext_list_len != 0:
                    for i in range(0, inputtext_list_len):
                        reault_check = self.activebrowser. \
                            findEleAndCheckTableWithColnumCounts(num, result_table_ele_find,
                                                                 result_table_ele_find_value, inputtext_list[i],
                                                                 table_colnum_counts)
                        self.assertTrue(reault_check)

                if iframe_inputtext_list_len != 0:
                    for i in range(0, iframe_inputtext_list_len):
                        reault_check = self.activebrowser. \
                            findEleAndCheckTableWithColnumCounts(num, result_table_ele_find,
                                                                 result_table_ele_find_value, iframe_inputtext_list[i],
                                                                 table_colnum_counts)
                        self.assertTrue(reault_check)

                # 如果没有断言文本或者断言添加的内容，则
                if asserttest_list_all_long == 0 and inputtext_list_len == 0 and iframe_inputtext_list_len ==0:
                    self.activebrowser.outPutErrorMyLog("【异常提示】：本用例为验证添加成功后，"
                                                        "是否存在添加的数据或弹框提示或文本验证，但实际没有添加要验证的数据"
                                                        "请检查用例测试数据，将测试数据补充完整！")
                    self.assertTrue(False)

    # def test001(self):
    #     print("第一条测试用例")
    #     self.definedepend(self.dependid)

    @staticmethod  # 根据不同的参数生成测试用例
    def getTestFunc(num, depend_click_case_id,
                     edit_ele_find,edit_ele_find_value,
                     edit_button_find,edit_button_find_value,
                     is_cancel,
                     edit_id,
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
                     edit_ele_find,edit_ele_find_value,
                     edit_button_find,edit_button_find_value,
                     is_cancel,
                     edit_id,
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
    from testdatas.models import EditAndCheck

    editandchecktestcase_all = EditAndCheck.objects.filter(test_project__contains="中石油").filter(is_run_case=True).order_by('id')

    for editandchecktestcase in editandchecktestcase_all:
        forcount = editandchecktestcase.case_counts
        starttime = GetTimeStr().getTimeStr()
        if len(str(editandchecktestcase.id)) == 1:
            editandchecktestcaseid = '0000%s' % editandchecktestcase.id
        elif len(str(editandchecktestcase.id)) == 2:
            editandchecktestcaseid = '000%s' % editandchecktestcase.id
        elif len(str(editandchecktestcase.id)) == 3:
            editandchecktestcaseid = '00%s' % editandchecktestcase.id
        elif len(str(editandchecktestcase.id)) == 4:
            editandchecktestcaseid = '0%s' % editandchecktestcase.id
        elif len(str(editandchecktestcase.id)) == 5:
            editandchecktestcaseid = '%s' % editandchecktestcase.id
        else:
            editandchecktestcaseid = 'Id已经超过5位数，请重新定义'

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
            args.append(editandchecktestcaseid)
            # args.append(i)
            args.append(editandchecktestcase.depend_click_case_id)
            args.append(editandchecktestcase.edit_ele_find)
            args.append(editandchecktestcase.edit_ele_find_value)
            args.append(editandchecktestcase.edit_button_find)
            args.append(editandchecktestcase.edit_button_find_value)

            args.append(editandchecktestcase.is_click_cancel)
            args.append(editandchecktestcase.id)
            args.append(editandchecktestcase.confirm_ele_find)
            args.append(editandchecktestcase.confirm_ele_find_value)
            args.append(editandchecktestcase.click_confirm_delay_time)
            args.append(editandchecktestcase.cancel_ele_find)
            args.append(editandchecktestcase.cancel_ele_find_value)
            args.append(editandchecktestcase.is_submit_success)
            args.append(editandchecktestcase.is_signel_page)
            args.append(editandchecktestcase.page_number_xpath)
            args.append(editandchecktestcase.result_table_ele_find)
            args.append(editandchecktestcase.result_table_ele_find_value)
            args.append(editandchecktestcase.table_colnum_counts)

            setattr(TestEditClass,
                    'test_func_%s_%s_%s_%s_%s_%s' % (
                    editandchecktestcaseid, editandchecktestcase.test_project,
                    editandchecktestcase.test_module,editandchecktestcase.test_page,
                    editandchecktestcase.test_case_title, forcount_i),
                    TestEditClass.getTestFunc(*args))  # 通过setattr自动为TestCase类添加成员方法，方法以“test_func_”开头


__generateTestCases()

if __name__ == '__main__':
    print("hello world")
    unittest.main()












