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



    #获取协议是否在对应路径下
    def run_telnet_command(self,mycommad_list):
        if self.telnet_clicent_object == None:
            self.telnet_clicent_object = TelnetClient()
        else:
            self.telnet_clicent_object = self.telnet_clicent_object
        # 如果登录结果返加True，则执行命令，然后退出
        if self.telnet_clicent_object.login_host(host_ip=self.telnet_host_ip,
                                                 username=self.telnet_username,
                                                 password=self.telnet_password):
            for mycommad in mycommad_list:
                self.telnet_clicent_object.execute_some_command(mycommad)

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
    mycommad_list = []
    mycommad1 = 'cd /usr/app_install/protocol/bin'
    mycommad2 = 'ls | grep 122_w>ls_122_w.txt &'

    mycommad_list.append(mycommad1)
    mycommad_list.append(mycommad2)
    print(mycommad_list)
    uxyc.run_telnet_command(mycommad_list)

    remote_file_1 = '/usr/app_install/protocol/bin/ls_122_w.txt'
    local_file_1 = 'ls_122_w.txt'
    print("shang")
    uxyc.run_ftp_down(remote_file_1,local_file_1)
    print("这里")
    expect_name1 = '122_w'
    is_exist = uxyc.run_handle_text_read(local_file_1,expect_name1)
    print(is_exist)
    if is_exist :
        pass
        #如果存在，则不进行上传
    else:
        #如果不存在，则进行上传
        remote_file_2 = '/usr/app_install/protocol/bin/122_w'
        local_file_2 = './upload/122_w'
        uxyc.run_ftp_up(remote_file_2,local_file_2)
        # remote_file_2 = '/usr/app_install/protocol/cfg/limits'
        # local_file_2 = './upload/limits'
        # uxyc.run_ftp_up(remote_file_2,local_file_2)

    mycommad_list=[]
    #加入写权限
    mycommad1 = 'cd /usr/app_install/protocol/bin'
    mycommad2 = 'chmod a+x 122_w'

    mycommad_list.append(mycommad1)
    mycommad_list.append(mycommad2)
    print(mycommad_list)
    uxyc.run_telnet_command(mycommad_list)



    mycommad_list = []
    mycommad1 = 'cd /usr/app_install/common/cfg/'
    # uxyc.run_telnet_command(mycommad1)
    mycommad2 = 'ls | grep limits>ls_limits.txt'
    mycommad_list.append(mycommad1)
    mycommad_list.append(mycommad2)
    uxyc.run_telnet_command(mycommad_list)
    remote_file_1 = '/usr/app_install/common/cfg/ls_limits.txt'
    local_file_1 = 'ls_limits.txt'
    uxyc.run_ftp_down(remote_file_1,local_file_1)
    expect_name1 = 'limits'
    is_exist = uxyc.run_handle_text_read(local_file_1,expect_name1)
    if is_exist :
        pass
        #如果存在，则不进行上传
    else:
        #如果不存在，则进行上传
        remote_file_2 = '/usr/app_install/common/cfg/limits'
        local_file_2 = './upload/limits'
        uxyc.run_ftp_up(remote_file_2,local_file_2)

    mycommad_list=[]
    #加入写权限
    mycommad1 = 'cd /usr/app_install/common/cfg/'
    mycommad2 = 'chmod a+x limits'

    mycommad_list.append(mycommad1)
    mycommad_list.append(mycommad2)
    print(mycommad_list)
    uxyc.run_telnet_command(mycommad_list)







