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

class LoadTimesDefineClass(object):
    def __init__(self):
        self.img = """           // 首屏图片加载完成
                            let mytiming = window.performance.timing;
                            return window.lastImgLoadTime - mytiming.navigationStart ;
                """
        self.intfaces = """   //https://blog.csdn.net/weixin_42284354/article/details/80416157
        // 接口完成加载完成
                            let mytiming = window.performance.timing;
                            return Report.SPEED.LASTCGI - mytiming.navigationStart ;
                """
        self.DNS = """          // DNS查询耗时
                    let mytiming = window.performance.timing;
                    return mytiming.domainLookupEnd - mytiming.domainLookupStart ;
        """
        self.TCP = """          // TCP链接耗时
                    let mytiming = window.performance.timing;
                    return mytiming.connectEnd - mytiming.connectStart ;
        """
        self.request = """          // request请求耗时
                    let mytiming = window.performance.timing;
                    return mytiming.responseEnd  - mytiming.responseStart ;
        """
        self.dom = """          //  解析dom树耗时
                    let mytiming = window.performance.timing;
                    return mytiming.domComplete - mytiming.domInteractive ;
        """
        self.Ari = """          // 白屏时间
                    let mytiming = window.performance.timing;
                    return mytiming.responseStart - mytiming.navigationStart ;
        """

        self.domready = """          // domready时间
                    let mytiming = window.performance.timing;
                    return mytiming.domContentLoadedEventEnd   - mytiming.fetchStart ;
        """
        self.loadEventTime = """
                   let mytiming = window.performance.timing;
                   return mytiming.loadEventEnd - mytiming.navigationStart ;
                      """




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
        # lpf.login(self.activebrowser)
        lpf.loginwithcookiesauto(self.activebrowser)
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
        self.activebrowser.delayTime(3)
        self.activebrowser.driver.refresh()

        navigationStart_Time_js = """
        let mytiming = window.performance.timing;
        return mytiming.navigationStart;
        """
        print("navigationStart_Time:%s"%self.activebrowser.driver.execute_script(navigationStart_Time_js))

        fetchStart_Time_js = """
        let mytiming = window.performance.timing;
        return mytiming.fetchStart;
        """
        print("fetchStart_Time_js:%s"%self.activebrowser.driver.execute_script(fetchStart_Time_js))

        domainLookupStart_Time_js = """
        let mytiming = window.performance.timing;
        return mytiming.domainLookupStart;
        """
        print("domainLookupStart_Time_js:%s"%self.activebrowser.driver.execute_script(domainLookupStart_Time_js))

        domainLookupEnd_Time_js = """
        let mytiming = window.performance.timing;
        return mytiming.domainLookupEnd;
        """
        print("domainLookupEnd_Time_js:%s"%self.activebrowser.driver.execute_script(domainLookupEnd_Time_js))

        connectStart_Time_js = """
        let mytiming = window.performance.timing;
        return mytiming.connectStart;
        """
        print("connectStart_Time_js:%s"%self.activebrowser.driver.execute_script(connectStart_Time_js))

        connectEnd_Time_js = """
        let mytiming = window.performance.timing;
        return mytiming.connectEnd;
        """
        print("connectEnd_Time_js:%s"%self.activebrowser.driver.execute_script(connectEnd_Time_js))





        requestStart_Time_js = """
        let mytiming = window.performance.timing;
        return mytiming.requestStart;
        """
        print("requestStart_Time_js:%s"%self.activebrowser.driver.execute_script(requestStart_Time_js))

        responseEnd_Time_js = """
        let mytiming = window.performance.timing;
        return mytiming.responseEnd;
        """
        print("responseEnd_Time_js:%s"%self.activebrowser.driver.execute_script(responseEnd_Time_js))

        domLoading_Time_js = """
        let mytiming = window.performance.timing;
        return mytiming.domLoading;
        """
        print("domLoading_Time_js:%s"%self.activebrowser.driver.execute_script(domLoading_Time_js))

        domInteractive_Time_js = """
        let mytiming = window.performance.timing;
        return mytiming.domInteractive;
        """
        print("domInteractive_Time_js:%s"%self.activebrowser.driver.execute_script(domInteractive_Time_js))

        domContentLoadedEventStart_Time_js = """
        let mytiming = window.performance.timing;
        return mytiming.domContentLoadedEventStart;
        """
        print("domContentLoadedEventStart_Time_js:%s"%self.activebrowser.driver.execute_script(domContentLoadedEventStart_Time_js))

        domContentLoadedEventEnd_Time_js = """
        let mytiming = window.performance.timing;
        return mytiming.domContentLoadedEventEnd;
        """
        print("domContentLoadedEventEnd_Time_js:%s"%self.activebrowser.driver.execute_script(domContentLoadedEventEnd_Time_js))



        domComplete_Time_js = """
        let mytiming = window.performance.timing;
        return mytiming.domComplete;
        """
        print("domComplete_Time_js:%s"%self.activebrowser.driver.execute_script(domComplete_Time_js))

        loadEventStart_Time_js = """
        let mytiming = window.performance.timing;
        return mytiming.loadEventStart;
        """
        print("loadEventStart_Time_js:%s"%self.activebrowser.driver.execute_script(loadEventStart_Time_js))

        loadEventEnd_Time_js = """
        let mytiming = window.performance.timing;
        return mytiming.loadEventEnd;
        """
        print("loadEventEnd_Time_js_Time_js:%s"%self.activebrowser.driver.execute_script(loadEventEnd_Time_js))

        print(type(self.activebrowser.driver.execute_script(loadEventEnd_Time_js)))
        print(type(int(self.activebrowser.driver.execute_script(loadEventEnd_Time_js))))

        print("DNS查询耗时:%s" % str(self.activebrowser.driver.execute_script(domainLookupEnd_Time_js)-self.activebrowser.driver.execute_script(domainLookupStart_Time_js)))
        print("TCP链接耗时:%s" % str(self.activebrowser.driver.execute_script(connectEnd_Time_js) - self.activebrowser.driver.execute_script(connectStart_Time_js)))
        print("request请求耗时:%s" % str(self.activebrowser.driver.execute_script(responseEnd_Time_js)-self.activebrowser.driver.execute_script(requestStart_Time_js)))
        print("解析dom树耗时:%s" % str(self.activebrowser.driver.execute_script(domComplete_Time_js)-self.activebrowser.driver.execute_script(domInteractive_Time_js )))
        print("白屏时间:%s" % str(self.activebrowser.driver.execute_script(domLoading_Time_js)-self.activebrowser.driver.execute_script(fetchStart_Time_js)))
        print("domready时间:%s" % str(self.activebrowser.driver.execute_script(domContentLoadedEventEnd_Time_js)- self.activebrowser.driver.execute_script(fetchStart_Time_js)))
        print("onload时间:%s" % str(self.activebrowser.driver.execute_script(loadEventEnd_Time_js)-self.activebrowser.driver.execute_script(fetchStart_Time_js)))
        print("onload时间:%s" % str(self.activebrowser.driver.execute_script(loadEventEnd_Time_js)-self.activebrowser.driver.execute_script(navigationStart_Time_js)))







        #统计页面加载时间
        img = """           // 首屏图片加载完成
                            let mytiming = window.performance.timing;
                            return window.lastImgLoadTime - mytiming.navigationStart ;
                """
        # intfaces = """   //https://blog.csdn.net/weixin_42284354/article/details/80416157
        # // 接口完成加载完成
        #                     let mytiming = window.performance.timing;
        #                     return Report.SPEED.LASTCGI - mytiming.navigationStart ;
        #         """
        DNS = """          // DNS查询耗时
                    let mytiming = window.performance.timing;
                    return mytiming.domainLookupEnd - mytiming.domainLookupStart ;
        """
        # TCP = """          // TCP链接耗时
        #             let mytiming = window.performance.timing;
        #             return mytiming.connectEnd - mytiming.connectStart ;
        # """
        request = """          // request请求耗时
                    let mytiming = window.performance.timing;
                    return mytiming.responseEnd  - mytiming.responseStart ;
        """
        dom = """          //  解析dom树耗时
                    let mytiming = window.performance.timing;
                    return mytiming.domComplete - mytiming.domInteractive ;
        """
        # Ari = """          // 白屏时间
        #             let mytiming = window.performance.timing;
        #             return mytiming.responseStart - mytiming.navigationStart ;
        # """

        domready = """          // domready时间
                    let mytiming = window.performance.timing;
                    return mytiming.domContentLoadedEventEnd   - mytiming.fetchStart ;
        """
        loadEventTime = """
                   let mytiming = window.performance.timing;
                   return mytiming.loadEventEnd - mytiming.navigationStart ;
                   """

        #首屏图片加载完成时间
        first_image_load_time = """
        let mytiming = window.performance.timing;
        return window.lastImgLoadTime 
        //return window.lastImgLoadTime - mytiming.navigationStart;
        """

        # HTML加载完成时间
        html_load_time = """
        let mytiming = window.performance.timing;
        //return mytiming.navigationStart;
        return window.loadHtmlTime
        //return window.loadHtmlTime - mytiming.navigationStart;
        """














        # self.activebrowser.driver.execute_script(img)
        # self.activebrowser.driver.execute_script(intfaces)
        # self.activebrowser.driver.execute_script(DNS)
        # self.activebrowser.driver.execute_script(TCP)
        # self.activebrowser.driver.execute_script(request)
        # self.activebrowser.driver.execute_script(dom)
        # self.activebrowser.driver.execute_script(Ari)
        DNS_time = self.activebrowser.driver.execute_script(DNS)
        request_time = self.activebrowser.driver.execute_script(request)
        first_image_load =self.activebrowser.driver.execute_script(first_image_load_time)
        html_load = self.activebrowser.driver.execute_script(html_load_time)

        page_time_NoCatch = int(self.activebrowser.driver.execute_script(loadEventTime))
        dom_time_NoCatch = int(self.activebrowser.driver.execute_script(domready))

        print("首屏图片加载完成时间：%s" % first_image_load)
        print("HTML加载完成时间：%s" % html_load)
        print("请求时间：%s" % request_time)
        print("DNS时间：%s" % DNS_time)
        print("无缓存页面加载时间：%s" % page_time_NoCatch)
        print("无缓存DOM加载时间：%s" % dom_time_NoCatch)

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

        self.activebrowser.delayTime(3)





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












