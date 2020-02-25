#1.读取文档内容
with open('DATA.log',encoding='UTF-8') as file_object:
    contents = file_object.read()

# print(type(contents))
# print(contents)
#2.分割出各个手机号，看手机号间有什么规律，比如以逗号隔开或有空格
content_list = contents.split("\n\n")  #把获取的内容分割成列表
# print(content_list)
#3.统计手机号
phone_list = []


content_list_len = len(content_list)  #获取列表长度
for i in range(0,content_list_len):  #遍历列表，统计手机号
    one_line_data = content_list[i]

    #换行显示
    one_line_data_len = len(one_line_data)
    print(one_line_data_len)
    print('\n'.join(one_line_data[i:i + 100] for i in range(0, len(one_line_data), 100)))

