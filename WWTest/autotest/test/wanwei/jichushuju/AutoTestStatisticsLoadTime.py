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


class TestClickAndBackClass(unittest.TestCase):  # 创建测试类

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
        lpf.login(self.activebrowser)
        # lpf.loginwithcookiesauto(self.activebrowser)
        pass

    def tearDown(self):  # 每条用例执行测试之后都要执行此方法
        self.activebrowser.closeBrowse()
        pass


    def definedepend(self,dependid):
        clickandbackdepend.clickandbackdepend(self.activebrowser,dependid)


    #定义点击返回函数
    def defineclickandback(self,num,case_counts,depend_case_id,
                           current_page_click_ele_find, current_page_click_ele_find_value,
                           is_new,
                           next_page_check_ele_find,next_page_check_ele_find_value,
                           testproject, testmodule, testpage,
                           testcasetitle, teststarttime,
                           forcount
                           ):


        #如果有依赖ID，则执行依赖函数，达到执行当前用例的前提条件
        if depend_case_id != None:
            self.definedepend(depend_case_id)
            self.activebrowser.outPutMyLog("依赖函数执行完毕！！！")

        self.activebrowser.outPutMyLog("开始正式执行测试用例")
        #点击当前页面元素
        self.activebrowser.findEleAndClickNoDelayTime(num, current_page_click_ele_find, current_page_click_ele_find_value)


        domready = """          // domready时间
                    let mytiming = window.performance.timing;
                    return mytiming.domContentLoadedEventEnd   - mytiming.fetchStart ;
        """
        loadEventTime = """
                   let mytiming = window.performance.timing;
                   return mytiming.loadEventEnd - mytiming.navigationStart ;
                   """

        all_time = """
                return window.performance.getEntries()
        """

        page_time_NoCatch = int(self.activebrowser.driver.execute_script(loadEventTime))
        dom_time_NoCatch = int(self.activebrowser.driver.execute_script(domready))
        load_all_time = self.activebrowser.driver.execute_script(all_time)

        print("无缓存页面加载时间：%s" % page_time_NoCatch)
        print("无缓存DOM加载时间：%s" % dom_time_NoCatch)
        print("load_all_time：%s" % load_all_time)

        #保存时间到库
        from reportdatas.models import PageLoadTimeReport
        pageloadtimereport = PageLoadTimeReport()
        pageloadtimereport.testproject = testproject
        pageloadtimereport.testmodule = testmodule
        pageloadtimereport.testpage = testpage
        pageloadtimereport.testcasetitle = testcasetitle
        pageloadtimereport.teststarttime = teststarttime
        pageloadtimereport.forcount = forcount
        pageloadtimereport.page_load_time_no_catch = page_time_NoCatch
        pageloadtimereport.dom_load_time_no_catch = dom_time_NoCatch
        pageloadtimereport.save()

        if page_time_NoCatch >= 1000 and page_time_NoCatch < 2000:
            #保存到统计1秒到2秒的库中
            from reportpageloadtime.models import PageLoadTimeReportOneSecond
            pageloadtimereportonesecond = PageLoadTimeReportOneSecond()
            pageloadtimereportonesecond.testproject = testproject
            pageloadtimereportonesecond.testmodule = testmodule
            pageloadtimereportonesecond.testpage = testpage
            pageloadtimereportonesecond.testcasetitle = testcasetitle
            pageloadtimereportonesecond.teststarttime = teststarttime
            pageloadtimereportonesecond.forcount = forcount
            pageloadtimereportonesecond.page_load_time_no_catch = page_time_NoCatch
            pageloadtimereportonesecond.dom_load_time_no_catch = dom_time_NoCatch
            pageloadtimereportonesecond.save()

        elif page_time_NoCatch >= 2000 and page_time_NoCatch < 3000:
            #保存到统计2秒到3秒的库中
            from reportpageloadtime.models import PageLoadTimeReportTwoSecond
            pageloadtimereporttwosecond = PageLoadTimeReportTwoSecond()
            pageloadtimereporttwosecond.testproject = testproject
            pageloadtimereporttwosecond.testmodule = testmodule
            pageloadtimereporttwosecond.testpage = testpage
            pageloadtimereporttwosecond.testcasetitle = testcasetitle
            pageloadtimereporttwosecond.teststarttime = teststarttime
            pageloadtimereporttwosecond.forcount = forcount
            pageloadtimereporttwosecond.page_load_time_no_catch = page_time_NoCatch
            pageloadtimereporttwosecond.dom_load_time_no_catch = dom_time_NoCatch
            pageloadtimereporttwosecond.save()

        elif page_time_NoCatch >= 3000 and page_time_NoCatch < 4000:
            # 保存到统计3秒到4秒的库中
            from reportpageloadtime.models import PageLoadTimeReportThereSecond
            pageloadtimereporttheresecond = PageLoadTimeReportThereSecond()
            pageloadtimereporttheresecond.testproject = testproject
            pageloadtimereporttheresecond.testmodule = testmodule
            pageloadtimereporttheresecond.testpage = testpage
            pageloadtimereporttheresecond.testcasetitle = testcasetitle
            pageloadtimereporttheresecond.teststarttime = teststarttime
            pageloadtimereporttheresecond.forcount = forcount
            pageloadtimereporttheresecond.page_load_time_no_catch = page_time_NoCatch
            pageloadtimereporttheresecond.dom_load_time_no_catch = dom_time_NoCatch
            pageloadtimereporttheresecond.save()

        elif page_time_NoCatch >= 4000 and page_time_NoCatch < 5000:
            #保存到统计4秒到5秒的库中
            from reportpageloadtime.models import PageLoadTimeReportFourSecond
            pageloadtimereportfoursecond = PageLoadTimeReportFourSecond()
            pageloadtimereportfoursecond.testproject = testproject
            pageloadtimereportfoursecond.testmodule = testmodule
            pageloadtimereportfoursecond.testpage = testpage
            pageloadtimereportfoursecond.testcasetitle = testcasetitle
            pageloadtimereportfoursecond.teststarttime = teststarttime
            pageloadtimereportfoursecond.forcount = forcount
            pageloadtimereportfoursecond.page_load_time_no_catch = page_time_NoCatch
            pageloadtimereportfoursecond.dom_load_time_no_catch = dom_time_NoCatch
            pageloadtimereportfoursecond.save()

        elif page_time_NoCatch >= 5000 :
            #保存到统计5秒及其以上的库中
            from reportpageloadtime.models import PageLoadTimeReportFiveSecond
            pageloadtimereportfivesecond = PageLoadTimeReportFiveSecond()
            pageloadtimereportfivesecond.testproject = testproject
            pageloadtimereportfivesecond.testmodule = testmodule
            pageloadtimereportfivesecond.testpage = testpage
            pageloadtimereportfivesecond.testcasetitle = testcasetitle
            pageloadtimereportfivesecond.teststarttime = teststarttime
            pageloadtimereportfivesecond.forcount = forcount
            pageloadtimereportfivesecond.page_load_time_no_catch = page_time_NoCatch
            pageloadtimereportfivesecond.dom_load_time_no_catch = dom_time_NoCatch
            pageloadtimereportfivesecond.save()






    # def test001(self):
    #     print("第一条测试用例")
    #     self.definedepend(self.dependid)

    @staticmethod    #根据不同的参数生成测试用例
    def getTestFunc(num,case_counts,depend_case_id,
                           current_page_click_ele_find, current_page_click_ele_find_value,
                           is_new,
                           next_page_check_ele_find,next_page_check_ele_find_value,
                           testproject, testmodule, testpage,
                           testcasetitle, teststarttime,
                           forcount):

        def func(self):
            self.defineclickandback(num,case_counts,depend_case_id,
                           current_page_click_ele_find, current_page_click_ele_find_value,
                           is_new,
                           next_page_check_ele_find,next_page_check_ele_find_value,
                           testproject, testmodule, testpage,
                           testcasetitle, teststarttime,
                           forcount)
        return func

def __generateTestCases():
    from testdatas.models import ClickAndBack

    clickandbacktestcase_all = ClickAndBack.objects.filter(id=123).order_by('id')

    for clickandbacktestcase in clickandbacktestcase_all:
        forcount = clickandbacktestcase.case_counts
        starttime = GetTimeStr().getTimeStr()
        if len(str(clickandbacktestcase.id)) == 1:
            clickandbacktestcaseid = '0000%s' % clickandbacktestcase.id
        elif len(str(clickandbacktestcase.id)) == 2:
            clickandbacktestcaseid = '000%s' % clickandbacktestcase.id
        elif len(str(clickandbacktestcase.id)) == 3:
            clickandbacktestcaseid = '00%s' % clickandbacktestcase.id
        elif len(str(clickandbacktestcase.id)) == 4:
            clickandbacktestcaseid = '0%s' % clickandbacktestcase.id
        elif len(str(clickandbacktestcase.id)) == 5:
            clickandbacktestcaseid = '%s' % clickandbacktestcase.id
        else:
            clickandbacktestcaseid = 'Id已经超过5位数，请重新定义'

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
            args.append(clickandbacktestcaseid)
            args.append(i)
            args.append(clickandbacktestcase.depend_case_id)
            args.append(clickandbacktestcase.current_page_click_ele_find)
            args.append(clickandbacktestcase.current_page_click_ele_find_value)
            args.append(clickandbacktestcase.is_new)
            args.append(clickandbacktestcase.next_page_check_ele_find)
            args.append(clickandbacktestcase.next_page_check_ele_find_value)

            args.append(clickandbacktestcase.test_project)
            args.append(clickandbacktestcase.test_module)
            args.append(clickandbacktestcase.test_page)
            args.append(clickandbacktestcase.test_case_title)
            args.append(starttime)
            args.append(i)



            setattr(TestClickAndBackClass,
                    'test_func_%s_%s_%s' % (clickandbacktestcaseid, clickandbacktestcase.test_case_title, forcount_i),
                    TestClickAndBackClass.getTestFunc(*args))  # 通过setattr自动为TestCase类添加成员方法，方法以“test_func_”开头


__generateTestCases()

if __name__ == '__main__':
    print("hello world")
    unittest.main()












