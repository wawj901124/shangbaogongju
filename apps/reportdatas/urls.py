from django.urls import  path

from .views import RdmAutoStaticRequest  #导入RdmAutoStaticRequest
from .views import RdmConfigRequest






urlpatterns = [
    # 节点配置页面的url配置,配置自动生成简报
    path('rdmautostatic/<path:rdmautostatic_id>/', RdmAutoStaticRequest, name="rdm_auto_static_id"),
    # 配置复制新增测试用例url,namespace指明命名空间，用命名空间做限定

    # 节点配置页面的url配置,配置自动获取RDM日志
    path('rdmconfig/<path:rdmconfig_id>/', RdmConfigRequest, name="rdm_config_id"),
    # 配置复制新增测试用例url,namespace指明命名空间，用命名空间做限定


]

app_name = 'rdmrecode'

