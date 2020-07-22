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


lpf = LoginPageFunction()


class WebEFourConfig(object):

    def __init__(self,select_xie_yi,select_jian_kong_yin_zi_list,ip,service_ip,service_port):
        self.activebrowser = ActiveBrowser()  # 实例化
        self.select_xie_yi = select_xie_yi
        self.select_jian_kong_yin_zi_list = select_jian_kong_yin_zi_list
        self.loginurl = "http://%s"% ip
        self.service_ip = service_ip
        self.service_port = service_port

    def login(self):   #登录
        lpf.login(self.activebrowser,self.loginurl)  #登录
        self.activebrowser.delayTime(20)  #等待20秒，等待页面刷新出来

    #切换到第一个frame
    def switchToOneFrame(self):
        frame_xpath = "/html/frameset/frameset/frame[1]"
        frame_ele = self.activebrowser.findELe("xpath",frame_xpath)
        self.activebrowser.swithToIframe(frame_ele)  #切换到串口参数配置所在frame

    #切换到第二个frame
    def switchToTwoFrame(self):
        frame_xpath = "/html/frameset/frameset/frame[2]"
        frame_ele = self.activebrowser.findELe("xpath",frame_xpath)
        self.activebrowser.swithToIframe(frame_ele)  #切换到串口协议所在frame

    #退出frame
    def quiteCurrentFrame(self):
        self.activebrowser.quiteCurrentIframe()  #退出当前frame

    # 处理alert弹框
    def handleAlert(self):
        self.activebrowser.swithToAlert()  # 处理alert弹框
        # self.activebrowser.delayTime(5)

    #点击“串口参数配置”
    def clickChuanKouCanShuPeiZhi(self):
        self.switchToOneFrame()
        #点击“串口参数配置”
        caijipeizhi_xpath = "/html/body/div/ul[1]/li[1]/a"
        caijipeizhi_link_text = "串口参数配置"
        self.activebrowser.findEleAndClick(0, "link_text", caijipeizhi_link_text )  # 点击“串口参数配置”
        self.quiteCurrentFrame()

    #查看串口4是否被选中，没有选中，则点击选择，否则，不做任何操作
    def checkChuanKou(self):
        self.switchToTwoFrame()
        self.activebrowser.delayTime(3)
        chuankou_4_input_xpath = "/html/body/form/div/div[2]/table/tbody/tr[6]/td[3]/input"
        chuankou_4_input_ele = self.activebrowser.findELe("xpath",chuankou_4_input_xpath)
        is_checked = self.activebrowser.input_is_checked(chuankou_4_input_ele)
        if not is_checked: #如果没有选中， 则点击选中
            self.activebrowser.findEleAndClick(0,"xpath",chuankou_4_input_xpath)
            self.activebrowser.outPutMyLog("点击选中串口4")
        self.quiteCurrentFrame()


    #选择串口协议
    def selectXieYi(self):
        pre_select_option_text = self.select_xie_yi

        self.switchToTwoFrame()
        select_xieyi_xpath = "/html/body/form/div/div[2]/table/tbody/tr[6]/td[8]/select"

        #查看所有选项
        # self.activebrowser.findElementByXpathAndReturnAllOptions(select_xieyi_xpath)

        #选择某个协议：
        self.activebrowser.findElementByXpathAndSelectOptionsNum(0,select_xieyi_xpath,pre_select_option_text)

        #点击保存
        save_xpath = "/html/body/form/div/div[2]/table/tbody/tr[13]/td/input[1]"
        self.activebrowser.findEleAndClick(0, "xpath", save_xpath)  # 点击“保存”
        # self.activebrowser.quiteCurrentIframe()  # 退出当前frame

        self.activebrowser.delayTime(5)   #等待5秒

        self.handleAlert()   # 处理alert弹框


    #点击“因子配置”
    def clickYinZiPeiZhi(self):
        self.switchToOneFrame()
        #点击“因子配置”
        yinzipeizhi_link_text = "因子配置"
        self.activebrowser.findEleAndClick(0, "link_text", yinzipeizhi_link_text )  # 点击“因子配置”
        self.quiteCurrentFrame()

    #获取“因子配置”页的所有因子,并返回不存在的因子
    def getAllYinZi(self):
        self.clickYinZiPeiZhi()
        self.switchToTwoFrame()
        allyinzi_tbody_xpath = "/html/body/form/div/div[2]/table/tbody"
        #因子代码是否在“因子配置”页
        allyinzi_dict = self.activebrowser.findEleAndReturnTable(0,"xpath",allyinzi_tbody_xpath)
        self.quiteCurrentFrame()
        print(allyinzi_dict)
        exist_code_list = []
        not_exist_code_list = []
        for yinzi_code in self.select_jian_kong_yin_zi_list:
            yinzi_code = yinzi_code.strip()  #去掉前后空格
            for value in allyinzi_dict.values():
                if yinzi_code == value[0]:  #如果查找的等于监控因子的因子，则保存监控因子到存在的因子列表中
                    exist_code_list.append(yinzi_code)
        print("预期监控因子：")
        print(self.select_jian_kong_yin_zi_list)

        print("因子配置列表中存在的因子：")
        print(exist_code_list)

        for yinzi_code in self.select_jian_kong_yin_zi_list:
            if yinzi_code not in exist_code_list:  #如果所有监控因子中存在有不在因子配置列表中，则保存到不存在的因子列表中
                not_exist_code_list.append(yinzi_code)

        print("因子配置列表应该存在而实际不存在的因子（需要在因子配置列表中添加）：")
        print(not_exist_code_list)
        return not_exist_code_list   #返回不存在的因子


    #获取不存在的因子，查看是否需要添加，不需要添加则返回True,需要添加，则提示先添加后再执行后续操作
    def isAddNotExistYinZi(self):
        not_exist_code_list = self.getAllYinZi()
        if not_exist_code_list==[]: #说明不存在需要添加的因子,即所有监控因子都在因子配置列表中
            return True
        else:
            print("需要在因子配置列表中添加如下因子：")
            print(not_exist_code_list)
            print("请在因子配置列表中先添加上面的因子！！！")
            return False



    #判断监测因子是否在因子配置列表页
    def checkJianCeYinZiInYinZiPeiZhi(self):
        #进入因子配置列表
        self.clickYinZiPeiZhi()
        #获取已有所有因子


        for yinzi_code in self.select_jian_kong_yin_zi_list:
            pass



    #点击“监测因子列表”
    def clickJianCeYinZiLieBiao(self):
        self.switchToOneFrame()
        #点击“串口参数配置”
        jianceyinziliebiao_xpath = "/html/body/div/ul[1]/li[2]/a"
        jianceyinziliebiao_link_text = "监测因子列表"
        self.activebrowser.findEleAndClick(0, "link_text", jianceyinziliebiao_link_text )  # 点击“监测因子列表”
        self.quiteCurrentFrame()

    #点击“清除所有”
    def clickDeleteAllYinZi(self):
        self.switchToTwoFrame()  # 切换到第二个frame
        qingchusuoyou_xpath = "/html/body/form/div/table/tbody/tr/td[2]/input"
        self.activebrowser.findEleAndClick(0, "xpath", qingchusuoyou_xpath)  # 点击“清除所有”
        self.handleAlert()  # 处理alert弹框
        self.activebrowser.delayTime(2)
        self.handleAlert()  # 处理alert弹框
        self.activebrowser.delayTime(2)



    #添加监测因子
    def addJianCeYinZi(self):
        for yinzi_code in self.select_jian_kong_yin_zi_list:
            #选择因子代码
            # self.switchToTwoFrame()   #切换到第二个frame
            #点击“添加”按钮
            add_button_xpath = "/html/body/form/div/table/tbody/tr/td[1]/input"
            self.activebrowser.findEleAndClick(0, "xpath", add_button_xpath)  # 点击“添加”按钮


            yinzi_code  = yinzi_code
            yinzidaimamingcheng_xpath = "/html/body/form/div/div[2]/table[1]/tbody/tr/td[2]/select"
            self.activebrowser.findElementByXpathAndSelectOptionsNum(0, yinzidaimamingcheng_xpath, yinzi_code)  #选择监测因子

            #信号属相选择数字信号
            shuzixinhao = "数字信号"
            xinhaoshuxing_xpath = "/html/body/form/div/div[2]/table[2]/tbody/tr[1]/td[2]/select"
            self.activebrowser.findElementByXpathAndSelectOptionsNum(0, xinhaoshuxing_xpath, shuzixinhao)  # 选择信号属性

            #协议列表选择相应的协议
            xieyi = self.select_xie_yi
            xieyixuanzeliebiao_xpath = "/html/body/form/div/div[2]/table[2]/tbody/tr[1]/td[4]/select"
            self.activebrowser.findElementByXpathAndSelectOptionsNum(0,xieyixuanzeliebiao_xpath, xieyi)  # 选择协议

            #点击全选
            quanxian_xpath = "/html/body/form/div/div[2]/table[3]/tbody/tr/td[1]/div/div[2]/table/tbody/tr[6]/td[1]/input"
            self.activebrowser.findEleAndClick(0, "xpath", quanxian_xpath)  # 点击“全选”选框

            #点击保存
            save_xpath = "/html/body/form/div/div[2]/table[5]/tbody/tr/td/input[2]"
            self.activebrowser.findEleAndClick(0, "xpath", save_xpath)  # 点击“保存”按钮

            self.handleAlert()  # 处理alert弹框
            self.activebrowser.delayTime(5)

        # #添加监控因子完成后，设置日志打印级别
        # self.setLogLevel()

        #循环完成后，要退出当前frame
        self.quiteCurrentFrame()


    #点击监控因子列表中的高级配置设置打印日志级别为develop
    def setLogLevel(self):
        #处于监测因子列表页
        #点击“高级配置”
        gaojipeizhi_xpath = "/html/body/form/div/div[2]/table[3]/tbody/tr/td/input[1]"
        self.activebrowser.findEleAndClick(0, "xpath", gaojipeizhi_xpath)  # 点击“高级配置”
        dayijibie_option_text = "develop"
        dayinjibie_select_xpath = "/html/body/form/div/div[2]/table[2]/tbody/tr/td[1]/table/tbody/tr/td[2]/select"
        self.activebrowser.findElementByXpathAndSelectOptionsNum(0, dayinjibie_select_xpath, dayijibie_option_text)  # 选择打印级别为develop

        baocun_xpath = "/html/body/form/div/div[2]/table[3]/tbody/tr/td/input[2]"
        self.activebrowser.findEleAndClick(0, "xpath", baocun_xpath)  # 点击“保存”
        self.handleAlert()   #处理弹出的弹框


    #设置上报平台
    #点击“网络参数配置”
    def clickWangLuoCanShuPeiZhi(self):
        self.switchToOneFrame()
        wangluocanshupeizhi_link_text = "网络参数配置"
        self.activebrowser.findEleAndClick(0, "link_text", wangluocanshupeizhi_link_text )  # 点击“网络参数配置”
        print("已经点击【网络参数配置】")
        self.quiteCurrentFrame()

    #添加上报平台,默认写有线网络第一个服务器地址
    def addServiceConfig(self):
        self.switchToTwoFrame()
        fuwuqidizhi_xpath = "/html/body/form/div/div[4]/div[2]/table/tbody/tr[2]/td[2]/input"
        fuwuqidizhi_input_text = self.service_ip
        self.activebroser.findEleAndInputNum(0, "xpath", fuwuqidizhi_xpath, fuwuqidizhi_input_text)  # 输入密码
        fuwuqiduankou_xpath = "/html/body/form/div/div[4]/div[2]/table/tbody/tr[2]/td[4]/input"






    #点击写入设备
    def clickXieRuSheBei(self):
        self.switchToOneFrame()
        xierushebei_xpath = "/html/body/div/div[4]/input"
        self.activebrowser.findEleAndClick(0, "xpath", xierushebei_xpath)
        self.handleAlert()   #处理处理alert弹框
        self.activebrowser.delayTime(60)   #等待60秒，保证机子重启完成

    def closeWeb(self):
        self.activebrowser.closeBrowse()

    def run(self):
        #登录
        self.login()
        #获取“因子配置”中的所有因子,查看因子配置中是否包含所有监测因子，如果都有，则执行后续操作，如果没有则提示进行添加
        is_continue = self.isAddNotExistYinZi()

        if is_continue:   #如果全部都有，则执行后续操作
            #点击“串口参数配置”
            self.clickChuanKouCanShuPeiZhi()
            # 查看串口4是否被选中，没有选中，则点击选择，否则，不做任何操作
            self.checkChuanKou()
            #选择协议
            self.selectXieYi()
            self.quiteCurrentFrame()
            #点击监测因子列表
            self.clickJianCeYinZiLieBiao()
            #点击清除所有
            self.clickDeleteAllYinZi()
            #添加监测因子
            self.addJianCeYinZi()
            # 点击“网络参数配置”
            self.clickWangLuoCanShuPeiZhi()
            #添加平台

            #点击写入设备
            self.clickXieRuSheBei()
        #关闭web
        self.closeWeb()
        return is_continue


if __name__ == '__main__':
    select_xie_yi = "134_E"
    select_jian_kong_yin_zi_list = [ "S01"]
    ip = "192.168.101.124"
    service_ip = "192.168.101.123"
    service_port = "65321"
    # select_jian_kong_yin_zi_list = ['a24087', 'a24088', 'a01016', 'a01011', 'a01012', 'a01013', 'a01014', 'a00000', 'a19001', 'a24088z']
    wc = WebEFourConfig(select_xie_yi,select_jian_kong_yin_zi_list,ip,service_ip,service_port)
    wc.run()



