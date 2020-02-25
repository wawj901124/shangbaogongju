
class SearchSelectTapSelectOption(object):
    def searchselecttapselectoption(self,activebrowser,searchid):
        selectoptiontext_list_all = []
        from testdatas.models import SearchSelectTapSelectOption
        searchselecttapselectoptions = SearchSelectTapSelectOption.objects.filter(searchandcheck_id=int(searchid))
        if str(searchselecttapselectoptions) != "<QuerySet []>":
            activebrowser.outPutMyLog("找到依赖数据")
            for searchselecttapselectoption in searchselecttapselectoptions:
                selectoptiontext_list = []
                #点击select选项框
                activebrowser.findEleAndClick(0,searchselecttapselectoption.select_ele_find,
                                                 searchselecttapselectoption.select_ele_find_value)
                #点击选项
                activebrowser.findEleAndClick(0,searchselecttapselectoption.select_option_ele_find,
                                                 searchselecttapselectoption.select_option_ele_find_value)

                #获取选项的文本信息
                select_ele_text_value = activebrowser.findEleAndReturnValueNum(0,searchselecttapselectoption.select_ele_find,
                                                 searchselecttapselectoption.select_ele_find_value,"value")
                activebrowser.outPutMyLog("获取到的文本信息为：%s" % select_ele_text_value)
                #添加选项文本信息到数组
                selectoptiontext_list.append(select_ele_text_value)

                #添加列数到数组
                selectoptiontext_list.append(searchselecttapselectoption.search_result_colnum)
                #添加数组到大数组
                selectoptiontext_list_all.append(selectoptiontext_list)
        else:
            activebrowser.outPutErrorMyLog("没有找到依赖id[%s]对应的数据！" % searchid)

        return selectoptiontext_list_all



searchselecttapselectoption = SearchSelectTapSelectOption()