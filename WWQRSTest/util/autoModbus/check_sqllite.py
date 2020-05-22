import time

from WWQRSTest.util.autoModbus.depend.startSCYXieYi import TelnetClient
from WWQRSTest.util.autoModbus.depend.myftp_get_file import MyFTP
from WWQRSTest.util.autoModbus.depend.handleTxt import HandleTxt


class UpXieYiCfg(object):
    def __init__(self):
        self.telnet_host_ip = '192.168.101.104'
        self.telnet_username = 'root'
        self.telnet_password = 'wwyc5166'
        self.telnet_clicent_object= None
        self.ftp_client_object = None
        self.xieyi_name = '122_w'

    #延时函数
    def time_delay(self,deletime):
        print("即将等待%s秒" % str(deletime))
        time.sleep(int(deletime))
        print("等待%s秒结束" % str(deletime))



    #ftp连接
    def ftp_connnect(self):
        host = self.telnet_host_ip
        username = self.telnet_username
        password = self.telnet_password
        ftp_client = MyFTP(host, username, password)
        return ftp_client

    #ftp下载远程路径文件
    def run_ftp_down(self,remote_file,local_file):
        if self.ftp_client_object == None:
            self.ftp_client_object = self.ftp_connnect()
        else:
            self.ftp_client_object = self.ftp_client_object

        remote_file = remote_file
        local_file = local_file
        #先删除现有文件
        ht = HandleTxt(file_name=local_file)
        ht.delete_file()
        #再下载新文件
        self.ftp_client_object.ftp_download(remote_file, local_file)
        self.time_delay(3)
        # print(self.ftp_client_object)

    #读取本地文件并解析内容
    def run_handle_text_read(self,local_file,expect_name):
        flag = False
        ht = HandleTxt(file_name=local_file)
        all_content_list = ht.read_all_content_list()
        print(all_content_list)
        for one_content in all_content_list:
            one = one_content.strip("\n")  #去掉换行符
            print(one)
            if expect_name == one:
                flag = True
                break
            print("***************************")
            print(one_content)
            print(flag)
            print("***************************")
        return flag

    #判断远程文件是否存在相应的文件
    def is_exist_remote_file(self,):
        pass

    #ftp上传文件
    def run_ftp_up(self,remote_file,local_file):
        if self.ftp_client_object == None:
            self.ftp_client_object = self.ftp_connnect()
        else:
            self.ftp_client_object = self.ftp_client_object
        remote_file = remote_file
        local_file = local_file
        self.ftp_client_object.ftp_upload(remote_file,local_file)
        self.time_delay(3)





    #一些善后工作
    def end_work(self):
        if self.telnet_clicent_object != None:
            self.telnet_clicent_object.logout_host()  #如果telnet连接则退出
        if self.ftp_client_object != None:
            self.ftp_client_object.ftp_close()   #如果tfp连接，则退出



if __name__ == '__main__':
    uxyc = UpXieYiCfg()
    remote_file ='/tmp/real.db'
    local_file ='real.db'
    uxyc.run_ftp_down(remote_file,local_file)
