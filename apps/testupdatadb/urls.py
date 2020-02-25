from django.urls import  path

from .views import UpdateDbDataView


urlpatterns = [
    # 批量替换的复制页面的url配置
    path('testupdatadbcopy/<path:testupdatadb_id>/', UpdateDbDataView.as_view(), name="test_up_data_db_id"),
    # 配置复制新增测试用例url,namespace指明命名空间，用命名空间做限定


]

app_name = 'testupdatadb'