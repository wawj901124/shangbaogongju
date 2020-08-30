from WWTest.util.getTimeStr import GetTimeStr
from WWTest.util.autoMakeString import AutoMakeString,automakestring

class HandleRequestsDatas(object):
    def handlerequestsdatas(self,activeapi,apirequestdataid):
        timestr = GetTimeStr().getTimeStr()
        requestdatases_list = []
        from testapidatas.models import RequestDatas
        requestdatases = RequestDatas.objects.filter(apirequestdata_id=int(apirequestdataid))
        if str(requestdatases) != "<QuerySet []>":
            activeapi.outPutMyLog("找到依赖数据")
            for requestdatas in requestdatases:
                requestdatas_one_list = []
                requestdatas_one_dict = {}
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




                requestdatas_one_dict[requestheader_dict_key]=requestheader_dict_value
                requestdatas_one_list.append(requestdatas_one_dict)  #添加参数键值对到列表第一项中
                requestdatas_one_list.append(requestdatas.sql_assert)  #添加参数值在对应数据库中内容
                requestdatases_list.append(requestdatas_one_list)

        else:
            activeapi.outPutErrorMyLog("没有找到依赖id[%s]对应的数据！" % apirequestdataid)
        activeapi.outPutMyLog("requestdatases_list:%s" % requestdatases_list )
        return requestdatases_list




handlerequestsdatas = HandleRequestsDatas()

if __name__ == '__main__':
    print("hello world")
    from WWAPITest.base.activeAPI import ActiveAPI
    aa = ActiveAPI()
    handlerequestsdatas.handlerequestsdatas(activeapi=aa,apirequestdataid='1')