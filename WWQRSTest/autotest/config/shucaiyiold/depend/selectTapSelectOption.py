class SelectTapSelectOption(object):
    def selecttapselectoption(self,activebrowser,newaddid):
        from testdatas.models import SelectTapSelectOption

        selecttapselectoptions = SelectTapSelectOption.objects.filter(newaddandcheck_id=int(newaddid))
        if str(selecttapselectoptions) != "<QuerySet []>":
            activebrowser.outPutMyLog("找到依赖数据")
            for selecttapselectoption in selecttapselectoptions:
                # inputtextwithtimestr = "%s%s"%(inputtapinputtext.input_text,timestr)
                activebrowser.findEleAndClick(0,selecttapselectoption.select_ele_find,
                                              selecttapselectoption.select_ele_find_value)
                activebrowser.findEleAndClick(0,selecttapselectoption.select_option_ele_find,
                                              selecttapselectoption.select_option_ele_find_value)

        else:
            activebrowser.outPutErrorMyLog("没有找到依赖id[%s]对应的数据！" % newaddid)


selecttapselectoption = SelectTapSelectOption()