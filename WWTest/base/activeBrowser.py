
# ----------------------------------------------------------------------
import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wanwenyc.settings")
django.setup()
# ----------------------------------------------------------------------
#独运行某一个py文件时会出现如下错误：django.core.exceptions.AppRegistryNotReady: Apps aren't loaded yet.，以上内容可以解决此问题,加载django中的App
from wanwenyc.settings import MEDIA_ROOT    #导入Settings中配置的MEDIA_ROOT

#------------------------导入系统包-----------------------------------------
import time   #导入时间
import os
import sys
import traceback
import json
# import win32gui
# import win32con

#------------------------导入第三方包-----------------------------------------
from selenium import webdriver   #导入驱动
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from PIL import Image   #导入Image
from PIL import ImageEnhance  #导入ImageEnhance
import pytesseract   #导入pytesseract
from selenium.webdriver.support.select import Select   #导入Select
from selenium.webdriver.common.action_chains import ActionChains   #导入ActionChains
# from bs4 import BeautifulSoup
from selenium.webdriver.support.wait import WebDriverWait

##------------------------导入自定义的包-----------------------------------------
from WWTest.util.getTimeStr import GetTimeStr   #导入获取时间串函数
from WWTest.util.myLogs import MyLogs
from WWTest.util.identificationVerificationCode import IdentificationVerificationCode
from WWTest.util.operationJson import OperationJson



class  ActiveBrowser(object):

    def __init__(self,driver=None):
        # self.driver = self.getChromeDriver()
        # self.driver = self.getIeDriver()
        if driver==None:
            self.driver = self.getChromeDriver()
            # self.driver = self.getFirefoxDriver()
        elif driver == 'firefox':
            self.driver = self.getFirefoxDriver()
        elif driver == 'chrome':
            self.driver = self.getChromeDriver()
        elif driver == 'ie':
            self.driver = self.getIeDriver()

        self.timeStr = GetTimeStr()   #实例化


    #使用火狐浏览器
    def getFirefoxDriver(self):
        # binary = FirefoxBinary(r'D:\Program Files (x86)\Mozilla Firefox\firefox.exe')
        # firefoxdriver = webdriver.Firefox(firefox_binary=binary)
        # fire_options = webdriver.FirefoxOptions()   #为驱动加入无界面配置
        # fire_options.add_argument('--headless')   #为驱动加入无界面配置
        # fire_options.debuggerAddress="127.0.0.1:12306"

        # 配置文件路径
        # profile_path = r'/usr/lib64/firefox/'
        # profile_path = r'/root/firefox/'
        # # 加载配置数据
        # profile = webdriver.FirefoxProfile(profile_path)
        firefoxdriver = webdriver.Firefox()
        # firefoxdriver = webdriver.Firefox(firefox_options=fire_options)  # 需要把驱动所在路径配置到系统环境变量里
        # path = r"%s/driver/geckodriver" % str(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) ) # 配置驱动路径
        # print("path:%s"%path)
        # firefoxdriver = webdriver.Firefox(firefox_profile=fire_options,executable_path=path)
        # firefoxdriver = webdriver.Firefox(executable_path=path)
        firefoxdriver.maximize_window()   #窗口最大化
        return  firefoxdriver



    #使用谷歌浏览器
    def getChromeDriver(self):

        print(sys.getdefaultencoding())  # 系统默认编码

        #谷歌浏览器下载网址：https://www.google.cn/chrome/
        #谷歌驱动更新网址：http://chromedriver.storage.googleapis.com/index.html



        #开启谷歌浏览器访问端口
        #1.将chrome的安装路径配置到环境变量中
        #2.在cmd中输入：chrome.exe --remote-debugging-port=9222 --user-data-dir="D:\Users\Administrator\PycharmProjects\wanwenyc\driver"，按回车键打开谷歌浏览器
            #其中--remote-debugging-port中的值，可以指定任何打开的端口
            #--user-data-dir标记，指定创建新Chrome配置文件的目录，它是为了保存在单独的配置文件中启动chrome,不会污染你的默认配置文件
        #3.在参数中设置chrome_options.add_experimental_option("debuggerAddress","127.0.0.1:9222") #连接之前打开的浏览器
        # chromd_exe_dir = r"C:\Program Files (x86)\Google\Chrome\Application"
        # my_data_dir = r"%s/driver/chromedatadir/"% str(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) )  #配置驱动路径
        # self.createdir(my_data_dir)
        # # cmdorder = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe --remote-debugging-port=9222 --user-data-dir="+'"%s"' %my_data_dir
        # cmdorder = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
        # print(cmdorder)
        # os.popen(cmdorder)

        chrome_options = webdriver.ChromeOptions()   #为驱动加入无界面配置

        chrome_options.add_argument('--headless')   #–headless”参数是不用打开图形界面
        chrome_options.add_argument('--no-sandbox')  #“–no - sandbox”参数是让Chrome在root权限下跑
        chrome_options.add_argument("--kiosk") #全屏启动
        chrome_options.add_argument("--start-maximized")  #全屏启动
        chrome_options.add_argument("--start-fullscreen")  #全屏启动
        #chrome_options.add_argument("--window-size=4000,1600")  #专门应对无头浏览器中不能最大化屏幕的方案
        chrome_options.add_argument("--window-size=1920,1050")  # 专门应对无头浏览器中不能最大化屏幕的方案
        # chrome_options.add_experimental_option("debuggerAddress","127.0.0.1:9222")   #设置打开谷歌浏览器用9222端口，保证只要有一个浏览器打开，再次会使用同一个
        ## chrome_options.debugger_address="127.0.0.1:9222" #设置打开谷歌浏览器用9222端口，保证只要有一个浏览器打开，再次会使用同一个
        # chrome_options.add_argument('--disable-dev-shm-usage') #不加载图片, 提升速度
        # chrome_options.add_argument('blink-settings=imagesEnabled=false')
        # chrome_options.add_argument('--disable-gpu') # 谷歌文档提到需要加上这个属性来规避bug
        # chromedriver = webdriver.Chrome(chrome_options=chrome_options)
        # chromedriver = webdriver.Chrome()  # 需要把驱动所在路径配置到系统环境变量里
        path = r"%s/driver/chromedriver"% str(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) )  #配置驱动路径
        print("path:%s" % path)
        # path = r"D:\Users\Administrator\PycharmProjects\webtestdata\TestCaseFunction\driver\chromedriver.exe"  #配置驱动路径
        # option = webdriver.ChromeOptions()
        # option.add_argument('--user-data-dir=C:\\Users\\Administrator\\Local\\Google\\Chrome\\User Data\\Default')  # 设置成用户自己的数据目录
        #                                                             #浏览器输入chrome://version 下个人资料路径就是自己的数据目录
        # chromedriver = webdriver.Chrome(chrome_options=chrome_options)
        chromedriver = webdriver.Chrome(executable_path=path,chrome_options=chrome_options)
        # chromedriver = webdriver.Chrome(executable_path=path)
        # chromedriver = webdriver.Chrome(executable_path=path)
        chromedriver.maximize_window()   #窗口最大化
        # self.delayTime(5)
        chromedriver.implicitly_wait(1)#设置隐形等待时间为1秒
        self.outPutMyLog("隐形等待1秒")
        return  chromedriver



    #使用IE浏览器
    def getIeDriver(self):
        iedriver = webdriver.Ie()  # 需要把驱动所在路径配置到系统环境变量里
        return  iedriver

    #使用Edge浏览器
    def getEdgeDriver(self):
        edgedriver = webdriver.Edge()  # 需要把驱动所在路径配置到系统环境变量里
        return  edgedriver


    #使用Opera浏览器
    def getOperaDriver(self):
        operadriver = webdriver.Opera  # 需要把驱动所在路径配置到系统环境变量里
        return  operadriver


    #显性等待函数
    def showWait(self,findstyle,findstylevalue):
        if str(findstyle) == "xpath":
            self.outPutMyLog("进入显性等待...")
            #设置查询十秒，每隔0.5秒查询一次，10秒查询不到则报超时
            WebDriverWait(self.driver,10,0.5).until(self.driver.find_element_by_xpath(findstylevalue),"等待10秒没有查找到元素")
            self.outPutMyLog("找到元素")
    def outPutMyLog(self,context):
        mylog = MyLogs(context)
        mylog.runMyLog()


    def outPutErrorMyLog(self,context):
        mylog = MyLogs(context)
        mylog.runErrorLog()



    #打开网址
    def getUrl(self,url):
        try:
            self.driver.get(url)
            self.outPutMyLog("进入网址：%s"% url)
            # print("进入网址：%s"% url)
        except Exception as e:
            self.getScreenshotAboutMySQL()  # 截图关联django服务
            self.outPutErrorMyLog("打开网页失败,关闭驱动.问题描述：[%s]" % e)
            self.closeBrowse()
            assert False


    #获取当前页面的url
    def getNowPageUrl(self):
        NowPageUrl = self.driver.current_url
        self.outPutMyLog("当前页面的URL为：%s" %  NowPageUrl)
        return NowPageUrl

    def getFatherSonElesList(self,fatherfindstyle,fatherfindstylevalue,sonfindstyle,sonfindstylevalue):

        father = self.findELe(fatherfindstyle,fatherfindstylevalue)
        issecond = False
        try:
            if str(sonfindstyle) == "class_name":
                sonElesList = father.find_elements_by_class_name(sonfindstylevalue)
                self.outPutMyLog("找到class_name为【%s】的元素" % sonfindstylevalue)
            elif str(sonfindstyle) == "css_selector":
                sonElesList = father.find_elements_by_css_selector(sonfindstylevalue)
                self.outPutMyLog("找到css_selector为【%s】的元素" % sonfindstylevalue)
            elif str(sonfindstyle) == "id":
                sonElesList = father.find_elements_by_id(sonfindstylevalue)
                self.outPutMyLog("找到id为【%s】的元素" % sonfindstylevalue)
            elif str(sonfindstyle) == "link_text":
                sonElesList = father.find_elements_by_link_text(sonfindstylevalue)
                self.outPutMyLog("找到link_text为【%s】的元素" % sonfindstylevalue)
            elif str(sonfindstyle) == "name":
                sonElesList = father.find_elements_by_name(sonfindstylevalue)
                self.outPutMyLog("找到name为【%s】的元素" % sonfindstylevalue)
            elif str(sonfindstyle) == "partial_link_text":
                sonElesList = father.find_elements_by_partial_link_text(sonfindstylevalue)
                self.outPutMyLog("找到link_text为【%s】的元素" % sonfindstylevalue)
            elif str(sonfindstyle) == "tag_name":
                sonElesList = father.find_elements_by_tag_name(sonfindstylevalue)
                self.outPutMyLog("找到tag_name为【%s】的元素" % sonfindstylevalue)
            elif str(sonfindstyle) == "xpath":
                sonElesList = father.find_elements_by_xpath(sonfindstylevalue)
                self.outPutMyLog("找到xpath为【%s】的元素" % sonfindstylevalue)
            else:
                self.outPutErrorMyLog("元素的查找方式不再八类（id、name、class_name、tag_name、"
                                      "link_text、partial_link_text、css_selector、xpath）之中，"
                                      "请输入正确的查找方式.")
        except Exception as e:
            self.outPutMyLog("问题描述：%s" % e)
            self.getScreenshotNormal()
            self.delayTime(5)
            issecond = True

        if issecond:
            try:
                if str(sonfindstyle) == "class_name":
                    sonElesList = father.find_elements_by_class_name(sonfindstylevalue)
                    self.outPutMyLog("再次查找，找到class_name为【%s】的元素" % sonfindstylevalue)
                elif str(sonfindstyle) == "css_selector":
                    sonElesList = father.find_elements_by_css_selector(sonfindstylevalue)
                    self.outPutMyLog("再次查找，找到css_selector为【%s】的元素" % sonfindstylevalue)
                elif str(sonfindstyle) == "id":
                    sonElesList = father.find_elements_by_id(sonfindstylevalue)
                    self.outPutMyLog("再次查找，找到id为【%s】的元素" % sonfindstylevalue)
                elif str(sonfindstyle) == "link_text":
                    sonElesList = father.find_elements_by_link_text(sonfindstylevalue)
                    self.outPutMyLog("再次查找，找到link_text为【%s】的元素" % sonfindstylevalue)
                elif str(sonfindstyle) == "name":
                    sonElesList = father.find_elements_by_name(sonfindstylevalue)
                    self.outPutMyLog("再次查找，找到name为【%s】的元素" % sonfindstylevalue)
                elif str(sonfindstyle) == "partial_link_text":
                    sonElesList = father.find_elements_by_partial_link_text(sonfindstylevalue)
                    self.outPutMyLog("再次查找，找到link_text为【%s】的元素" % sonfindstylevalue)
                elif str(sonfindstyle) == "tag_name":
                    sonElesList = father.find_elements_by_tag_name(sonfindstylevalue)
                    self.outPutMyLog("再次查找，找到tag_name为【%s】的元素" % sonfindstylevalue)
                elif str(sonfindstyle) == "xpath":
                    sonElesList = father.find_elements_by_xpath(sonfindstylevalue)
                    self.outPutMyLog("再次查找，找到xpath为【%s】的元素" % sonfindstylevalue)
                else:
                    self.outPutErrorMyLog("元素的查找方式不再八类（id、name、class_name、tag_name、"
                                          "link_text、partial_link_text、css_selector、xpath）之中，"
                                          "请输入正确的查找方式.")
            except Exception as e:
                self.getScreenshotAboutMySQL()  #截图关联django服务
                # self.getScreenshot()  #截图不关联django服务
                self.outPutErrorMyLog("停顿5秒后再次查找依然未找到元素.问题描述：%s" % e)
                self.closeBrowse()
                assert False
        return sonElesList

    #查找ul中对应的li元素并点击
    def findUlAndClickSelectLi(self,ul_xpath,li_text):
        li_text_list = []
        li_like_text_list = []
        son_ele_s = self.getFatherSonElesList("xpath", ul_xpath, "tag_name", "li")  # 获取选项的所有li元素
        son_count = len(son_ele_s)
        for son_count_one in range(1, son_count + 1, 1):
            li_xpath_one = "%s/%s[%s]" % (ul_xpath, "li", son_count_one)
            # 获取li的文本内容
            li_one_text = self.findElementByXpathAndReturnTextNotNum(li_xpath_one)
            print(li_one_text)
            li_text_list.append(li_one_text)

            if li_text in li_one_text:  # 如果元素文本包含预期，则进行点击选择
                li_like_text_list.append(li_one_text)
                # self.findEleAndClick(0, "xpath", li_xpath_one)  # 点击
                # break  # 退出循环

        self.outPutMyLog("已经获取到的列表的所有选项内容：")
        self.outPutMyLog(li_text_list)
        self.outPutMyLog("已经获取到的列表中与预期相同或相似的选项内容：")
        self.outPutMyLog(li_like_text_list)
        li_like_text_list_len = len(li_like_text_list)
        if li_like_text_list_len == 0:  #说明不存在内容
            self.outPutErrorMyLog("【%s】不在列表选项【%s】中" % (str(li_text), str(li_text_list)))
            return False
        elif li_like_text_list_len == 1: #说明找到一个相似的
            #找到该内容在li_text_list中的位置，并点击该内容
            li_text = li_like_text_list[0]
            xiabiao = li_text_list.index(li_text)
            print("xiabiao:")
            print(xiabiao)
            xiabiao = int(xiabiao)+1
            li_xpath_one = "%s/%s[%s]" % (ul_xpath, "li", xiabiao)
            self.findEleAndClick(0, "xpath", li_xpath_one)  # 点击
            return True
        else:  #如果大于等于1，则说明有多个
            #先找有没有相等的，有，则选择相等的一项，无则选择第一项作为选项
            for li_like_text_one in li_like_text_list:  #遍历
                if li_text.strip().lower() == li_like_text_one.strip().lower(): #如果去掉空格后且小写匹配，则赋值
                    li_text = li_like_text_one
                    xiabiao = li_text_list.index(li_text)
                    print("xiabiao:")
                    print(xiabiao)
                    xiabiao = int(xiabiao) + 1
                    li_xpath_one = "%s/%s[%s]" % (ul_xpath, "li", xiabiao)
                    self.findEleAndClick(0, "xpath", li_xpath_one)  # 点击
                    return True
            #如果没有找到相等项，则赋值第一项内容
            li_text = li_like_text_list[0]
            xiabiao = li_text_list.index(li_text)
            print("xiabiao:")
            print(xiabiao)
            xiabiao = int(xiabiao) + 1
            li_xpath_one = "%s/%s[%s]" % (ul_xpath, "li", xiabiao)
            self.findEleAndClick(0, "xpath", li_xpath_one)  # 点击
            return True

    #获取元素
    def findELesList(self,findstyle,findstylevalue):
        issecond = False
        try:
            if str(findstyle) == "class_name":
                eleList = self.driver.find_elements_by_class_name(findstylevalue)
                self.outPutMyLog("找到class_name为【%s】的元素" % findstylevalue)
            elif str(findstyle) == "css_selector":
                eleList = self.driver.find_elements_by_css_selector(findstylevalue)
                self.outPutMyLog("找到css_selector为【%s】的元素" % findstylevalue)
            elif str(findstyle) == "id":
                eleList = self.driver.find_elements_by_id(findstylevalue)
                self.outPutMyLog("找到id为【%s】的元素" % findstylevalue)
            elif str(findstyle) == "link_text":
                eleList = self.driver.find_elements_by_link_text(findstylevalue)
                self.outPutMyLog("找到link_text为【%s】的元素" % findstylevalue)
            elif str(findstyle) == "name":
                eleList = self.driver.find_elements_by_name(findstylevalue)
                self.outPutMyLog("找到name为【%s】的元素" % findstylevalue)
            elif str(findstyle) == "partial_link_text":
                eleList = self.driver.find_elements_by_partial_link_text(findstylevalue)
                self.outPutMyLog("找到link_text为【%s】的元素" % findstylevalue)
            elif str(findstyle) == "tag_name":
                eleList = self.driver.find_elements_by_tag_name(findstylevalue)
                self.outPutMyLog("找到tag_name为【%s】的元素" % findstylevalue)
            elif str(findstyle) == "xpath":
                eleList = self.driver.find_elements_by_xpath(findstylevalue)
                self.outPutMyLog("找到xpath为【%s】的元素" % findstylevalue)
            else:
                self.outPutErrorMyLog("元素的查找方式不再八类（id、name、class_name、tag_name、"
                                      "link_text、partial_link_text、css_selector、xpath）之中，"
                                      "请输入正确的查找方式.")
            self.driver.execute_script("arguments[0].scrollIntoView();", eleList)  # 拖动到可见的元素去，影响截取特定区域的截图，不影响整个页面截图
            self.driver.execute_script("arguments[0].setAttribute('style',arguments[1]);", eleList,"background:green;border:2px solid red")   #高亮显示操作的元素
        except Exception as e:
            self.outPutMyLog("问题描述：%s" % e)
            self.getScreenshotNormal()
            self.delayTime(5)
            issecond = True

        if issecond:
            try:
                if str(findstyle) == "class_name":
                    eleList = self.driver.find_elements_by_class_name(findstylevalue)
                    self.outPutMyLog("再次查找，找到class_name为【%s】的元素" % findstylevalue)
                elif str(findstyle) == "css_selector":
                    eleList = self.driver.find_elements_by_css_selector(findstylevalue)
                    self.outPutMyLog("再次查找，找到css_selector为【%s】的元素" % findstylevalue)
                elif str(findstyle) == "id":
                    eleList = self.driver.find_elements_by_id(findstylevalue)
                    self.outPutMyLog("再次查找，找到id为【%s】的元素" % findstylevalue)
                elif str(findstyle) == "link_text":
                    eleList = self.driver.find_elements_by_link_text(findstylevalue)
                    self.outPutMyLog("再次查找，找到link_text为【%s】的元素" % findstylevalue)
                elif str(findstyle) == "name":
                    eleList = self.driver.find_elements_by_name(findstylevalue)
                    self.outPutMyLog("再次查找，找到name为【%s】的元素" % findstylevalue)
                elif str(findstyle) == "partial_link_text":
                    eleList = self.driver.find_elements_by_partial_link_text(findstylevalue)
                    self.outPutMyLog("再次查找，找到link_text为【%s】的元素" % findstylevalue)
                elif str(findstyle) == "tag_name":
                    eleList = self.driver.find_elements_by_tag_name(findstylevalue)
                    self.outPutMyLog("再次查找，找到tag_name为【%s】的元素" % findstylevalue)
                elif str(findstyle) == "xpath":
                    eleList = self.driver.find_elements_by_xpath(findstylevalue)
                    self.outPutMyLog("再次查找，找到xpath为【%s】的元素" % findstylevalue)
                else:
                    self.outPutErrorMyLog("元素的查找方式不再八类（id、name、class_name、tag_name、"
                                          "link_text、partial_link_text、css_selector、xpath）之中，"
                                          "请输入正确的查找方式.")
                self.driver.execute_script("arguments[0].scrollIntoView();", eleList)  # 拖动到可见的元素去，影响截取特定区域的截图，不影响整个页面截图
                self.driver.execute_script("arguments[0].setAttribute('style',arguments[1]);", eleList,
                                           "background:green;border:2px solid red")  # 高亮显示操作的元素
            except Exception as e:
                self.getScreenshotAboutMySQL()  #截图关联django服务
                # self.getScreenshot()  #截图不关联django服务
                self.outPutErrorMyLog("停顿5秒后再次查找依然未找到元素.问题描述：%s" % e)
                self.closeBrowse()
                assert False
        return eleList

    #获取元素
    def findELe(self,findstyle,findstylevalue):
        issecond = False
        try:
            if str(findstyle) == "class_name":
                ele = self.driver.find_element_by_class_name(findstylevalue)
                self.outPutMyLog("找到class_name为【%s】的元素" % findstylevalue)
            elif str(findstyle) == "css_selector":
                ele = self.driver.find_element_by_css_selector(findstylevalue)
                self.outPutMyLog("找到css_selector为【%s】的元素" % findstylevalue)
            elif str(findstyle) == "id":
                ele = self.driver.find_element_by_id(findstylevalue)
                self.outPutMyLog("找到id为【%s】的元素" % findstylevalue)
            elif str(findstyle) == "link_text":
                ele = self.driver.find_element_by_link_text(findstylevalue)
                self.outPutMyLog("找到link_text为【%s】的元素" % findstylevalue)
            elif str(findstyle) == "name":
                ele = self.driver.find_element_by_name(findstylevalue)
                self.outPutMyLog("找到name为【%s】的元素" % findstylevalue)
            elif str(findstyle) == "partial_link_text":
                ele = self.driver.find_element_by_partial_link_text(findstylevalue)
                self.outPutMyLog("找到link_text为【%s】的元素" % findstylevalue)
            elif str(findstyle) == "tag_name":
                ele = self.driver.find_element_by_tag_name(findstylevalue)
                self.outPutMyLog("找到tag_name为【%s】的元素" % findstylevalue)
            elif str(findstyle) == "xpath":
                ele = self.driver.find_element_by_xpath(findstylevalue)
                self.outPutMyLog("找到xpath为【%s】的元素" % findstylevalue)
            else:
                self.outPutErrorMyLog("元素的查找方式不再八类（id、name、class_name、tag_name、"
                                      "link_text、partial_link_text、css_selector、xpath）之中，"
                                      "请输入正确的查找方式.")
            # self.driver.execute_script("arguments[0].scrollIntoView();", ele)  # 拖动到可见的元素去，影响截取特定区域的截图，不影响整个页面截图
            # self.driver.execute_script("arguments[0].setAttribute('style',arguments[1]);", ele,"background:green;border:2px solid red")   #高亮显示操作的元素
        except Exception as e:
            self.outPutMyLog("问题描述：%s" % e)
            self.getScreenshotNormal()
            self.delayTime(5)
            issecond = True

        if issecond:
            try:
                if str(findstyle) == "class_name":
                    ele = self.driver.find_element_by_class_name(findstylevalue)
                    self.outPutMyLog("再次查找，找到class_name为【%s】的元素" % findstylevalue)
                elif str(findstyle) == "css_selector":
                    ele = self.driver.find_element_by_css_selector(findstylevalue)
                    self.outPutMyLog("再次查找，找到css_selector为【%s】的元素" % findstylevalue)
                elif str(findstyle) == "id":
                    ele = self.driver.find_element_by_id(findstylevalue)
                    self.outPutMyLog("再次查找，找到id为【%s】的元素" % findstylevalue)
                elif str(findstyle) == "link_text":
                    ele = self.driver.find_element_by_link_text(findstylevalue)
                    self.outPutMyLog("再次查找，找到link_text为【%s】的元素" % findstylevalue)
                elif str(findstyle) == "name":
                    ele = self.driver.find_element_by_name(findstylevalue)
                    self.outPutMyLog("再次查找，找到name为【%s】的元素" % findstylevalue)
                elif str(findstyle) == "partial_link_text":
                    ele = self.driver.find_element_by_partial_link_text(findstylevalue)
                    self.outPutMyLog("再次查找，找到link_text为【%s】的元素" % findstylevalue)
                elif str(findstyle) == "tag_name":
                    ele = self.driver.find_element_by_tag_name(findstylevalue)
                    self.outPutMyLog("再次查找，找到tag_name为【%s】的元素" % findstylevalue)
                elif str(findstyle) == "xpath":
                    ele = self.driver.find_element_by_xpath(findstylevalue)
                    self.outPutMyLog("再次查找，找到xpath为【%s】的元素" % findstylevalue)
                else:
                    self.outPutErrorMyLog("元素的查找方式不再八类（id、name、class_name、tag_name、"
                                          "link_text、partial_link_text、css_selector、xpath）之中，"
                                          "请输入正确的查找方式.")
                self.driver.execute_script("arguments[0].scrollIntoView();", ele)  # 拖动到可见的元素去，影响截取特定区域的截图，不影响整个页面截图
                self.driver.execute_script("arguments[0].setAttribute('style',arguments[1]);", ele,
                                           "background:green;border:2px solid red")  # 高亮显示操作的元素
            except Exception as e:
                self.getScreenshotAboutMySQL()  #截图关联django服务
                # self.getScreenshot()  #截图不关联django服务
                self.outPutErrorMyLog("停顿5秒后再次查找依然未找到元素.问题描述：%s" % e)
                self.closeBrowse()
                assert False
        return ele

    #获取控件截图
    def findEleImageNum(self,num,findstyle,findstylevalue):
        ele = self.findELe(findstyle,findstylevalue)   #获取元素控件
        pageScreenshotpath = self.getScreenshotNormal()  # 获取整个页面截图
        # location = ele.location   #获取验证码x,y轴坐标   #截取了BUSINESS
        location = ele.location_once_scrolled_into_view  # 获取元素x,y轴坐标   #消除self.driver.execute_script("arguments[0].scrollIntoView();", ele) 对截图的影响 截取了login imgae
        size = ele.size   #获取元素的长宽
        coderange = (int(location['x']),int(location['y']),int(location['x']+size['width']),int(location['y']+size['height'])) #写成我们需要截取的位置坐标
        pageScreenshot = Image.open(pageScreenshotpath)   #打开截图
        imageScreen = pageScreenshot.crop(coderange)   #使用Image的crop函数，从截图中再次截取我们需要的区域,即验证码区域
        tStr = self.getTimeStr()
        firedir = r'%s/imagefile/ele/' % str(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        self.createdir(firedir)
        eleimage = "%s/%s_%s_ele.png" % (firedir,num,tStr)
        imageScreen.save(eleimage)   #保存控件截图
        self.outPutMyLog('获取到的元素的截图路径为：%s'% eleimage)
        return ele

    #判断元素不存在
    def assertEleNotExist(self,findstyle,findstylevalue):
        try:
            if str(findstyle) == "class_name":
                ele = self.driver.find_element_by_class_name(findstylevalue)
                self.outPutMyLog("找到class_name为【%s】的元素" % findstylevalue)
            elif str(findstyle) == "css_selector":
                ele = self.driver.find_element_by_css_selector(findstylevalue)
                self.outPutMyLog("找到css_selector为【%s】的元素" % findstylevalue)
            elif str(findstyle) == "id":
                ele = self.driver.find_element_by_id(findstylevalue)
                self.outPutMyLog("找到id为【%s】的元素" % findstylevalue)
            elif str(findstyle) == "link_text":
                ele = self.driver.find_element_by_link_text(findstylevalue)
                self.outPutMyLog("找到link_text为【%s】的元素" % findstylevalue)
            elif str(findstyle) == "name":
                ele = self.driver.find_element_by_name(findstylevalue)
                self.outPutMyLog("找到name为【%s】的元素" % findstylevalue)
            elif str(findstyle) == "partial_link_text":
                ele = self.driver.find_element_by_partial_link_text(findstylevalue)
                self.outPutMyLog("找到link_text为【%s】的元素" % findstylevalue)
            elif str(findstyle) == "tag_name":
                ele = self.driver.find_element_by_tag_name(findstylevalue)
                self.outPutMyLog("找到tag_name为【%s】的元素" % findstylevalue)
            elif str(findstyle) == "xpath":
                ele = self.driver.find_element_by_xpath(findstylevalue)
                self.outPutMyLog("找到xpath为【%s】的元素" % findstylevalue)
            else:
                self.outPutErrorMyLog("元素的查找方式不再八类（id、name、class_name、tag_name、"
                                      "link_text、partial_link_text、css_selector、xpath）之中，"
                                      "请输入正确的查找方式.")
            self.driver.execute_script("arguments[0].scrollIntoView();", ele)  # 拖动到可见的元素去，影响截取特定区域的截图，不影响整个页面截图
            self.driver.execute_script("arguments[0].setAttribute('style',arguments[1]);", ele,"background:green;border:2px solid red")   #高亮显示操作的元素
            self.getScreenshotAboutMySQL()
            self.outPutErrorMyLog("问题描述：元素应该消失，而实际没有消失")
            self.closeBrowse()
            assert  False
        except:
            pass


    #判断元素是否存在
    # 存在则返回True，不存在则返回False
    def is_exist_ele(self, findstyle, findstylevalue):
        try:
            if str(findstyle) == "class_name":
                ele = self.driver.find_element_by_class_name(findstylevalue)
                self.outPutMyLog("找到class_name为【%s】的元素" % findstylevalue)
            elif str(findstyle) == "css_selector":
                ele = self.driver.find_element_by_css_selector(findstylevalue)
                self.outPutMyLog("找到css_selector为【%s】的元素" % findstylevalue)
            elif str(findstyle) == "id":
                ele = self.driver.find_element_by_id(findstylevalue)
                self.outPutMyLog("找到id为【%s】的元素" % findstylevalue)
            elif str(findstyle) == "link_text":
                ele = self.driver.find_element_by_link_text(findstylevalue)
                self.outPutMyLog("找到link_text为【%s】的元素" % findstylevalue)
            elif str(findstyle) == "name":
                ele = self.driver.find_element_by_name(findstylevalue)
                self.outPutMyLog("找到name为【%s】的元素" % findstylevalue)
            elif str(findstyle) == "partial_link_text":
                ele = self.driver.find_element_by_partial_link_text(findstylevalue)
                self.outPutMyLog("找到link_text为【%s】的元素" % findstylevalue)
            elif str(findstyle) == "tag_name":
                ele = self.driver.find_element_by_tag_name(findstylevalue)
                self.outPutMyLog("找到tag_name为【%s】的元素" % findstylevalue)
            elif str(findstyle) == "xpath":
                ele = self.driver.find_element_by_xpath(findstylevalue)
                self.outPutMyLog("找到xpath为【%s】的元素" % findstylevalue)
            else:
                self.outPutErrorMyLog("元素的查找方式不再八类（id、name、class_name、tag_name、"
                                      "link_text、partial_link_text、css_selector、xpath）之中，"
                                      "请输入正确的查找方式.")
            self.driver.execute_script("arguments[0].scrollIntoView();", ele)  # 拖动到可见的元素去，影响截取特定区域的截图，不影响整个页面截图
            self.driver.execute_script("arguments[0].setAttribute('style',arguments[1]);", ele,
                                       "background:green;border:2px solid red")  # 高亮显示操作的元素
            self.outPutMyLog("元素存在")
            return True
        except:
            self.outPutErrorMyLog("元素不存在")
            return False





    #查找元素，然后输入内容
    def findEleAndInputNum(self,num,findstyle,findstylevalue,inputcontent):
        ele = self.findEleImageNum(num,findstyle,findstylevalue)

        ele.clear()   #清除输入框内容
        #清除函数失效，使用双击选中内容然后再输入内容
        #双击
        self.doubleClick(ele)
        ele.send_keys(inputcontent)   #输入内容
        # self.delayTime(3)
        displaytext = self.findEleAndReturnValueNum(num,findstyle,findstylevalue,'value')
        if str(inputcontent) == str(displaytext):
            self.outPutMyLog("输入内容：%s;显示内容：%s"% (inputcontent,displaytext))
        else:
            self.outPutErrorMyLog("输入内容：%s;显示内容：%s"% (inputcontent,displaytext))
        # self.delayTime

    #查找元素，然后返回元素的默认显示文字
    def findEleAndReturnValueNum(self,num,findstyle,findstylevalue,valuename):
        ele = self.findEleImageNum(num,findstyle,findstylevalue)
        eletext = ele.get_attribute(valuename)
        self.outPutMyLog("得到的元素属性【%s】的值为：%s"%(valuename,eletext))
        return eletext

    #查找元素，然后点击
    def findEleAndClickNoDelayTime(self,num,findstyle,findstylevalue):
        ele = self.findEleImageNum(num,findstyle,findstylevalue)
        try:
            ele.click()   #点击
            self.outPutMyLog("点击元素")
        except Exception as e:
            self.getScreenshotAboutMySQL()
            self.outPutErrorMyLog("点击失败，关闭驱动，问题描述：%s" % e)
            self.closeBrowse()
            assert False
        return ele

    #查找元素，然后点击
    def findEleAndClick(self,num,findstyle,findstylevalue):
        ele = self.findEleImageNum(num,findstyle,findstylevalue)
        try:
            ele.click()   #点击
            self.outPutMyLog("点击元素")
            self.delayTime(3)
        except Exception as e:
            self.getScreenshotAboutMySQL()
            self.outPutErrorMyLog("点击失败，关闭驱动，问题描述：%s" % e)
            self.closeBrowse()
            assert False
        return ele

    #查找元素，然后使用JS点击
    def findEleAndClickWithJS(self,num,findstyle,findstylevalue):
        ele = self.findEleImageNum(num,findstyle,findstylevalue)
        try:
            self.singleClick(ele)   #点击
            self.outPutMyLog("点击元素")
            self.delayTime(3)
        except Exception as e:
            self.getScreenshotAboutMySQL()
            self.outPutErrorMyLog("点击失败，关闭驱动，问题描述：%s" % e)
            self.closeBrowse()
            assert False
        return ele

    #查找元素，然后点击
    def findEleAndClickConfigDelayTime(self,num,findstyle,findstylevalue,delaytime):
        ele = self.findEleImageNum(num,findstyle,findstylevalue)
        try:
            ele.click()   #点击
            self.outPutMyLog("点击元素")
            if delaytime == None:
                delaytime = 3   #默认设置为3秒
            else:
                delaytime = delaytime

            self.delayTime(int(delaytime))
        except Exception as e:
            self.getScreenshotAboutMySQL()
            self.outPutErrorMyLog("点击失败，关闭驱动，问题描述：%s" % e)
            self.closeBrowse()
            assert False
        return ele

    #查找元素，然后点击
    def findEleAndClickWithAlert(self,num,findstyle,findstylevalue):
        ele = self.findEleImageNum(num,findstyle,findstylevalue)
        try:
            ele.click()   #点击
            self.outPutMyLog("点击元素")
            self.delayTime(3)
            alertele = self.driver.switch_to.alert()
            self.outPutMyLog("alert信息：%s" % alertele)
            # self.delayTime(3)
        except Exception as e:
            self.getScreenshotAboutMySQL()
            self.outPutErrorMyLog("点击失败，关闭驱动，问题描述：%s" % e)
            self.closeBrowse()
            assert False
        return ele

    #查找到tbody并打印表格里所有内容
    def findEleAndReturnTable(self,num,findstyle,findstylevalue):
        ele = self.findEleImageNum(num,findstyle,findstylevalue)
        # print('tagname:',ele.tag_name)
        tabledic = {}
        try:
            trlist = ele.find_elements_by_tag_name('tr')
            # print(len(trlist))
            for i in range(0,len(trlist)):
                # print('第%s行内容如下:\n'% str(i+1))
                #遍历行对象，并获取每一行中所有列对象
                tdlist = trlist[i].find_elements_by_tag_name('td')
                collist = []
                for j in range(0,len(tdlist)):
                    #遍历表格中的列，并打印单元格内容
                    collist.append(tdlist[j].text)
                    # print('第%s列内容如下：'% str(j+1),tdlist[j].text)
                    tabledic[i+1] = collist
            self.outPutMyLog('获取的表格内容：%s'% tabledic)
            # print('获取的表格内容：',tabledic)
            return tabledic
            # print('列表内容为：',option.text)
        except Exception as e:
            self.outPutErrorMyLog("获取表格内容出错，关闭驱动.问题描述：%s"% e)
            self.closeBrowse()
            assert False

    #找到表格，并验证输入内容
    def findEleAndCheckTableWithColnumCounts(self,num,findstyle,findstylevalue,inputtext,colnum_counts):

        tabledic = self.findEleAndReturnTable(num,findstyle,findstylevalue)
        is_exist = False

        for value in tabledic.values():
            for i in range(0,int(colnum_counts)):
                if inputtext.lower() in value[i].lower():
                    is_exist = True
                    break
            #     self.outPutMyLog('input输入内容变小写：%s'% inputtext.lower())
            #
            #     self.outPutMyLog('搜索到的表格内容变小写：%s'% value[colnum].lower())
            # else:
            #     self.outPutMyLog("搜索到的内容不匹配！！！")

        if is_exist:
            self.outPutMyLog('%s in %s' % (inputtext,tabledic))
        else:
            self.outPutErrorMyLog('%s not in %s' % (inputtext,tabledic))
            self.getScreenshotAboutMySQL()

        return is_exist

    #找到表格，并验证某个列中包含或是某个元素
    def findEleAndCheckTableOneColnum(self,num,findstyle,findstylevalue,inputtext,colnum):
        tabledic = self.findEleAndReturnTable(num,findstyle,findstylevalue)
        is_exist = False
        for value in tabledic.values():
            intcolnum = int(colnum)
            if inputtext.lower() not in value[intcolnum].lower():
                self.outPutErrorMyLog('预期结果应该为【%s】，而实际出现不匹配的结果【%s】'
                                 % (inputtext.lower(),value[intcolnum].lower()))
                is_exist = False
                break
            else:
                self.outPutMyLog('实际结果【%s】,符合预期结果【%s】' % (value[intcolnum].lower(), inputtext.lower()))
                is_exist = True
        return is_exist

    #找到表格，并验证输入内容
    def findEleAndCheckTable(self,num,findstyle,findstylevalue,inputtext,colnum):

        tabledic = self.findEleAndReturnTable(num,findstyle,findstylevalue)
        is_exist = False

        for value in tabledic.values():

            if inputtext.lower() in value[colnum].lower():
                is_exist = True
            #     self.outPutMyLog('input输入内容变小写：%s'% inputtext.lower())
            #
            #     self.outPutMyLog('搜索到的表格内容变小写：%s'% value[colnum].lower())
            # else:
            #     self.outPutMyLog("搜索到的内容不匹配！！！")

        if is_exist:
            self.outPutMyLog('%s in %s' % (inputtext,tabledic))
        else:
            self.outPutErrorMyLog('%s not in %s' % (inputtext,tabledic))

        return is_exist

    #查找到select元素,选择要选择的项
    def findEleAndReturnOptions(self,num,findstyle,findstylevalue,optiontext):
        ele = Select(self.findEleImageNum(num,findstyle,findstylevalue))
        try:
            selectoption = ele.select_by_visible_text(optiontext)
            self.delayTime(2)
        except Exception as e:
            self.getScreenshotAboutMySQL()
            self.outPutMyLog("填写内容与选项内容对不上，关闭驱动.问题描述：%s"% e)
            self.closeBrowse()
            assert False


    #查找到要输入文件的input元素，然后上传文件
    def findEleAndUploadFile(self,num,findstyle,findstylevalue,filepath,inputclassname=None):
        if inputclassname == None:
            inputclassname = "el-upload__input"
        else:
            inputclassname = inputclassname
        self.quDiaoInputStyle(inputclassname)
        ele = self.findEleImageNum(num,findstyle,findstylevalue)
        try:
            ele.send_keys(filepath)
            self.delayTime(1)
        except Exception as e:
            self.getScreenshotAboutMySQL()
            self.outPutErrorMyLog("上传文件失败，关闭驱动.问题描述：%s"% e)
            self.closeBrowse()
            assert False

    #查找到要输入文件的input元素，然后上传文件
    def findEleAndUploadFileNotCloseBrowser(self,num,findstyle,findstylevalue,filepath,inputclassname=None):
        if inputclassname == None:
            inputclassname = "el-upload__input"
        else:
            inputclassname = inputclassname
        self.quDiaoInputStyle(inputclassname)
        ele = self.findEleImageNum(num,findstyle,findstylevalue)
        ele.send_keys(filepath)
        self.delayTime(1)



    def quDiaoInputStyle(self,inputclassname):
        js = '$(".%s").attr("style", "display:block");'  % inputclassname# 改变类el-upload__input的属性为block(可见)
        print(js)
        # self.driver.execute_script(js)
        
    #查找元素，然后返回元素的text内容
    def findEleAndReturnText(self,num,findstyle,findstylevalue):
        ele = self.findEleImageNum(num, findstyle, findstylevalue)
        eletext = ele.text
        self.outPutMyLog("%s为%s的元素对应的文本信息为：%s"%(findstyle,findstylevalue,eletext))
        self.delayTime(3)
        return eletext



    #通过xpath查找元素
    def findElementByXpath(self,path):
        issecond = False
        try:
            ele = self.driver.find_element_by_xpath(path)
            self.outPutMyLog("找到Xpath为【%s】的元素" % path)
            self.driver.execute_script("arguments[0].scrollIntoView();", ele)  # 拖动到可见的元素去，影响截取特定区域的截图，不影响整个页面截图
            self.driver.execute_script("arguments[0].setAttribute('style',arguments[1]);", ele,"background:green;border:2px solid red")   #高亮显示操作的元素
            #使用JavaScript代码将传入的页面元素对象的背景颜色和边框颜分别设置为绿色和红色
        except Exception as e:
            self.outPutErrorMyLog("问题描述：%s" % e)
            # print(e)
            self.getScreenshotNormal()
            self.delayTime(5)
            issecond = True

        if issecond:
            try:
                ele = self.driver.find_element_by_xpath(path)
                self.outPutMyLog("再次找到Xpath为【%s】的元素" % path)
                self.driver.execute_script("arguments[0].scrollIntoView();", ele)  # 拖动到可见的元素去，影响截取特定区域的截图，不影响整个页面截图
                self.driver.execute_script("arguments[0].setAttribute('style',arguments[1]);", ele,"background:green;border:2px solid red")  # 高亮显示操作的元素
                # 使用JavaScript代码将传入的页面元素对象的背景颜色和边框颜分别设置为绿色和红色
                # print("最终找到元素")
            except Exception as e:
                self.getScreenshotAboutMySQL()  #截图关联django服务
                # self.getScreenshot()  #截图不关联django服务
                self.outPutErrorMyLog("停顿5秒后再次查找依然未找到元素.问题描述：%s" % e)
                self.closeBrowse()
                self.isActiveBrowser = True
        return ele



    #获取控件截图
    def getEleImage(self,num,path):
        ele = self.findElementByXpath(path)   #获取元素控件
        pageScreenshotpath = self.getScreenshotNormal()  # 获取整个页面截图
        # location = ele.location   #获取验证码x,y轴坐标   #截取了BUSINESS
        location = ele.location_once_scrolled_into_view  # 获取元素x,y轴坐标   #消除self.driver.execute_script("arguments[0].scrollIntoView();", ele) 对截图的影响 截取了login imgae
        size = ele.size   #获取元素的长宽
        coderange = (int(location['x']),int(location['y']),int(location['x']+size['width']),int(location['y']+size['height'])) #写成我们需要截取的位置坐标
        pageScreenshot = Image.open(pageScreenshotpath)   #打开截图
        imageScreen = pageScreenshot.crop(coderange)   #使用Image的crop函数，从截图中再次截取我们需要的区域,即验证码区域
        tStr = self.getTimeStr()
        eleimage = "%s/imagefile/ele/%s_%s_ele.png" % (str(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),num,tStr)
        imageScreen.save(eleimage)   #保存控件截图
        self.outPutMyLog('获取到的元素的截图路径为：%s'% eleimage)
        return ele



    #通过xpath查找元素，然后返回元素的text内容
    def findElementByXpathAndReturnText(self,num,path):
        ele = self.getEleImage(num,path)
        eletext = ele.text
        self.outPutMyLog("元素的Xpath路径为：%s;对应的文本信息为：%s"%(path,eletext))
        self.delayTime(3)
        return eletext


    def findElementByXpathAndReturnTextNotNum(self,path):
        ele = self.findElementByXpath(path)
        eletext = ele.text
        self.outPutMyLog("元素的Xpath路径为：%s;对应的文本信息为：%s"%(path,eletext))
        # self.delayTime(1)
        return eletext


    #通过xpath查找元素，然后返回元素的标签名(例如input)
    def findElementByXpathAndReturnTagName(self,path):
        ele = self.findElementByXpath(path)
        eletext = ele.tag_name
        return eletext


    #通过xpath查找元素，然后返回元素的默认显示文字
    def findElementByXpathAndReturnValue(self,path,valuename):
        ele = self.findElementByXpath(path)
        eletext = ele.get_attribute(valuename)
        return eletext

    #通过xpath查找元素，然后返回元素的html信息
    def findElementByXpathAndReturnHTML(self,path):
        ele = self.findElementByXpath(path)
        elehtml = ele.get_attribute("innerHTML")  #获取标签的html内容
        return elehtml



    #通过xpath查找元素，然后返回元素的默认显示文字
    def findElementByXpathAndReturnValueNum(self,num,path,valuename):
        ele = self.getEleImage(num,path)
        eletext = ele.get_attribute(valuename)
        self.outPutMyLog("得到的元素属性【%s】的值为：%s"%(valuename,eletext))
        return eletext



    #通过xpath查找元素，然后输入内容
    def findElementByXpathAndInput(self,path,inputcontent):
        ele = self.findElementByXpath(path)
        ele.clear()   #清除输入框内容
        ele.send_keys(inputcontent)   #输入内容



    #通过xpath查找元素，然后输入内容
    def findElementByXpathAndInputNum(self,num,path,inputcontent):
        ele = self.getEleImage(num, path)
        ele.clear()   #清除输入框内容
        ele.send_keys(inputcontent)   #输入内容
        # self.delayTime(3)
        displaytext = self.findElementByXpathAndReturnValueNum(num,path,'value')
        self.outPutMyLog("输入内容：%s;显示内容：%s"% (inputcontent,displaytext))
        # self.delayTime



    #通过xpath查找元素，然后情况输入框中的内容
    def findElementByXpathAndDeleteInputContentNum(self,num,path):
        ele = self.getEleImage(num, path)
        displaytext = self.findElementByXpathAndReturnValueNum(num,path,'value')
        ele.clear()   #清除输入框内容
        self.outPutMyLog("已经删除内容：%s."% displaytext)
        # self.delayTime(3000)


    #通过xpath查找元素，移除其Readonly属性然后输入内容

    def findElementByXpathAndInputNumRemoveReadonly(self,num,path,inputcontent):
        ele = self.getEleImage(num, path)
        #移除Readonly属型
        self.removeReadonly(ele)
        ele.clear()   #清除输入框内容
        ele.send_keys(inputcontent)   #输入内容
        # 设置Readonly属型为空
        self.setReadonly(ele)
        # 点击使日期谈框消失
        self.mockClickBlank(0,0)
        displaytext = self.findElementByXpathAndReturnValueNum(num,path,'value')
        self.outPutMyLog("输入内容：%s;显示内容：%s"% (inputcontent,displaytext))
        # self.delayTime(3000)



    #通过xpath查找元素，使用JS直接设置Input框属性值（value=）
    def findElementByXpathAndInputNumJsSetValue(self,num,path,inputcontent):
        ele = self.getEleImage(num, path)
        self.jsSetValue(ele,inputcontent)
        displaytext = self.findElementByXpathAndReturnValueNum(num,path,'value')
        self.outPutMyLog("输入内容：%s;显示内容：%s"% (inputcontent,displaytext))
        # self.delayTime(3000)



    # 通过xpath查找元素，然后点击日期input框，点击选择日期路径

    #日期控件路径path1，日期路径path2，日期左移月路径path3,日期右移月路径path4
    def findElementByXpathAndClickAbountData(self, num, path1,path2,pathleft=None,pathright=None,pathconfirm=None):
        #点击日期input框
        self.findElementByXpathAndClickNum(num,path1)
        if pathleft != None:
            #点击日期左移月按钮
            self.findElementByXpathAndClickNum(num, pathleft)
        if pathright != None:
            #点击日期右移月按钮
            self.findElementByXpathAndClickNum(num, pathright)
        #点击日期日路径
        self.findElementByXpathAndClickNum(num,path2)
        if pathconfirm !=None:
            self.findElementByXpathAndClickNum(num, pathconfirm)
        displaytext = self.findElementByXpathAndReturnValueNum(num, path1, 'value')
        self.outPutMyLog("日期显示内容：%s" % displaytext)
        self.mockClickBlank(0,0)



    # 通过xpath查找元素，然后点击日期input框，点击选择日期路径,选择时分秒（预留）
    #日期控件路径path1，日期路径path2，分路径path3，日期左移月路径pathleft,日期右移月路径pathright
    def findElementByXpathAndClickAbountDataToSecound(self, num, path1,path2,path3,pathleft=None,pathright=None):
        #点击日期input框
        self.findElementByXpathAndClickNum(num,path1)
        if pathleft != None:
            #点击日期左移月按钮
            self.findElementByXpathAndClickNum(num, pathleft)
        if pathright != None:
            #点击日期右移月按钮
            self.findElementByXpathAndClickNum(num, pathright)
        #点击日期日路径
        self.findElementByXpathAndClickNum(num,path2)
        #点击日期时分秒路径
        self.findElementByXpathAndClickNum(num,path3)
        displaytext = self.findElementByXpathAndReturnValueNum(num, path1, 'value')
        self.outPutMyLog("日期显示内容：%s" % displaytext)
        self.mockClickBlank(0,0)


    #通过xpath查找元素，设置其Readonly属性值为空
    def findElementByXpathAndInputNumSetReadonly(self,num,path):
        ele = self.getEleImage(num, path)
        self.setReadonly(ele)
        # self.delayTime(3000)


    #通过xpath查找元素，然后点击
    def findElementByXpathAndClick(self,path):
        ele = self.findElementByXpath(path)
        ele.click()   #点击
        self.outPutMyLog("点击元素的Xpath路径为：%s" % path)
        # print("点击元素的Xpath路径为：%s" % path)
        self.delayTime(3)
        return ele


    #通过xpath查找元素，然后点击
    def findElementByXpathAndClickNum(self,num,path):
        self.delayTime(1)
        ele = self.getEleImage(num,path)
        ele.click()   #点击
        self.outPutMyLog("点击Xpath路径为[%s]的元素" % path)
        # print("点击元素的Xpath路径为：%s" % path)
        self.delayTime(2)
        return ele


    #通过xpath查找元素，然后点击
    def findElementByXpathAndScriptClick(self,path):
        ele = self.findElementByXpath(path)
        self.driver.execute_script("arguments[0].click();", ele)
        self.delayTime(3)
        return ele


    #通过xpath查找元素，然后点击
    def findElementByXpathAndScriptClickNum(self,num,path):
        self.delayTime(1)
        ele = self.getEleImage(num,path)
        self.driver.execute_script("arguments[0].click();", ele)
        self.outPutMyLog("点击xpath为[%s]的元素" % path )
        self.delayTime(2)
        return ele


    #通过xpath查找到要输入文件的input元素，然后上传文件
    def findElementByXpathAndAndFile(self,path,filepath):
        ele = self.findElementByXpath(path)
        try:
            ele.send_keys(filepath)
            self.delayTime(1)
        except Exception as e:
            self.outPutErrorMyLog("上传文件失败，关闭驱动.问题描述：%s"% e)
            self.closeBrowse()



    #通过xpath查找到要输入文件的input元素，然后上传文件
    def findElementByXpathAndAndFileNum(self,num,path,filepath):
        ele = self.getEleImage(num,path)
        try:
            ele.send_keys(filepath)
            self.delayTime(1000)
        except Exception as e:
            self.outPutErrorMyLog("上传文件失败，关闭驱动.问题描述：%s"% e)
            self.closeBrowse()



    #通过xpath查找到要输入文件的input元素，然后上传文件
    #pip install SendKeys
    #import win32gui
    #import win32con
    #import time
    def findElementByXpathAndAndFileNumVue(self,num,path,filepath):
        ele = self.findElementByXpathAndScriptClickNum(num,path)
        # ele = self.getEleImage(num,path)
        try:
            #pip install pywin32
            #import win32gui
            # import win32con
            #文件名：D:\pic\1.jpg
            dialog = win32gui.FindWindow('#32770', '文件上传')  # 对话框
            ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, 'ComboBoxEx32', None)
            ComboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, 'ComboBox', None)
            Edit = win32gui.FindWindowEx(ComboBox, 0, 'Edit', None)  # 上面三句依次寻找对象，直到找到输入框Edit对象的句柄
            button = win32gui.FindWindowEx(dialog, 0, 'Button', None)  # 确定按钮Button
            win32gui.SendMessage(Edit, win32con.WM_SETTEXT, None, filepath)  # 往输入框输入绝对地址
            win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)  # 按button
            self.delayTime(5)
        except Exception as e:
            self.outPutErrorMyLog("上传文件失败，关闭驱动.问题描述：%s"% e)
            # self.delayTime(1000)
            self.closeBrowse()



    #通过xpath查找到select元素,然后点击，然后点击要选择的项
    def findElementByXpathAndClickOptionXpath(self,xpath,optiontextxpath):
        try:
            self.findElementByXpathAndScriptClick(xpath)
            self.findElementByXpathAndScriptClick(optiontextxpath)
            self.delayTime(2)
        except Exception as e:
            self.outPutErrorMyLog("出现问题，关闭驱动.问题描述：%s" % e)
            self.closeBrowse()



    #通过xpath查找到select元素,然后点击，然后点击要选择的项
    def findElementByXpathAndClickOptionXpathNum(self,num,xpath,optiontextxpath):
        try:
            self.findElementByXpathAndScriptClickNum(num,xpath)
            self.findElementByXpathAndScriptClickNum(num,optiontextxpath)
            self.delayTime(2)
        except Exception as e:
            self.outPutErrorMyLog("出现问题，关闭驱动.问题描述：%s"% e)
            self.closeBrowse()

    #通过xpath查找到select元素,选择要选择的项
    def findElementByXpathAndReturnOptions(self,path,optiontext):
        ele = Select(self.findElementByXpath(path))
        try:
            selectoption = ele.select_by_visible_text(optiontext)
            self.delayTime(2)
        except Exception as e:
            self.outPutMyLog("填写内容与选项内容对不上，关闭驱动.问题描述：%s"% e)
            self.closeBrowse()

    #通过xpath查找到select元素,选择要选择的项
    def findElementByXpathAndReturnOptionsNum(self,num,path,optiontext):
        ele = Select(self.getEleImage(num,path))
        try:
            selectoption = ele.select_by_visible_text(optiontext)
            self.delayTime(2)
        except Exception as e:
            self.outPutErrorMyLog("填写内容与选项内容对不上，关闭驱动.问题描述：%s"% e)
            self.closeBrowse()


    #通过xpath查找到select元素,选择要选择的项
    def findElementByXpathAndSelectOptionsNum(self,num,path,optiontext):
        optionlist = self.findElementByXpathAndReturnAllOptions(path)
        optiontext = optiontext.strip()  #去掉前后空格
        acturl_optiontext_list = []
        for optionone in optionlist:
            if optiontext in optionone:  #如果文本在选项中，则将选项内容赋值给文本
                acturl_optiontext_list.append(optionone)
        self.outPutMyLog("相同或相似的选项：")
        self.outPutMyLog(acturl_optiontext_list)
        acturl_optiontext_list_len = len(acturl_optiontext_list)
        if acturl_optiontext_list_len == 0: #如果没有，则还用传入值
            optiontext = optiontext
            self.outPutErrorMyLog("没有查找到相同或相似的选项，还用原值（去掉前后空格）")
        elif acturl_optiontext_list_len == 1: #如果只有一项，则将该项作为选项
            optiontext = acturl_optiontext_list[0]
            self.outPutMyLog("查找到相同或相似一项，直接使用查找到的项")
        else : #如果有好几项，则说明有包含的内容，则优先选择相等的内容
            is_equal = False
            optiontext = optiontext
            self.outPutMyLog("查找到多项相同或相似的值，先使用原值（去掉前后空格）")
            for acturl_optiontext_one in acturl_optiontext_list:
                if optiontext == acturl_optiontext_one.strip(): #有相等的则说明存在,选相等的
                    optiontext = acturl_optiontext_one
                    self.outPutMyLog("从多项相同或相似的值中查找到相等的一项(去掉前后空格后)，将该项作为选项值")
                    is_equal = True
                    break  #退出循环
            if not is_equal: #如果没有找到相等的，且有包含的，则选择第一项作为
                optiontext = acturl_optiontext_list[0]
                self.outPutErrorMyLog("从多项相同或相似的值中没有查找到相等的一项，将第一项内容作为选项值")

        ele = Select(self.getEleImage(num,path))
        try:
            selectoption = ele.select_by_visible_text(optiontext)
            self.delayTime(2)
        except Exception as e:
            self.outPutErrorMyLog("填写内容与选项内容对不上，关闭驱动.问题描述：%s"% e)
            self.closeBrowse()

    #通过xpath查找到select并打印其所有的options
    def findElementByXpathAndReturnAllOptions(self,path):
        ele = Select(self.findElementByXpath(path))
        optionlist = []
        try:
            all_options = ele.options
            # print('所有选项内容如下：',all_options)
            for option in all_options:
                optionlist.append(option.text)
                # print('选项内容为：',option.text)
            self.outPutMyLog('获取的选项所有内容：%s'% optionlist)
            return optionlist
        except Exception as e:
            self.outPutErrorMyLog("获取选项内容出错，关闭驱动.问题描述%e"% e)
            self.closeBrowse()



    #通过xpath查找到tbody并打印表格里所有内容
    def findElementByXpathAndReturnTable(self,path):
        ele = self.findElementByXpath(path)
        # print('tagname:',ele.tag_name)
        tabledic = {}
        try:
            trlist = ele.find_elements_by_tag_name('tr')
            # print(len(trlist))
            for i in range(0,len(trlist)):
                # print('第%s行内容如下:\n'% str(i+1))
                #遍历行对象，并获取每一行中所有列对象
                tdlist = trlist[i].find_elements_by_tag_name('td')
                collist = []
                for j in range(0,len(tdlist)):
                    #遍历表格中的列，并打印单元格内容
                    collist.append(tdlist[j].text)
                    # print('第%s列内容如下：'% str(j+1),tdlist[j].text)
                    tabledic[i+1] = collist
            self.outPutMyLog('获取的表格内容：%s'% tabledic)
            # print('获取的表格内容：',tabledic)
            return tabledic
            # print('列表内容为：',option.text)
        except Exception as e:
            self.outPutErrorMyLog("获取表格内容出错，关闭驱动.问题描述：%s"% e)
            self.closeBrowse()



    #通过xpath查找到tbody并打印表格里所有内容
    def findElementByXpathAndReturnTableNum(self,num,path):
        ele = self.getEleImage(num,path)
        # ele = self.findElementByXpath(path)
        # print('tagname:',ele.tag_name)
        tabledic = {}
        try:
            trlist = ele.find_elements_by_tag_name('tr')
            # print(len(trlist))
            for i in range(0,len(trlist)):
                # print('第%s行内容如下:\n'% str(i+1))
                #遍历行对象，并获取每一行中所有列对象
                tdlist = trlist[i].find_elements_by_tag_name('td')
                collist = []
                for j in range(0,len(tdlist)):
                    #遍历表格中的列，并打印单元格内容
                    collist.append(tdlist[j].text)
                    # print('第%s列内容如下：'% str(j+1),tdlist[j].text)
                    tabledic[i+1] = collist
            self.outPutMyLog('获取的表格内容：%s'%tabledic)
            # print('获取的表格内容：',tabledic)
            return tabledic
            # print('列表内容为：',option.text)
        except Exception as e:
            self.outPutErrorMyLog("获取表格内容出错，关闭驱动.问题描述：%s"% e)
            self.closeBrowse()



    def checktable(self,path,inputtext,colnum):

        tabledic = self.findElementByXpathAndReturnTable(path)
        is_exist = False

        for value in tabledic.values():

            if inputtext.lower() in value[colnum].lower():
                is_exist = True
            #     self.outPutMyLog('input输入内容变小写：%s'% inputtext.lower())
            #
            #     self.outPutMyLog('搜索到的表格内容变小写：%s'% value[colnum].lower())
            # else:
            #     self.outPutMyLog("搜索到的内容不匹配！！！")

        if is_exist:
            self.outPutMyLog('%s in %s' % (inputtext,tabledic))
        else:
            self.outPutErrorMyLog('%s not in %s' % (inputtext,tabledic))

        return is_exist





    #获取页面截图
    def getScreenshot(self):
        driver = self.driver
        self.outPutMyLog("调用截取图片函数")
        tStr = self.getTimeStr()   #获取当前时间串
        currentny = self.getTimeStrNY()   #获取当前时间的年月

        # path = "../imagefile/%s.png"% tStr

        # path = '%s/screenshots/screenpicture_%s.png' % (

        # str(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), tStr)

        firedir = r'%s/media/report/%s/screenshots/' % (os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),currentny)
        self.createdir(firedir)
        path = '%s/screenpicture_%s.png' % (firedir,tStr)
        print(path)
        driver.get_screenshot_as_file(path)

        self.outPutMyLog("*****")
        self.outPutMyLog(path)
        self.outPutMyLog("*****")
        return path



    #获取页面截图
    def getScreenshotAboutMySQL(self):
        driver = self.driver
        self.outPutErrorMyLog("调用截取图片函数")
        tStr = self.getTimeStr()   #获取当前时间串
        currentny = self.getTimeStrNY()   #获取当前时间的年月
        firedir = r'%s/media/report/%s/screenshots/' % (os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),currentny)
        self.createdir(firedir)
        path = '%s/screenpicture_%s.png' % (firedir,tStr)
        pathaboutmysql = r'media\report\%s\screenshots\screenpicture_%s.png'%(currentny,tStr)
        driver.get_screenshot_as_file(path)
        self.outPutErrorMyLog("*****")
        self.outPutErrorMyLog(pathaboutmysql)  #打印截图路径，供报告截图使用
        self.outPutErrorMyLog("*****")
        return path

    #获取爬虫图片并保存
    def saveSpiderImage(self):
        tStr = self.getTimeStr()   #获取当前时间串
        currentny = self.getTimeStrNY()   #获取当前时间的年月
        firedir = r'%s/media/report/%s/screenshots/' % (os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),currentny)
        self.createdir(firedir)
        path = '%sscreenpicture_%s.png' % (firedir,tStr)
        pathaboutmysql = r'media\report\%s\screenshots\screenpicture_%s.png'%(currentny,tStr)
        self.outPutErrorMyLog("*****")
        self.outPutErrorMyLog(pathaboutmysql)  #打印截图路径，供报告截图使用
        self.outPutErrorMyLog("*****")
        return path




    #获取页面截图
    def getScreenshotNormal(self):
        driver = self.driver
        self.outPutMyLog("调用截取图片函数")
        tStr = self.getTimeStr()
        firedir = r'%s/imagefile/' % str(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        self.createdir(firedir)
        path = "%s/%s.png"% (firedir,tStr)
        print("yyyyyyyyyyyyyyyyyyyyyyyy:%s" % path)
        driver.get_screenshot_as_file(path)
        return path



    #获取code码截图
    def getCodeImage(self,path):
        pageScreenshotpath = self.getScreenshotNormal()  # 获取整个页面截图
        image = self.findElementByXpath(path)   #获取图片验证码控件
        # location = image.location   #获取验证码x,y轴坐标
        location = image.location_once_scrolled_into_view  # 获取验证码x,y轴坐标   #消除self.driver.execute_script("arguments[0].scrollIntoView();", ele) 对截图的影响
        size = image.size   #获取验证码的长宽
        coderange = (int(location['x']),int(location['y']),int(location['x']+size['width']),int(location['y']+size['height'])) #写成我们需要截取的位置坐标
        pageScreenshot = Image.open(pageScreenshotpath)   #打开截图
        imageScreen = pageScreenshot.crop(coderange)   #使用Image的crop函数，从截图中再次截取我们需要的区域,即验证码区域
        tStr = self.getTimeStr()
        path = "%s/imagefile/%s_code.png"%(str(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),tStr)
        imageScreen.save(path)   #保存验证码图片
        return tStr

    def getCodeTextByThreeInterfase(self,path):
        imagecodestr = self.getCodeImage(path)
        imagecode = r"%s/imagefile/%s_code.png" % (str(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),imagecodestr)# 打开验证码图片
        #验证码类型（n4:4位纯数字，
                    # n5:5位纯数字
                    # n6:6位纯数字
                    # e4:4位纯英文
                    # e5:5位纯英文
                    # e6:6位纯英文
                    # ne4:4位英文数字
                    # ne5:5位英文数字
                    # ne6:6位英文数字）
        #请准确填写，以免影响识别准确性。（其他类型，请使用：图片验证码识别-复杂版）
        codetext = IdentificationVerificationCode(picture=imagecode,v_type="n4")
        return codetext

    def getCodeTextByThreeInterfaseWithCodeType(self,path,codetype):
        imagecodestr = self.getCodeImage(path)
        imagecode = r"%s/imagefile/%s_code.png" % (str(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),imagecodestr)# 打开验证码图片
        #验证码类型（n4:4位纯数字，
                    # n5:5位纯数字
                    # n6:6位纯数字
                    # e4:4位纯英文
                    # e5:5位纯英文
                    # e6:6位纯英文
                    # ne4:4位英文数字
                    # ne5:5位英文数字
                    # ne6:6位英文数字）
        #请准确填写，以免影响识别准确性。（其他类型，请使用：图片验证码识别-复杂版）
        codetext = IdentificationVerificationCode(picture=imagecode,v_type=codetype)
        return codetext



    #获取验证码文字信息
    def getcodetext(self,path):
        imagecodestr = self.getCodeImage(path)
        imagecode = Image.open("%s/imagefile/%s_code.png" % (str(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),imagecodestr)) # 打开验证码图片
        pixtongji = []
        for x in range(imagecode.size[1]):
            for y in range(imagecode.size[0]):
                # 遍历图片的xy坐标像素点颜色
                pix = imagecode.getpixel((y, x))
                pixtongji.append(pix)
        nonepixtongjidic = {}
        for item in pixtongji:
            if item in nonepixtongjidic.keys():
                nonepixtongjidic[item] += 1
            else:
                nonepixtongjidic[item] = 1
        self.outPutMyLog("nonepixtongjidic:%s" % nonepixtongjidic)
        nonepixtongjilist = sorted(nonepixtongjidic.values(),reverse=True)   #按照键值对的值对字典进行倒序排序
        numvalue = []
        numvalue.append(nonepixtongjilist[1])   #获取第二个值
        getkey = self.getDictKey(nonepixtongjidic,numvalue)
        img_new = Image.new('P', imagecode.size, 255)
        for x in range(imagecode.size[1]):
            for y in range(imagecode.size[0]):
                # 遍历图片的xy坐标像素点颜色
                pix = imagecode.getpixel((y, x))
                # print(pix)
                # 自己调色，r（pix[0]）=0，g（pix[1]）=0，b（pix[2]）>0为蓝色
                for i in range(len(getkey)):
                    if (pix[0] == getkey[i][0] and pix[1] == getkey[i][1] and pix[2] == getkey[i][2]):
                        # 把遍历的结果放到新图片上，0为透明度，不透明
                        img_new.putpixel((y, x), 0)
        newpath = "%s/imagefile/%s_codegary.png" % (str(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),imagecodestr)
        img_new.save(newpath, format='png')
        imagecode = Image.open(newpath)   #打开验证码图片
        imgry = imagecode.convert('L')  # 图像加强，二值化，PIL中有九种不同模式。分别为1，L，P，RGB，RGBA，CMYK，YCbCr，I，F。L为灰度图像
        sharpness = ImageEnhance.Contrast(imgry)   #对比度增强
        imagecodegary = sharpness.enhance(2.0)#2.0为图像的饱和度
        imagecodegary.save(newpath)   #保存灰度值验证码
        endcode = Image.open(newpath)    #打开灰度值验证码
        codetext = pytesseract.image_to_string(endcode).strip()   #获取验证码文本文件
        return codetext



    #获取字典对应值的键
    def getDictKey(self,dict,prevalue):
        getkey = []
        for key,value in dict.items():
            for i in range(len(prevalue)):
                if value == prevalue[i]:
                    getkey.append(key)
        return getkey


    #获取时间串
    def getTimeStr(self):
        tStr = self.timeStr.getTimeStr()
        return tStr

    def getTimeStrNY(self):
        tStrNY = self.timeStr.getTimeStrNY()
        return tStrNY


    #获取cookies
    def getCookies(self):
        cookies = self.driver.get_cookies()
        for cookie in cookies:
            self.outPutMyLog("获取的cookie的值为：%s" % cookie)
        return cookies



    #写入cookies
    def writerCookies(self,cookies,url,url2):
        self.outPutMyLog("\n开始写入cookie-----------------\n")
        self.getUrl(url)
        long = len(cookies)
        for i in range(long):
            cookie = {'name': cookies[i]['name'], 'value': cookies[i]['value']}
            self.driver.add_cookie(cookie)   #selenium添加cookies时，得先登录网址才能添加cookies的
            self.outPutMyLog("写入cookie的值为：%s" % cookie)
        self.driver.refresh()  #
        self.outPutMyLog("刷新当前页面---------")
        self.getUrl(url2)
        self.outPutMyLog("url2为：%s."% url2)
        self.driver.refresh()   #刷新当前页面
        self.outPutMyLog("刷新当前页面---------")
        self.delayTime(5)   #等待5秒
        self.getCookies()

    #写入cookies
    def writerCookiesWithOneUrl(self,cookies,url):
        self.outPutMyLog("\n开始写入cookie-----------------\n")
        self.getUrl(url)
        long = len(cookies)
        for i in range(long):
            cookie = {'name': cookies[i]['name'], 'value': cookies[i]['value']}
            self.driver.add_cookie(cookie)   #selenium添加cookies时，得先登录网址才能添加cookies的
            self.outPutMyLog("写入cookie的值为：%s" % cookie)
        self.delayTime(2)  # 等待2秒
        self.driver.refresh()  #
        self.outPutMyLog("刷新当前页面---------")
        self.delayTime(3)   #等待3秒
        self.getCookies()

    #写入cookies到文件
    def writerCookieToJson(self,cookiefile):
        cookies = self.getCookies()
        cookie_wenjianjian = '%s/myJsonFile' % str(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        self.createdir(cookie_wenjianjian)
        cookie_file = '%s/%s' % (cookie_wenjianjian,cookiefile)
        oj = OperationJson(cookie_file)
        oj.write_data(cookies)
        self.outPutMyLog("\ncookie信息‘%s’已经写入‘%s’文件里。\n" % (cookies,cookie_file))

    #写入cookies到文件
    def writerCookieToJsonFile(self,cookiefile):
        cookies = self.getCookies()
        cookie_wenjianjian = '%s/myJsonFile' % str(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        self.createdir(cookie_wenjianjian)
        cookie_file = '%s/%s' % (cookie_wenjianjian,cookiefile)
        oj = OperationJson(cookie_file)
        oj.write_data(cookies)
        self.outPutMyLog("\ncookie信息‘%s’已经写入‘%s’文件里。\n" % (cookies,cookie_file))

    #从cookies文件获取cookies
    def readCookieFromJsonFile(self,cookiefile):
        cookies = self.getCookies()
        cookie_wenjianjian = '%s/myJsonFile' % str(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        self.createdir(cookie_wenjianjian)
        cookie_file = '%s/%s' % (cookie_wenjianjian,cookiefile)
        oj = OperationJson(cookie_file)
        cookies =  oj.read_data()
        self.outPutMyLog("\n获取到的cookies类型为;%s\n" % type(cookies))
        self.outPutMyLog("\n获取到的cookie信息为‘%s’从‘%s’文件里。\n" % (cookies,cookie_file))
        return  cookies


    #延迟3秒
    def delayTime(self,dalaytime):
        time.sleep(int(dalaytime))   #延迟，
        self.outPutMyLog("等待%s秒---"% dalaytime)


    #使用js去掉input框中的readonly（只读）属性，设置为可输入状态，主要处理日期输入
    def removeReadonly(self,ele):
        self.driver.execute_script("arguments[0].removeAttribute('readonly')", ele)  # 使用js去掉元素中的readonly属性
        self.outPutMyLog("移除input元素中readonly属性，使其可编辑")


    def setReadonly(self,ele):
        self.driver.execute_script("arguments[0].setAttribute('readOnly','')", ele)  # 使用js去掉元素中的readonly属性
        self.outPutMyLog("设置input元素中readonly属性值为true，使其不可编辑")


    #用js方法输入日期
    def jsSetValue(self,ele,value):
        self.driver.execute_script("arguments[0].value='%s'" % value, ele)  # 使用js去掉元素中的readonly属性
        self.outPutMyLog("设置input元素中value属性值为%s" % value)
        self.delayTime(1)



    #模拟鼠标点击空白处
    def mockClickBlank(self,xoffset, yoffset):
        action = ActionChains(self.driver)
        action.move_by_offset(xoffset, yoffset).click().perform()  #点击空白区域：坐标（0，0）
        self.outPutMyLog("模拟点击空白区域（点击坐标（%s，%s））" % (xoffset, yoffset))
        self.delayTime(1)


    def createdir(self,filedir):
        filelist = filedir.split("/")
        # print(filelist)
        long = len(filelist)
        # print(long)
        zuhefiledir = filelist[0]
        for i in range(1,long):
            zuhefiledir = zuhefiledir+"/"+filelist[i]
            if os.path.exists(zuhefiledir):
                self.outPutMyLog("已经存在目录：%s" % zuhefiledir)
            else:
                os.mkdir(zuhefiledir)
                self.outPutMyLog("已经创建目录：%s" % zuhefiledir)

    def clickBack(self):
        self.driver.back()
        url = self.getNowPageUrl()
        self.outPutMyLog("返回到页面URL为：%s的页面" % url)

    def switchNewWindows(self):
        window_handles = self.driver.window_handles
        long = len(window_handles)
        self.outPutMyLog("目前打开的窗口有%s个。" % long)
        window_before = self.driver.window_handles[long-2]
        print("之前窗口的窗口句柄作为:%s" % window_before)
        window_after = self.driver.window_handles[long-1]
        print("新打开的窗口的窗口句柄作为:%s"% window_after)
        self.driver.switch_to.window(window_after)
        # print("当前窗口：%s" % self.driver.current_window_handle)
        #
        # handles = self.driver.window_handles  # 输出当前所有句柄
        # print("所有窗口：%s" % handles)
        # for handle in handles:
        #     if handle != self.driver.current_window_handle:
        #         print("目前条件：%s" % handle)
        #         self.driver.switch_to.window(handle)
        self.delayTime(3)
        print("切换到新窗口")

    def getPageSource(self):
        pagesource = self.driver.page_source
        # bs = BeautifulSoup(self.driver.page_source,"html.parser")
        self.outPutMyLog("\n#####################################################\n")
        self.outPutMyLog("页面源代码为;%s"%pagesource)
        self.outPutMyLog("\n#####################################################\n")
        # self.outPutMyLog(bs)
        return pagesource

    #双击某个元素
    def doubleClick(self,ele):
        ActionChains(self.driver).double_click(ele).perform()

    #单击某个元素
    def singleClick(self,ele):
        ActionChains(self.driver).click(ele).perform()


    #切换到iframe
    def swithToIframe(self,iframeele):
        self.driver.switch_to.frame(iframeele)
        self.outPutMyLog("切换到iframe框")

    #退出iframe
    def quiteCurrentIframe(self):
        self.driver.switch_to.default_content()
        self.outPutMyLog("退出当前iframe框")
        self.outPutMyLog("切换回进入iframe框之前的内容")

    #切换到alert
    def swithToAlert(self):
        now_alert =  self.driver.switch_to.alert
        self.outPutMyLog("切换到alert框")
        self.outPutMyLog("alert框文本信息：")
        self.outPutMyLog(now_alert.text)
        now_alert.accept()   #alert对话框属于警告对话框，我们这里只能接受弹窗
        self.outPutMyLog("接受弹窗")
        self.delayTime(2)

    #判断input是否被选中
    def input_is_checked(self,inputele):
        input_is_chaecked = inputele.is_selected()
        self.outPutMyLog("input框是否被选中（目前状态）：")
        self.outPutMyLog(input_is_chaecked)
        return input_is_chaecked



    #关闭浏览器
    def closeBrowse(self):
        self.driver.quit()


if __name__ == "__main__":
    #驱动下载地址：https://www.cnblogs.com/yhleng/p/8056120.html
    activeweb = ActiveBrowser()  # 实例化
    # activeweb.quDiaoInputStyle("1")
    url = "http://www.baidu.com"
    activeweb.getUrl(url)

    # for i in range(0,10):
    #     activeweb = ActiveBrowser() #实例化
    #     # activeweb.quDiaoInputStyle("1")
    #     url = "http://111.207.18.22:22044/#/login"
    #     activeweb.getUrl(url)
    #     # account = "/html/body/div[2]/div/div/div[2]/div/form/div[1]/input"
    #     # password = "/html/body/div[2]/div/div/div[2]/div/form/div[2]/input"
    #     loginbutton = "/html/body/div[1]/div/div[3]/div[1]/div/form/div[4]/div/button"
    #     # activeweb.findElementByXpathAndInput(account, '17090177294')
    #     # activeweb.findElementByXpathAndInput(password, '900805')
    #     activeweb.findEleAndClickWithAlert(0,"xpath",loginbutton)
    #     # activeweb.delayTime(3)
    #     continue
