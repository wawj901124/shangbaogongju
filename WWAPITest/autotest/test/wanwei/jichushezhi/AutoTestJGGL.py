import unittest
# ----------------------------------------------------------------------
import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wanwenyc.settings")
django.setup()
# ----------------------------------------------------------------------
#独运行某一个py文件时会出现如下错误：django.core.exceptions.AppRegistryNotReady: Apps aren't loaded yet.，以上内容可以解决此问题,加载django中的App

from WWTest.autotest.config.wanwei.page.jichushezhi.JGGLPage import *
from WWTest.util.getTimeStr import GetTimeStr



class TestTestJCSZ_JGGLClass(unittest.TestCase):  # 创建测试类


    @classmethod  # 类方法，只执行一次，但必须要加注解@classmethod,且名字固定为setUpClass
    def setUpClass(cls):
        # cls.activebroswer = ActiveBrowser()  # 实例化
        # cls.loginurl = LoginPage().pageurl
        # cls.activeweb.getUrl(cls.loginurl)  # 打开网址
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
        self.activebrowser = ActiveBrowser()
        lpf.login(self.activebrowser)
        # lpf.loginwithcookies(self.activebrowser)
        clickandbackdepend.clickandbackdepend(self.activebrowser,"10")
        self.activebrowser.delayTime(3)
        # self.activebrowser.findEleAndClick(0,"xpath","/html/body/div/div/div/div[1]/div/div/div[2]/i")
        #
        # # self.activebrowser.findEleAndClick(0, "xpath", "/html/body/div/div/div/div[2]/div/div[2]/ul/li[1]/div/div/div/span")
        #
        # self.activebrowser.findEleAndClick(0, "xpath",
        #                                    "/html/body/div/div/div/div[2]/div/div[2]/ul/li[5]/div/div/div/span")
        #
        # self.activebrowser.findEleAndClick(0, "xpath",
        #                                    "/html/body/div/div/div/div[2]/div/div[2]/ul/li[5]/ul/div[1]/li/div/div/span")
        #
        # self.activebrowser.getPageSource()

        # self.activebrowser.getUrl(jigouguanlipage.pageurl)
        # self.activebrowser.delayTime(5)
        # jigouguanlipagefunction.clickAdd(self.activebrowser)
        # timestr = GetTimeStr().getTimeStr()
        # jigougunaliaddpagefunction.add_JiGOu(self.activebrowser,False,timestr,timestr,timestr)
        pass

    def tearDown(self):  # 每条用例执行测试之后都要执行此方法
        # self.activeweb.closeBrowse()
        pass

    def defineAdd_JiGou(self,):
        timestr = GetTimeStr().getTimeStr()
        jigougunaliaddpagefunction.add_JiGOu(self.activebrowser,False,timestr,timestr,timestr)




    def test001(self):
        # print("第一条测试用例")
        self.defineAdd_JiGou()

    # def test002(self):
    #     print("第二条测试用例")






if __name__ == '__main__':
    print("hello world")
    unittest.main()










