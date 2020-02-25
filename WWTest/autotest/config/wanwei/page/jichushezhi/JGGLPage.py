from WWTest.base.activeBrowser import ActiveBrowser
from WWTest.autotest.config.wanwei.globalconfig.globalConfig import GlobalConfig,gc
from WWTest.autotest.config.wanwei.depend.clickAndBackDepend import clickandbackdepend
from WWTest.util.getTimeStr import GetTimeStr
from WWTest.autotest.config.wanwei.page.loginPage import lpf

class JiGouGuanliPage(object):
    if gc.ISONLINE:
        pageurl = "%s/#/systemBase/baseSet/organizationInfo"%gc.ONLINE_WEB_YUMING

    else:
        pageurl= "%s/#/systemBase/baseSet/organizationInfo"%gc.TEST_WEB_YUMING

    add_button_xpath = "/html/body/div/div/div/div[2]/div/div[1]/div[2]/div[2]/div[1]/div[1]/button"
    page_number_xpath = "/html/body/div/div/div/div[2]/div/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/ul"

    result_table_xpath = "/html/body/div/div/div/div[2]/div/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[3]/table/tbody"

jigouguanlipage = JiGouGuanliPage()

class JiGouGuanliPageFunction(object):

    def clickAdd(self,activebrowser):
        activebrowser = activebrowser
        # activebrowser = ActiveBrowser()
        activebrowser.findEleAndClick(0,"xpath",jigouguanlipage.add_button_xpath)

    def getLastPage(self,activebrowser):
        activebrowser = activebrowser
        son_ele_s = activebrowser.getFatherSonElesList("xpath",jigouguanlipage.page_number_xpath,"tag_name","li")
        son_count = len(son_ele_s)
        son_last_xpath = "%s/%s[%s]" % (jigouguanlipage.page_number_xpath,"li",son_count)
        activebrowser.findEleAndClick(0,"xpath",son_last_xpath)


jigouguanlipagefunction = JiGouGuanliPageFunction()


class JiGouGunaLiAddPage(object):
    jigoubianma_input_xpath = "/html/body/div[1]/div/div/div[2]/div/div[1]/div[2]/div[2]/div[2]/div/div[2]/div/form/div[1]/div/div/input"
    jigoubianma_input_tip_xpath = "/html/body/div[1]/div/div/div[2]/div/div[1]/div[2]/div[2]/div[2]/div/div[2]/div/form/div[1]/div/div[2]"
    jigoubianma_input_tip_text = u"请输入内容"

    jigoumingcheng_input_xpath = "/html/body/div[1]/div/div/div[2]/div/div[1]/div[2]/div[2]/div[2]/div/div[2]/div/form/div[2]/div/div[1]/input"
    jigoumingcheng_input_tip_xpath = "/html/body/div[1]/div/div/div[2]/div/div[1]/div[2]/div[2]/div[2]/div/div[2]/div/form/div[2]/div/div[2]"
    jigoumingcheng_input_tip_text = u"请输入内容"

    beizhu_input_xpath = "/html/body/div[1]/div/div/div[2]/div/div[1]/div[2]/div[2]/div[2]/div/div[2]/div/form/div[3]/div/div/textarea"
    confirm_button_xpath = "/html/body/div[1]/div/div/div[2]/div/div[1]/div[2]/div[2]/div[2]/div/div[3]/span/button[1]"
    cancel_button_xpath = "/html/body/div[1]/div/div/div[2]/div/div[1]/div[2]/div[2]/div[2]/div/div[3]/span/button[2]"

jigougunaliaddpage = JiGouGunaLiAddPage()



class JiGouGunaLiAddPageFunction(object):

    def add_JiGOu(self,activebrowser,is_cancel,jigoubianma_input_text=None,jigoumingcheng_input_text=None,
                  beizhu_input_text=None):
        activebrowser = activebrowser
        # activebrowser = ActiveBrowser()
        if jigoubianma_input_text == None:
            activebrowser.findEleAndInputNum(0,"xpath",jigougunaliaddpage.jigoubianma_input_xpath,"")
        else:
            activebrowser.findEleAndInputNum(0, "xpath", jigougunaliaddpage.jigoubianma_input_xpath,
                                             jigoubianma_input_text)

        if jigoumingcheng_input_text == None:
            activebrowser.findEleAndInputNum(0,"xpath",jigougunaliaddpage.jigoumingcheng_input_xpath,"")
        else:
            activebrowser.findEleAndInputNum(0, "xpath", jigougunaliaddpage.jigoumingcheng_input_xpath,
                                             jigoumingcheng_input_text)

        if beizhu_input_text == None:
            activebrowser.findEleAndInputNum(0,"xpath",jigougunaliaddpage.beizhu_input_xpath,"")
        else:
            activebrowser.findEleAndInputNum(0, "xpath", jigougunaliaddpage.beizhu_input_xpath,
                                             beizhu_input_text)

        if is_cancel:
            activebrowser.findEleAndClick(0,"xpath",jigougunaliaddpage.cancel_button_xpath)
            activebrowser.delayTime(3)
        else:
            activebrowser.findEleAndClick(0,"xpath",jigougunaliaddpage.confirm_button_xpath)
            activebrowser.delayTime(3)
            jigouguanlipagefunction.getLastPage(activebrowser)
            activebrowser.checktable(jigouguanlipage.result_table_xpath,jigoubianma_input_text,1)
            activebrowser.checktable(jigouguanlipage.result_table_xpath, jigoumingcheng_input_text, 2)
            activebrowser.checktable(jigouguanlipage.result_table_xpath, beizhu_input_text, 4)


jigougunaliaddpagefunction = JiGouGunaLiAddPageFunction()



if __name__ == "__main__":
    activebrowser = ActiveBrowser()
    # lpf.loginwithcookies(activebrowser)
    # activebrowser.getUrl(jigouguanlipage.pageurl)
    lpf.login(activebrowser)
    activebrowser.delayTime(10)
    clickandbackdepend.clickandbackdepend(activebrowser,10)
    timestr = GetTimeStr().getTimeStr()
    jigougunaliaddpagefunction.add_JiGOu(activebrowser,False,timestr,timestr,timestr)





