from WWTest.util.getTimeStr import GetTimeStr
from WWTest.util.autoMakeString import AutoMakeString,automakestring

class HandleRequestsHeaders(object):
    def handlerequestsheaders(self,activeapi,apirequestdataid):
        timestr = GetTimeStr().getTimeStr()
        requestheaders_dict = {}
        from testapidatas.models import RequestHeaders
        requestheaderses = RequestHeaders.objects.filter(apirequestdata_id=int(apirequestdataid))
        if str(requestheaderses) != "<QuerySet []>":
            activeapi.outPutMyLog("找到依赖数据")
            for requestheaders in requestheaderses:
                #处理键值对的键
                requestheader_dict_key = requestheaders.request_key

                #处理键值对的值
                # if requestheaders.is_auto_input:
                #     if requestheaders.auto_input_type == '1' :
                #         requestheader_dict_value = automakestring.getDigits(requestheaders.auto_input_long)
                #     elif requestheaders.auto_input_type == '2' :
                #         requestheader_dict_value = automakestring.getAsciiLowercase(requestheaders.auto_input_long)
                #     elif requestheaders.auto_input_type == '3' :
                #         requestheader_dict_value = automakestring.getLettersAndDigits(requestheaders.auto_input_long)
                #     elif requestheaders.auto_input_type == '4' :
                #         requestheader_dict_value = automakestring.getLetterAndDigitsAndSymbols(requestheaders.auto_input_long)
                #     elif requestheaders.auto_input_type == '5' :
                #         requestheader_dict_value = automakestring.getLetterAndDigitsAndSymbolsAndWhitespace(requestheaders.auto_input_long)
                #     elif requestheaders.auto_input_type == '6' :
                #         requestheader_dict_value = automakestring.getUnicodeZh(requestheaders.auto_input_long)
                #     else:
                #         requestheader_dict_value = u"自动输入字符的类型不正确，请输入正确的自动输入字符的类型"
                #         activeapi.outPutErrorMyLog(u"自动输入字符的类型不正确，请输入正确的自动输入字符的类型")
                # else:
                #     if requestheaders.is_with_time:
                #         requestheader_dict_value = "%s%s"%(requestheaders.request_value,timestr)
                #     else:
                requestheader_dict_value = requestheaders.request_value


                requestheaders_dict[requestheader_dict_key]=requestheader_dict_value

        else:
            activeapi.outPutErrorMyLog("没有找到依赖id[%s]对应的数据！" % apirequestdataid)
        activeapi.outPutMyLog("requestheaders_dict:%s" % requestheaders_dict )
        return requestheaders_dict




handlerequestsheaders = HandleRequestsHeaders()