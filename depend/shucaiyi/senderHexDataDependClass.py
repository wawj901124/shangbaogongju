# ----------------------------------------------------------------------
import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wanwenyc.settings")
django.setup()
# ----------------------------------------------------------------------
#独运行某一个py文件时会出现如下错误：django.core.exceptions.AppRegistryNotReady: Apps aren't loaded yet.，以上内容可以解决此问题,加载django中的App


class SenderHexDataDepend(object):

    def makeSenderHexDataList(self,depend_id):
        sender_hex_data_list = []
        from shucaiyidate.models import SenderHexData
        SenderHexData_list = SenderHexData.objects.filter(xieyiconfigdate_id=depend_id)
        SenderHexData_list_count = SenderHexData_list.count()
        if SenderHexData_list_count==0:
            pass
        else:
            for SenderHexData_one in SenderHexData_list:
                sender_hex_data_list.append(SenderHexData_one.sender_data)
        print("sender_hex_data_list:")
        print(sender_hex_data_list)
        return sender_hex_data_list


senderhexdatadepend = SenderHexDataDepend()


