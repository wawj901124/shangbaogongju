import serial
import binascii
ser = serial.Serial()

def port_open():
    ser.port = 'COM4'           #设置端口号
    ser.baudrate = 9600     #设置波特率
    ser.bytesize = 8        #设置数据位
    ser.parity = "N"        #设置校验位
    ser.stopbits = 1        #设置停止位
    ser.open()              #打开串口,要找到对的串口号才会成功
    if(ser.isOpen()):
        print("打开成功")
    else:
        print("打开失败")


def port_close():
    ser.close()
    if (ser.isOpen()):
        print("关闭失败")
    else:
        print("关闭成功")

def send(send_data):
    if (ser.isOpen()):
        # ser.write(send_data.encode('utf-8'))  #utf-8 编码发送
        # ser.write(binascii.a2b_hex(send_data))  #Hex发送
        ser.write(send_data)
        print("发送数据：",send_data)
    else:
        print("发送失败")


if __name__ == '__main__':
    port_open()
    send_data=b'\x03\x03\x04\xF8\x00\x3F\xAC\xF9\x1E'
    send(send_data)
    # port_close()

