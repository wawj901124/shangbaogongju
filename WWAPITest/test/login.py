import requests
import unittest
import json
import re


class TestClass(unittest.TestCase):
    # def test002Post(self):
    #
    #     #body数据
    #     keyword={
    #         'csrfmiddlewaretoken':'qOiT4xNs0VSXOkYgZAISr2wAeLf65Ffc4NyBbCtZCnpAq6139fiBLiPofv0BFSfX',
    #         'username':'bobby',
    #         'password':'admin123',
    #         'this_is_the_login_form':'1',
    #         'next':'/'
    #     }
    #
    #     #header部分的配置
    #     headers = {
    #         'User-Agent':'Mozilla/5.0 (Windows NT 6.2; WOW64; Trident/7.0; rv:11.0) like Gecko',
    #         'Accept':'image/gif, image/jpeg, image/pjpeg, application/x-ms-application, application/xaml+xml, application/x-ms-xbap, */*',
    #         'Accept-Language':'zh-CN'
    #     }
    #
    #     #cookie部分的配置
    #     cookies = dict(
    #         beacon_id='MTAxLjI1MS4xOTuuMTE5LTE0QzZELTUzQkE4OTQ5QjUyNzctNjE',
    #         search_test='1',
    #         search_r='32'
    #     )
    #
    #     #get请求的构造
    #     res = requests.post(
    #         "https://customer-api.helijia.com/app-customer/transformers/1030/widgets",
    #         data=keyword,  # post数据
    #         headers=headers,
    #         cookies=cookies
    #     )
    #
    #     print(res.text)
    #     print(res.status_code)
    #     self.assertTrue(u'今日上新' in res.text)


    def test001Get(self):
        #header部分的配置
        #header部分的配置
        headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 6.2; WOW64; Trident/7.0; rv:11.0) like Gecko',
            'Accept':'image/gif, image/jpeg, image/pjpeg, application/x-ms-application, application/xaml+xml, application/x-ms-xbap, */*',
            'Accept-Language':'zh-CN'
        }

        #cookie部分的配置
        cookies = dict(
            beacon_id='MTAxLjI1MS4xOTuuMTE5LTE0QzZELTUzQkE4OTQ5QjUyNzctNjE',
            search_test='1',
            search_r='32'
        )

        params = []

        #get请求的构造
        res = requests.get(
            "http://127.0.0.1:8000/",
            headers=headers,
            cookies=cookies,
            params= params

        )
        reposon_headers = res.headers
        print(res.text)
        print("\n")
        print(res.status_code)
        print("\n")
        print("reposon_headers:%s"%reposon_headers)
        print(type(reposon_headers))
        print("\n")
        print(res.cookies)
        print("\n")
        print(res.json)
        print("\n")
        print(res.content)
        print("\n")
        # self.assertTrue(u'http://img.cudn.static.helijia.com' in res.text)
        print(str(reposon_headers))
        match = "csrftoken=(.+?);"
        re_csr = re.findall(match,str(reposon_headers))
        print(re_csr)
        print("\n")
        print(type(re_csr))

if __name__ == "__main__":
    print("1******************1")
    unittest.main()