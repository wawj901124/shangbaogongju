# ----------------------------------------------------------------------
import os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wanwenyc.settings")
django.setup()
# ----------------------------------------------------------------------
# 独运行某一个py文件时会出现如下错误：django.core.exceptions.AppRegistryNotReady: Apps aren't loaded yet.，以上内容可以解决此问题,加载django中的App
import datetime

from WWTest.base.activeBrowser import ActiveBrowser

from threading import Thread


def async_call(fn):
    def wrapper(*args, **kwargs):
        Thread(target=fn, args=args, kwargs=kwargs).start()

    return wrapper


class GlobalConfig(object):
    ISONLINE = False
    ONLINE_WEB_YUMING= ""
    ONLINE_LOGIN_ACCOUNT = ""
    ONLINE_LOGIN_PASSWORD = ""

    TEST_WEB_YUMING = "http://192.168.8.98:2000/main.do"
    TEST_LOGIN_ACCOUNT = "xkz"
    TEST_LOGIN_PASSWORD = "123456"

    COOKIE_FILE_NAME = "zhongshiyoulogincookie.json"

gc = GlobalConfig()


class LoginPage(object):
    login_account_input_xpath = "/html/body/table/tbody/tr/td/table/tbody/tr/td/div/form/table/tbody/tr[4]/td/input"
    login_password_input_xpath = "/html/body/table/tbody/tr/td/table/tbody/tr/td/div/form/table/tbody/tr[7]/td/input"
    # login_code_xpath = "/html/body/div[1]/div/div[3]/div[1]/div/form/div[3]/div/div/div[2]/img"
    # login_code_input_xpath = "/html/body/div/div/div[2]/div[2]/div/form/div[3]/div/div[1]/div[1]/input"
    login_button_xpath = "/html/body/table/tbody/tr/td/table/tbody/tr/td/div/form/table/tbody/tr[15]/td/input"


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

    def login(self,activebroser,loginurl,loginaccount,loginpassword):
        # activebroser = ActiveBrowser()
        activebroser = activebroser
        if gc.ISONLINE:
            loginurl = gc.ONLINE_WEB_YUMING
            loginaccount = gc.ONLINE_LOGIN_ACCOUNT
            loginpassword = gc.ONLINE_LOGIN_PASSWORD
        else:
            loginurl = loginurl
            loginaccount = loginaccount
            loginpassword = loginpassword

        activebroser.getUrl(loginurl)
        activebroser.findEleAndInputNum(0,"xpath",loginpage.login_account_input_xpath,loginaccount)   #输入账号
        activebroser.findEleAndInputNum(0,"xpath",loginpage.login_password_input_xpath,loginpassword)  #输入密码
        # code = activebroser.getcodetext(loginpage.login_code_xpath)
        # code = activebroser.getCodeTextByThreeInterfase(loginpage.login_code_xpath)
        # code = input("请输入验证码：")
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

class WebRemoteUphild(object):

    def __init__(self,loginurl,loginaccount,loginpassword,predate=None):
        self.activebrowser = ActiveBrowser()  # 实例化
        self.loginurl = loginurl
        self.loginaccount = loginaccount
        self.loginpassword = loginpassword
        if predate ==None:
            self.predate = str(datetime.datetime.now().strftime('%Y'))
        else:
            self.predate = predate

        # self.select_xie_yi = select_xie_yi
        # self.select_jian_kong_yin_zi_list = select_jian_kong_yin_zi_list

    def login(self):   #登录
        # lpf.loginwithcookiesauto(self.activebrowser)  #登录
        lpf.login(activebroser=self.activebrowser,
                  loginurl=self.loginurl,
                  loginaccount=self.loginaccount,
                  loginpassword=self.loginpassword
            )  #登录
        print("登录完成")
        # self.activebrowser.delayTime(20)  #等待20秒，等待页面刷新出来

    #处理弹框
    def handleAlert(self):
        self.activebrowser.swithToAlert()

    #点击“工作日志”
    def clickGongZuoRiZhi(self):
        #点击“工作日志”
        gongzuotizhi_text = "工作日志"
        self.activebrowser.findEleAndClick(0,"link_text",gongzuotizhi_text)
        print("已经点击【工作日志】")

    #点击提示弹框的确定
    def clickQueDing(self):
        queding_xpath = "/html/body/div[10]/div[2]/table/tbody/tr/td[2]/input"
        #先判断元素是否存在
        is_exist_ele = self.activebrowser.is_exist_ele("xpath",queding_xpath)
        if is_exist_ele:  #如果存在元素，则点击
            self.activebrowser.findEleAndClick(0,"xpath",queding_xpath)
            print("已经点击【确定】")


    def jinRuIframe(self):
        iframe_xpath = "/html/body/div[4]/iframe"
        frame_ele = self.activebrowser.findELe("xpath",iframe_xpath)
        self.activebrowser.swithToIframe(frame_ele)  #切换到串口参数配置所在frame

    #退出iframe
    def quitIframe(self):
        self.activebrowser.quiteCurrentIframe()

    #点击"我的工作日志"
    def clickMyWorkLog(self):
        self.jinRuIframe()
        myworklog_xpath = "/html/body[1]/div[2]/div[2]/table[1]/tbody/tr/td[3]/div/a"
        self.activebrowser.findEleAndClick(0,"xpath",myworklog_xpath)
        print("已经点击【我的工作日志】")
        self.quitIframe()  #退出所有iframe

    #进入周报Iframe二
    def jinRuIframeAboutZhouBaoTwo(self):
        iframe_xpath = "/html/body[1]/iframe"
        frame_ele = self.activebrowser.findELe("xpath",iframe_xpath)
        self.activebrowser.swithToIframe(frame_ele)  #切换到串口参数配置所在frame

    #点击“上周”
    def clickShangZhou(self):
        self.jinRuIframe()
        self.jinRuIframeAboutZhouBaoTwo()
        #点击“上周”
        shangzhou_link_text = "上周"
        self.activebrowser.findEleAndClick(0,"link_text",shangzhou_link_text)
        print("已经点击【上周】")
        self.quitIframe()  # 退出所有iframe


    #进入周报Iframe三
    def jinRuIframeAboutZhouBaoThree(self):
        iframe_xpath = "/html/body/div[3]/iframe[1]"
        frame_ele = self.activebrowser.findELe("xpath",iframe_xpath)
        self.activebrowser.swithToIframe(frame_ele)  #切换到串口参数配置所在frame

    #获取日期，进行日期判断
    def checkData(self):
        self.jinRuIframe()
        self.jinRuIframeAboutZhouBaoTwo()
        self.jinRuIframeAboutZhouBaoThree()

        print("需要获取的信息的年限是【%s】年"% self.predate)
        #获取日期
        date_xpath = "/html/body[1]/div[1]/ul/li[2]/div[2]/span"
        date_text = self.activebrowser.findEleAndReturnText(0,"xpath",date_xpath)
        self.quitIframe()  #退出当前iframe
        print("日期：%s"% date_text)
        date_year = date_text.split("-")[0].strip()
        print("年：%s" % date_year)
        if str(date_year)== str(self.predate):
            return True
        else:
            print("需要获取的信息的年限是【%s】年,而实际为【%s】年，停止获取"% (predate,date_year))
            return False




    #获取一周即一个周页面的内容信息
    def getWeekInfo(self):
        info_list = []
        info_dict = {}
        self.jinRuIframe()
        self.jinRuIframeAboutZhouBaoTwo()
        self.jinRuIframeAboutZhouBaoThree()
        #获取人员
        name_xpath = "/html/body[1]/div[1]/ul/li[1]/div[2]"
        name_text = self.activebrowser.findEleAndReturnText(0,"xpath",name_xpath)
        print("人员：%s" % name_text)
        info_dict["name"] = name_text

        #获取日期
        date_xpath = "/html/body[1]/div[1]/ul/li[2]/div[2]/span"
        date_text = self.activebrowser.findEleAndReturnText(0,"xpath",date_xpath)
        print("日期：%s"% date_text)
        date_year = date_text.split("-")[0].strip()
        print("年：%s" % date_year)
        info_dict["year"] = date_year
        info_dict["date_range"] = date_text

        #获取日记工作情况及存在问题
        riji_table_xpath = "/html/body[1]/div[1]/div[11]/table/tbody"

        riji_tr_ele_list = self.activebrowser.getFatherSonElesList("xpath", riji_table_xpath, "tag_name", "tr")  # 获取tbody选项的所有tr元素
        riji_tr_ele_list_count = len(riji_tr_ele_list)
        print("tr元素列表:")
        print(riji_tr_ele_list_count)

        riji_list = []   #一周中所有天的数据的列表
        for tr_count_one in range(0, riji_tr_ele_list_count, 2):  #步长为2
            one_day_info_dict = {}
            #处理一天的工作情况和存在问题
            #获取一天的工作情况
            gongzuoqingkaung_tr_ele = riji_tr_ele_list[tr_count_one]
            cunzaiwenti_tr_ele = riji_tr_ele_list[tr_count_one+1]
            gongzuoqingkaung_td_ele_list = gongzuoqingkaung_tr_ele.find_elements_by_tag_name("td")
            gongzuoqingkaung_td_ele_list_count = len(gongzuoqingkaung_td_ele_list)
            print("工作情况下td的元素个数：%s" % gongzuoqingkaung_td_ele_list_count)
            #获取周信息
            zhou_ele = gongzuoqingkaung_td_ele_list[0]
            zhou_text = zhou_ele.text
            print("周情况：")
            print(zhou_text)
            one_day_info_dict["date_info"]=zhou_text

            #获取工作情况信息
            gongzuoqingkuang_ele = gongzuoqingkaung_td_ele_list[1]
            gongzuoqingkuang_text = gongzuoqingkuang_ele.text
            print("工作情况：")
            print(gongzuoqingkuang_text)
            #获取工作内容详情
            gongzuoxiangqing_ele = gongzuoqingkaung_td_ele_list[2]
            gongzuoxiangqing_div_ele_list = gongzuoxiangqing_ele.find_elements_by_tag_name("div")
            # 获取任务名和工作详情
            one_day_gongzuoxiangqing_list = []
            for gongzuoxiangqing_div_ele_one in gongzuoxiangqing_div_ele_list:
                one_task_gongzuoxiangqing_dict ={}   #一条div框中记录的工作内容
                gongzuoxiangqing_div_ele_one_html  = gongzuoxiangqing_div_ele_one.get_attribute("innerHTML")  #获取div标签的文本内容
                gongzuoxiangqing_div_ele_one_a_ele_list = gongzuoxiangqing_div_ele_one.find_elements_by_tag_name("a") #获取a链接
                one_day_renwumingcheng_list = []
                for gongzuoxiangqing_div_ele_one_a_ele_one in gongzuoxiangqing_div_ele_one_a_ele_list:
                    renwumingcheng_text = gongzuoxiangqing_div_ele_one_a_ele_one.text
                    print("任务名称：%s" % renwumingcheng_text)
                    one_day_renwumingcheng_list.append(renwumingcheng_text)

                #将任务名称添加到工作情况字典中
                one_task_gongzuoxiangqing_dict["task_name"] = one_day_renwumingcheng_list  #获取工作任务名称

                print("工作详情div信息:%s" % gongzuoxiangqing_div_ele_one_html)
                one_task_gongzuoxiangqing_dict["task_details"] = gongzuoxiangqing_div_ele_one_html
                one_day_gongzuoxiangqing_list.append(one_task_gongzuoxiangqing_dict)  #多条div组成一天的任务
            print("工作详情：")
            print(one_day_gongzuoxiangqing_list)
            one_day_info_dict["work"] = one_day_gongzuoxiangqing_list   #工作内容保存到一天工作内容的字典中

            #获取存在问题信息
            cunzaiwenti_td_ele_list = cunzaiwenti_tr_ele.find_elements_by_tag_name("td")
            #获取存在问题内容
            cunzaiwenti_ele = cunzaiwenti_td_ele_list[0]
            cunzaiwenti_text = cunzaiwenti_ele.text
            print("存在问题：%s"%cunzaiwenti_text)
            #获取问题详情信息
            wentixiangqing_ele = cunzaiwenti_td_ele_list[1]
            wentixiangqing_div_ele_list = wentixiangqing_ele.find_elements_by_tag_name("div")
            one_day_wentixiangqing_list = []
            for wentixiangqing_div_ele_one in wentixiangqing_div_ele_list:
                one_task_wentixiangqing_dict ={}   #一条div框中记录的工作内容
                wentixiangqingxiangqing_div_ele_one_html  = wentixiangqing_div_ele_one.get_attribute("innerHTML")  #获取div标签的文本内容
                one_task_wentixiangqing_dict["question_details"] = wentixiangqingxiangqing_div_ele_one_html  #保存问题详情
                one_day_wentixiangqing_list.append(one_task_wentixiangqing_dict)  #多条div组成一天的问题

            print("问题详情：")
            print(one_day_wentixiangqing_list)
            one_day_info_dict["problem"] = one_day_wentixiangqing_list  # 问题保存到一天工作内容的字典中

            print("一天内容的数据：")
            print(one_day_info_dict)
            riji_list.append(one_day_info_dict)
        print("日记列表：")
        print(riji_list)
        info_dict["riji_datails"] = riji_list  #日记写入字典


        #周记统计信息
        zhouji_xpath = "/html/body[1]/div[1]/div[13]/div"
        zhouji_ele = self.activebrowser.findELe("xpath",zhouji_xpath)
        zhouji_html = zhouji_ele.get_attribute("innerHTML")  # 获取div标签的文本内容
        print("周记内容：")
        print(zhouji_html)
        info_dict["zhouji_html"] = zhouji_html

        self.quitIframe()  # 退出当前iframe
        print("一周工作信息统计：")
        print(info_dict)
        import json
        print(json.dumps(info_dict, indent=1))  #字典树形结构输出
        return info_dict


    def closeWeb(self):
        self.activebrowser.closeBrowse()
    @async_call
    def run(self):
        #登录
        self.login()
        #点击工作日志
        self.clickGongZuoRiZhi()
        # 点击提示弹框的确定
        self.clickQueDing()
        # 点击"我的工作日志"
        self.clickMyWorkLog()
        #点击上周
        self.clickShangZhou()
        is_continue = self.checkData()
        while_num = 1
        while is_continue:  #如果不等于预设年限，则
            # 获取一周即一个周页面的内容信息
            one_week_info_dict = self.getWeekInfo()
            # 点击上周
            self.clickShangZhou()
            is_continue = self.checkData()
            print("获取数据【%s】次,获取的数据为：【%s】"% (str(while_num),str(one_week_info_dict)))

            people_name = one_week_info_dict['name']
            rdm_year = one_week_info_dict['year']
            rdm_data_range = one_week_info_dict['date_range']
            riji_datails_list = one_week_info_dict['riji_datails']

            for riji_datails_dict in riji_datails_list:
                day_date = riji_datails_dict['date_info']
                is_week = False
                day_work_list =  riji_datails_dict['work']
                for day_work_dict in day_work_list:
                    day_task_name = day_work_dict['task_name']
                    day_task_desc = day_work_dict['task_details']
                    #问题
                    problem_list = riji_datails_dict['problem']
                    for problem_dict in problem_list:
                        day_task_quse =problem_dict['question_details']

                        from reportdatas.models import RdmStatic
                        fil_list = RdmStatic.objects.filter(people_name=people_name).\
                            filter(rdm_year=rdm_year).\
                            filter(rdm_data_range=rdm_data_range).\
                            filter(day_date=day_date)
                        fil_list_count = fil_list.count()
                        if fil_list_count == 0: #说明没有数据要保存
                            new_rdmstatic = RdmStatic()
                            new_rdmstatic.people_name = people_name
                            new_rdmstatic.rdm_year = rdm_year
                            new_rdmstatic.rdm_data_range = rdm_data_range
                            new_rdmstatic.day_date = day_date
                            new_rdmstatic.is_week = is_week
                            new_rdmstatic.day_task_name = day_task_name
                            new_rdmstatic.day_task_desc = day_task_desc
                            new_rdmstatic.day_task_quse = day_task_quse
                            new_rdmstatic.save()   #保存日记

            #保存完日志之后，保存周记
            week_task_deck = one_week_info_dict['zhouji_html']  #周记内容
            from reportdatas.models import RdmStatic
            fil_list = RdmStatic.objects.filter(people_name=people_name). \
                filter(rdm_year=rdm_year). \
                filter(rdm_data_range=rdm_data_range). \
                filter(is_week=True)
            fil_list_count = fil_list.count()
            if fil_list_count == 0:  # 说明没有数据则说明没有周记，保存周记
                new_rdmstatic = RdmStatic()
                new_rdmstatic.people_name = people_name
                new_rdmstatic.rdm_year = rdm_year
                new_rdmstatic.rdm_data_range = rdm_data_range
                new_rdmstatic.is_week = True
                new_rdmstatic.week_task_deck = week_task_deck
                new_rdmstatic.save()  # 保存周记

            print("一页RDM周记录入完成")
            while_num = while_num+1





if __name__ == '__main__':
    loginurl="http://192.168.8.98:2000/main.do"
    loginaccount="相开征"
    loginpassword="xkz190903"
    predate = "2020"

    wc = WebRemoteUphild(loginurl=loginurl,loginaccount=loginaccount,loginpassword=loginpassword,predate=predate)
    wc.run()





