# ----------------------------------------------------------------------
import os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wanwenyc.settings")
django.setup()
# ----------------------------------------------------------------------
# 独运行某一个py文件时会出现如下错误：django.core.exceptions.AppRegistryNotReady: Apps aren't loaded yet.，以上内容可以解决此问题,加载django中的App

from WWTest.base.activeBrowser import ActiveBrowser


class GlobalConfig(object):
    ISONLINE = False
    ONLINE_WEB_YUMING= ""
    ONLINE_LOGIN_ACCOUNT = ""
    ONLINE_LOGIN_PASSWORD = ""

    TEST_WEB_YUMING = "http://111.207.18.22:62662/#/login"
    TEST_LOGIN_ACCOUNT = "zsy"
    TEST_LOGIN_PASSWORD = "admin123A"

    COOKIE_FILE_NAME = "zhongshiyoulogincookie.json"

gc = GlobalConfig()


class LoginPage(object):
    login_account_input_xpath = "/html/body/div/div/div[2]/div[2]/div/form/div[1]/div/div/div/input"
    login_password_input_xpath = "/html/body/div/div/div[2]/div[2]/div/form/div[2]/div/div/div/input"
    # login_code_xpath = "/html/body/div[1]/div/div[3]/div[1]/div/form/div[3]/div/div/div[2]/img"
    login_code_input_xpath = "/html/body/div/div/div[2]/div[2]/div/form/div[3]/div/div[1]/div[1]/input"
    login_button_xpath = "/html/body/div/div/div[2]/div[2]/div/form/div[5]/div/button/span"


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

    def login(self,activebroser):
        # activebroser = ActiveBrowser()
        activebroser = activebroser
        if gc.ISONLINE:
            loginurl = gc.ONLINE_WEB_YUMING
            loginaccount = gc.ONLINE_LOGIN_ACCOUNT
            loginpassword = gc.ONLINE_LOGIN_PASSWORD
        else:
            loginurl = gc.TEST_WEB_YUMING
            loginaccount = gc.TEST_LOGIN_ACCOUNT
            loginpassword = gc.TEST_LOGIN_PASSWORD

        activebroser.getUrl(loginurl)
        activebroser.findEleAndInputNum(0,"xpath",loginpage.login_account_input_xpath,loginaccount)   #输入账号
        activebroser.findEleAndInputNum(0,"xpath",loginpage.login_password_input_xpath,loginpassword)  #输入密码
        # code = activebroser.getcodetext(loginpage.login_code_xpath)
        # code = activebroser.getCodeTextByThreeInterfase(loginpage.login_code_xpath)
        code = input("请输入验证码：")
        print("code:%s" %code)
        activebroser.findEleAndInputNum(0, "xpath",loginpage.login_code_input_xpath,code)
        activebroser.findEleAndClick(0,"xpath",loginpage.login_button_xpath)  #点击登录
        try:
            activebroser.swithToAlert()
            activebroser.delayTime(3)
            activebroser.swithToAlert()
        except:
            pass
        activebroser.writerCookieToJson(gc.COOKIE_FILE_NAME)  #写入cookie


    def loginwithcookiesauto(self,activebroser):
        # activebroser = ActiveBrowser()
        activebroser = activebroser
        if gc.ISONLINE:
            loginurl = gc.ONLINE_WEB_YUMING
            loginaccount = gc.ONLINE_LOGIN_ACCOUNT
            loginpassword = gc.ONLINE_LOGIN_PASSWORD
        else:
            loginurl = gc.TEST_WEB_YUMING
            loginaccount = gc.TEST_LOGIN_ACCOUNT
            loginpassword = gc.TEST_LOGIN_PASSWORD

        cookies = activebroser.readCookieFromJsonFile(gc.COOKIE_FILE_NAME)

        activebroser.writerCookiesWithOneUrl(cookies,loginurl)
        if self.isExistLoginButton(activebroser):   #如果登录按钮存在，则进行登录命令
            self.login(activebroser)

lpf = LoginPageFunction()

class WebRemoteUphild(object):

    def __init__(self):
        self.activebrowser = ActiveBrowser()  # 实例化
        # self.select_xie_yi = select_xie_yi
        # self.select_jian_kong_yin_zi_list = select_jian_kong_yin_zi_list

    def login(self):   #登录
        # lpf.loginwithcookiesauto(self.activebrowser)  #登录
        lpf.login(self.activebrowser)  #登录
        print("登录完成")
        # self.activebrowser.delayTime(20)  #等待20秒，等待页面刷新出来

    #点击“远程维护”
    def clickYuanChengWeiHu(self):
        #点击“系统配置”
        yuanchenweihu_text = "远程维护"
        ul_xpath = "/html/body/div/div/div[1]/div[2]/div/ul"
        self.activebrowser.findUlAndClickSelectLi(ul_xpath=ul_xpath,li_text=yuanchenweihu_text)  #点击“远程维护”
        print("已经点击【远程维护】")

    #点选“第一个排口”,查看排口是否被选中，没有则点击选中
    def clickPaiKou(self):
        paikou_xpath = "/html/body/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div[1]/div[2]/div/div[2]/div/div/label"

        paikou_ele = self.activebrowser.findELe("xpath",paikou_xpath)
        is_checked = self.activebrowser.input_is_checked(paikou_ele)
        if not is_checked: #如果没有选中， 则点击选中
            self.activebrowser.findEleAndClick(0,"xpath",paikou_xpath)
            self.activebrowser.outPutMyLog("点击选择排口")
        else:
            self.activebrowser.outPutMyLog("已经选中排口，无需再选中")

    #点击ul中的li
    def clickLi(self,ul_xpath,li_text):
        self.activebrowser.findUlAndClickSelectLi(ul_xpath=ul_xpath,li_text=li_text)  #点击“远程重启”
        print("已经点击【%s】"% li_text)


    #点击“数据补传”
    def clickShuJuBuChuan(self):
        #点击“数据补传”
        shujubuchuan_text = "数据补传"
        ul_xpath = "/html/body/div/div/div[2]/div/div/div[2]/div[2]/div/div/div/div/div/section[1]/ul"
        self.activebrowser.findUlAndClickSelectLi(ul_xpath=ul_xpath,li_text=shujubuchuan_text)  #点击“数据补传”
        print("已经点击【数据补传】")

    #点击“远程校时”
    def clickYuanChengJiaoShi(self):
        #点击“远程校时”
        yuanchengjiaoshi_text = "远程校时"
        ul_xpath = "/html/body/div/div/div[2]/div/div/div[2]/div[2]/div/div/div/div/div/section[1]/ul"
        self.activebrowser.findUlAndClickSelectLi(ul_xpath=ul_xpath,li_text=yuanchengjiaoshi_text)  #点击“远程校时”
        print("已经点击【远程校时】")


    #点击“远程重启”
    def clickYuanChengChongQi(self):
        #点击“远程重启”
        yuanchengchongqi_text = "远程重启"
        ul_xpath = "/html/body/div/div/div[2]/div/div/div[2]/div[2]/div/div/div/div/div/section[1]/ul"
        self.activebrowser.findUlAndClickSelectLi(ul_xpath=ul_xpath,li_text=yuanchengchongqi_text)  #点击“远程重启”
        print("已经点击【%s】"% yuanchengchongqi_text)


    #点击“屏幕快照”
    def clickPingMuKuaiZhao(self):
        #点击“屏幕快照”
        yuanchengchongqi_text = "屏幕快照"
        ul_xpath = "/html/body/div/div/div[2]/div/div/div[2]/div[2]/div/div/div/div/div/section[1]/ul"
        self.activebrowser.findUlAndClickSelectLi(ul_xpath=ul_xpath,li_text=yuanchengchongqi_text)  #点击“屏幕快照”
        print("已经点击【%s】"% yuanchengchongqi_text)


    #点击“远程配置”
    def clickYuanChengPeiZhi(self):
        #点击“远程配置”
        yuanchengpeizhi_text = "远程配置"
        ul_xpath = "/html/body/div/div/div[2]/div/div/div[2]/div[2]/div/div/div/div/div/section[2]/ul"
        self.activebrowser.findUlAndClickSelectLi(ul_xpath=ul_xpath,li_text=yuanchengpeizhi_text)  #点击“远程配置”
        print("已经点击【%s】"% yuanchengpeizhi_text)


    #点击“远程升级”
    def clickYuanChengShengJi(self):
        li_text = "远程升级"
        ul_xpath = "/html/body/div/div/div[2]/div/div/div[2]/div[2]/div/div/div/div/div/section[3]/ul"
        self.clickLi(ul_xpath=ul_xpath,li_text=li_text)

    #点击“提取下发文件”
    def clickTiQuXiaFaWenJian(self):
        li_text = "提取下发文件"
        ul_xpath = "/html/body/div/div/div[2]/div/div/div[2]/div[2]/div/div/div/div/div/section[4]/ul"
        self.clickLi(ul_xpath=ul_xpath,li_text=li_text)

    #点击“远程指令”
    def clickYuanChengZhiLing(self):
        li_text = "远程指令"
        ul_xpath = "/html/body/div/div/div[2]/div/div/div[2]/div[2]/div/div/div/div/div/section[4]/ul"
        self.clickLi(ul_xpath=ul_xpath,li_text=li_text)

    #点击“维护平台地址配置”
    def clickWeiHuPingTaiDiZhiPeiZhi(self):
        li_text = "维护平台地址配置"
        ul_xpath = "/html/body/div/div/div[2]/div/div/div[2]/div[2]/div/div/div/div/div/section[4]/ul"
        self.clickLi(ul_xpath=ul_xpath,li_text=li_text)


    def closeWeb(self):
        self.activebrowser.closeBrowse()

    def run(self):
        #登录
        self.login()
        #点击远程维护
        self.clickYuanChengWeiHu()
        #点选排口
        self.clickPaiKou()
        # #点击“数据补传”
        # self.clickShuJuBuChuan()

        # 点击“维护平台地址配置”
        self.clickWeiHuPingTaiDiZhiPeiZhi()




if __name__ == '__main__':
    wc = WebRemoteUphild()
    wc.run()




