from WWTest.base.activeBrowser import ActiveBrowser
from WWTest.autotest.config.youyanweixin.globalconfig.globalConfig import gc,GlobalConfig

class LoginPage(object):
    login_account_input_xpath = "/html/body/div[1]/div/div/div[2]/div[1]/div[1]/a/div[2]/div[2]/input"
    login_password_input_xpath = "/html/body/div[1]/div/div/div[2]/div[1]/div[2]/a/div[2]/div[2]/input"
    # login_code_xpath = "/html/body/div[1]/div/div[3]/div[1]/div/form/div[3]/div/div/div[2]/img"
    # login_code_input_xpath = "/html/body/div/div/div[3]/div[1]/div/form/div[3]/div/div/div[1]/div/input"
    login_button_xpath = "/html/body/div[1]/div/div/div[2]/div[2]/button"


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
        activebroser = ActiveBrowser()
        # activebroser = activebroser
        if gc.ISONLINE:
            loginurl = gc.ONLINE_WEB_YUMING
            loginaccount = gc.ONLINE_LOGIN_ACCOUNT
            loginpassword = gc.ONLINE_LOGIN_PASSWORD
        else:
            loginurl = gc.TEST_WEB_YUMING
            loginaccount = gc.TEST_LOGIN_ACCOUNT
            loginpassword = gc.TEST_LOGIN_PASSWORD

        #加载登录页面
        activebroser.getUrl(loginurl)
        #s输入账号
        activebroser.findEleAndInputNum(0,"xpath",loginpage.login_account_input_xpath,loginaccount)
        #输入密码
        activebroser.findEleAndInputNum(0,"xpath",loginpage.login_password_input_xpath,loginpassword)
        # # code = activebroser.getcodetext(loginpage.login_code_xpath)
        # code = activebroser.getCodeTextByThreeInterfase(loginpage.login_code_xpath)
        # print("code:%s" %code)
        # activebroser.findEleAndInputNum(0, "xpath",loginpage.login_code_input_xpath,code)
        #点击登录按钮
        activebroser.findEleAndClick(0,"xpath",loginpage.login_button_xpath)
        #写入cookies
        activebroser.writerCookieToJson(gc.COOKIE_FILE_NAME)


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
        activebroser. writerCookiesWithOneUrl(cookies,loginurl)
        # activebroser.delayTime(30000)
        if self.isExistLoginButton(activebroser):   #如果登录按钮存在，则进行登录命令
            self.login(activebroser)


lpf = LoginPageFunction()
lpf.login(111)
# lpf.loginwithcookiesauto(111)