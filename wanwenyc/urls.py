"""wanwenyc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin  #导入admin
from django.urls import path,include
import xadmin
from django.views.static import serve   #导入django处理静态文件的包serve ,用于处理midia路径下的文件
from .settings import MEDIA_ROOT    #导入Settings中配置的MEDIA_ROOT
from .settings import STATIC_ROOT   #导入静态文件根目录
from django.conf import settings   #debug_toolbar url配置-1-导入设置

urlpatterns = [
    path('admin/', admin.site.urls),  # 配置上传文件的访问处理函数,配置admin入口
    path('', xadmin.site.urls),       # 配置上传文件的访问处理函数

    # 配置处理引用midia路径下文件的路径,调用serve方法,需要传入参数{"document_root":MEDIA_ROOT}
    # 配置上传文件的访问处理函数
    path('media/<path:path>', serve, {"document_root": MEDIA_ROOT}),

    #静态文件配置
    path('static/<path:path>', serve, {"document_root": STATIC_ROOT}),

    # 配置点击返回场景url,namespace指明命名空间，用命名空间做限定
    path('testdatas/', include('testdatas.urls', namespace='testdatas')),

    # 配置接口数据url,namespace指明命名空间，用命名空间做限定
    path('testapidatas/', include('testapidatas.urls', namespace='testapidatas')),

    # 配置批量替换场景url,namespace指明命名空间，用命名空间做限定
    path('testupdatadb/', include('testupdatadb.urls', namespace='testupdatadb')),

    # 配置爬取数据场景url,namespace指明命名空间，用命名空间做限定
    path('spiderdata/', include('spiderdata.urls', namespace='spiderdata')),

    # 配置爬取数据场景url,namespace指明命名空间，用命名空间做限定
    path('shucaiyidate/', include('shucaiyidate.urls', namespace='shucaiyidate')),

    # 配置RDM日志统计,namespace指明命名空间，用命名空间做限定
    path('rdmrecode/', include('reportdatas.urls', namespace='rdmrecode')),
]

#debug_toolbar url配置-2-设置url
if settings.DEBUG:  #判断是否为调试模式
    import debug_toolbar
    # urlpatterns = [
    #     path('__debug__/', include(debug_toolbar.urls)),  # 配置debug_toolbar 的url,其中‘__debug__/’可以为任何未使用的路径名
    # ]+urlpatterns
    urlpatterns.append(path('__debug__/', include(debug_toolbar.urls))) #  # 配置debug_toolbar 的url,其中‘__debug__/’可以为任何未使用的路径名

