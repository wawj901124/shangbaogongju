# 再次打开文件，此时获取每行的内容
with open("1985_N_4.txt", "r", encoding='utf-8') as f:
    result_list = f.readlines()

print(result_list)
for one in result_list:
    print(one)