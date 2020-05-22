from binascii import *
from crcmod import *

#CRC16-MODBUS
def crc16Add_di(read):
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

def crc16Add_gao(read):
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


if __name__ == '__main__':
    crc16Add_di("01 03 04 F8 00 3F AC")
    crc16Add_gao("01 03 04 F8 00 3F AC")


