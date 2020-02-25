#1.读取文档内容
with open('data.log',encoding='UTF-8') as file_object:
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
print("列表长度:%s" % content_list_effective_list_len)
for i in range(0,content_list_effective_list_len):  #遍历列表，统计手机号
    qiepian = content_list_effective_list[i][119:133]
    # print("切片：%s"%qiepian)
    # fengelong = content_list_effective_list[i].split("CP=&&DataTime=")
    # print(len("CP=&&DataTime="))
    # print(fengelong)
    # print(len(fengelong[0]))
    if qiepian not in phone_list:
        phone_list.append(qiepian)
print(phone_list)
#4.计算重复次数
phone_list_len = len(phone_list)

print("日期维度统计")
for i in range(0,phone_list_len):
    count_num = 0
    for j in range(0, content_list_len):  # 遍历列表，统计手机号
        if phone_list[i] in content_list[j]:
            count_num = count_num +1
    print("%s出现的次数：%s" % (phone_list[i], count_num))



