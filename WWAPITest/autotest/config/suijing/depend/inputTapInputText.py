from WWTest.util.getTimeStr import GetTimeStr
class InputTapInputText(object):
    def inputtapinputtext(self,activebrowser,newaddid):
        timestr = GetTimeStr().getTimeStr()
        inputtext_list = []
        from testdatas.models import InputTapInputText
        inputtapinputtexts = InputTapInputText.objects.filter(newaddandcheck_id=int(newaddid))
        if str(inputtapinputtexts) != "<QuerySet []>":
            activebrowser.outPutMyLog("找到依赖数据")
            for inputtapinputtext in inputtapinputtexts:
                if inputtapinputtext.is_with_time:
                    inputtextwithtimestr = "%s%s"%(inputtapinputtext.input_text,timestr)
                else:
                    inputtextwithtimestr = inputtapinputtext.input_text

                activebrowser.findEleAndInputNum(0,inputtapinputtext.input_ele_find,
                                                 inputtapinputtext.input_ele_find_value,inputtextwithtimestr)
                if inputtapinputtext.is_check:
                    inputtext_list.append(inputtextwithtimestr)
        else:
            activebrowser.outPutErrorMyLog("没有找到依赖id[%s]对应的数据！" % newaddid)

        return inputtext_list



inputtapinputtext = InputTapInputText()