# 修改MAC地址
import logging
import ftplib
import telnetlib
import time

#Telnet连接
class TelnetClient():
    def __init__(self):
        self.tn = telnetlib.Telnet()

    # 此函数实现telnet登录主机
    def login_host(self,host_ip,username,password):
        try:
            # self.tn = telnetlib.Telnet(host_ip,port=23)
            self.tn.open(host_ip,port=23)
        except:
            logging.warning('%s网络连接失败'%host_ip)
            return False
        # 等待login出现后输入用户名，最多等待10秒
        self.tn.read_until(b'login: ',timeout=10)
        self.tn.write(username.encode('ascii') + b'\n')
        # 等待Password出现后输入用户名，最多等待10秒
        self.tn.read_until(b'Password: ',timeout=10)
        self.tn.write(password.encode('ascii') + b'\n')
        # 延时两秒再收取返回结果，给服务端足够响应时间
        time.sleep(2)
        # 获取登录结果
        # read_very_eager()获取到的是的是上次获取之后本次获取之前的所有输出
        command_result = self.tn.read_very_eager().decode('ascii')
        if 'Login incorrect' not in command_result:
            logging.warning('%s登录成功'%host_ip)
            return True
        else:
            logging.warning('%s登录失败，用户名或密码错误'%host_ip)
            return False

    # 此函数实现执行传过来的命令，并输出其执行结果
    def execute_some_command(self,command):
        # 执行命令
        self.tn.write(command.encode('ascii')+b'\n')
        time.sleep(2)
        # 获取命令结果
        command_result = self.tn.read_very_eager().decode('ascii')
        logging.warning('命令执行结果：\n%s' % command_result)
        return command_result

    # 退出telnet
    def logout_host(self):
        self.tn.write(b"exit\n")


#FTP连接
class MyFTP(object):
    def __init__(self,host,username,password):
        self.host = host
        self.username=username
        self.password=password
        self.my_ftp = self.login_ftp()

    def login_ftp(self):
        myftp = ftplib.FTP(self.host)  # 实例化FTP对象
        myftp.login(self.username, self.password)  # 登录
        return myftp

    def ftp_download(self,remote_file,local_file):
        '''以二进制形式下载文件'''
        file_remote = remote_file
        file_local = local_file
        bufsize = 1024  # 设置缓冲器大小
        fp = open(file_local, 'wb')
        self.my_ftp.retrbinary('RETR %s' % file_remote, fp.write, bufsize)
        logging.info("下载远程文件【%s】到本地文件【%s】" % (remote_file,local_file))
        fp.close()


    def ftp_upload(self,remote_file,local_file):
        '''以二进制形式上传文件'''
        file_remote = remote_file
        file_local = local_file
        bufsize = 1024  # 设置缓冲器大小
        fp = open(file_local, 'rb')
        self.my_ftp.storbinary('STOR ' + file_remote, fp, bufsize)
        logging.info("上传本地文件【%s】到远程文件【%s】" % (local_file,remote_file))
        fp.close()

    def ftp_dir(self):
        '''列出某个文件夹的的文件目录'''
        a = self.my_ftp.dir('/usr/')
        print("a:")
        print(a)

    def ftp_close(self):
        self.my_ftp.quit()


class ModifyMac(object):
    def __init__(self,host_ip,username,password):
        self.host_ip = host_ip
        self.username = username
        self.password = password
        self.telnet_client =None
        self.my_ftp =None

    def set_telnet_client(self):
        self.telnet_client = TelnetClient()
        self.telnet_client.login_host(host_ip=self.host_ip,username=self.username,password=self.password)

    def set_my_ftp(self):
        self.my_ftp = MyFTP(host=self.host_ip,username=self.username,password=self.password)

    def end_work(self):
        if self.telnet_client !=None:
            self.telnet_client.logout_host()   #退出telnet_client
        if self.my_ftp !=None:
            self.my_ftp.ftp_close()

    def modify_mac(self):
        #设置telnet
        self.set_telnet_client()

        #执行command命令
        commmand_one = "cd /usr/app_install/common/cfg/"
        self.telnet_client.execute_some_command()

        self.end_work()  #善后处理




if __name__ == '__main__':
    pass