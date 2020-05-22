from WWQRSTest.util.handleTxt import HandleTxt
from WWQRSTest.util.handleTxt import HandleTxt
file_name='w_option.txt'
ht = HandleTxt(file_name)

w_list = []
with open('select_option.txt', "r") as f:
    one_list =  f.readlines()
    for one in one_list:
        if 'w' in one:
            # print(one)
            ht.add_content(one)
