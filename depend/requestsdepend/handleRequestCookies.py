from WWTest.util.getTimeStr import GetTimeStr
from WWTest.util.autoMakeString import AutoMakeString,automakestring

class HandleRequestsCookies(object):
    def handlerequestscookies(self,activeapi,apirequestdataid):
        timestr = GetTimeStr().getTimeStr()
        requestcookies_dict = {}
        from testapidatas.models import RequestCookies
        requestcookieses = RequestCookies.objects.filter(apirequestdata_id=int(apirequestdataid))
        if str(requestcookieses) != "<QuerySet []>":
            activeapi.outPutMyLog("找到依赖数据")
            for requestcookies in requestcookieses:
                #处理键值对的键
                requestheader_dict_key = requestcookies.request_key

                #处理键值对的值
                if requestcookies.is_auto_input:
                    if requestcookies.auto_input_type == '1' :
                        requestheader_dict_value = automakestring.getDigits(requestcookies.auto_input_long)
                    elif requestcookies.auto_input_type == '2' :
                        requestheader_dict_value = automakestring.getAsciiLowercase(requestcookies.auto_input_long)
                    elif requestcookies.auto_input_type == '3' :
                        requestheader_dict_value = automakestring.getLettersAndDigits(requestcookies.auto_input_long)
                    elif requestcookies.auto_input_type == '4' :
                        requestheader_dict_value = automakestring.getLetterAndDigitsAndSymbols(requestcookies.auto_input_long)
                    elif requestcookies.auto_input_type == '5' :
                        requestheader_dict_value = automakestring.getLetterAndDigitsAndSymbolsAndWhitespace(requestcookies.auto_input_long)
                    elif requestcookies.auto_input_type == '6' :
                        requestheader_dict_value = automakestring.getUnicodeZh(requestcookies.auto_input_long)
                    else:
                        requestheader_dict_value = u"自动输入字符的类型不正确，请输入正确的自动输入字符的类型"
                        activeapi.outPutErrorMyLog(u"自动输入字符的类型不正确，请输入正确的自动输入字符的类型")
                else:
                    if requestcookies.is_with_time:
                        requestheader_dict_value = "%s%s"%(requestcookies.request_value,timestr)
                    else:
                        requestheader_dict_value = requestcookies.request_value


                requestcookies_dict[requestheader_dict_key]=requestheader_dict_value

        else:
            activeapi.outPutErrorMyLog("没有找到依赖id[%s]对应的数据！" % apirequestdataid)
        activeapi.outPutMyLog("requestcookies_dict:%s" % requestcookies_dict )
        return requestcookies_dict




handlerequestscookies = HandleRequestsCookies()