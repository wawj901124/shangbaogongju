import socket
import sys
import struct
import datetime

from WWQRSTest.util.autoModbus.depend.handleTxt import HandleTxt

SEND_BUF_SIZE = 256
RECV_BUF_SIZE = 256
Communication_Count: int = 0
receive_count: int = 0


class TcpServerReceive(object):
    def __init__(self, ip,port,file_name):
        self.ip = ip
        self.port = port
        self.file_name = file_name
        self.ht = HandleTxt(self.file_name)
        self.sock =self.start_sock()
        self.tcp_server_client = self.tcp_server_start()

    def start_sock(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        return sock

    #启动tcp服务
    def tcp_server_start(self):
        # create socket
        # sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address = (self.ip, self.port)

        # bind port
        print("starting listen on ip %s, port %s" % server_address)
        self.sock.bind(server_address)

        # get the old receive and send buffer size
        s_send_buffer_size = self.sock.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
        s_recv_buffer_size = self.sock.getsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF)
        print("socket send buffer size[old] is %d" % s_send_buffer_size)
        print("socket receive buffer size[old] is %d" % s_recv_buffer_size)

        # set a new buffer size
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, SEND_BUF_SIZE)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, RECV_BUF_SIZE)

        # get the new buffer size
        s_send_buffer_size = self.sock.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
        s_recv_buffer_size = self.sock.getsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF)
        print("socket send buffer size[new] is %d" % s_send_buffer_size)
        print("socket receive buffer size[new] is %d" % s_recv_buffer_size)

        # start listening, allow only one connection

        try:
            self.sock.listen(1)
        except socket.error as e:
            print("fail to listen on port %s" % e)
            sys.exit(1)

        while True:
            print("waiting for connection")
            client, addr = self.sock.accept()
            print("having a connection")
            break

        msg = 'welcome to tcp server' + "\r\n"
        return client

    #获取当前时间-分钟
    def get_now_time_minute(self):
        now_time = datetime.datetime.now()
        timestr = now_time.strftime('%Y%m%d%H%M')
        print("当前时间：%s" % now_time)
        print("时间串：%s" % timestr)
        timestr_minute = '%s00'% timestr
        print("当前时间串（分钟）：%s" % timestr_minute)
        return timestr_minute

    #接受数据
    def tcp_server_receive(self):
        #接受前，先删除之前存在的文件
        self.ht.delete_file()
        #获取当前时间
        now_timestr_minute = self.get_now_time_minute()
        receive_count = 0
        receive_count += 1
        while True:
            print("\r\n")
            msg = self.tcp_server_client.recv(16384)
            # print(msg)
            msg_de = msg.decode('utf-8')
            print("recv len is : [%d]" % len(msg_de))
            print("###############################")
            print(msg_de)
            print("###############################")
            print(type(msg_de))

            self.ht.add_content(msg_de)  # 将接受到的报文保存在一个文件中
            if msg_de == 'disconnect':
                break
            msg = ("hello, client, i got your msg %d times, now i will send back to you " % receive_count)
            self.tcp_server_client.send(msg.encode('utf-8'))
            print("send len is : [%d]" % len(msg))
            print("第%s次接收" % receive_count)
            # 如果当前时间的数据在接受的报文中，则停止退出循环
            if now_timestr_minute in msg_de:
                print("接受到【%s】分钟时间串的数据，停止Tcp服务器接受！"% now_timestr_minute)
                break
            receive_count += 1

    #关闭连接
    def tcp_server_close(self):
        print("finish test, close connect")
        self.tcp_server_client.close()
        self.sock.close()
        print(" close client connect ")

if __name__=='__main__':
    import time
    ip = "192.168.101.123"
    port =  63501
    file_name = 'tcp_server_receive.txt'
    tsr = TcpServerReceive(ip=ip,port=port,file_name=file_name)
    tsr.tcp_server_receive()
    tsr.tcp_server_close()

