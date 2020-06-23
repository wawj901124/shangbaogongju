# #ascii转字符串
# a_ascii = 97
# b = chr(a_ascii)
# # print(b)
#
# #字符串转ascii
# # abc = '#1,1.86,130.41,128.65,10.62,20.00,161.12,-150.00,6.21,132.38,Z,21322.67,513.89,74.36,18749.54,N,2017-06-12 12:26*'
# # abc = 'PRDIQ23, 08/03/18,12:56:09, +0.566.22, 0, 1.279, 1.279, 3.21, 0.506, 6.35, 17.62, 0.93, 0.09, 12.7'
# # abc = '2020 05 05 11 52 50    -6.4     0.9   2.783   1.5   0.6  10.0 187 184   6   0  152.9   0.0   1.6  0.0  0.0  0.0  23.45      0.675    0.002  14.2   2.0   11.0  50  64  28      -1.5231      23.7994       -1094.050   0.0090 0'
#
# abc = '1D0\x00'
# # for i in abc:
# #     x = ord(i)   #字节转为ASCII码
# #     print(x)
# #     print(type(x))
# #     erjinzhi = bin(x)
# #     print(erjinzhi)
# #     print(type(erjinzhi))
# print(abc)
# print(type(abc))
# b_abc =bytes(abc ,'utf-8')
# print(b_abc)
# print(type(b_abc))
# b_two_abc = abc.encode('utf-8')
# print(b_two_abc)
# print(type(b_two_abc))
# import datetime
# now_time = datetime.datetime.now()
# print(now_time)
import time
time.sleep(0)

