import unittest
# ----------------------------------------------------------------------
import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wanwenyc.settings")
django.setup()
# ----------------------------------------------------------------------
#独运行某一个py文件时会出现如下错误：django.core.exceptions.AppRegistryNotReady: Apps aren't loaded yet.，以上内容可以解决此问题,加载django中的App
import ddt

from WWAPITest.autotest.config.suijing.globalconfig.globalConfig import gc   #导入全局变量
from WWAPITest.base.activeAPI import ActiveAPI
from WWAPITest.util.getTimeStr import GetTimeStr

from depend.requestsdepend.apiRequestDataDepend import ApiRequestDataDepend,apirequestdatadepend
from WWAPITest.autotest.config.suijing.page.loginPage import *  #导入登录页
from depend.requestsdepend.handleRequestsHeaders import handlerequestsheaders
from depend.requestsdepend.handleRequestCookies import handlerequestscookies
from depend.requestsdepend.handleRequestDatas import handlerequestsdatas





class TestAPIClass(unittest.TestCase):  # 创建测试类

    @classmethod  # 类方法，只执行一次，但必须要加注解@classmethod,且名字固定为setUpClass
    def setUpClass(cls):
        pass

    @classmethod  # 类方法，只执行一次，但必须要加注解@classmethod,且名字固定为tearDownClass
    def tearDownClass(cls):
        pass


    def setUp(self):  # 每条用例执行测试之前都要执行此方法
        self.activeapi = ActiveAPI()  # 实例化
        pass

    def tearDown(self):  # 每条用例执行测试之后都要执行此方法
        pass


    def definedepend(self,dependid):
        apirequestdatadepend.apirequestdatadepend(self.activeapi,dependid)


    #定义点击返回函数
    def definetestapi(self,num,case_counts,depend_case_id,
                      id,
                      request_url,
                      is_auto_get_cookies,is_use_cache,
                      is_post,is_json,
                      testproject,testmodule,testpage,
                      testcasetitle,teststarttime,
                      forcount
                      ):


        #如果有依赖ID，则执行依赖函数，达到执行当前用例的前提条件
        if depend_case_id != None:
            self.definedepend(depend_case_id)
            self.activeapi.outPutMyLog("依赖函数执行完毕！！！")

        self.activeapi.outPutMyLog("开始正式执行测试用例")

        if gc.ISONLINE:
            url = "%s%s" % (gc.ONLINE_REQUESTS_YU_MING,request_url)
        else:
            url = "%s%s" % (gc.TEST_REQUESTS_YU_MING,request_url)

        print("url:%s" % url)

        headers = handlerequestsheaders.handlerequestsheaders(self.activeapi, id)
        if is_auto_get_cookies:
            if not is_use_cache:
                lpf.login()
            cookies = lpf.get_cookie_dic()
        else:
            cookies = handlerequestscookies.handlerequestscookies(self.activeapi, id)
        data = handlerequestsdatas.handlerequestsdatas(self.activeapi, id)

        if is_post:  #进行post请求
                if is_json:
                    print("url:%s" % url)
                    print("headers:%s" % headers)
                    print("cookies:%s" % cookies)
                    print("data:%s" %data)
                    res = self.activeapi.define_Post_Json(url=url,headers=headers,cookies=cookies,json=data)
                else:
                    print("url:%s" % url)
                    print("headers:%s" % headers)
                    print("cookies:%s" % cookies)
                    print("data:%s" %data)
                    res = self.activeapi.define_Post_Data(url=url,headers=headers,cookies=cookies,data=data)

        else:  #进行get请求
           res = self.activeapi.define_Get(url=url,url_params=data,headers=headers,cookies=cookies)

        #保存请求结果
        from reportdatas.models import RequestReport
        requestreport = RequestReport()
        requestreport.testproject = testproject
        requestreport.testmodule = testmodule
        requestreport.testpage = testpage
        requestreport.testcasetitle = testcasetitle
        requestreport.teststarttime = teststarttime
        requestreport.forcount = forcount
        requestreport.response_status_code = res.status_code
        requestreport.response_text = res.text
        requestreport.response_content = res.content
        requestreport.response_json = res.json
        requestreport.response_elapsed = res.elapsed
        requestreport.response_elapsed_microseconds = res.elapsed.microseconds/1000
        requestreport.response_headers = res.headers
        requestreport.response_cookies = res.cookies
        requestreport.save()

        #如果登录存在响应结果中则自动化登录获取cookies
        if "注销" not in res.text:
            lpf.login()



    # def test001(self):
    #     print("第一条测试用例")
    #     self.definedepend(self.dependid)

    @staticmethod    #根据不同的参数生成测试用例
    def getTestFunc(num,case_counts,depend_case_id,
                      id,
                      request_url,
                      is_auto_get_cookies,is_use_cache,
                      is_post,is_json,
                      testproject,testmodule,testpage,
                      testcasetitle,teststarttime,
                      forcount):

        def func(self):
            self.definetestapi(num,case_counts,depend_case_id,
                      id,
                      request_url,
                      is_auto_get_cookies,is_use_cache,
                      is_post,is_json,
                      testproject,testmodule,testpage,
                      testcasetitle,teststarttime,
                      forcount)
        return func

def __generateTestCases():
    from testapidatas.models import ApiRequestData

    apirequestdatatestcase_all = ApiRequestData.objects.filter(id=1).order_by('id')

    for apirequestdatatestcase in apirequestdatatestcase_all:
        forcount = apirequestdatatestcase.case_counts
        starttime = GetTimeStr().getTimeStr()
        if len(str(apirequestdatatestcase.id)) == 1:
            apirequestdatatestcaseid = '0000%s' % apirequestdatatestcase.id
        elif len(str(apirequestdatatestcase.id)) == 2:
            apirequestdatatestcaseid = '000%s' % apirequestdatatestcase.id
        elif len(str(apirequestdatatestcase.id)) == 3:
            apirequestdatatestcaseid = '00%s' % apirequestdatatestcase.id
        elif len(str(apirequestdatatestcase.id)) == 4:
            apirequestdatatestcaseid = '0%s' % apirequestdatatestcase.id
        elif len(str(apirequestdatatestcase.id)) == 5:
            apirequestdatatestcaseid = '%s' % apirequestdatatestcase.id
        else:
            apirequestdatatestcaseid = 'Id已经超过5位数，请重新定义'

        for i in range(1, forcount + 1):  # 循环，从1开始
            if len(str(i)) == 1:
                forcount_i = '0000%s' % i
            elif len(str(i)) == 2:
                forcount_i = '000%s' % i
            elif len(str(i)) == 3:
                forcount_i = '00%s' % i
            elif len(str(i)) == 4:
                forcount_i = '0%s' % i
            elif len(str(i)) == 5:
                forcount_i = '%s' % i
            else:
                forcount_i = 'Id已经超过5位数，请重新定义'

            args = []
            args.append(apirequestdatatestcaseid)
            args.append(i)
            args.append(apirequestdatatestcase.depend_case_id)
            args.append(apirequestdatatestcase.id)
            args.append(apirequestdatatestcase.request_url)
            args.append(apirequestdatatestcase.is_auto_get_cookies)
            args.append(apirequestdatatestcase.is_use_cache)
            args.append(apirequestdatatestcase.is_post)
            args.append(apirequestdatatestcase.is_json)
            args.append(apirequestdatatestcase.test_project)
            args.append(apirequestdatatestcase.test_module)
            args.append(apirequestdatatestcase.test_page)
            args.append(apirequestdatatestcase.test_case_title)
            args.append(starttime)
            args.append(i)


            setattr(TestAPIClass,
                    'test_func_%s_%s_%s' % (apirequestdatatestcaseid, apirequestdatatestcase.test_case_title, forcount_i),
                    TestAPIClass.getTestFunc(*args))  # 通过setattr自动为TestCase类添加成员方法，方法以“test_func_”开头


__generateTestCases()

if __name__ == '__main__':
    print("hello world")
    unittest.main()












