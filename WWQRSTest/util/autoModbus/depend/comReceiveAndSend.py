#coding=gb18030

import threading
import time
import serial

class ComThread:
    def __init__(self, Port='COM4',Baudrate=9600,Bytesize=8,Parity ="N",Stopbits=1,Timeout=2,
                 IsNeedExpectDate=None,ExpectDateBytesList=None,
                 ExpectDateBytes=None,Senddatelist=None,Senddate=None,
                 SenderHexDataOrderBytesList=None):
        self.l_serial = None
        self.alive = False
        self.waitEnd = None
        self.ID = None
        self.data = None
        self.port = Port
        self.baudrate = Baudrate   # 设置波特率
        self.bytesize = Bytesize  # 设置数据位
        self.parity = Parity  # 设置校验位
        self.stopbits = Stopbits  # 设置停止位
        self.timeout = Timeout   #超时设置
        self.expectdatebytes=ExpectDateBytes
        self.senddate =Senddate  #发送数据
        self.senddate_list = Senddatelist  # 发送数据
        self.isneedeexpectdate = IsNeedExpectDate
        self.expectdatebyteslist = ExpectDateBytesList
        self.senderhexdataorderbyteslist = SenderHexDataOrderBytesList

    #获取多个


    def waiting(self):
        if not self.waitEnd is None:
            self.waitEnd.wait()

    def SetStopEvent(self):
        if not self.waitEnd is None:
            self.waitEnd.set()
        self.alive = False
        self.stop()

    def start(self):
        self.l_serial = serial.Serial()
        self.l_serial.port = self.port  # 设置端口号
        self.l_serial.baudrate = self.baudrate   # 设置波特率
        self.l_serial.bytesize = self.bytesize  # 设置数据位
        self.l_serial.parity = self.parity  # 设置校验位
        self.l_serial.stopbits = self.stopbits  # 设置停止位
        self.l_serial.timeout = self.timeout   #超时设置
        self.l_serial.open()
        if self.l_serial.isOpen():
            self.waitEnd = threading.Event()
            self.alive = True
            self.thread_read = None
            self.thread_read = threading.Thread(target=self.FirstReader)
            self.thread_read.setDaemon(1)
            self.thread_read.start()
            return True
        else:
            return False

    # def SendDate(self,i_msg,send):
    def SendDate(self,send):
        # lmsg = ''
        isOK = False
        # if isinstance(i_msg):
        #     lmsg = i_msg.encode('gb18030')
        # else:
        #     lmsg = i_msg
        try:
            # 发送数据到相应的处理组件
            self.l_serial.write(send)
            print("发送数据：")
            print(send)
        except Exception as ex:
            pass;
        return isOK

    def FirstReader(self):
        while self.alive:
            time.sleep(0.1)

            data = ''
            data = data.encode('utf-8')

            n = self.l_serial.inWaiting()
            if n:
                 data = data + self.l_serial.read(n)
                 print('get data from serial port:', data)
                 print("接收数据类型：")
                 print(type(data))
            # print("接收的数据：")
            # print(data)
            n = self.l_serial.inWaiting()
            if len(data)>0 and n==0:
                #循环发送列表中的所有数据
                zonghe_list = self.senderhexdataorderbyteslist
                for zonghe_list_one in zonghe_list:  # 循环发送列表中的所有数据
                    print("开始for循环")
                    if zonghe_list_one[1]:  # 如果需要接收
                        if data == zonghe_list_one[2]:
                            print("发送数据：")
                            print(zonghe_list_one[0])
                            self.SendDate(zonghe_list_one[0])
                    else:  # 如果不需要接收，则直接发送数据
                        print("发送数据：")
                        print(zonghe_list_one[0])
                        self.SendDate(zonghe_list_one[0])
                print("结束for循环")
                break  # 退出循环
                # #如果接收到数据：
                # if data !=b'':
                #     zonghe_list = self.senderhexdataorderbyteslist
                #     for zonghe_list_one in zonghe_list:   #循环发送列表中的所有数据
                #         print("开始for循环")
                #         if zonghe_list_one[1]:  #如果需要接收
                #             if data == zonghe_list_one[2]:
                #                 print("发送数据：")
                #                 print(zonghe_list_one[0])
                #                 self.SendDate(zonghe_list_one[0])
                #         else:  #如果不需要接收，则直接发送数据
                #             print("发送数据：")
                #             print(zonghe_list_one[0])
                #             self.SendDate(zonghe_list_one[0])
                #     print("结束for循环")
                #     break  #退出循环
                    # for expectdatebytes in self.expectdatebyteslist:
                    #     if data == expectdatebytes:
                    #         print("预期二进制：")
                    #         print(expectdatebytes)
                    #         print(type(expectdatebytes))
                    #         # #发送数据
                    #         # print("发送数据：")
                    #         # print(self.senddate)
                    #         # self.SendDate(self.senddate)
                    #         #则发送列表数据
                    #         for send_one in self.senddate_list:
                    #             print("发送数据：")
                    #             print(send_one)
                    #             self.SendDate(send_one)




            # n = self.l_serial.inWaiting()
            # if len(data)>0 and n==0:
            #     try:
            #         # temp = data.decode('gb18030') # 解码
            #         temp= data.decode('utf-8')  #解码
            #         print("编码后的数据类型：")
            #         print(type(temp))
            #         print("编码后的数据：")
            #         print(temp)
            #         car,temp = str(temp).split("\n",1)
            #         print(car,temp)
            #
            #         string = str(temp).strip().split(":")[1]
            #         str_ID,str_data = str(string).split("*",1)
            #
            #         print(str_ID)
            #         print(str_data)
            #         print(type(str_ID),type(str_data))
            #
            #         if str_data[-1]== '*':
            #             break
            #         else:
            #             print(str_data[-1])
            #             print('str_data[-1]!=*')
            #     except Exception as e:
            #         print("错误：")
            #         print(e)
            #         print("读卡错误，请重试！\n")

        # self.ID = str_ID
        # self.data = str_data[0:-1]
        self.waitEnd.set()
        self.alive = False

    def stop(self):
        self.alive = False
        self.thread_read.join()
        if self.l_serial.isOpen():
            self.l_serial.close()


class ComThreadTwo(object):
    def __init__(self, Port='COM4',Baudrate=9600,Bytesize=8,Parity ="N",Stopbits=1,Timeout=2,Senddate=None):
        self.l_serial = None
        self.alive = False
        self.waitEnd = None
        self.ID = None
        self.data = None
        self.port = Port
        self.baudrate = Baudrate   # 设置波特率
        self.bytesize = Bytesize  # 设置数据位
        self.parity = Parity  # 设置校验位
        self.stopbits = Stopbits  # 设置停止位
        self.timeout = Timeout   #超时设置
        self.senddate =Senddate  #发送数据


    def waiting(self):
        if not self.waitEnd is None:
            self.waitEnd.wait()

    def SetStopEvent(self):
        if not self.waitEnd is None:
            self.waitEnd.set()
        self.alive = False
        self.stop()

    def start(self):
        self.l_serial = serial.Serial()
        self.l_serial.port = self.port  # 设置端口号
        self.l_serial.baudrate = self.baudrate   # 设置波特率
        self.l_serial.bytesize = self.bytesize  # 设置数据位
        self.l_serial.parity = self.parity  # 设置校验位
        self.l_serial.stopbits = self.stopbits  # 设置停止位
        self.l_serial.timeout = self.timeout   #超时设置
        self.l_serial.open()
        if self.l_serial.isOpen():
            self.waitEnd = threading.Event()
            self.alive = True
            self.thread_read = None
            self.thread_read = threading.Thread(target=self.FirstReader)
            self.thread_read.setDaemon(1)
            self.thread_read.start()
            return True
        else:
            return False

    # def SendDate(self,i_msg,send):
    def SendDate(self,send):
        # lmsg = ''
        isOK = False
        # if isinstance(i_msg):
        #     lmsg = i_msg.encode('gb18030')
        # else:
        #     lmsg = i_msg
        try:
            # 发送数据到相应的处理组件
            self.l_serial.write(send)
            print("发送数据：")
            print(send)
        except Exception as ex:
            pass;
        return isOK

    def FirstReader(self):
        while self.alive:
            time.sleep(0.1)

            data = ''
            data = data.encode('utf-8')

            n = self.l_serial.inWaiting()
            if n:
                 data = data + self.l_serial.read(n)
                 print('get data from serial port:', data)
                 print("接收数据类型：")
                 print(type(data))
            # print("接收的数据：")
            # print(data)
            n = self.l_serial.inWaiting()
            if len(data)>0 and n==0:
                #如果接收到数据：
                if data !=b'':
                    #发送数据
                    print("发送数据：")
                    print(self.senddate)
                    self.SendDate(self.senddate)
                    break   #退出循环



            # n = self.l_serial.inWaiting()
            # if len(data)>0 and n==0:
            #     try:
            #         # temp = data.decode('gb18030') # 解码
            #         temp= data.decode('utf-8')  #解码
            #         print("编码后的数据类型：")
            #         print(type(temp))
            #         print("编码后的数据：")
            #         print(temp)
            #         car,temp = str(temp).split("\n",1)
            #         print(car,temp)
            #
            #         string = str(temp).strip().split(":")[1]
            #         str_ID,str_data = str(string).split("*",1)
            #
            #         print(str_ID)
            #         print(str_data)
            #         print(type(str_ID),type(str_data))
            #
            #         if str_data[-1]== '*':
            #             break
            #         else:
            #             print(str_data[-1])
            #             print('str_data[-1]!=*')
            #     except Exception as e:
            #         print("错误：")
            #         print(e)
            #         print("读卡错误，请重试！\n")

        # self.ID = str_ID
        # self.data = str_data[0:-1]
        self.waitEnd.set()
        self.alive = False

    def stop(self):
        self.alive = False
        self.thread_read.join()
        if self.l_serial.isOpen():
            self.l_serial.close()
#调用串口，测试串口
def run_com():
    rt = ComThread()
    rt.sendport = b'\x03\x03\x04\xF8\x00\x3F\xAC\xF9\x1E'
    try:
        if  rt.start():
            print(rt.l_serial.name)
            rt.waiting()
            print("The data is:%s,The Id is:%s"%(rt.data,rt.ID))
            rt.stop()
        else:
            pass
    except Exception as se:
        print(str(se))

    if rt.alive:
        rt.stop()

    print('')
    print ('End OK .')
    temp_ID=rt.ID
    temp_data=rt.data
    del rt
    return temp_ID,temp_data


if __name__ == '__main__':
    Port = "COM4"
    Baudrate = 9600
    Bytesize = 8
    Parity = "N"
    Stopbits = 1
    # Senddate =self.com_send_date_bytes
    Senddate = None
    Senddatelist = b'\x03\x03\x04\xF8\x00\x3F\xAC\xF9\x1E'
    ExpectDateBytes = b'\x03\x03\x04\xF8\x00\x3F\xAC\xF9\x1E'
    rt = ComThread(Port=Port, Baudrate=Baudrate, Bytesize=Bytesize, Parity=Parity, Stopbits=Stopbits,
                   ExpectDateBytes=ExpectDateBytes, Senddate=Senddate, Senddatelist=Senddatelist)
    try:
        if rt.start():
            print(rt.l_serial.name)
            rt.waiting()
            print("The data is:%s,The Id is:%s" % (rt.data, rt.ID))
            rt.stop()
        else:
            pass
    except Exception as se:
        print(str(se))
    if rt.alive:
        rt.stop()
    print('')
    print('End OK .')
    del rt
    time.sleep(30)  # 等待30秒

    # #设置一个run_com函数，用来运行窗口，便于若其他地方下需要调用串口是可以直接调用main函数
    # ID,data = run_com()
    #
    # print("******")
    # print(ID,data)