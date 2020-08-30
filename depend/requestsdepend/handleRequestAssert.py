from WWTest.util.getTimeStr import GetTimeStr
from WWTest.util.autoMakeString import AutoMakeString,automakestring

class HandleRequestAssert(object):
    def handlerequestassert(self,activeapi,apirequestdataid):
        timestr = GetTimeStr().getTimeStr()
        requestassertes_list = []
        from testapidatas.models import RequestAssert
        requestassertes = RequestAssert.objects.filter(apirequestdata_id=int(apirequestdataid))
        if str(requestassertes) != "<QuerySet []>":
            activeapi.outPutMyLog("找到依赖数据")
            for requestassert in requestassertes:
                requestassert_one_list= []
                requestassert_one_list.append(requestassert.request_assert_type)  #断言类型
                requestassert_one_list.append(requestassert.input_assert)  # 输入断言内容
                requestassert_one_list.append(requestassert.sql_assert)  # 断言sql语句
                requestassert_one_list.append(requestassert.code_assert)  # 断言状态码
                requestassert_one_list.append(requestassert.time_assert)  # 断言响应时间
                requestassertes_list.append(requestassert_one_list)
        else:
            activeapi.outPutErrorMyLog("没有找到依赖id[%s]对应的数据！" % apirequestdataid)
        activeapi.outPutMyLog("requestassertes_list:%s" % requestassertes_list )
        return requestassertes_list




handlerequestassert = HandleRequestAssert()

if __name__ == '__main__':
    print("hello world")
    from WWAPITest.base.activeAPI import ActiveAPI
    aa = ActiveAPI()
    handlerequestassert.handlerequestassert(activeapi=aa,apirequestdataid='1')