
# ----------------------------------------------------------------------
import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wanwenyc.settings")
django.setup()
# ----------------------------------------------------------------------
#独运行某一个py文件时会出现如下错误：django.core.exceptions.AppRegistryNotReady: Apps aren't loaded yet.，以上内容可以解决此问题,加载django中的App
from wanwenyc.settings import MEDIA_ROOT    #导入Settings中配置的MEDIA_ROOT

#------------------------导入系统包-----------------------------------------
import time   #导入时间
import os
import traceback
import json
# import win32gui
# import win32con

#------------------------导入第三方包-----------------------------------------
from selenium import webdriver   #导入驱动
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from PIL import Image   #导入Image
from PIL import ImageEnhance  #导入ImageEnhance
import pytesseract   #导入pytesseract
from selenium.webdriver.support.select import Select   #导入Select
from selenium.webdriver.common.action_chains import ActionChains   #导入ActionChains
from bs4 import BeautifulSoup

##------------------------导入自定义的包-----------------------------------------
from WWTest.util.getTimeStr import GetTimeStr   #导入获取时间串函数
from WWAPITest.util.myLogs import MyLogs
from WWTest.util.identificationVerificationCode import IdentificationVerificationCode
from WWTest.util.operationJson import OperationJson

import requests
import unittest
import json
import re


class ActiveAPI(object):

    def outPutMyLog(self,context):
        mylog = MyLogs(context)
        mylog.runMyLog()

    def outPutErrorMyLog(self,context):
        mylog = MyLogs(context)
        mylog.runErrorLog()


    def define_Get(self,url,url_params,headers,cookies):
        #header部分的配置
        #header部分的配置
        # headers = {
        #     'User-Agent':'Mozilla/5.0 (Windows NT 6.2; WOW64; Trident/7.0; rv:11.0) like Gecko',
        #     'Accept':'image/gif, image/jpeg, image/pjpeg, application/x-ms-application, application/xaml+xml, application/x-ms-xbap, */*',
        #     'Accept-Language':'zh-CN',
        #     'Host':'111.207.18.22:40660'
        # }

        # #cookie部分的配置
        # cookies = dict(
        #     beacon_id='MTAxLjI1MS4xOTuuMTE5LTE0QzZELTUzQkE4OTQ5QjUyNzctNjE',
        #     search_test='1',
        #     search_r='32'
        # )

        # params = []

        #get请求的构造
        res = requests.get(
            # url="http://127.0.0.1:8000/",
            url=url,
            headers=headers,
            cookies=cookies,
            params= url_params

        )
        # reposon_headers = res.headers
        # print(res.text)
        # print("\n")
        # print(res.status_code)
        # print("\n")
        # print("reposon_headers:%s"%reposon_headers)
        # print(type(reposon_headers))
        # print("\n")
        # print(res.cookies)
        # print("\n")
        # print(res.json)
        # print("\n")
        # print(res.content)
        # print("\n")
        # # self.assertTrue(u'http://img.cudn.static.helijia.com' in res.text)
        # print(str(reposon_headers))
        # match = "csrftoken=(.+?);"
        # re_csr = re.findall(match,str(reposon_headers))
        # print(re_csr)
        # print("\n")
        # print(type(re_csr))
        return res


    def define_Post_Json(self,url,headers,cookies,json,):
        # body数据
        # json = {
        #     'enterName': '企业名称02',
        #     'enterShort': 'qiyejiancheng02',
        #     'industryId': 'B',
        #     'controlId': 'ff80808153747baa01537967302a000e',
        #     'provicneCode': '555555',
        #     'areaId': '5555555',
        #     'longitude': '233',
        #     'latitude': '233',
        #     'enterAddress': 'weqe',
        #     'typeId': '国有企业'
        #
        # }

        # header部分的配置
        # headers = {
        #     'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64; Trident/7.0; rv:11.0) like Gecko',
        #     'Accept': 'image/gif, image/jpeg, image/pjpeg, application/x-ms-application, application/xaml+xml, application/x-ms-xbap, */*;charset=utf-8',
        #     'Accept-Language': 'zh-CN',
        #     'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8'
        #     # 'Accept-Encoding': 'gzip, deflate'
        # }

        # # cookie部分的配置
        # cookies = dict(
        #     # JSESSIONID='48814BABDC0A5ED76628587B5688CCB7',
        #     JSESSIONID='075C1DAA84E6A1C5DBAE33CC08210A59'
        # )
        # cookies = {
        #     'JSESSIONID':'075C1DAA84E6A1C5DBAE33CC08210A59'
        # }


        # get请求的构造
        res = requests.post(
            # url="http://111.207.18.22:40660/app/enterprise/addEnterprise",
            url=url,
            json=json,  # post数据
            headers=headers,
            cookies=cookies
        )
        #
        # print(res.text)
        # print(res.status_code)
        # print(res.content)
        # print(res.history)
        # print(res.elapsed)
        # print(res.elapsed.microseconds)
        # print(res.elapsed.total_seconds())
        # print(res.elapsed.seconds)
        # print(res.headers)
        # print(res.cookies)
        # assert u'登录' in res.text
        return res

    def define_Post_Data(self,url,headers,cookies,data):
        # # body数据
        # data = {
        #     'enterName': '企业名称02',
        #     'enterShort': 'qiyejiancheng02',
        #     'industryId': 'B',
        #     'controlId': 'ff80808153747baa01537967302a000e',
        #     'provicneCode': '555555',
        #     'areaId': '5555555',
        #     'longitude': '233',
        #     'latitude': '233',
        #     'enterAddress': '',
        #     'typeId': '国有企业'
        #
        # }

        # # header部分的配置
        # headers = {
        #     'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64; Trident/7.0; rv:11.0) like Gecko',
        #     'Accept': 'image/gif, image/jpeg, image/pjpeg, application/x-ms-application, application/xaml+xml, application/x-ms-xbap, */*',
        #     'Accept-Language': 'zh-CN',
        #     'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8'
        # }

        # # cookie部分的配置
        # cookies = dict(
        #     # JSESSIONID='A42D1E6B2C5B6AAB07439B017811BDC0'
        #     JSESSIONID='173FD725B0976BC853DAAF0F0C4A74CF'
        # )

        # get请求的构造
        res = requests.post(
            # url="http://111.207.18.22:40660/app/enterprise/addEnterprise",
            url=url,
            data=data,  # post数据
            headers=headers,
            cookies=cookies
        )

        # print(res.text)
        # print(res.status_code)
        # print(res.content)
        # print(res.history)
        # print(res.elapsed)
        # print(res.elapsed.microseconds)
        # print(res.elapsed.total_seconds())
        # print(res.elapsed.seconds)
        # print(res.headers)
        # print(res.cookies)
        # assert u'登录' in res.text
        return res


    def define_create_dic(self,key,value):
        create_dic = {key:value}
        print(type(create_dic))
        return create_dic

    def define_add_dic(self,ori_dic,add_dic_key,add_dic_value):
        ori_dic[add_dic_key] = add_dic_value
        print(ori_dic)
        return ori_dic



if __name__ == "__main__":
    print("1******************1")
    activeapi = ActiveAPI()
    # activeapi.define_Post()
    # ori_dic={}
    # activeapi.define_add_dic(ori_dic,"apple","1")
    # activeapi.define_add_dic(ori_dic,"banana","2")
    # print(ori_dic)
    # activeapi.define_Post_Json(1,2,3,4)

