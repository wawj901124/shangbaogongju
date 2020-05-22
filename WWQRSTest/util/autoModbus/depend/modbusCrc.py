from binascii import *
from crcmod import *

#参考网址：https://blog.csdn.net/wang_hugh/article/details/83995604
#http://crcmod.sourceforge.net/crcmod.predefined.html#predefined-crc-algorithms
class ModbusCrc(object):

    # CRC16-MODBUS
    def crc16Add_di(self,read):
        crc16 =crcmod.mkCrcFun(0x18005,rev=True,initCrc=0xFFFF,xorOut=0x0000)
        data = read.replace(" ","")
        readcrcout=hex(crc16(unhexlify(data))).upper()
        str_list = list(readcrcout)
        crc_data = "".join(str_list)
        print(crc_data)
        read = read.strip()+' '+crc_data[4:]+' '+crc_data[2:4]
        print('CRC16校验(低字节在前):',crc_data[4:]+' '+crc_data[2:4])
        print('增加Modbus CRC16校验：>>>',read)
        return read

    def crc16Add_gao(self,read):
        crc16 =crcmod.mkCrcFun(0x18005,rev=True,initCrc=0xFFFF,xorOut=0x0000)
        data = read.replace(" ","")
        readcrcout=hex(crc16(unhexlify(data))).upper()
        str_list = list(readcrcout)
        crc_data = "".join(str_list)
        print(crc_data)
        read = read.strip()+' '+crc_data[2:4]+' '+crc_data[4:]
        print('CRC16校验(高字节在前):',crc_data[2:4]+' '+crc_data[4:])
        print('增加Modbus CRC16校验：>>>',read)
        return read

    def crc8(self,read):
        crc16 =crcmod.mkCrcFun(0x131,rev=True,initCrc=0x0000,xorOut=0x0000)
        data = read.replace(" ","")
        readcrcout=hex(crc16(unhexlify(data))).upper()
        str_list = list(readcrcout)
        crc_data = "".join(str_list)
        print(crc_data)
        read = read.strip()+' '+crc_data[2:4]+' '+crc_data[4:]
        print('CRC16校验(高字节在前):',crc_data[2:4]+' '+crc_data[4:])
        print('增加Modbus CRC16校验：>>>',read)
        return read



if __name__ == '__main__':
    hex_str = "01 03 04 F8 00 3F AC"
    mc = ModbusCrc()
    mc.crc16Add_di(hex_str)
    mc.crc16Add_gao(hex_str)
    mc.crc8(hex_str)


