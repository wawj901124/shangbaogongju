
class SearchInputTapInputText(object):
    def searchinputtapinputtext(self,activebrowser,searchid):
        inputtext_list_all = []
        from testdatas.models import SearchInputTapInputText
        searchinputtapinputtexts = SearchInputTapInputText.objects.filter(searchandcheck_id=int(searchid))
        if str(searchinputtapinputtexts) != "<QuerySet []>":
            activebrowser.outPutMyLog("找到依赖数据")
            for searchinputtapinputtext in searchinputtapinputtexts:
                inputtext_list = []
                activebrowser.findEleAndInputNum(0,searchinputtapinputtext.input_ele_find,
                                                 searchinputtapinputtext.input_ele_find_value,searchinputtapinputtext.input_text)
                input_ele_text_value = activebrowser.findEleAndReturnValueNum(0,searchinputtapinputtext.input_ele_find,
                                                 searchinputtapinputtext.input_ele_find_value,"value")
                inputtext_list.append(input_ele_text_value)

                inputtext_list.append(searchinputtapinputtext.search_result_colnum)
                inputtext_list_all.append(inputtext_list)
        else:
            activebrowser.outPutErrorMyLog("没有找到依赖id[%s]对应的数据！" % searchid)

        return inputtext_list_all



searchinputtapinputtext = SearchInputTapInputText()