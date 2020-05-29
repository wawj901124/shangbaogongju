# ----------------------------------------------------------------------
import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wanwenyc.settings")
django.setup()
# ----------------------------------------------------------------------
#独运行某一个py文件时会出现如下错误：django.core.exceptions.AppRegistryNotReady: Apps aren't loaded yet.，以上内容可以解决此问题,加载django中的App


class RestartXieYiCommandDepend(object):

    def makeRestartXieYiCommandList(self,depend_id):
        restart_xie_yi_commad_list = []
        from shucaiyidate.models import RestartXieYiCommand
        restartxieyicommand_list = RestartXieYiCommand.objects.filter(xieyiconfigdate_id=depend_id)
        restartxieyicommand_list_count = restartxieyicommand_list.count()
        if restartxieyicommand_list_count==0:
            pass
        else:
            for restartxieyicommand_one in restartxieyicommand_list:
                restart_xie_yi_commad_list.append(restartxieyicommand_one.restart_command)
        print("restart_xie_yi_commad_list:")
        print(restart_xie_yi_commad_list)
        return restart_xie_yi_commad_list


restartxieyicommanddepend = RestartXieYiCommandDepend()


