#coding=gb18030

import threading
import time
import serial

class ComThread:
    def __init__(self, Port='COM4',Baudrate=9600,Bytesize=8,Parity ="N",Stopbits=1,Timeout=2):
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
                    #�жϽ��յ��������Ƿ�������ļ�һ�£����Է��ͺ���У�顣�����첽У��
                    #��������
                    orige_data = '03 03 04 F8 00 3F AC F9 1E'
                    #�Կշָ��ַ���
                    orige_data_list = orige_data.split(' ')
                    print()

                    senddata =  r'\x01\x03\x04\xF8\x00\x3F\xAC\xF9\x1E'

                    self.SendDate(senddata)
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
def main():
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

    #����һ�����������������д��ڣ������������ط�����Ҫ���ô����ǿ���ֱ�ӵ���main����
    ID,data = main()

    print("******")
    print(ID,data)