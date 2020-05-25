# ----------------------------------------------------------------------
import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wanwenyc.settings")
django.setup()
# ----------------------------------------------------------------------
#独运行某一个py文件时会出现如下错误：django.core.exceptions.AppRegistryNotReady: Apps aren't loaded yet.，以上内容可以解决此问题,加载django中的App


class CloseXieYiCommandDepend(object):

    def makeCloseXieYiCommandList(self,depend_id):
        close_xie_yi_commad_list = []
        from shucaiyidate.models import CloseXieYiCommand
        closexieyicommand_list = CloseXieYiCommand.objects.filter(xieyiconfigdate_id=depend_id)
        closexieyicommand_list_count = closexieyicommand_list.count()
        if closexieyicommand_list_count==0:
            pass
        else:
            for closexieyicommand_one in closexieyicommand_list:
                close_xie_yi_commad_list.append(closexieyicommand_one.close_command)
        print("close_xie_yi_commad_list:")
        print(close_xie_yi_commad_list)
        return close_xie_yi_commad_list


closexieyicommanddepend = CloseXieYiCommandDepend()


