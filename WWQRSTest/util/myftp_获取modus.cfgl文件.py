# FTP操作
import ftplib

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
        fp.close()

    def ftp_upload(self):
        '''以二进制形式上传文件'''
        file_remote = '/usr/result.txt'
        file_local = 'D:/pycharmproject/shangbaogongju/WWQRSTest/util/result.txt'
        bufsize = 1024  # 设置缓冲器大小
        fp = open(file_local, 'rb')
        self.my_ftp.storbinary('STOR ' + file_remote, fp, bufsize)
        fp.close()

    def ftp_dir(self):
        '''列出某个文件夹的的文件目录'''
        a = self.my_ftp.dir('/usr/')
        print("a:")
        print(a)

    #退出ftp
    def ftp_close(self):
        self.my_ftp.quit()


if __name__ == '__main__':
    host = '192.168.101.104'
    username = 'root'
    password = "wwyc5166"
    m = MyFTP(host,username,password)

    remote_file = '/usr/app_install/protocol/cfg/modbus.cfg'
    local_file = 'modbus.cfg'
    m.ftp_download(remote_file,local_file)
    # m.ftp_upload()
    # m.ftp_dir()




# f = ftplib.FTP(host)  # 实例化FTP对象
# f.login(username, password)  # 登录
# print(f.dir('bin'))


# def ftp_download():
#     '''以二进制形式下载文件'''
#     file_remote = '1.txt'
#     file_local = 'D:\\test_data\\ftp_download.txt'
#     bufsize = 1024  # 设置缓冲器大小
#     fp = open(file_local, 'wb')
#     f.retrbinary('RETR %s' % file_remote, fp.write, bufsize)
#     fp.close()
#
#
# def ftp_upload():
#     '''以二进制形式上传文件'''
#
#
# file_remote = 'ftp_upload.txt'
# file_local = 'D:\\test_data\\ftp_upload.txt'
# bufsize = 1024  # 设置缓冲器大小
# fp = open(file_local, 'rb')
# f.storbinary('STOR ' + file_remote, fp, bufsize)
# fp.close()
#
# ftp_download()
# ftp_upload()
# f.quit()