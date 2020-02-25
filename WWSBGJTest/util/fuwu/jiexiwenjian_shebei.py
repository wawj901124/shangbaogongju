#1.读取文档内容
with open('DATA.log',encoding='UTF-8') as file_object:
    contents = file_object.read()

# print(type(contents))
# print(contents)
#2.分割出各个手机号，看手机号间有什么规律，比如以逗号隔开或有空格
content_list = contents.split("\n\n")  #把获取的内容分割成列表
# print(content_list)

content_list_effective_list = []

content_list_len = len(content_list)  #获取列表长度
for i in range(0,content_list_len):  #遍历列表，统计手机号
    if "CP=&&DataTime=" in content_list[i]:
        content_list_effective_list.append(content_list[i])

print(content_list_effective_list)
#3.统计手机号
phone_list = []



content_list_effective_list_len = len(content_list_effective_list)  #获取列表长度
for i in range(0,content_list_effective_list_len):  #遍历列表，统计手机号

    fengelong = content_list_effective_list[i].split("MN=")
    # print(fengelong)
    if fengelong != ['']:
        fengelong_one_len = len(fengelong[0])
        # print(fengelong_one_len)
        qiepian_qian_num = fengelong_one_len+3
        fengelong_two_split_list = fengelong[1].split(";CP=&&DataTime=")
        shebei_MN = fengelong_two_split_list[0]
        # print(shebei_MN)
        if shebei_MN not in phone_list:
            phone_list.append(shebei_MN)
print(phone_list)


#4.计算重复次数
phone_list_len = len(phone_list)
print(phone_list_len)
phone_list_sort = sorted(phone_list)
print(phone_list_sort)

print("设备MN号维度统计")
for i in range(0,phone_list_len):
    count_num = 0
    for j in range(0, content_list_len):  # 遍历列表，统计手机号
        if phone_list_sort[i] in content_list[j]:
            count_num = count_num +1
    print("%s出现的次数：%s" % (phone_list_sort[i], count_num))



    # if phone_list[i] in content_list
    # count_num = content_list.count(phone_list[i])  #计算一个手机号在列表中出现的次数
    # print("%s出现的次数：%s" % (phone_list[i],count_num))