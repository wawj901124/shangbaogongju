import os
#打开需要替换的文件
with open('yuan.txt','r',encoding='utf-8') as ca: #打开文件
    wc = ca.readlines() #把文件内容读到列表中

pre_list = []

f=open("wenjian.txt","r",encoding="utf8")
#查看多少行
# print(len(f.read().split("\n")))

qianzui = "new_udd."
houzui = "qs_one."
expect_list = []
yuqi = ""

tihuan_list = []
for i in f:
    tihuan_one_list = []
    lie_list = i.split("=")
    ziduan = lie_list[0].strip()
    expect_list.append(ziduan)
    # print(ziduan)
    yuqi = """senderhexdataorderform.%s"""% ziduan
    print(yuqi)
    b = yuqi
    c = """senderhexdataorderform.%s.value"""% ziduan
    tihuan_one_list.append(b)
    tihuan_one_list.append(c)
    tihuan_list.append(tihuan_one_list)

for tihuan_one_list in tihuan_list:
    old = tihuan_one_list[0]
    new = tihuan_one_list[1]
    wc_len = len(wc)
    for i in range(0,wc_len):
        if old in wc[i]:
            wc[i] = wc[i].replace(old,new)

print("替换后的wc:")
new_file_name = "new.txt"
if os.path.exists(new_file_name):
    os.remove(new_file_name)
with open(new_file_name, "w",encoding='utf-8') as f:
    for one in wc:
        f.write(one)
        print(one)









# print("替换后的内容：")
# for pre_one in pre_list:
#     print(pre_one)






