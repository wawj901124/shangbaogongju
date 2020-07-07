# ----------------------------------------------------------------------
import os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wanwenyc.settings")
django.setup()
# ----------------------------------------------------------------------
# 独运行某一个py文件时会出现如下错误：django.core.exceptions.AppRegistryNotReady: Apps aren't loaded yet.，以上内容可以解决此问题,加载django中的App

from WWQRSTest.autotest.config.shucaiyi.page.loginPage import *  # 导入登录页


class WebVSixConfig(object):

    def __init__(self,select_xie_yi,select_jian_kong_yin_zi_list):
        self.activebrowser = ActiveBrowser()  # 实例化
        self.select_xie_yi = select_xie_yi
        self.select_jian_kong_yin_zi_list = select_jian_kong_yin_zi_list

    def login(self):   #登录
        lpf.loginwithcookiesauto(self.activebrowser)  #登录
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
        chuankou_4_input_xpath = "/html/body/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/section[1]/div[2]/div[3]/table/tbody/tr[4]/td[1]/div/div/div/label/span[1]"
        chuankou_4_input_ele = self.activebrowser.findELe("xpath",chuankou_4_input_xpath)
        is_checked = self.activebrowser.input_is_checked(chuankou_4_input_ele)
        if not is_checked: #如果没有选中， 则点击选中
            self.activebrowser.findEleAndClick(0,"xpath",chuankou_4_input_xpath)
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
            return False
        else:
            #进行选择
            #选项列表父标签xpath路径
            select_ul_xpath = "/html/body/div[2]/div[1]/div[1]/ul"
            self.activebrowser.findUlAndClickSelectLi(ul_xpath=select_ul_xpath,li_text=pre_select_option_text)
            return True

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
        if is_continue: #如果选择的协议不是当前的协议，则继续往下执行，否则，不再继续往下，而是直接关闭web配置
            #保存选择的协议
            self.clickXieYiBaoCun()
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
            #点击重启
            self.clickRestart()
        #关闭web
        self.closeWeb()
        return True


if __name__ == '__main__':
    select_xie_yi = "1055"
    select_jian_kong_yin_zi_list = ['a21005', 'a19001', 'a01012']
    wc = WebVSixConfig(select_xie_yi,select_jian_kong_yin_zi_list)
    wc.run()



