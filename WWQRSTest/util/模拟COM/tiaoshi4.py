hex_str = '''B2 CA BB AD'''
b = bytes.fromhex(hex_str)
print(b)
print(type(b))
print(b.decode(encoding='GB18030',errors="replace"))