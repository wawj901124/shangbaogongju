from django.urls import  path

from .views import TagContentView  #导入TagContentView
from .views import XieyiConfigDateView
from .views import NodeConfigMakeDevRequest,NodeConfigCopyRequest,NodeConfigReadAndSaveRequest
from .views import XieyiConfigDateOrderView,XieyiTestCaseView,SenderHexDataOrderView,RecriminatDataOrderView





urlpatterns = [
    # 节点配置页面的url配置
    path('tagcontent/<path:tagcontent_id>/', TagContentView.as_view(), name="tag_content_id"),
    # 配置复制新增测试用例url,namespace指明命名空间，用命名空间做限定

    # 协议测试用例页面的url配置
    path('xieyiconfigdate/<path:xieyiconfigdate_id>/', XieyiConfigDateView.as_view(), name="xie_yi_config_date_id"),
    # 配置复制新增测试用例url,namespace指明命名空间，用命名空间做限定

    # 节点配置NodeConfig页面的url配置-生成dev的配置
    path('nodeconfigmakedev/<path:nodeconfig_id>/', NodeConfigMakeDevRequest, name="node_config_make_dev_id"),
    # 配置复制新增测试用例url,namespace指明命名空间，用命名空间做限定

    # 节点配置NodeConfig页面的url配置-完全复制
    path('nodeconfigallcopy/<path:nodeconfig_id>/', NodeConfigCopyRequest, name="node_config_all_copy_id"),
    # 配置复制新增测试用例url,namespace指明命名空间，用命名空间做限定

    # 节点配置NodeConfig页面的url配置-将上传的文件入库
    path('nodeconfigreadandsave/<path:nodeconfig_id>/', NodeConfigReadAndSaveRequest, name="node_config_read_and_save_id"),
    # 配置复制新增测试用例url,namespace指明命名空间，用命名空间做限定

    # 协议测试用例之依赖配置url配置
    path('xieyiconfigdateorder/<path:xieyiconfigdateorder_id>/', XieyiConfigDateOrderView.as_view(), name="xie_yi_config_date_order_id"),
    # 配置复制新增测试用例url,namespace指明命名空间，用命名空间做限定

    # 协议测试用例之测试用例url配置
    path('xieyitestcase/<path:xieyitestcase_id>/', XieyiTestCaseView.as_view(),
         name="new_xie_yi_test_case_id"),
    # 配置复制新增测试用例url,namespace指明命名空间，用命名空间做限定

    # 协议测试用例之串口收发数据url配置
    path('senderhexdataorder/<path:senderhexdataorder_id>/', SenderHexDataOrderView.as_view(),name="sender_hex_date_order_id"),
    # 配置复制新增测试用例url,namespace指明命名空间，用命名空间做限定

    # 协议测试用例之反控收发数据url配置
    path('recriminatdataorder/<path:recriminatdataorder_id>/', RecriminatDataOrderView.as_view(),
         name="recriminat_data_order_id"),
    # 配置复制新增测试用例url,namespace指明命名空间，用命名空间做限定



]

app_name = 'shucaiyidate'

