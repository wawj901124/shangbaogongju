# ----------------------------------------------------------------------
import os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wanwenyc.settings")
django.setup()
# ----------------------------------------------------------------------
# 独运行某一个py文件时会出现如下错误：django.core.exceptions.AppRegistryNotReady: Apps aren't loaded yet.，以上内容可以解决此问题,加载django中的App

import datetime

from WWTest.base.activeBrowser import ActiveBrowser


class GlobalConfig(object):
    ISONLINE = False
    ONLINE_WEB_YUMING= ""
    ONLINE_LOGIN_ACCOUNT = ""
    ONLINE_LOGIN_PASSWORD = ""

    TEST_WEB_YUMING = "http://111.207.18.22:62060/"
    TEST_LOGIN_ACCOUNT = "wanwei"
    TEST_LOGIN_PASSWORD = "admin123"

    COOKIE_FILE_NAME = "shucaiyilogincookie.json"

gc = GlobalConfig()

class LoginPage(object):
    login_account_input_xpath = "/html/body/div/form/div/div[2]/div[1]/div/div/input"
    login_password_input_xpath = "/html/body/div/form/div/div[2]/div[2]/div/div/input"
    # login_code_xpath = "/html/body/div[1]/div/div[3]/div[1]/div/form/div[3]/div/div/div[2]/img"
    # login_code_input_xpath = "/html/body/div/div/div[3]/div[1]/div/form/div[3]/div/div/div[1]/div/input"
    login_button_xpath = "/html/body/div/form/div/div[2]/button"


loginpage = LoginPage()

class LoginPageFunction(object):
    def isExist(self,activebrowser,x_xpath):
        try:
            activebrowser.driver.find_element_by_xpath(x_xpath)
            return True
        except:
            return False

    def isExistLoginButton(self,activebrowser):
        return self.isExist(activebrowser,loginpage.login_button_xpath)

    def login(self,activebroser,loginurl):
        # activebroser = ActiveBrowser()
        activebroser = activebroser
        if gc.ISONLINE:
            loginurl = gc.ONLINE_WEB_YUMING
            loginaccount = gc.ONLINE_LOGIN_ACCOUNT
            loginpassword = gc.ONLINE_LOGIN_PASSWORD
        else:
            loginurl = loginurl
            loginaccount = gc.TEST_LOGIN_ACCOUNT
            loginpassword = gc.TEST_LOGIN_PASSWORD

        activebroser.getUrl(loginurl)
        activebroser.findEleAndInputNum(0,"xpath",loginpage.login_account_input_xpath,loginaccount)
        activebroser.findEleAndInputNum(0,"xpath",loginpage.login_password_input_xpath,loginpassword)  #输入密码
        # code = activebroser.getcodetext(loginpage.login_code_xpath)
        # code = activebroser.getCodeTextByThreeInterfase(loginpage.login_code_xpath)
        # print("code:%s" %code)
        # activebroser.findEleAndInputNum(0, "xpath",loginpage.login_code_input_xpath,code)
        activebroser.findEleAndClick(0,"xpath",loginpage.login_button_xpath)  #点击登录
        # activebroser.writerCookieToJson(gc.COOKIE_FILE_NAME)  #写入cookie


lpf = LoginPageFunction()


class WebAutoConfig(object):

    def __init__(self,select_xie_yi,select_jian_kong_yin_zi_list,
                 ip, service_ip, service_port, device_id,
                 select_shangbao_xieyi="2017"
                 ):
        self.activebrowser = ActiveBrowser()  # 实例化
        self.select_xie_yi = select_xie_yi
        self.select_jian_kong_yin_zi_list = select_jian_kong_yin_zi_list
        self.loginurl = "http://%s" % ip
        self.service_ip = service_ip
        self.service_port = service_port
        self.device_id = device_id
        self.select_shangbao_xieyi = select_shangbao_xieyi

    def login(self):   #登录
        lpf.login(self.activebrowser,self.loginurl)  #登录
        # self.activebrowser.delayTime(3)
        print("登录完成")

    #点击"认证和授权"
    def clickRenZhengHeShouQuan(self):
        #点击“认证和授权”
        renzhengheshouquan_xpath = "/html/body/div[2]/div[1]/div/div[10]/div[1]/h6/a"
        self.activebrowser.findEleAndClick(0, "xpath", renzhengheshouquan_xpath)  # 点击"采集配置"
        print("已经点击【认证和授权】")

    #点击"组"
    def clickZu(self):
        #点击“组”
        zu_xpath = "/html/body/div[2]/div[1]/div/div[10]/div[2]/a[1]"
        self.activebrowser.findEleAndClick(0, "xpath", zu_xpath)  # 点击"采集配置"
        print("已经点击【组】")

    #点击"普通用户"
    def clickPuTongaYuHu(self):
        #点击“普通用户”
        putongyonghu_xpath = "/html/body/div[2]/div[2]/form/div[1]/table/tbody/tr[3]/td[2]/a"
        self.activebrowser.findEleAndClick(0, "xpath", putongyonghu_xpath)  # 点击"采集配置"
        print("已经点击【普通用户】")

    #获取已选项权限内容
    def getAlreadyAuth(self):
        yixuanxiang_select_xpath = "/html/body/div[2]/div[2]/form/div[1]/div/div/div[2]/div[2]/div/div/div[1]/div[2]/select"
        quanxian_list = self.activebrowser.findElementByXpathAndReturnAllOptions(yixuanxiang_select_xpath )
        for one in quanxian_list:
            print(one)



    def closeWeb(self):
        self.activebrowser.closeBrowse()
        print("已经关闭浏览器")

    def run(self):
        #登录
        self.login()
        self.clickRenZhengHeShouQuan()  #点击授权
        self.clickZu()  #点击组
        self.clickPuTongaYuHu() #点击普通用户
        self.getAlreadyAuth()  #获取权限

        #关闭web
        # self.closeWeb()
        # return True


if __name__ == '__main__':
    select_xie_yi = "13212"
    select_jian_kong_yin_zi_list = ['a21005', 'a19001', 'a01012']
    ip = "111.207.18.22:62060/"
    service_ip = "192.168.101.123"
    service_port = "65321"
    device_id = "16"
    # select_jian_kong_yin_zi_list = ['a24087', 'a24088', 'a01016', 'a01011', 'a01012', 'a01013', 'a01014', 'a00000', 'a19001', 'a24088z']
    wc = WebAutoConfig(select_xie_yi,select_jian_kong_yin_zi_list,ip,service_ip,service_port,device_id)
    wc.run()



