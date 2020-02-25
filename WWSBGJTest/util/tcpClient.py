import json
import socket
import sys



if __name__=="__main__":

    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    s.connect(("192.168.8.205", 57001))

    s.send(b'##0321ST=32;CN=2011;PW=123456;MN=DM000001;CP=&&DataTime=20191223165100;w01001-Rtd=15.294,w01001-Flag=N;w01006-Rtd=12.122,w01006-Flag=N;w01010-Rtd=21.639,w01010-Flag=N;w01014-Rtd=92.088,w01014-Flag=N;w21003-Rtd=78.741,w21003-Flag=N;w21011-Rtd=92.488,w21011-Flag=N;w01019-Rtd=51.248,w01019-Flag=N;w01003-Rtd=3.262,w01003-Flag=N&&A141') # 前面为十六进制数据，后面可接字符串等正文

    print(s.recv(1024))

    s.close()