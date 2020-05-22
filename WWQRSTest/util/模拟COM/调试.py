orige_data = '01 03 04 F8 00 3F AC F9 1E'
# 以空分隔字符串
send_data_hex_str_list = orige_data.split(' ')
print(send_data_hex_str_list)

send_data_bytes = b''
print(send_data_hex_str_list)
for i in send_data_hex_str_list:
    str_hex_to_bytes = bytes.fromhex(i)  # 十六进制字符串转二进制
    send_data_bytes = send_data_bytes+str_hex_to_bytes

print(send_data_bytes)


# he_data_pre = "\x"
# he_data = "\x".join(orige_data_list)
# he_data_end = '%s%s'%(he_data_pre,he_data)
# print(he_data_end)
# print(type(he_data_end))
#
# # he_data_end =  '\x01\x03\x00\x00\x00\x02\xc4\x0b'
# print(he_data_end)
# print(type(he_data_end))
#
#
# he_data_end_bytes = he_data_end.encode('utf-8')  #编码
# print(he_data_end_bytes)
# print(type(he_data_end_bytes))