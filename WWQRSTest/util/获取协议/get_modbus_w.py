from WWQRSTest.util.handleTxt import HandleTxt
from WWQRSTest.util.handleTxt import HandleTxt
file_name='modbus_w.txt'
ht = HandleTxt(file_name)

w_list = []
with open('modbus.cfg', "r") as f:
    one_list =  f.readlines()
    for one in one_list:
        if 'w' in one:
            # print(one)
            ht.add_content(one)