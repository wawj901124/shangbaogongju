import unittest
# ----------------------------------------------------------------------
import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wanwenyc.settings")
django.setup()
# ----------------------------------------------------------------------
#独运行某一个py文件时会出现如下错误：django.core.exceptions.AppRegistryNotReady: Apps aren't loaded yet.，以上内容可以解决此问题,加载django中的App
import ddt

from WWTest.autotest.config.wanwei.globalconfig.globalConfig import GlobalConfig,gc   #导入全局变量
from WWTest.base.activeBrowser import ActiveBrowser
from WWTest.util.getTimeStr import GetTimeStr
from WWTest.autotest.config.wanwei.page.loginPage import *   #导入登录页
from WWTest.autotest.config.wanwei.depend.clickAndBackDepend import ClickAndBackDepend,clickandbackdepend
    #导入 ClickAndBack依赖
from WWTest.autotest.config.wanwei.depend.searchInputTapInputText import SearchInputTapInputText,searchinputtapinputtext
from WWTest.autotest.config.wanwei.depend.searchSelectTapSelectOption import SearchSelectTapSelectOption,searchselecttapselectoption





class TestSearchClass(unittest.TestCase):  # 创建测试类

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


    def definedepend(self,dependid):
        clickandbackdepend.clickandbackdepend(self.activebrowser,dependid)


    #定义查询函数
    def definenewadd(self,num,depend_click_case_id,
                     search_id,
                     serach_ele_find,search_ele_find_value,
                     is_with_date,
                     result_table_ele_find,result_table_ele_find_value
                     ):


        #如果有依赖ID，则执行依赖函数，达到执行当前用例的前提条件
        if depend_click_case_id != None:
            print("depend_click_case_id：%s" % depend_click_case_id)
            self.definedepend(depend_click_case_id)
            self.activebrowser.outPutMyLog("依赖函数执行完毕！！！")

        self.activebrowser.outPutMyLog("开始正式执行测试用例")




        #文本输入框搜素内容
        inputtext_list = searchinputtapinputtext.searchinputtapinputtext(self.activebrowser,search_id)
        inputtext_list_len = len(inputtext_list)

        #选项框添加内容
        selectoptiontext_list = searchselecttapselectoption.searchselecttapselectoption(self.activebrowser,search_id)
        selectoptiontext_list_long = len(selectoptiontext_list)

        # #日期添加内容
        # inputtapinputdatetime.inputtapinputdatetime(self.activebrowser,addnew_id)


        #点击查询按钮
        self.activebrowser.findEleAndClick(num,serach_ele_find,search_ele_find_value)

        if is_with_date:   #如果预期是查询到数据，则对数据进行验证

            #验证输入框文本信息
            inputtext_list_len = len(inputtext_list)
            for i in range(0, inputtext_list_len):
                colmun_list = inputtext_list[i][1].split(",")
                self.activebrowser.outPutMyLog("colmun_list:%s" % colmun_list)
                colmun_list_long = len(colmun_list)
                result_check_list = []
                for j in range(0,colmun_list_long):
                    result_check_j = self.activebrowser.findEleAndCheckTableOneColnum(num, result_table_ele_find,
                                                                                result_table_ele_find_value,
                                                                                inputtext_list[i][0],
                                                                                      int(colmun_list[j])-1)
                    result_check_list.append(result_check_j)
                self.activebrowser.outPutMyLog("result_check_list:%s" % result_check_list)
                self.assertIn(True, result_check_list)
                # self.assertTrue(result_check)

            #验证选项框文本信息
            selectoptiontext_list_long = len(selectoptiontext_list)
            for i in range(0, selectoptiontext_list_long):
                result_check = self.activebrowser.findEleAndCheckTableOneColnum(num, result_table_ele_find,
                                                                                result_table_ele_find_value,
                                                                                selectoptiontext_list[i][0],
                                                                                int(selectoptiontext_list[i][1])-1)
                self.assertTrue(result_check)

        else: #否则断言“暂无数据”在页面中
            self.activebrowser.delayTime(10)
            self.assertIn("暂无数据",self.activebrowser.getPageSource())


        if inputtext_list_len == 0 and selectoptiontext_list_long == 0:
            self.activebrowser.getScreenshotAboutMySQL()
            self.activebrowser.outPutErrorMyLog("【异常提示】：本用例为查询测试用例，"
                                                "但没有添加要输入或选择的测试数据，"
                                                "请检查用例测试数据，将测试数据补充完整！")
            self.assertTrue(False)

            

    # def test001(self):
    #     print("第一条测试用例")
    #     self.definedepend(self.dependid)

    @staticmethod    #根据不同的参数生成测试用例
    def getTestFunc(num,depend_click_case_id,
                    search_id,
                     serach_ele_find,search_ele_find_value,
                     is_with_date,
                     result_table_ele_find,result_table_ele_find_value):

        def func(self):
            self.definenewadd(num,depend_click_case_id,
                     search_id,
                     serach_ele_find,search_ele_find_value,
                     is_with_date,
                     result_table_ele_find,result_table_ele_find_value)
        return func

def __generateTestCases():
    from testdatas.models import SearchAndCheck

    searchandchecktestcase_all = SearchAndCheck.objects.filter(is_run_case=True).\
        filter(test_project="餐饮油烟监管治服一体化平台").\
        filter(test_module="基础数据").\
        filter(test_page="监测设备").\
        order_by('id')

    for searchandchecktestcase in searchandchecktestcase_all:
        forcount = searchandchecktestcase.case_counts
        starttime = GetTimeStr().getTimeStr()
        if len(str(searchandchecktestcase.id)) == 1:
            searchandchecktestcaseid = '0000%s' % searchandchecktestcase.id
        elif len(str(searchandchecktestcase.id)) == 2:
            searchandchecktestcaseid = '000%s' % searchandchecktestcase.id
        elif len(str(searchandchecktestcase.id)) == 3:
            searchandchecktestcaseid = '00%s' % searchandchecktestcase.id
        elif len(str(searchandchecktestcase.id)) == 4:
            searchandchecktestcaseid = '0%s' % searchandchecktestcase.id
        elif len(str(searchandchecktestcase.id)) == 5:
            searchandchecktestcaseid = '%s' % searchandchecktestcase.id
        else:
            searchandchecktestcaseid = 'Id已经超过5位数，请重新定义'

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
            args.append(searchandchecktestcaseid)
            # args.append(i)
            args.append(searchandchecktestcase.depend_click_case_id)
            args.append(searchandchecktestcase.id)
            args.append(searchandchecktestcase.search_ele_find)
            args.append(searchandchecktestcase.search_ele_find_value)
            args.append(searchandchecktestcase.is_with_date)
            args.append(searchandchecktestcase.result_table_ele_find)
            args.append(searchandchecktestcase.result_table_ele_find_value)


            setattr(TestSearchClass,
                    'test_func_%s_%s_%s' % (searchandchecktestcaseid, searchandchecktestcase.test_case_title, forcount_i),
                    TestSearchClass.getTestFunc(*args))  # 通过setattr自动为TestCase类添加成员方法，方法以“test_func_”开头


__generateTestCases()

if __name__ == '__main__':
    print("hello world")
    unittest.main()












