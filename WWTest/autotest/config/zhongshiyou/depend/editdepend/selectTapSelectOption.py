class SelectTapSelectOption(object):
    def selecttapselectoption(self,activebrowser,editid):
        from testdatas.models import SelectTapSelectOption

        selecttapselectoptions = SelectTapSelectOption.objects.filter(editandcheck_id=int(editid))

        if str(selecttapselectoptions) != "<QuerySet []>":
            activebrowser.outPutMyLog("找到依赖数据")
            for selecttapselectoption in selecttapselectoptions:
                # inputtextwithtimestr = "%s%s"%(inputtapinputtext.input_text,timestr)
                # activebrowser.delayTime(30000)
                if selecttapselectoption.select_ele_find !=None and selecttapselectoption.select_ele_find_value != None:
                    activebrowser.findEleAndClick(0,selecttapselectoption.select_ele_find,
                                                  selecttapselectoption.select_ele_find_value)
                if selecttapselectoption.select_option_ele_find != None and selecttapselectoption.select_option_ele_find_value != None:
                    activebrowser.findEleAndClick(0,selecttapselectoption.select_option_ele_find,
                                                  selecttapselectoption.select_option_ele_find_value)
                # activebrowser.delayTime(30000)

                #如果点击清除图片，则点击清除图标
                if selecttapselectoption.is_click_clear_icon:
                    if selecttapselectoption.clear_icon_find !=None and selecttapselectoption.clear_icon_find_value != None:
                        activebrowser.findEleAndClick(0, selecttapselectoption.clear_icon_find,
                                                      selecttapselectoption.clear_icon_find_value)
                    else:
                        activebrowser.outPutErrorMyLog("问题描述：元素查找风格和查找风格的确切值有至少一项未填写，请补充填写相应的数据！")
                        assert False

        else:
            activebrowser.outPutErrorMyLog("没有找到依赖id[%s]对应的数据！" % editid)


selecttapselectoption = SelectTapSelectOption()