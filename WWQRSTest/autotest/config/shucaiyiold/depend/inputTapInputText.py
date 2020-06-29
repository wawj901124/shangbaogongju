from WWTest.util.getTimeStr import GetTimeStr
from WWTest.util.autoMakeString import AutoMakeString,automakestring
class InputTapInputText(object):
    def inputtapinputtext(self,activebrowser,newaddid):
        timestr = GetTimeStr().getTimeStr()
        inputtext_list = []
        from testdatas.models import InputTapInputText
        inputtapinputtexts = InputTapInputText.objects.filter(newaddandcheck_id=int(newaddid))
        if str(inputtapinputtexts) != "<QuerySet []>":
            activebrowser.outPutMyLog(u"找到依赖数据")
            for inputtapinputtext in inputtapinputtexts:
                if inputtapinputtext.is_auto_input:
                    if inputtapinputtext.auto_input_type == '1' :
                        inputtextwithtimestr = automakestring.getDigits(inputtapinputtext.auto_input_long)
                    elif inputtapinputtext.auto_input_type == '2' :
                        inputtextwithtimestr = automakestring.getAsciiLowercase(inputtapinputtext.auto_input_long)
                    elif inputtapinputtext.auto_input_type == '3' :
                        inputtextwithtimestr = automakestring.getLettersAndDigits(inputtapinputtext.auto_input_long)
                    elif inputtapinputtext.auto_input_type == '4' :
                        inputtextwithtimestr = automakestring.getLetterAndDigitsAndSymbols(inputtapinputtext.auto_input_long)
                    elif inputtapinputtext.auto_input_type == '5' :
                        inputtextwithtimestr = automakestring.getLetterAndDigitsAndSymbolsAndWhitespace(inputtapinputtext.auto_input_long)
                    elif inputtapinputtext.auto_input_type == '6' :
                        inputtextwithtimestr = automakestring.getUnicodeZh(inputtapinputtext.auto_input_long)
                    else:
                        inputtextwithtimestr = u"自动输入字符的类型不正确，请输入正确的自动输入字符的类型"
                        activebrowser.outPutErrorMyLog(u"自动输入字符的类型不正确，请输入正确的自动输入字符的类型")
                else:
                    if inputtapinputtext.is_with_time:
                        inputtextwithtimestr = "%s%s"%(inputtapinputtext.input_text,timestr)
                    else:
                        inputtextwithtimestr = inputtapinputtext.input_text

                if inputtapinputtext.input_ele_find!=None and inputtapinputtext.input_ele_find_value != None:
                    activebrowser.findEleAndInputNum(0,inputtapinputtext.input_ele_find,
                                                     inputtapinputtext.input_ele_find_value,inputtextwithtimestr)
                if inputtapinputtext.is_check:
                    inputtext_list.append(inputtextwithtimestr)
        else:
            activebrowser.outPutErrorMyLog(u"没有找到依赖id[%s]对应的数据！" % newaddid)

        return inputtext_list



inputtapinputtext = InputTapInputText()