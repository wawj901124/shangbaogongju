class ApiRequestDataDepend(object):
    def apirequestdatadepend(self,activeapi,dependid):
        activeapi.outPutMyLog("依赖ID（dependid）为:%s" % dependid)
        if dependid != None:
            activeapi.outPutMyLog("执行依赖")
            from testapidatas.models import ApiRequestData
            apirequestdatatestcases = ApiRequestData.objects.filter(id=int(dependid))
            print("apirequestdatatestcases:%s" % apirequestdatatestcases)
            if str(apirequestdatatestcases) != "<QuerySet []>":
                activeapi.outPutMyLog("找到依赖数据")
                for apirequestdatatestcase in  apirequestdatatestcases:
                    depend = apirequestdatatestcase.depend_case_id
                    activeapi.outPutMyLog("depend:%s" % depend)
                    if depend != None:
                        activeapi.outPutMyLog("进入下一层依赖")
                        self.apirequestdatadepend(activeapi,depend)

                    activeapi.outPutMyLog("执行的caseid:%s" % apirequestdatatestcase.id)

                    #进行接口请求
                    url = apirequestdatatestcase.request_url

                    from depend.requestsdepend.handleRequestsHeaders import handlerequestsheaders
                    from depend.requestsdepend.handleRequestCookies import handlerequestscookies
                    from depend.requestsdepend.handleRequestDatas import handlerequestsdatas

                    headers = handlerequestsheaders.handlerequestsheaders(activeapi,apirequestdatatestcase.id)
                    cookies = handlerequestscookies.handlerequestscookies(activeapi,apirequestdatatestcase.id)
                    data = handlerequestsdatas.handlerequestsdatas(activeapi,apirequestdatatestcase.id)

                    if apirequestdatatestcase.is_post:  # 进行post请求
                        if apirequestdatatestcase.is_json:
                            activeapi.define_Post_Json(url=url, headers=headers, cookies=cookies, json=data)
                        else:
                            activeapi.define_Post_Data(url=url, headers=headers, cookies=cookies, data=data)

                    else:  # 进行get请求
                        activeapi.define_Get(url=url, url_params=data, headers=headers, cookies=cookies)


            else:
                activeapi.outPutErrorMyLog("没有找到依赖id[%s]对应的数据！" % dependid)
        else:
            activeapi.outPutMyLog("依赖ID为None，不执行依赖！")

apirequestdatadepend = ApiRequestDataDepend()