def dec_hex(
        str1):  # 十转十六

    a = str(hex(eval(str1)))
    print('十进制: %s  转换成 十六进制为：%s' % (str1, a))
    return a


def hex_dec(str2):  # 十六转十
    b = eval(str2)
    print('十六进制： %s 转换成十进制为：%s:' % (str2, b))
    return b

import struct

def float_to_hex(f):
    return hex(struct.unpack('<I', struct.pack('<f', f))[0])

def float_to_hex_da(f):
    return hex(struct.unpack('<I', struct.pack('>f', f))[0])


float_to_hex(17.5)  # Output: '0x418c0000'


if __name__ == '__main__':
    # str1 = input("十进制数值:")
    # print(dec_hex(str1))
    # str2 = input("十六进制数值:")
    str2 = '0x3facf800'
    print(hex_dec(str2))
    fstr = 1.351318359375
    # fstr = 1.351
    print(float_to_hex(fstr))
    print(float_to_hex_da(fstr))
    import struct

    # s = 'F8003FAC'
    # print(s)
    # # <是小端，>是大端，f代表浮点数
    # print(struct.unpack('<f', bytes.fromhex(s))[0])  # 小端
    # print(struct.unpack('>f', bytes.fromhex(s))[0])  # 小端
    # 输出：120.40420532226562
    # s = float('6.55563714424545E-10')
    # print(struct.pack('<f', s).hex())  # 小端
    # # 输出：32333430
    # print(struct.pack('>f', s).hex())  # 大端
    # 输出：30343332
