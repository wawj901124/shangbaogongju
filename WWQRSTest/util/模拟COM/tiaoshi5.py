# 数据段CRC校验
def shujuduancrc16():  # 进行crc校验，invert为True表示校验码按照先高字节后低字节的顺序存放， False表示校验码按照先低字节后高字节的顺序存放
    x = '\x01\x03\x04\xf8\x00?\xac'
    invert=False
    print(x)
    crc_reg = 0xFFFF
    b = 0xA001
    for x_byte in x:
        # print("x_byte:"+x_byte)
        # time.sleep(30000)
        crc_reg >>= 8
        crc_reg ^= ord(x_byte)

        for i in range(8):
            last = crc_reg % 2
            crc_reg >>= 1
            if last == 1:
                crc_reg ^= b
    s = hex(crc_reg).upper()
    print(s)
    s_list = s.split("X")
    print(s_list)
    s_list_two = s_list[1]
    s_list_two_str = str(s_list_two)
    print(s_list_two_str)
    s_list_two_str_wei = len(s_list_two_str)
    if s_list_two_str_wei == 1:
        s_two = "000%s" % s_list_two_str
    elif s_list_two_str_wei == 2:
        s_two = "00%s" % s_list_two_str
    elif s_list_two_str_wei == 3:
        s_two = "0%s" % s_list_two_str
    elif s_list_two_str_wei == 4:
        s_two = "%s" % s_list_two_str
    else:
        s_two = None
        print("错误：数据段的CRC校验值最大应该为4位，而实际超过4位")
    s = "0X%s" % s_two
    print(s)
    result = s[4:6] + s[2:4] if invert == False else s[2:4] + s[4:6]
    print("--------------------------------")
    print("CRCjiaoyanjieguo")
    print(result)
    print("--------------------------------")
    return result

shujuduancrc16()