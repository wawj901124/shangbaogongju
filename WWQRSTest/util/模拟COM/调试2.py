a= b'\x01\x03\x00\x00\x00\x02\xc4\x0b'
b = '\x01\x03\x00\x00\x00\x02\xc4\x0b'
# print(a)
# print(type(a))
# a_str = str(a)
# print(a_str)
# print(type(a_str))

# print(b)
# print(type(b))
# b_byte = bytes(b,encoding="utf-8")
# print(b_byte)
# print(type(b_byte))
# b_str = str(b_byte, encoding="utf-8")
# b_raw_bytes = b_str.encode()
# print(b_str)
# print(type(b_str))

print(b)
print(type(b))
b_two = b.encode('utf-8')#.decode('unicode_escape')
print(b_two)
print(type(b_two))
# b_raw_bytes = b.encode()  #编码
# print(b_raw_bytes)
# print(type(b_raw_bytes))
# b_byte = b_raw_bytes.decode('unicode_escape')  #解码
# print(b_byte)
# print(type(b_byte))

