from WWTest.base.activeBrowser import ActiveBrowser
from WWTest.autotest.config.wanwei.globalconfig.globalConfig import GlobalConfig,gc

class LoginPage(object):
    login_account_input_xpath = "/html/body/div/div/div[3]/div[1]/div/form/div[1]/div/div/input"
    login_password_input_xpath = "/html/body/div/div/div[3]/div[1]/div/form/div[2]/div/div/input"
    login_code_xpath = "/html/body/div[1]/div/div[3]/div[1]/div/form/div[3]/div/div/div[2]/img"
    login_code_input_xpath = "/html/body/div/div/div[3]/div[1]/div/form/div[3]/div/div/div[1]/div/input"
    login_button_xpath = "/html/body/div/div/div[3]/div[1]/div/form/div[4]/div/button"


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
        activebroser.findEleAndInputNum(0,"xpath",loginpage.login_account_input_xpath,loginaccount)
        activebroser.findEleAndInputNum(0,"xpath",loginpage.login_password_input_xpath,loginpassword)
        # code = activebroser.getcodetext(loginpage.login_code_xpath)
        code = activebroser.getCodeTextByThreeInterfase(loginpage.login_code_xpath)
        print("code:%s" %code)
        activebroser.findEleAndInputNum(0, "xpath",loginpage.login_code_input_xpath,code)
        activebroser.findEleAndClick(0,"xpath",loginpage.login_button_xpath)
        activebroser.writerCookieToJson(gc.COOKIE_FILE_NAME)


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

import time
lpf = LoginPageFunction()
activebroser = ActiveBrowser()
# if gc.ISONLINE:
#     loginurl = gc.ONLINE_WEB_YUMING
#     loginaccount = gc.ONLINE_LOGIN_ACCOUNT
#     loginpassword = gc.ONLINE_LOGIN_PASSWORD
# else:
#     loginurl = gc.TEST_WEB_YUMING
#     loginaccount = gc.TEST_LOGIN_ACCOUNT
#     loginpassword = gc.TEST_LOGIN_PASSWORD
#
# activebroser.getUrl(loginurl)
# activebroser.findEleAndInputNum(0, "xpath", loginpage.login_account_input_xpath, loginaccount)
# activebroser.findEleAndInputNum(0, "xpath", loginpage.login_password_input_xpath, loginpassword)
# # code = activebroser.getcodetext(loginpage.login_code_xpath)
# code = activebroser.getCodeTextByThreeInterfase(loginpage.login_code_xpath)
# print("code:%s" % code)
# activebroser.findEleAndInputNum(0, "xpath", loginpage.login_code_input_xpath, code)
# activebroser.findEleAndClick(0, "xpath", loginpage.login_button_xpath)
# lpf.login(activebroser)

driver = activebroser.driver
Url = "http://111.207.18.22:22044/#/login"
activebroser.getUrl(Url)
time.sleep(20)
loginbutton = "/html/body/div/div/div[3]/div[1]/div/form/div[4]/div/button/span"
activebroser.findEleAndClick(0,"xpath",loginbutton)
# time.sleep(3)

Url =  activebroser.driver.current_url
print(Url)


#
# 调用浏览器打开一个新窗口
# driver.execute_script("window.open('','_blank');")
# # 窗口定位到新打开的窗口
# driver.switch_to.window(driver.window_handles[-1])
driver.get(Url)
ld = LoadTimesDefineClass()
print(id(ld))

driver.execute_script(ld.img)
# driver.execute_script(ld.intfaces)
driver.execute_script(ld.DNS)
driver.execute_script(ld.TCP)
driver.execute_script(ld.request)
driver.execute_script(ld.dom)
driver.execute_script(ld.Ari)
page_time_NoCatch = int(driver.execute_script(ld.loadEventTime))
dom_time_NoCatch = int(driver.execute_script(ld.domready))
time.sleep(5)
print("无缓存页面加载时间：%s" % page_time_NoCatch)
print("无缓存DOM加载时间：%s" % dom_time_NoCatch)
# # # 关闭窗口
# # driver.execute_script("window.close();")
# # # 窗口定位返回旧窗口
# # driver.switch_to.window(driver.window_handles[-1])
# #
# # time.sleep(5)
# # 调用浏览器打开一个新窗口
# driver.execute_script("window.open('','_blank');")
# # 窗口定位到新打开的窗口
# driver.switch_to.window(driver.window_handles[-1])
#
# driver.get(Url)
# # driver.refresh()
# ld2 = LoadTimesDefineClass()
# print(id(ld2))
# driver.execute_script(ld2.img)
# # driver.execute_script(ld2.intfaces)
# driver.execute_script(ld2.DNS)
# driver.execute_script(ld2.TCP)
# driver.execute_script(ld2.request)
# driver.execute_script(ld2.dom)
# driver.execute_script(ld2.Ari)
# page_time_Catch = int(driver.execute_script(ld2.loadEventTime))
# dom_time_Catch = int(driver.execute_script(ld2.domready))
# # time.sleep(0.5)
# print("有缓存页面加载时间：%s" % page_time_Catch)
# print("有缓存DOM加载时间：%s" % dom_time_Catch)
# # 关闭窗口
# driver.execute_script("window.close();")
# # 窗口定位返回旧窗口
# driver.switch_to.window(driver.window_handles[-1])
driver.quit()