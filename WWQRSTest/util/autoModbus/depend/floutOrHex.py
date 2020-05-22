import struct

#浮点数据转16进制
def float_to_hex(f):
    return hex(struct.unpack('<I', struct.pack('<f', f))[0])

#十六进制转浮点数据
def hex_to_float(h):
    i = int(h,16)
    return struct.unpack('<f',struct.pack('<I', i))[0]

#十六进制字符串转二进制
def str_hex_to_bytes(hex_str):
    str_hex_to_bytes = bytes.fromhex(hex_str)   #十六进制字符串转二进制
    return str_hex_to_bytes

# 字节列表以16进制格式打印数据
def print_bytes_hex(data):
    lin = ['%02X' % i for i in data]
    print(lin)
    print(" ".join(lin))

#处理十六进制文本
def str2hex(s):
    odata = 0;
    su =s.upper()
    for c in su:
        tmp=ord(c)
        if tmp <= ord('9') :
            odata = odata << 4
            odata += tmp - ord('0')
        elif ord('A') <= tmp <= ord('F'):
            odata = odata << 4
            odata += tmp - ord('A') + 10
    return odata

if __name__ == '__main__':
    #字符串转整数:
    int('10')  # 字符串转换成10进制整数
    int('10', 16)  # 字符串转换成16进制整数
    int('0x10', 16)  # 字符串转换成16进制整数
    int('10', 8)  # 字符串转换成8进制整数
    int('010', 8)  # 字符串转换成8进制整数
    int('10', 2)  # 字符串转换成2进制整数
    # 整数之间的进制转换:
    hex(16)  # 10进制转16进制
    oct(8)  # 10进制转8进制
    bin(8)  # 10进制转2进制
    # pre_s= 213.8721466064453
    # print(float_to_hex(pre_s))
    # hex_str = '0x4355df45'
    # ff = hex_to_float(hex_str)
    # print(ff)
    # print('%3f' % ff)
    arr = [0x4B, 0x43, 0x09, 0xA1, 0x01, 0x02, 0xAB, 0x4A, 0x43]
    print_bytes_hex(arr)

    a= '0E'
    a_hex = int(a,16) #字符串转为16进制整数
    print(a_hex)
    a2 =a_hex * 2
    print(a2)
    a2_hex = hex(a2)
    print(a2_hex)
    print(type(a2_hex))
    print('%02X'% a2_hex)
    # a2_hex_str = str(a2_hex)
    # print(a2_hex_str)




    # hex_to_float(pre_s):
    # data = str2hex(pre_s)
    # print(data)
    # print(str(data))   #十进制
    # print(hex(data))   #十六进制

    # result = str_hex_to_bytes(pre_s)
    # print(result)
    # result2 = result+result
    # print(result2)

