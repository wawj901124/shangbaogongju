from WWTest.util.getTimeStr import GetTimeStr
from WWTest.util.autoMakeString import AutoMakeString,automakestring

class HandleRequestsDatas(object):
    def handlerequestsdatas(self,activeapi,apirequestdataid):
        timestr = GetTimeStr().getTimeStr()
        requestdatas_dict = {}
        from testapidatas.models import RequestDatas
        requestdatases = RequestDatas.objects.filter(apirequestdata_id=int(apirequestdataid))
        if str(requestdatases) != "<QuerySet []>":
            activeapi.outPutMyLog("找到依赖数据")
            for requestdatas in requestdatases:
                #处理键值对的键
                requestheader_dict_key = requestdatas.request_key

                #处理键值对的值
                if requestdatas.is_auto_input:
                    if requestdatas.auto_input_type == '1' :
                        requestheader_dict_value = automakestring.getDigits(requestdatas.auto_input_long)
                    elif requestdatas.auto_input_type == '2' :
                        requestheader_dict_value = automakestring.getAsciiLowercase(requestdatas.auto_input_long)
                    elif requestdatas.auto_input_type == '3' :
                        requestheader_dict_value = automakestring.getLettersAndDigits(requestdatas.auto_input_long)
                    elif requestdatas.auto_input_type == '4' :
                        requestheader_dict_value = automakestring.getLetterAndDigitsAndSymbols(requestdatas.auto_input_long)
                    elif requestdatas.auto_input_type == '5' :
                        requestheader_dict_value = automakestring.getLetterAndDigitsAndSymbolsAndWhitespace(requestdatas.auto_input_long)
                    elif requestdatas.auto_input_type == '6' :
                        requestheader_dict_value = automakestring.getUnicodeZh(requestdatas.auto_input_long)
                    else:
                        requestheader_dict_value = u"自动输入字符的类型不正确，请输入正确的自动输入字符的类型"
                        activeapi.outPutErrorMyLog(u"自动输入字符的类型不正确，请输入正确的自动输入字符的类型")
                else:
                    if requestdatas.is_with_time:
                        requestheader_dict_value = "%s%s"%(requestdatas.request_value,timestr)
                    else:
                        requestheader_dict_value = requestdatas.request_value


                requestdatas_dict[requestheader_dict_key]=requestheader_dict_value

        else:
            activeapi.outPutErrorMyLog("没有找到依赖id[%s]对应的数据！" % apirequestdataid)
        activeapi.outPutMyLog("requestdatas_dict:%s" % requestdatas_dict )
        return requestdatas_dict




handlerequestsdatas = HandleRequestsDatas()