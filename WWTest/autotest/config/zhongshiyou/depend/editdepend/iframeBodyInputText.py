from WWTest.util.getTimeStr import GetTimeStr

from WWTest.util.autoMakeString import AutoMakeString,automakestring
from WWTest.util.autoMakePhoneNumber import AutoMakePhoneNumber,automakephonenumber
from WWTest.util.autoMakeIDNumber import AutoMakeIDNumber,automakeidnumber


class IframeBodyInputText(object):
    def iframebodyinputtext(self,activebrowser,editid):
        timestr = GetTimeStr().getTimeStr()
        inputtext_list = []
        from testdatas.models import IframeBodyInputText
        iframebodyinputtexts = IframeBodyInputText.objects.filter(editandcheck_id=int(editid))
        if str(iframebodyinputtexts) != "<QuerySet []>":
            activebrowser.outPutMyLog(u"找到依赖数据")
            for iframebodyinputtext in iframebodyinputtexts:

                #查找富文本iframe框
                if iframebodyinputtext.iframe_ele_find != None and iframebodyinputtext.iframe_ele_find_value != None:
                    iframe_ele = activebrowser.findELe(iframebodyinputtext.iframe_ele_find, iframebodyinputtext.iframe_ele_find_value)
                    activebrowser.swithToIframe(iframe_ele)

                    #iframe body 输入内容
                    if iframebodyinputtext.is_auto_input:
                        if iframebodyinputtext.auto_input_type == '1' :   #自动生成0~9数字字符串
                            inputtextwithtimestr = automakestring.getDigits(iframebodyinputtext.auto_input_long)
                        elif iframebodyinputtext.auto_input_type == '2' :  #小写字母
                            inputtextwithtimestr = automakestring.getAsciiLowercase(iframebodyinputtext.auto_input_long)
                        elif iframebodyinputtext.auto_input_type == '3' :  #字母（大写）
                            inputtextwithtimestr = automakestring.getAsciiUppercase(iframebodyinputtext.auto_input_long)
                        elif iframebodyinputtext.auto_input_type == '4' :  #特殊符号
                            inputtextwithtimestr = automakestring.getSymbols(iframebodyinputtext.auto_input_long)
                        elif iframebodyinputtext.auto_input_type == '5' :  #数字和字母（小写）
                            inputtextwithtimestr = automakestring.getLowercaseAndDigits(iframebodyinputtext.auto_input_long)
                        elif iframebodyinputtext.auto_input_type == '6' :  #数字和字母（大写）
                            inputtextwithtimestr = automakestring.getUppercaseAndDigits(iframebodyinputtext.auto_input_long)
                        elif iframebodyinputtext.auto_input_type == '7' :  #字母（大小写）
                            inputtextwithtimestr = automakestring.getAsciiLetters(iframebodyinputtext.auto_input_long)
                        elif iframebodyinputtext.auto_input_type == '8' :  #数字和字母（大小写）
                            inputtextwithtimestr = automakestring.getLettersAndDigits(iframebodyinputtext.auto_input_long)
                        elif iframebodyinputtext.auto_input_type == '9' :  #数字和字母和特殊符号
                            inputtextwithtimestr = automakestring.getLetterAndDigitsAndSymbols(iframebodyinputtext.auto_input_long)
                        elif iframebodyinputtext.auto_input_type == '10' :  #数字和字母和特殊符号和空白字符
                            inputtextwithtimestr = automakestring.getLetterAndDigitsAndSymbolsAndWhitespace(iframebodyinputtext.auto_input_long)
                        elif iframebodyinputtext.auto_input_type == '11' : #汉字
                            inputtextwithtimestr = automakestring.getUnicodeZh(iframebodyinputtext.auto_input_long)
                        elif iframebodyinputtext.auto_input_type == '12':  #手机号
                            inputtextwithtimestr = automakephonenumber.creat_phone()
                        elif iframebodyinputtext.auto_input_type == '13':  #身份证号
                            inputtextwithtimestr = automakeidnumber.create_IDcard()

                        else:
                            inputtextwithtimestr = u"自动输入字符的类型不正确，请输入正确的自动输入字符的类型"
                            activebrowser.outPutErrorMyLog(u"自动输入字符的类型不正确，请输入正确的自动输入字符的类型")
                    else:
                        if iframebodyinputtext.is_with_time:
                            inputtextwithtimestr = "%s%s"%(iframebodyinputtext.input_text,timestr)
                        else:
                            inputtextwithtimestr = iframebodyinputtext.input_text

                    if iframebodyinputtext.input_ele_find!=None and iframebodyinputtext.input_ele_find_value != None:
                        activebrowser.findEleAndInputNum(0,iframebodyinputtext.input_ele_find,
                                                         iframebodyinputtext.input_ele_find_value,inputtextwithtimestr)
                    if iframebodyinputtext.is_check:
                        inputtext_list.append(inputtextwithtimestr)

                    activebrowser.quiteCurrentIframe()
                else:
                    activebrowser.outPutErrorMyLog(u"没有找到Iframe框，请确保iframe框的查找风格和查找风格的确切值已经填写！")
        else:
            activebrowser.outPutErrorMyLog(u"没有找到依赖id[%s]对应的数据！" % editid)

        return inputtext_list



iframebodyinputtext = IframeBodyInputText()