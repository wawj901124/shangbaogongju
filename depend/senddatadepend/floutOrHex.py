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

#处理字符串转为字节
def strtobytes(s):
    b_s = bytes(s ,'utf-8')   #字符串转为字节
    print(b_s)
    return b_s

#处理字符串转为字节
def strtobytestwo(s):
    b_s = s.encode('utf-8')   #字符串转为字节
    print(b_s)
    return b_s

if __name__ == '__main__':
    f = 200.129685
    h = float_to_hex(f)
    print(h)
    hex_to_hex_txt(hex_to_hex_txt)
