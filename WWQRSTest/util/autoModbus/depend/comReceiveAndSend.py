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
        self.baudrate = Baudrate   # ���ò�����
        self.bytesize = Bytesize  # ��������λ
        self.parity = Parity  # ����У��λ
        self.stopbits = Stopbits  # ����ֹͣλ
        self.timeout = Timeout   #��ʱ����
        self.expectdatebytes=ExpectDateBytes
        self.senddate =Senddate  #��������
        self.senddate_list = Senddatelist  # ��������
        self.isneedeexpectdate = IsNeedExpectDate
        self.expectdatebyteslist = ExpectDateBytesList
        self.senderhexdataorderbyteslist = SenderHexDataOrderBytesList

    #��ȡ���


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
        self.l_serial.port = self.port  # ���ö˿ں�
        self.l_serial.baudrate = self.baudrate   # ���ò�����
        self.l_serial.bytesize = self.bytesize  # ��������λ
        self.l_serial.parity = self.parity  # ����У��λ
        self.l_serial.stopbits = self.stopbits  # ����ֹͣλ
        self.l_serial.timeout = self.timeout   #��ʱ����
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
            # �������ݵ���Ӧ�Ĵ������
            self.l_serial.write(send)
            print("�������ݣ�")
            print(send)
        except Exception as ex:
            pass;
        return isOK
    #һ��һ����б�����
    def GetZongheListOne(self,zonghe_list):
        for zonghe_list_one in zonghe_list:
            yield zonghe_list_one


    def FirstReader(self):

        zonghe_list = self.senderhexdataorderbyteslist
        print("zonghe_list��")
        print(zonghe_list)

        is_end_while = False  # �Ƿ����ѭ����־
        zonghe_list_len = len(zonghe_list)
        #����ѭ���б�
        end_while_num = 1


        for zonghe_list_one in zonghe_list:
            print("��Ҫ������շ����ݸ�����")
            print(zonghe_list_len)
            print("���ڴ�����շ����ݸ�����")
            print(end_while_num)
            print("���ڴ�����շ����ݣ�")
            print(zonghe_list_one)

            com_send_date_one_bytes = zonghe_list_one[0]
            is_need_expect = zonghe_list_one[1]
            com_expect_date_bytes = zonghe_list_one[2]
            is_need_after_expect = zonghe_list_one[3]
            is_just_one = zonghe_list_one[4]
            is_sand_data = False

            #����һ�����ݵ��շ�
            while self.alive:
                time.sleep(0.1)

                data = ''
                data = data.encode('utf-8')

                n = self.l_serial.inWaiting()
                if n !=0:
                    print("n��ֵ��")
                    print(n)
                if n:
                     data = data + self.l_serial.read(n)
                     print('get data from serial port:', data)
                     print("�����������ͣ�")
                     print(type(data))
                # print("���յ����ݣ�")
                # print(data)
                n = self.l_serial.inWaiting()

                # print("data���ݣ�")
                # print(data)

                if is_need_expect:    #�����������ǰ��Ҫ�������ݣ�����н������ݺ������ݲ���
                    if len(data) > 0 and n == 0:
                        #�鿴���յ������Ƿ��Ԥ�ڽ��ƥ�䣬Ȼ��ظ�����
                        print("��������ǰ���յ������ݣ�")
                        print(data)
                        if data == com_expect_date_bytes:
                            print("��������ǰ������յ���Ӧָ��������ݣ�")

                            print(com_send_date_one_bytes)
                            self.SendDate(com_send_date_one_bytes)
                            print("�Ѿ�����ĸ�����")
                            print(end_while_num)
                            end_while_num = end_while_num+1  #��1
                            break #����whileѭ��

                if is_need_after_expect: #����������ݺ���Ҫ�������ݣ� ����з������ݺ���֤���յ�����
                    if data == com_expect_date_bytes:
                        print("�������ݺ���յ�����Ԥ�ڵ����ݣ�")
                        print(data)
                        print("�Ѿ�����ĸ�����")
                        print(end_while_num)
                        end_while_num = end_while_num + 1  # ��1
                        break # ����whileѭ��

                    if is_just_one:  #�����ֻ����һ������
                        if not is_sand_data:   #���û�з������ݣ���������,ֻ����һ������
                            print("�������ݺ����յ���Ӧ�ظ���ֻ����һ�����ݣ��������ݣ�")
                            print(com_send_date_one_bytes)
                            self.SendDate(com_send_date_one_bytes)
                            is_sand_data = True  #������ɺ󣬲��ٷ���
                    else:
                        print("�������ݺ����յ���Ӧ�ظ��������������ݣ��������ݣ�")
                        print(com_send_date_one_bytes)
                        self.SendDate(com_send_date_one_bytes)



                if not is_need_expect and not is_need_after_expect:  #��������Ƿ���ǰ�������ݣ�Ҳ���Ƿ��ͺ�������ݣ��򴿷�������
                    print("���������ݣ�")
                    if is_just_one:
                        print("�����������ݣ�ֻ����һ�����ݡ����������ݣ�")
                        print(com_send_date_one_bytes)
                        self.SendDate(com_send_date_one_bytes)
                    else:
                        for i in range(1,61,1):
                            print("�����������ݣ�����60�η�������֮��%s�Ρ����������ݣ�" % str(i))
                            print(com_send_date_one_bytes)
                            self.SendDate(com_send_date_one_bytes)

                    print("�Ѿ�����ĸ�����")
                    print(end_while_num)
                    end_while_num = end_while_num + 1  # ��1
                    break  # ����whileѭ��










                # if len(data)>0 and n==0:
                #     #ѭ�������б��е���������
                #     zonghe_list = self.senderhexdataorderbyteslist
                #     for zonghe_list_one in zonghe_list:  # ѭ�������б��е���������
                #         print("��ʼforѭ��")
                #         if zonghe_list_one[1]:  # �����Ҫ����
                #             if data == zonghe_list_one[2]:
                #                 print("�������ݣ�")
                #                 print(zonghe_list_one[0])
                #                 self.SendDate(zonghe_list_one[0])
                #         else:  # �������Ҫ���գ���ֱ�ӷ�������
                #             print("�������ݣ�")
                #             print(zonghe_list_one[0])
                #             self.SendDate(zonghe_list_one[0])
                #     print("����forѭ��")
                #     break  # �˳�ѭ��
                # else:
                #     print("���ڿ���״̬")
                #     # #������յ����ݣ�
                #     # if data !=b'':
                #     #     zonghe_list = self.senderhexdataorderbyteslist
                #     #     for zonghe_list_one in zonghe_list:   #ѭ�������б��е���������
                #     #         print("��ʼforѭ��")
                #     #         if zonghe_list_one[1]:  #�����Ҫ����
                #     #             if data == zonghe_list_one[2]:
                #     #                 print("�������ݣ�")
                #     #                 print(zonghe_list_one[0])
                #     #                 self.SendDate(zonghe_list_one[0])
                #     #         else:  #�������Ҫ���գ���ֱ�ӷ�������
                #     #             print("�������ݣ�")
                #     #             print(zonghe_list_one[0])
                #     #             self.SendDate(zonghe_list_one[0])
                #     #     print("����forѭ��")
                #     #     break  #�˳�ѭ��
                #         # for expectdatebytes in self.expectdatebyteslist:
                #         #     if data == expectdatebytes:
                #         #         print("Ԥ�ڶ����ƣ�")
                #         #         print(expectdatebytes)
                #         #         print(type(expectdatebytes))
                #         #         # #��������
                #         #         # print("�������ݣ�")
                #         #         # print(self.senddate)
                #         #         # self.SendDate(self.senddate)
                #         #         #�����б�����
                #         #         for send_one in self.senddate_list:
                #         #             print("�������ݣ�")
                #         #             print(send_one)
                #         #             self.SendDate(send_one)




                # n = self.l_serial.inWaiting()
                # if len(data)>0 and n==0:
                #     try:
                #         # temp = data.decode('gb18030') # ����
                #         temp= data.decode('utf-8')  #����
                #         print("�������������ͣ�")
                #         print(type(temp))
                #         print("���������ݣ�")
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
                #         print("����")
                #         print(e)
                #         print("�������������ԣ�\n")

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
        self.baudrate = Baudrate   # ���ò�����
        self.bytesize = Bytesize  # ��������λ
        self.parity = Parity  # ����У��λ
        self.stopbits = Stopbits  # ����ֹͣλ
        self.timeout = Timeout   #��ʱ����
        self.senddate =Senddate  #��������


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
        self.l_serial.port = self.port  # ���ö˿ں�
        self.l_serial.baudrate = self.baudrate   # ���ò�����
        self.l_serial.bytesize = self.bytesize  # ��������λ
        self.l_serial.parity = self.parity  # ����У��λ
        self.l_serial.stopbits = self.stopbits  # ����ֹͣλ
        self.l_serial.timeout = self.timeout   #��ʱ����
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
            # �������ݵ���Ӧ�Ĵ������
            self.l_serial.write(send)
            print("�������ݣ�")
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
                 print("�����������ͣ�")
                 print(type(data))
            # print("���յ����ݣ�")
            # print(data)
            n = self.l_serial.inWaiting()
            if len(data)>0 and n==0:
                #������յ����ݣ�
                if data !=b'':
                    #��������
                    print("�������ݣ�")
                    print(self.senddate)
                    self.SendDate(self.senddate)
                    break   #�˳�ѭ��



            # n = self.l_serial.inWaiting()
            # if len(data)>0 and n==0:
            #     try:
            #         # temp = data.decode('gb18030') # ����
            #         temp= data.decode('utf-8')  #����
            #         print("�������������ͣ�")
            #         print(type(temp))
            #         print("���������ݣ�")
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
            #         print("����")
            #         print(e)
            #         print("�������������ԣ�\n")

        # self.ID = str_ID
        # self.data = str_data[0:-1]
        self.waitEnd.set()
        self.alive = False

    def stop(self):
        self.alive = False
        self.thread_read.join()
        if self.l_serial.isOpen():
            self.l_serial.close()
#���ô��ڣ����Դ���
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
    time.sleep(30)  # �ȴ�30��

    # #����һ��run_com�������������д��ڣ������������ط�����Ҫ���ô����ǿ���ֱ�ӵ���main����
    # ID,data = run_com()
    #
    # print("******")
    # print(ID,data)