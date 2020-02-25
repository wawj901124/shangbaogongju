class SelectTapSelectOption(object):
    def selecttapselectoption(self,activebrowser,newaddid):
        from testdatas.models import SelectTapSelectOption

        selecttapselectoptions = SelectTapSelectOption.objects.filter(newaddandcheck_id=int(newaddid))
        if str(selecttapselectoptions) != "<QuerySet []>":
            activebrowser.outPutMyLog("找到依赖数据")
            for selecttapselectoption in selecttapselectoptions:
                # inputtextwithtimestr = "%s%s"%(inputtapinputtext.input_text,timestr)
                # activebrowser.delayTime(30000)
                activebrowser.findEleAndClick(0,selecttapselectoption.select_ele_find,
                                              selecttapselectoption.select_ele_find_value)
                activebrowser.findEleAndClick(0,selecttapselectoption.select_option_ele_find,
                                              selecttapselectoption.select_option_ele_find_value)

                if selecttapselectoption.is_multiple_choices:   #如果是多选，点击空白处
                    activebrowser.mockClickBlank(0,0)
                # activebrowser.delayTime(30000)

        else:
            activebrowser.outPutErrorMyLog("没有找到依赖id[%s]对应的数据！" % newaddid)


selecttapselectoption = SelectTapSelectOption()