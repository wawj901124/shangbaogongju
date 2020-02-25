# 计算字符串中空格或者ASCII个数
s = input("请输入字符串：")
a = 0  # 用来记录空格个数
for ch in s:
    if ch == ' ':  # if ord(ch)==32:
        a += 1
print("空格的个数是：", a)
i = 0
while i < len(s):
    ch = s[i]
    if ch == '':
        a += 1
    i += 1

b = 0  # 用来记录ascii个数
for ch in s:
    if ord(ch) <= 127:
        b += 1
print("ascii字符个数是：", b)
# 请输入字符串：n n n n
# 空格的个数是： 3
# ascii字符个数是： 7
