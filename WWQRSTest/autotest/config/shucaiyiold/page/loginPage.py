from WWTest.base.activeBrowser import ActiveBrowser

class GlobalConfig(object):
    ISONLINE = False
    ONLINE_WEB_YUMING= ""
    ONLINE_LOGIN_ACCOUNT = ""
    ONLINE_LOGIN_PASSWORD = ""

    TEST_WEB_YUMING = "http://192.168.101.124"
    TEST_LOGIN_ACCOUNT = "config"
    TEST_LOGIN_PASSWORD = "config"

    COOKIE_FILE_NAME = "shucaiyioldlogincookie.json"

gc = GlobalConfig()

class LoginPage(object):
    login_account_input_xpath = "/html/body/div/div/div/form/table/tbody/tr[2]/td[2]/input"
    login_password_input_xpath = "/html/body/div/div/div/form/table/tbody/tr[3]/td[2]/input"
    # login_code_xpath = "/html/body/div[1]/div/div[3]/div[1]/div/form/div[3]/div/div/div[2]/img"
    # login_code_input_xpath = "/html/body/div/div/div[3]/div[1]/div/form/div[3]/div/div/div[1]/div/input"
    login_button_xpath = "/html/body/div/div/div/form/table/tbody/tr[4]/td/input[1]"


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

    def login(self,activebroser,):
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
        # print("code:%s" %code)
        # activebroser.findEleAndInputNum(0, "xpath",loginpage.login_code_input_xpath,code)
        activebroser.findEleAndClick(0,"xpath",loginpage.login_button_xpath)  #点击登录
        try:
            activebroser.swithToAlert()
            activebroser.delayTime(3)
            activebroser.swithToAlert()
        except:
            pass
        activebroser.writerCookieToJson(gc.COOKIE_FILE_NAME)  #写入cookie


    def loginwithcookies(self,activebroser):
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
        cookie1 = {'name': 'wanwei_dcloud_rememberMe', 'value': 'eyJ1c2VybmFtZSI6ImZtYWRtaW4iLCJwYXNzd29yZCI6ImFkbWluMTIzQSJ9'}
        activebroser.driver.add_cookie(cookie1)
        cookie2 = {'name':'wanwei_dcloud_LOGIN_NAME','value':'fmadmin'}
        activebroser.driver.add_cookie(cookie2)
        cookie3 = {'name':'wanwei_dcloud_REGION_CODE','value':'220211'}
        activebroser.driver.add_cookie(cookie3)
        cookie4 = {'name':'wanwei_dcloud_AUTH_TOKEN','value':'{%22access_token%22:%22eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX25hbWUiOiJmbWFkbWluIiwiZXhwIjoxNTY4MjcyNDc4LCJqdGkiOiI2NTI3ODQxMzg3IiwiY2xpZW50X2lkIjoiZGNsb3VkLWNsaWVudC1hdXRoIn0.B0e1CpMTsPwIgMW1mNVrZOzb2e26FlCwV-jry2Hm7AE%22%2C%22expires_in%22:7199%2C%22scope%22:%22*%22%2C%22timestamp%22:1568265278414%2C%22loginName%22:%22fmadmin%22}'}
        activebroser.driver.add_cookie(cookie4)
        cookie5 = {'name':'wanwei_dcloud_REFRESH_TOKEN','value':'%22refresh_token%22:%22eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX25hbWUiOiJmbWFkbWluIiwiYXRpIjoiNDk5NDU1NDA0NiIsImV4cCI6MTU3MDg0MTk0NSwianRpIjoiNDk5NDU1NDAxMDAiLCJjbGllbnRfaWQiOiJkY2xvdWQtY2xpZW50LWF1dGgifQ.n1vhQKC7F_b3YE0DGwHDjTTgOiCODxAiOG5VQPbeyEo%22%2C%22expires_in%22:7197%2C%22scope%22:%22*%22%2C%22timestamp%22:1568249945541%2C%22loginName%22:%22fmadmin%22}'}
        activebroser.driver.add_cookie(cookie5)
        activebroser.delayTime(3)
        activebroser.getUrl(loginurl)
        activebroser.getCookies()
        activebroser.delayTime(10)


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
        if self.isExistLoginButton(activebroser):   #如果登录按钮存在，则进行登录命令
            self.login(activebroser)








lpf = LoginPageFunction()
# lpf.login(111)
# lpf.loginwithcookies(111)
# lpf.loginwithcookiesauto(111)

if __name__ == '__main__':
    # print("hello world")
    # unittest.main()
    ac = ActiveBrowser()
    # lpf.login(activebroser=ac)
    lpf.loginwithcookiesauto(activebroser=ac)
