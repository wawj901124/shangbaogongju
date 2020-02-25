from django.urls import  path


from .views import ApiRequestDataView #导入ClickAndBackView


urlpatterns = [
    #相同参数的路径名一定不能一样。比如copy/<path:testcase_id>/与<path:testcase_id>/不能并列存在
    path('apirequestdatacopy/<path:apirequestdata_id>/', ApiRequestDataView.as_view(), name="api_request_data_id"),  # 配置复制新增测试用例url,namespace指明命名空间，用命名空间做限定

]

app_name = 'apirequestdata'