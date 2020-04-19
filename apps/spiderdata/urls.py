from django.urls import  path

from .views import SpiderHMChapterImageView  #导入ClickAndBackView



urlpatterns = [
    # 漫画图片页面的url配置
    path('spiderhmchapterdata/<path:spiderhmchapterdata_id>/', SpiderHMChapterImageView.as_view(), name="spider_hm_chapter_data_id"),
    # 配置复制新增测试用例url,namespace指明命名空间，用命名空间做限定


]

app_name = 'spiderhanman'

