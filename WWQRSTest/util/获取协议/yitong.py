with open('w_option.txt', "r") as f:
    w_option_list =  f.readlines()

with open('modbus_w.txt', "r") as f:
    modbus_w_list =  f.readlines()

# print(w_option_list)
# print(modbus_w_list)

w_option_one_list=[]
for w_option_one in w_option_list:
    one = w_option_one.split(' ')[0]
    if one != '\n':
        w_option_one_list.append(one)

# print(w_option_one_list)
# print(modbus_w_list)
end_list=[]
for w_option_one_list_one in w_option_one_list:
    for modbus_w_one in modbus_w_list:
        modbus_w_one_one = modbus_w_one.split(';')[0]
        print(modbus_w_one_one)
        if len(modbus_w_one_one)>1:
            m_one = modbus_w_one_one.split('=')[1]
            if w_option_one_list_one == m_one:
                end_list.append(w_option_one_list_one)
                break

print(end_list)
