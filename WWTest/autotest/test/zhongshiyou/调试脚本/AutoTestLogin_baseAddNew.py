import unittest
# ----------------------------------------------------------------------
import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wanwenyc.settings")
django.setup()
# ----------------------------------------------------------------------
#独运行某一个py文件时会出现如下错误：django.core.exceptions.AppRegistryNotReady: Apps aren't loaded yet.，以上内容可以解决此问题,加载django中的App
import ddt

from WWTest.autotest.config.zhongshiyou.globalconfig.globalConfig import GlobalConfig,gc   #导入全局变量
from WWTest.base.activeBrowser import ActiveBrowser
from WWTest.util.getTimeStr import GetTimeStr
from WWTest.autotest.config.zhongshiyou.page.loginPage import *   #导入登录页
from WWTest.autotest.config.zhongshiyou.depend.clickAndBackDepend import ClickAndBackDepend,clickandbackdepend
    #导入 ClickAndBack依赖
from WWTest.autotest.config.zhongshiyou.depend.inputTapInputText import InputTapInputText,inputtapinputtext
from WWTest.autotest.config.zhongshiyou.depend.selectTapSelectOption import SelectTapSelectOption,selecttapselectoption
from WWTest.autotest.config.zhongshiyou.depend.selectTapSelectText import SelectTapSelectText,selecttapselecttext
from WWTest.autotest.config.zhongshiyou.depend.inputTapInputFile import InputTapInputFile,inputtapinputfile
from WWTest.autotest.config.zhongshiyou.depend.assertTipText import AssertTipText,asserttiptext
from WWTest.autotest.config.zhongshiyou.depend.inputTapInputDateTime import inputtapinputdatetime,InputTapInputDateTime
from WWTest.autotest.config.zhongshiyou.depend.radioAndReelectionLabel import RadioAndReelectionLabel,radioandreelectionlabel




class TestLoginClass(unittest.TestCase):  # 创建测试类

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
        self.activebrowser.getUrl(gc.TEST_WEB_YUMING)
        # lpf.login(self.activebrowser)
        pass

    def tearDown(self):  # 每条用例执行测试之后都要执行此方法
        self.activebrowser.closeBrowse()
        pass


    def definedepend(self,dependid):
        clickandbackdepend.clickandbackdepend(self.activebrowser,dependid)


    #定义新增函数
    def definelogin(self,num,login_id,
                    confirm_ele_find,confirm_ele_find_value,
                    click_confirm_delay_time
                     ):



        self.activebrowser.outPutMyLog("开始正式执行测试用例")
 
        #文本输入框添加内容
        inputtext_list = inputtapinputtext.inputtapinputtext(self.activebrowser,login_id)


        #点击登录按钮
        self.activebrowser.findEleAndClickConfigDelayTime(num, confirm_ele_find, confirm_ele_find_value,click_confirm_delay_time)
        self.activebrowser.getPageSource()
        print("已经点击确定按钮")
        # self.activebrowser.delayTime(30000)

        #验证验证文本信息
        asserttest_list_all = asserttiptext.assertiptext(self.activebrowser, login_id)
        asserttest_list_all_long = len(asserttest_list_all)
        for i in range(0, asserttest_list_all_long):
            self.assertTrue(asserttest_list_all[i][0], asserttest_list_all[i][1])

        if asserttest_list_all_long == 0 :
            self.activebrowser.outPutErrorMyLog("【异常提示】：本用例为验证点击登录按钮后的提示信息，"
                                                "但没有添加要验证的提示信息，"
                                                "请检查用例测试数据，将测试数据补充完整！")
            self.assertTrue(False)


    # def test001(self):
    #     print("第一条测试用例")
    #     self.definedepend(self.dependid)

    @staticmethod    #根据不同的参数生成测试用例
    def getTestFunc(num,login_id,
                    confirm_ele_find,confirm_ele_find_value,
                    click_confirm_delay_time):

        def func(self):
            self.definelogin(num,login_id,
                    confirm_ele_find,confirm_ele_find_value,
                    click_confirm_delay_time)
        return func

def __generateTestCases():
    from testdatas.models import NewAddAndCheck

    newaddandchecktestcase_all = NewAddAndCheck.objects.filter(is_run_case=True).\
        filter(test_project="中石油_迭代一").filter(test_module="登录").filter(id=214)\
        .order_by('id')

    for newaddandchecktestcase in newaddandchecktestcase_all:
        forcount = newaddandchecktestcase.case_counts
        starttime = GetTimeStr().getTimeStr()
        if len(str(newaddandchecktestcase.id)) == 1:
            newaddandchecktestcaseid = '0000%s' % newaddandchecktestcase.id
        elif len(str(newaddandchecktestcase.id)) == 2:
            newaddandchecktestcaseid = '000%s' % newaddandchecktestcase.id
        elif len(str(newaddandchecktestcase.id)) == 3:
            newaddandchecktestcaseid = '00%s' % newaddandchecktestcase.id
        elif len(str(newaddandchecktestcase.id)) == 4:
            newaddandchecktestcaseid = '0%s' % newaddandchecktestcase.id
        elif len(str(newaddandchecktestcase.id)) == 5:
            newaddandchecktestcaseid = '%s' % newaddandchecktestcase.id
        else:
            newaddandchecktestcaseid = 'Id已经超过5位数，请重新定义'

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
            args.append(newaddandchecktestcaseid)
            # args.append(i)
            args.append(newaddandchecktestcase.id)
            args.append(newaddandchecktestcase.confirm_ele_find)
            args.append(newaddandchecktestcase.confirm_ele_find_value)
            args.append(newaddandchecktestcase.click_confirm_delay_time)

            setattr(TestLoginClass,
                    'test_func_%s_%s_%s' % (newaddandchecktestcaseid, newaddandchecktestcase.test_case_title, forcount_i),
                    TestLoginClass.getTestFunc(*args))  # 通过setattr自动为TestCase类添加成员方法，方法以“test_func_”开头


__generateTestCases()

if __name__ == '__main__':
    print("hello world")
    unittest.main()












