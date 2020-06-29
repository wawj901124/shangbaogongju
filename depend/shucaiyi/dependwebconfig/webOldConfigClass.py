# ----------------------------------------------------------------------
import os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wanwenyc.settings")
django.setup()
# ----------------------------------------------------------------------
# 独运行某一个py文件时会出现如下错误：django.core.exceptions.AppRegistryNotReady: Apps aren't loaded yet.，以上内容可以解决此问题,加载django中的App

from WWQRSTest.autotest.config.shucaiyiold.page.loginPage import *


class WebOldConfig(object):

    def __init__(self,select_xie_yi,select_jian_kong_yin_zi_list):
        self.activebrowser = ActiveBrowser()  # 实例化
        self.select_xie_yi = select_xie_yi
        self.select_jian_kong_yin_zi_list = select_jian_kong_yin_zi_list

    def login(self):   #登录
        lpf.loginwithcookiesauto(self.activebrowser)  #登录
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
        self.activebrowser.findElementByXpathAndReturnOptionsNum(0,select_xieyi_xpath,pre_select_option_text)

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
            for value in allyinzi_dict.values():
                if yinzi_code.lower() in value[0].lower():  #如果监控因子在列表中,则加入到列表因子中
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
        #加一个空点（空白点击）



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

        #循环完成后，要退出当前frame
        self.quiteCurrentFrame()




    #点击写入设备
    def clickXieRuSheBei(self):
        self.switchToOneFrame()
        xierushebei_xpath = "/html/body/div/div[5]/input"
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
            #点击写入设备
            self.clickXieRuSheBei()
        #关闭web
        self.closeWeb()
        return is_continue


if __name__ == '__main__':
    select_xie_yi = "1985_N"
    select_jian_kong_yin_zi_list = ['a05002', 'a24087', 'a24088', 'a01016', 'a01011', 'a01012', 'a01013', 'a01014', 'a00000', 'a19001', 'a24088z']
    # select_jian_kong_yin_zi_list = ['a24087', 'a24088', 'a01016', 'a01011', 'a01012', 'a01013', 'a01014', 'a00000', 'a19001', 'a24088z']
    wc = WebOldConfig(select_xie_yi,select_jian_kong_yin_zi_list)
    wc.run()



