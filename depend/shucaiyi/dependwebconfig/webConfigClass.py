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

    TEST_WEB_YUMING = "http://192.168.101.124/#/login"
    TEST_LOGIN_ACCOUNT = "管理员"
    TEST_LOGIN_PASSWORD = "51297180"

    COOKIE_FILE_NAME = "shucaiyilogincookie.json"

gc = GlobalConfig()

class LoginPage(object):
    login_account_input_xpath = "/html/body/div[1]/div/div[2]/div[2]/div/form/div[1]/div/div/div/div/input"
    login_password_input_xpath = "/html/body/div[1]/div/div[2]/div[2]/div/form/div[2]/div/div/div/input"
    # login_code_xpath = "/html/body/div[1]/div/div[3]/div[1]/div/form/div[3]/div/div/div[2]/img"
    # login_code_input_xpath = "/html/body/div/div/div[3]/div[1]/div/form/div[3]/div/div/div[1]/div/input"
    login_button_xpath = "/html/body/div[1]/div/div[2]/div[2]/div/form/div[4]/div/button/span"


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
        # activebroser.findEleAndInputNum(0,"xpath",loginpage.login_account_input_xpath,loginaccount)
        activebroser.findEleAndInputNum(0,"xpath",loginpage.login_password_input_xpath,loginpassword)  #输入密码
        # code = activebroser.getcodetext(loginpage.login_code_xpath)
        # code = activebroser.getCodeTextByThreeInterfase(loginpage.login_code_xpath)
        # print("code:%s" %code)
        # activebroser.findEleAndInputNum(0, "xpath",loginpage.login_code_input_xpath,code)
        activebroser.findEleAndClick(0,"xpath",loginpage.login_button_xpath)  #点击登录
        activebroser.writerCookieToJson(gc.COOKIE_FILE_NAME)  #写入cookie


lpf = LoginPageFunction()


class WebVSixConfig(object):

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
        print("登录完成")

    #点击“采集配置”
    def clickCaijiPeiZhi(self):
        #点击“采集配置”
        caijipeizhi_xpath = "/html/body/div/div/div/div[2]/div[1]/div/div[2]/ul/li[5]/ul/li[1]/span[2]"
        self.activebrowser.findEleAndClick(0, "xpath", caijipeizhi_xpath)  # 点击"采集配置"
        print("已经点击【采集配置】")

    #查看串口4是否被选中，没有选中，则点击选择，否则，不做任何操作
    def checkChuanKou(self):
        #此处的选中路径不一定是input，而是选中前后有选中属性区别的标签
        chuankou_4_input_xpath = "/html/body/div[1]/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/section[1]/div[2]/div[3]/table/tbody/tr[4]/td[1]/div/div/div/label/span[1]/input"
        chuankou_4_input_ele = self.activebrowser.findELe("xpath",chuankou_4_input_xpath)
        is_checked = self.activebrowser.input_is_checked(chuankou_4_input_ele)
        print("串口4是否选中：")
        print(is_checked)
        if not is_checked: #如果没有选中， 则点击选中  #点击选中的路径与判断的input的路径不同，未选中时，找不到input路径，只能找到span
            chuankou_4_input_click_xpath = "/html/body/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/section[1]/div[2]/div[3]/table/tbody/tr[4]/td[1]/div/div/div/label/span[1]/span"
            self.activebrowser.findEleAndClick(0,"xpath",chuankou_4_input_click_xpath)
            self.activebrowser.outPutMyLog("点击选中串口4")

    #选择串口协议
    def selectXieYi(self):
        pre_select_option_text = self.select_xie_yi
        select_xieyi_xpath = "/html/body/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/section[1]/div[2]/div[3]/table/tbody/tr[4]/td[2]/div/div/div/div[1]/input"

        #点击选项框
        self.activebrowser.findEleAndClick(0, "xpath", select_xieyi_xpath )  # 点击"选择协议"选项框

        #获取当前选项的属性值
        select_option_placeholder = self.activebrowser.findElementByXpathAndReturnValue(select_xieyi_xpath,"placeholder")
        print("当前选项（placeholder）的值：")
        print(select_option_placeholder)



        if pre_select_option_text in select_option_placeholder:
            print("已经选择协议【%s】" % select_option_placeholder)

            # 填写设备ID
            device_id_xpath = "/html/body/div[1]/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/section[1]/div[2]/div[3]/table/tbody/tr[4]/td[3]/div/div/div/input"
            device_id_input_text = self.device_id
            self.activebrowser.findEleAndInputNum(0, "xpath", device_id_xpath, device_id_input_text)
            self.clickXieYiBaoCun()  #保存
            return False
        else:
            #进行选择
            #选项列表父标签xpath路径
            self.activebrowser.delayTime(2)
            select_ul_xpath = "/html/body/div[2]/div[1]/div[1]/ul"
            is_exist_xieyi = self.activebrowser.findUlAndClickSelectLi(ul_xpath=select_ul_xpath,li_text=pre_select_option_text)
            if is_exist_xieyi: #如果存在协议，则填写设备
                # 填写设备ID
                device_id_xpath = "/html/body/div[1]/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/section[1]/div[2]/div[3]/table/tbody/tr[4]/td[3]/div/div/div/input"
                device_id_input_text = self.device_id
                self.activebrowser.findEleAndInputNum(0, "xpath", device_id_xpath, device_id_input_text)
                self.clickXieYiBaoCun()  #保存
                return True
            else:
                self.activebrowser.outPutErrorMyLog("在协议列表中不存在协议【%s】，请确认协议列表"% pre_select_option_text)
                assert False  #说明协议不在列表中，断言失败

    def clickXieYiBaoCun(self):
        #点击“保存”
        xeiyi_baocun_xpath = "/html/body/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/section/div/button/span"
        self.activebrowser.findEleAndClick(0, "xpath",  xeiyi_baocun_xpath)  # 点击"保存"
        self.activebrowser.delayTime(5)  #等待5秒
        print("已经点击【保存】按钮")

    #根据提供的第一个新增因子选项框自动获取多个新增因子选项框
    def get_auto_xinzeng_yinzi_xpath_list(self,xinzeng_first_xpath, select_jian_kong_yin_zi_list):
        auto_xinzeng_yinzi_xpath_list = []
        xinzeng_yinzi_xpath_list = xinzeng_first_xpath.split("ul/")
        xinzeng_yinzi_xpath_list_one = xinzeng_yinzi_xpath_list[1]
        xinzeng_yinzi_xpath_list_one_list = xinzeng_yinzi_xpath_list_one.split("]/")
        xinzeng_yinzi_xpath_list_one_list_zero = xinzeng_yinzi_xpath_list_one_list[0]
        xinzeng_yinzi_xpath_list_one_list_zero_list = xinzeng_yinzi_xpath_list_one_list_zero.split("[")
        xinzeng_yinzi_xpath_li_num_yuan = xinzeng_yinzi_xpath_list_one_list_zero_list[1]
        print(xinzeng_yinzi_xpath_list)
        print(xinzeng_yinzi_xpath_list_one)
        print(xinzeng_yinzi_xpath_list_one_list)
        print(xinzeng_yinzi_xpath_list_one_list_zero)
        print(xinzeng_yinzi_xpath_list_one_list_zero_list)
        print(xinzeng_yinzi_xpath_li_num_yuan)

        select_jian_kong_yin_zi_list_len = len(select_jian_kong_yin_zi_list)

        for addnum in range(0, select_jian_kong_yin_zi_list_len):
            auto_xinzeng_yinzi_xpath_li_num = int(xinzeng_yinzi_xpath_li_num_yuan) + addnum
            xinzeng_yinzi_xpath_list_one_list_zero_list[1] = str(auto_xinzeng_yinzi_xpath_li_num)
            auto_xinzeng_yinzi_xpath_list_one_list_zero = "[".join(xinzeng_yinzi_xpath_list_one_list_zero_list)
            xinzeng_yinzi_xpath_list_one_list[0] = auto_xinzeng_yinzi_xpath_list_one_list_zero
            auto_xinzeng_yinzi_xpath_list_one = "]/".join(xinzeng_yinzi_xpath_list_one_list)
            xinzeng_yinzi_xpath_list[1] = auto_xinzeng_yinzi_xpath_list_one
            auto_yinzi_xpath = "ul/".join(xinzeng_yinzi_xpath_list)
            print(auto_yinzi_xpath)
            auto_xinzeng_yinzi_xpath_list.append(auto_yinzi_xpath)
        print("新增因子xpath列表：")
        print(auto_xinzeng_yinzi_xpath_list)
        return auto_xinzeng_yinzi_xpath_list

    #根据提供的第一个新增因子选项列表的xpath路径自动获取多个因子的选项列表的ulxpath
    def get_auto_xinzeng_yinzi_select_ul_xpath_list(self,xinzeng_first_select_ul_xpath, select_jian_kong_yin_zi_list):
        auto_xinzeng_yinzi_select_ul_xpath_list = []

        xinzeng_yinzi_select_ul_xpath_list = xinzeng_first_select_ul_xpath.split("div[")
        xinzeng_yinzi_select_ul_xpath_list_one = xinzeng_yinzi_select_ul_xpath_list[1]
        xinzeng_yinzi_select_ul_xpath_list_one_list = xinzeng_yinzi_select_ul_xpath_list_one.split("]")
        xinzeng_yinzi_select_ul_xpath_list_one_list_zero = xinzeng_yinzi_select_ul_xpath_list_one_list[0]

        print(xinzeng_yinzi_select_ul_xpath_list)
        print(xinzeng_yinzi_select_ul_xpath_list_one_list)
        print(xinzeng_yinzi_select_ul_xpath_list_one_list_zero)

        select_jian_kong_yin_zi_list_len = len(select_jian_kong_yin_zi_list)
        for addnum in range(0, select_jian_kong_yin_zi_list_len):
            auto_xinzeng_yinzi_select_ul_xpath_list_one_list_zero = int(
                xinzeng_yinzi_select_ul_xpath_list_one_list_zero) + addnum
            xinzeng_yinzi_select_ul_xpath_list_one_list[0] = str(auto_xinzeng_yinzi_select_ul_xpath_list_one_list_zero)
            auto_xinzeng_yinzi_select_ul_xpath_list_one = "]".join(xinzeng_yinzi_select_ul_xpath_list_one_list)
            xinzeng_yinzi_select_ul_xpath_list[1] = auto_xinzeng_yinzi_select_ul_xpath_list_one
            auto_xinzeng_yinzi_select_ul_xpath = "div[".join(xinzeng_yinzi_select_ul_xpath_list)
            auto_xinzeng_yinzi_select_ul_xpath_list.append(auto_xinzeng_yinzi_select_ul_xpath)

        print("新增因子列表选项Xpath：")
        print(auto_xinzeng_yinzi_select_ul_xpath_list)
        return auto_xinzeng_yinzi_select_ul_xpath_list

    #点击因子配置
    def clickYinZiPeiZhi(self):
        yinzipeizhi_xpath = "/html/body/div[1]/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/section[1]/div[2]/div[3]/table/tbody/tr[4]/td[6]/div/div/button[2]/span"
        #点击因子配置
        self.activebrowser.findEleAndClick(0, "xpath", yinzipeizhi_xpath)
        print("已经点击【因子配置】")

    #点击监控因子配置页面的新增按钮
    def clickYinZiPeiZhiXinZeng(self):
        #点击“新增”
        xinzeng_xpath = "/html/body/div[1]/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[2]/div/div/div[1]/div[2]/button/span"
        self.activebrowser.findEleAndClick(0, "xpath", xinzeng_xpath)
        print("已经点击【新增】按钮")

    #选择监控因子
    def selectJianKongYinZi(self):
        xinzeng_first_xpath = "/html/body/div[1]/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[2]/div/div/div[1]/ul/li[2]/div[1]/div/div[1]/input"
        xinzeng_first_select_ul_xpath = "/html/body/div[3]/div[1]/div[1]/ul"
        select_jian_kong_yin_zi_list = self.select_jian_kong_yin_zi_list

        select_jian_kong_yin_zi_list_len = len(select_jian_kong_yin_zi_list)
        auto_xinzeng_yinzi_xpath_list = self.get_auto_xinzeng_yinzi_xpath_list(xinzeng_first_xpath, select_jian_kong_yin_zi_list)
        auto_xinzeng_yinzi_select_ul_xpath_list = self.get_auto_xinzeng_yinzi_select_ul_xpath_list(xinzeng_first_select_ul_xpath, select_jian_kong_yin_zi_list)

        for i in range(0,select_jian_kong_yin_zi_list_len):
            #点击新增
            self.clickYinZiPeiZhiXinZeng()
            #点击新增监控因子选项框
            xinzeng_yinzi_xpath = auto_xinzeng_yinzi_xpath_list[i]
            self.activebrowser.findEleAndClick(0, "xpath", xinzeng_yinzi_xpath)

            #选择监控因子
            xinzeng_yinzi_select_ul_xpath = auto_xinzeng_yinzi_select_ul_xpath_list[i]
            pre_select_option_text= select_jian_kong_yin_zi_list[i]
            self.activebrowser.findUlAndClickSelectLi(ul_xpath=xinzeng_yinzi_select_ul_xpath, li_text=pre_select_option_text)
            print("已经点击新增【%s】监控因子"%pre_select_option_text)


    def clickJianKongYinZiQueDing(self):
        jiankongyinziqueding_xpath = "/html/body/div[1]/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[2]/div/div/div[2]/button[2]/span"
        self.activebrowser.findEleAndClick(0, "xpath", jiankongyinziqueding_xpath)
        print("已经点击【确定】按钮")


    #写入上报平台
    #点击“上报配置”
    def clickShangBaoPeiZhi(self):
        shangbaopeizhi_xpath = "/html/body/div/div/div/div[2]/div[1]/div/div[2]/ul/li[5]/ul/li[2]/span[2]"
        self.activebrowser.findEleAndClick(0, "xpath", shangbaopeizhi_xpath)
        print("已经点击【确定】按钮")

    #点击“有线配置”
    def clickYouXianPeiZhi(self):
        youxianpeizhi_xpath = "/html/body/div/div/div/div[2]/div[2]/div/div/div[2]/div[1]/div[1]/div/div/div/div[2]"
        self.activebrowser.findEleAndClick(0, "xpath", youxianpeizhi_xpath)
        print("已经点击【确定】按钮")

    #检查平台1是否勾选
    #查看平台1是否被选中，没有选中，则点击选择，否则，不做任何操作
    def checkPingTai(self):
        #此处的选中路径不一定是input，而是选中前后有选中属性区别的标签
        pingtai_1_input_xpath = "/html/body/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/section[2]/div/div/div[3]/table/tbody/tr[1]/td[1]/div/div/div/label/span[1]/input"
        pingtai_1_input_ele = self.activebrowser.findELe("xpath",pingtai_1_input_xpath)
        is_checked = self.activebrowser.input_is_checked(pingtai_1_input_ele)
        print("平台1是否选中：")
        print(is_checked)
        if not is_checked: #如果没有选中， 则点击选中  #点击选中的路径与判断的input的路径不同，未选中时，找不到input路径，只能找到span
            pingtai_1_input_click_xpath = "/html/body/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/section[2]/div/div/div[3]/table/tbody/tr[1]/td[1]/div/div/div/label/span[1]/span"
            self.activebrowser.findEleAndClick(0,"xpath",pingtai_1_input_click_xpath)
            self.activebrowser.outPutMyLog("点击选中平台1")

    #添加上报平台,默认选有线网络第一个平台
    def addServiceConfig(self):
        fuwuqidizhi_xpath = "/html/body/div[1]/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/section[2]/div/div/div[3]/table/tbody/tr[1]/td[3]/div/div/div/input"
        fuwuqidizhi_input_text = self.service_ip
        self.activebrowser.findEleAndInputNum(0, "xpath", fuwuqidizhi_xpath, fuwuqidizhi_input_text)  # 输入服务器IP
        fuwuqiduankou_xpath = "/html/body/div[1]/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/section[2]/div/div/div[3]/table/tbody/tr[1]/td[4]/div/div/div/input"
        fuwuqiduankou_input_text = self.service_port
        self.activebrowser.findEleAndInputNum(0, "xpath", fuwuqiduankou_xpath, fuwuqiduankou_input_text)  # 输入服务器端口

        #选择上报协议
        #点击上报协议选项框
        select_shangbaoxieyi_xpath = "/html/body/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/section[2]/div/div/div[3]/table/tbody/tr[1]/td[2]/div/div/div/div[1]/input"
        #点击选项框
        self.activebrowser.findEleAndClick(0, "xpath", select_shangbaoxieyi_xpath )  # 点击"平台协议"选项框

        #选择上报协议
        shangbao_pingtai_xieyi_option_text = self.select_shangbao_xieyi
        select_ul_xpath = "/html/body/div[2]/div[1]/div[1]/ul"
        self.activebrowser.findUlAndClickSelectLi(ul_xpath=select_ul_xpath, li_text=shangbao_pingtai_xieyi_option_text)

        #固定写死平台名称
        pingtaimingcheng_xpath = "/html/body/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/section[2]/div/div/div[3]/table/tbody/tr[1]/td[5]/div/div/div/input"
        pingtaimingcheng_input_text = "测试平台"
        self.activebrowser.findEleAndInputNum(0, "xpath", pingtaimingcheng_xpath, pingtaimingcheng_input_text)  # 输入平台名称

        #点击“保存”
        baocun_xpath = "/html/body/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/section/div/button/span"
        self.activebrowser.findEleAndClick(0,"xpath",baocun_xpath)



    #点击设备重启
    def clickRestart(self):
        shebeichongqi_xpath = "/html/body/div/div/div/div[2]/div[1]/div/div[2]/ul/li[5]/ul/li[5]/span[2]"
        self.activebrowser.findEleAndClick(0, "xpath", shebeichongqi_xpath)
        shebeichongqi_queding_xpath = "/html/body/div[1]/div/div/div[2]/div[2]/div/div/div[3]/div/div[3]/div/button[2]/span"
        self.activebrowser.findEleAndClick(0, "xpath", shebeichongqi_queding_xpath)
        self.activebrowser.delayTime(60)   #等待60秒
        print("已经重启设备")


    def closeWeb(self):
        self.activebrowser.closeBrowse()
        print("已经关闭浏览器")

    def run(self):
        #登录
        self.login()
        #点击“采集配置”
        self.clickCaijiPeiZhi()
        # 查看串口4是否被选中
        self.checkChuanKou()
        #选择协议
        is_continue = self.selectXieYi()
        if is_continue: #如果选择的协议不是当前的协议，则继续往下执行，否则，写入设备ID号，保存，重启，然后关闭web配置
            #点击重启
            self.clickRestart()

            #登录
            self.login()
            #点击采集配置
            self.clickCaijiPeiZhi()
            # 点击因子配置
            self.clickYinZiPeiZhi()
            #选择监控因子
            self.selectJianKongYinZi()
            #点击添加监控因子确定按钮
            self.clickJianKongYinZiQueDing()
            #点击保存协议
            self.clickXieYiBaoCun()

        # 点击“上报配置”
        self.clickShangBaoPeiZhi()
        # 点击“有线配置”
        self.clickYouXianPeiZhi()
        # 查看平台1是否被选中，没有选中，则点击选择，否则，不做任何操作
        self.checkPingTai()
        # 添加上报平台,默认选有线网络第一个平台
        self.addServiceConfig()
        #点击重启
        self.clickRestart()
        #关闭web
        self.closeWeb()
        return True


if __name__ == '__main__':
    select_xie_yi = "13212"
    select_jian_kong_yin_zi_list = ['a21005', 'a19001', 'a01012']
    ip = "192.168.101.124"
    service_ip = "192.168.101.123"
    service_port = "65321"
    device_id = "16"
    # select_jian_kong_yin_zi_list = ['a24087', 'a24088', 'a01016', 'a01011', 'a01012', 'a01013', 'a01014', 'a00000', 'a19001', 'a24088z']
    wc = WebVSixConfig(select_xie_yi,select_jian_kong_yin_zi_list,ip,service_ip,service_port,device_id)
    wc.run()



