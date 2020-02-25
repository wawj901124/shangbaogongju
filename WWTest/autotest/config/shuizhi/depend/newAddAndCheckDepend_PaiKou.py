from depend.seleniumdepend.clickAndBackDepend import clickandbackdepend
from depend.seleniumdepend.inputTapInputText import inputtapinputtext
from depend.seleniumdepend.inputTapInputFile import inputtapinputfile
from depend.seleniumdepend.selectTapSelectOption import selecttapselectoption
from depend.seleniumdepend.radioAndReelectionLabel import radioandreelectionlabel
from depend.seleniumdepend.inputTapInputDateTime import inputtapinputdatetime

class NewAddAndCheckDepend(object):
    def newaddandcheckdepend(self,activebrowser,dependid,MN_devices_number):
        activebrowser.outPutMyLog("依赖ID（dependid）为:%s" % dependid)
        inputtext_list = []
        if dependid != None:
            activebrowser.outPutMyLog("执行依赖")
            from testdatas.models import NewAddAndCheck
            newaddandchecktestcases = NewAddAndCheck.objects.filter(id=int(dependid))
            print("newaddandchecktestcases:%s" % newaddandchecktestcases)
            if str(newaddandchecktestcases) != "<QuerySet []>":
                activebrowser.outPutMyLog("找到依赖数据")
                for newaddandchecktestcase in  newaddandchecktestcases:
                    depend = newaddandchecktestcase.depend_new_add_and_check_case_id
                    activebrowser.outPutMyLog("depend:%s" % depend)
                    # if depend != None:
                    #     activebrowser.outPutMyLog("进入下一层依赖")
                    #     self.newaddandcheckdepend(activebrowser,depend)

                    activebrowser.driver.refresh() #刷新页面
                    activebrowser.delayTime(3)  #等待3秒
                    #执行正常步骤
                    # 如果有依赖ID，则执行依赖函数，达到执行当前用例的前提条件
                    if newaddandchecktestcase.depend_click_case_id != None:
                        clickandbackdepend.clickandbackdepend(activebrowser, newaddandchecktestcase.depend_click_case_id)

                    # 文本输入框添加内容
                    inputtext_list = inputtapinputtext.inputtapinputtext(activebrowser, newaddandchecktestcase.id )

                    # 文件输入框添加内容
                    inputtapinputfile.inputtapinputfile(activebrowser, newaddandchecktestcase.id)

                    # 选项框添加内容
                    selecttapselectoption.selecttapselectoption(activebrowser, newaddandchecktestcase.id)

                    # 单选项与复选项添加内容
                    radioandreelectionlabel.radioandreelectionlabel(activebrowser, newaddandchecktestcase.id)

                    # 日期添加内容
                    inputtapinputdatetime.inputtapinputdatetime(activebrowser, newaddandchecktestcase.id)

                    #主机MN号重新选择开始
                    activebrowser.findEleAndClick(0,"xpath",
                                                       "/html/body/div[1]/div/div/div[2]/div/div[1]/div[2]/div[2]/div[2]/div/div[2]/div/form/div[8]/div/div/div[1]/input")
                    #ul路径（选项父路径）
                    ul_xpath = "/html/body/div[1]/div/div/div[2]/div/div[1]/div[2]/div[2]/div[2]/div/div[2]/div/form/div[8]/div/div/div[2]/div[1]/div[1]/ul"
                    #获取ul中所有的li元素
                    son_ele_s = activebrowser.getFatherSonElesList("xpath", ul_xpath, "tag_name", "li")

                    for son_ele in son_ele_s:
                        li_text = son_ele.text
                        if MN_devices_number == li_text:
                            son_ele.click()
                            print("点选的设备：%s" % li_text)
                            activebrowser.delayTime(3)
                            break
                    # 主机MN号重新选择完成

                    #点击确定按钮
                    activebrowser.findEleAndClick(0, newaddandchecktestcase.confirm_ele_find, newaddandchecktestcase.confirm_ele_find_value)

                    inputtext_list_len = len(inputtext_list)
                    if inputtext_list_len != 0:
                        for i in range(0,inputtext_list_len):
                            reault_check = activebrowser.\
                                findEleAndCheckTableWithColnumCounts(0,newaddandchecktestcase.result_table_ele_find,
                                                                     newaddandchecktestcase.result_table_ele_find_value,inputtext_list[i],
                                                                     newaddandchecktestcase.table_colnum_counts)
                            assert  reault_check
                    else:
                        activebrowser.outPutErrorMyLog("【异常提示】：本用例为验证添加成功后，"
                                                            "是否存在添加的数据，但实际没有添加要输入的测试数据"
                                                            "请检查用例测试数据，将测试数据补充完整！")
                        assert  False




            else:
                activebrowser.outPutErrorMyLog("没有找到依赖id[%s]对应的数据！" % dependid)
        else:
            activebrowser.outPutMyLog("依赖ID为None，不执行依赖！")

        return inputtext_list

newaddandcheckdepend = NewAddAndCheckDepend()

