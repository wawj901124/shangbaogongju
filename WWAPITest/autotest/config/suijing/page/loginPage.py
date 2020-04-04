from WWTest.base.activeBrowser import ActiveBrowser
from WWAPITest.autotest.config.suijing.globalconfig.globalConfig import gc

class LoginPage(object):
    # login_account_input_xpath = "/html/body/div/div/form/div[1]/input"
    # login_password_input_xpath = "/html/body/div/div/form/div[2]/input[1]"
    # login_code_xpath = "/html/body/div/div/form/div[3]/img"
    # login_code_input_xpath = "/html/body/div/div/form/div[3]/input"
    # login_button_xpath = "/html/body/div/div/form/input[4]"

    login_account_input_xpath = "/html/body/div/form/div/div[2]/div[1]/div/div/input"
    login_password_input_xpath = "/html/body/div/form/div/div[2]/div[2]/div/div/input"
    login_code_xpath = "/html/body/div/div/form/div[3]/img"
    login_code_input_xpath = "/html/body/div/div/form/div[3]/input"
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

    def login(self):
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

        activebroser.getUrl(loginurl)
        # activebroser.delayTime(30000)
        activebroser.findEleAndInputNum(0,"xpath",loginpage.login_account_input_xpath,loginaccount)
        activebroser.findEleAndInputNum(0,"xpath",loginpage.login_password_input_xpath,loginpassword)
        # # code = activebroser.getcodetext(loginpage.login_code_xpath)
        # code = activebroser.getCodeTextByThreeInterfase(loginpage.login_code_xpath)
        # print("code:%s" %code)
        # code = code.lower()   #转为小写
        # print("code:%s" %code)
        # activebroser.findEleAndInputNum(0, "xpath",loginpage.login_code_input_xpath,code)
        activebroser.findEleAndClick(0,"xpath",loginpage.login_button_xpath)
        activebroser.delayTime(5)
        if not self.isExistLoginButton(activebroser):   #如果登录按钮不存在，则进行cookies写入文件
            activebroser.writerCookieToJson(gc.COOKIE_FILE_NAME)
            activebroser.closeBrowse()
        else:
            activebroser.closeBrowse()
            self.login()


    def get_JSESSIONID(self):
        activebroser = ActiveBrowser()
        # activebroser = activebroser
        cookies = activebroser.readCookieFromJsonFile(gc.COOKIE_FILE_NAME)
        activebroser.closeBrowse()
        print(cookies)
        JSESSIONID = cookies[0]['value']
        print(JSESSIONID)
        return JSESSIONID

    def get_cookie_dic(self):
        activebroser = ActiveBrowser()
        # activebroser = activebroser
        cookies = activebroser.readCookieFromJsonFile(gc.COOKIE_FILE_NAME)
        cookie_dic = {}
        long = len(cookies)
        for i in range(long):
            cookie_dic[cookies[i]['name']] =cookies[i]['value']

        activebroser.closeBrowse()
        print(cookies)
        print(cookie_dic)
        return cookie_dic

lpf = LoginPageFunction()
# lpf.login()
# lpf.get_cookie_dic()