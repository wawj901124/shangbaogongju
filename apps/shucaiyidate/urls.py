from django.urls import  path

from .views import TagContentView  #导入TagContentView
from .views import XieyiConfigDateView



urlpatterns = [
    # 节点配置页面的url配置
    path('tagcontent/<path:tagcontent_id>/', TagContentView.as_view(), name="tag_content_id"),
    # 配置复制新增测试用例url,namespace指明命名空间，用命名空间做限定

    # 协议测试用例页面的url配置
    path('xieyiconfigdate/<path:xieyiconfigdate_id>/', XieyiConfigDateView.as_view(), name="xie_yi_config_date_id"),
    # 配置复制新增测试用例url,namespace指明命名空间，用命名空间做限定



]

app_name = 'shucaiyidate'

