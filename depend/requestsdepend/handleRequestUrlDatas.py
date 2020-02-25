
# ----------------------------------------------------------------------
import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wanwenyc.settings")
django.setup()
# ----------------------------------------------------------------------

from WWTest.util.getTimeStr import GetTimeStr
from WWTest.util.autoMakeString import AutoMakeString,automakestring

class HandleRequestsUrlDatas(object):
    def handlerequestsdatas(self,activeapi,apirequestdataid):
        timestr = GetTimeStr().getTimeStr()
        requesturldatas_str=""
        requesturldatas_dict = {}
        from testapidatas.models import RequestUrlDatas
        requesturldatases = RequestUrlDatas.objects.filter(apirequestdata_id=int(apirequestdataid))
        requesturldatases_count = requesturldatases.count()
        if str(requesturldatases) != "<QuerySet []>":
            activeapi.outPutMyLog("找到依赖数据")
            for requesturldatas in requesturldatases:
                #处理键值对的键
                requestheader_dict_key = requesturldatas.request_key

                #处理键值对的值
                if requesturldatas.is_auto_input:
                    if requesturldatas.auto_input_type == '1' :
                        requestheader_dict_value = automakestring.getDigits(requesturldatas.auto_input_long)
                    elif requesturldatas.auto_input_type == '2' :
                        requestheader_dict_value = automakestring.getAsciiLowercase(requesturldatas.auto_input_long)
                    elif requesturldatas.auto_input_type == '3' :
                        requestheader_dict_value = automakestring.getLettersAndDigits(requesturldatas.auto_input_long)
                    elif requesturldatas.auto_input_type == '4' :
                        requestheader_dict_value = automakestring.getLetterAndDigitsAndSymbols(requesturldatas.auto_input_long)
                    elif requesturldatas.auto_input_type == '5' :
                        requestheader_dict_value = automakestring.getLetterAndDigitsAndSymbolsAndWhitespace(requesturldatas.auto_input_long)
                    elif requesturldatas.auto_input_type == '6' :
                        requestheader_dict_value = automakestring.getUnicodeZh(requesturldatas.auto_input_long)
                    else:
                        requestheader_dict_value = u"自动输入字符的类型不正确，请输入正确的自动输入字符的类型"
                        activeapi.outPutErrorMyLog(u"自动输入字符的类型不正确，请输入正确的自动输入字符的类型")
                else:
                    if requesturldatas.is_with_time:
                        if requesturldatas.request_value == None:
                            requesturldatas_request_value = ""
                        else:
                            requesturldatas_request_value = requesturldatas.request_value
                        requestheader_dict_value = "%s%s"%(requesturldatas_request_value,timestr)
                    else:
                        if requesturldatas.request_value == None:
                            requesturldatas_request_value = ""
                        else:
                            requesturldatas_request_value = requesturldatas.request_value
                        requestheader_dict_value = requesturldatas_request_value


                requesturldatas_dict[requestheader_dict_key]=requestheader_dict_value

            for key, value in requesturldatas_dict.items():
                requesturldatas_str = requesturldatas_str + "%s=%s" % (key, value) + "&"

            requesturldatas_str=requesturldatas_str[:-1]   #去掉最后一位&内容

            print("requesturldatas_str:%s" % requesturldatas_str)

        else:
            activeapi.outPutErrorMyLog("没有找到依赖id[%s]对应的数据！" % apirequestdataid)
        activeapi.outPutMyLog("requesturldatas_dict:%s" % requesturldatas_dict )
        return requesturldatas_str




handlerequestsurldatas = HandleRequestsUrlDatas()

if __name__ == '__main__':
    print("hello world")
    from WWAPITest.base.activeAPI import ActiveAPI
    ac = ActiveAPI()
    str = handlerequestsurldatas.handlerequestsdatas(ac,"3")
    print(str)

