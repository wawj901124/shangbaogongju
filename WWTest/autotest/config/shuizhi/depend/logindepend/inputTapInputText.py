from WWTest.util.getTimeStr import GetTimeStr

from WWTest.util.autoMakeString import AutoMakeString,automakestring
from WWTest.util.autoMakePhoneNumber import AutoMakePhoneNumber,automakephonenumber
from WWTest.util.autoMakeIDNumber import AutoMakeIDNumber,automakeidnumber


class InputTapInputText(object):
    def inputtapinputtext(self,activebrowser,loginid):
        timestr = GetTimeStr().getTimeStr()
        inputtext_list = []
        from testdatas.models import InputTapInputText
        inputtapinputtexts = InputTapInputText.objects.filter(loginandcheck_id=int(loginid))
        if str(inputtapinputtexts) != "<QuerySet []>":
            activebrowser.outPutMyLog(u"找到依赖数据")
            for inputtapinputtext in inputtapinputtexts:
                if inputtapinputtext.is_auto_input:
                    if inputtapinputtext.auto_input_type == '1' :   #自动生成0~9数字字符串
                        inputtextwithtimestr = automakestring.getDigits(inputtapinputtext.auto_input_long)
                    elif inputtapinputtext.auto_input_type == '2' :  #小写字母
                        inputtextwithtimestr = automakestring.getAsciiLowercase(inputtapinputtext.auto_input_long)
                    elif inputtapinputtext.auto_input_type == '3' :  #字母（大写）
                        inputtextwithtimestr = automakestring.getAsciiUppercase(inputtapinputtext.auto_input_long)
                    elif inputtapinputtext.auto_input_type == '4' :  #特殊符号
                        inputtextwithtimestr = automakestring.getSymbols(inputtapinputtext.auto_input_long)
                    elif inputtapinputtext.auto_input_type == '5' :  #数字和字母（小写）
                        inputtextwithtimestr = automakestring.getLowercaseAndDigits(inputtapinputtext.auto_input_long)
                    elif inputtapinputtext.auto_input_type == '6' :  #数字和字母（大写）
                        inputtextwithtimestr = automakestring.getUppercaseAndDigits(inputtapinputtext.auto_input_long)
                    elif inputtapinputtext.auto_input_type == '7' :  #字母（大小写）
                        inputtextwithtimestr = automakestring.getAsciiLetters(inputtapinputtext.auto_input_long)
                    elif inputtapinputtext.auto_input_type == '8' :  #数字和字母（大小写）
                        inputtextwithtimestr = automakestring.getLettersAndDigits(inputtapinputtext.auto_input_long)
                    elif inputtapinputtext.auto_input_type == '9' :  #数字和字母和特殊符号
                        inputtextwithtimestr = automakestring.getLetterAndDigitsAndSymbols(inputtapinputtext.auto_input_long)
                    elif inputtapinputtext.auto_input_type == '10' :  #数字和字母和特殊符号和空白字符
                        inputtextwithtimestr = automakestring.getLetterAndDigitsAndSymbolsAndWhitespace(inputtapinputtext.auto_input_long)
                    elif inputtapinputtext.auto_input_type == '11' : #汉字
                        inputtextwithtimestr = automakestring.getUnicodeZh(inputtapinputtext.auto_input_long)
                    elif inputtapinputtext.auto_input_type == '12':  #手机号
                        inputtextwithtimestr = automakephonenumber.creat_phone()
                    elif inputtapinputtext.auto_input_type == '13':  #身份证号
                        inputtextwithtimestr = automakeidnumber.create_IDcard()

                    else:
                        inputtextwithtimestr = u"自动输入字符的类型不正确，请输入正确的自动输入字符的类型"
                        activebrowser.outPutErrorMyLog(u"自动输入字符的类型不正确，请输入正确的自动输入字符的类型")
                else:
                    if inputtapinputtext.is_with_time:
                        inputtextwithtimestr = "%s%s"%(inputtapinputtext.input_text,timestr)
                    else:
                        inputtextwithtimestr = inputtapinputtext.input_text

                if inputtapinputtext.input_ele_find !=None and inputtapinputtext.input_ele_find_value != None:
                    activebrowser.findEleAndInputNum(0,inputtapinputtext.input_ele_find,
                                                     inputtapinputtext.input_ele_find_value,inputtextwithtimestr)

                #如果点击清除图片，则点击清除图标
                if inputtapinputtext.is_click_clear_icon:
                    if inputtapinputtext.clear_icon_find !=None and inputtapinputtext.clear_icon_find_value != None:
                        activebrowser.findEleAndClick(0, inputtapinputtext.clear_icon_find,
                                                      inputtapinputtext.clear_icon_find_value)
                    else:
                        activebrowser.outPutErrorMyLog("问题描述：元素查找风格和查找风格的确切值有至少一项未填写，请补充填写相应的数据！")
                        assert False


                if inputtapinputtext.is_check:
                    inputtext_list.append(inputtextwithtimestr)
        else:
            activebrowser.outPutErrorMyLog(u"没有找到依赖id[%s]对应的数据！" % loginid)

        return inputtext_list



inputtapinputtext = InputTapInputText()