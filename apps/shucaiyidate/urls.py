from django.urls import  path

from .views import TagContentView  #导入TagContentView
from .views import XieyiConfigDateView

from .views import NodeConfigMakeDevRequest,NodeConfigCopyRequest,NodeConfigReadAndSaveRequest



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



]

app_name = 'shucaiyidate'

