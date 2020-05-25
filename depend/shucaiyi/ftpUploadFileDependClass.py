# ----------------------------------------------------------------------
import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wanwenyc.settings")
django.setup()
# ----------------------------------------------------------------------
#独运行某一个py文件时会出现如下错误：django.core.exceptions.AppRegistryNotReady: Apps aren't loaded yet.，以上内容可以解决此问题,加载django中的App


class FtpUploadFileDepend(object):

    def makeFtpUpliadFileList(self,depend_id):
        ftp_up_load_file_list = []
        from shucaiyidate.models import FtpUploadFile
        ftpuploadfile_list = FtpUploadFile.objects.filter(xieyiconfigdate_id=depend_id)
        ftpuploadfile_list_count = ftpuploadfile_list.count()
        if ftpuploadfile_list_count==0:
            pass
        else:
            for ftpuploadfile_one in ftpuploadfile_list:
                ftpuploadfile_one_list = []
                ftpuploadfile_one_list.append(ftpuploadfile_one.up_remote_file)
                ftpuploadfile_one_list.append(ftpuploadfile_one.up_local_file)
                ftp_up_load_file_list.append(ftpuploadfile_one_list)

        print("ftp_up_load_file_list:")
        print(ftp_up_load_file_list)
        return ftp_up_load_file_list


ftpuploadfiledepend = FtpUploadFileDepend()


