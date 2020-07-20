# ----------------------------------------------------------------------
import os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wanwenyc.settings")
django.setup()
# ----------------------------------------------------------------------
# 独运行某一个py文件时会出现如下错误：django.core.exceptions.AppRegistryNotReady: Apps aren't loaded yet.，以上内容可以解决此问题,加载django中的App
from shucaiyidate.modelsorder import XieyiTestCase

fields_data = XieyiTestCase._meta.fields

l_model_name = list(key.name for key in fields_data)
print(l_model_name)