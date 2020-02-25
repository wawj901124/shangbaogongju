from depend.seleniumdepend.clickAndBackDepend import clickandbackdepend
from depend.seleniumdepend.inputTapInputText import inputtapinputtext
from depend.seleniumdepend.inputTapInputFile import inputtapinputfile
from depend.seleniumdepend.selectTapSelectOption import selecttapselectoption
from depend.seleniumdepend.radioAndReelectionLabel import radioandreelectionlabel
from depend.seleniumdepend.inputTapInputDateTime import inputtapinputdatetime

class NewAddAndCheckDepend(object):
    def newaddandcheckdepend(self,activebrowser,dependid):
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
                    if depend != None:
                        activebrowser.outPutMyLog("进入下一层依赖")
                        self.newaddandcheckdepend(activebrowser,depend)

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

                    #

                    #点击确定按钮
                    activebrowser.findEleAndClick(0, newaddandchecktestcase.confirm_ele_find, newaddandchecktestcase.confirm_ele_find_value)


            else:
                activebrowser.outPutErrorMyLog("没有找到依赖id[%s]对应的数据！" % dependid)
        else:
            activebrowser.outPutMyLog("依赖ID为None，不执行依赖！")

        return inputtext_list

newaddandcheckdepend = NewAddAndCheckDepend()

