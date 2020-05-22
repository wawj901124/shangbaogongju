#python实现输入16进制转换成任意10进制数
def func():
    x = input()
    x = int('0x'+x, 16)
    y = int(input())
    str_out = ''
    while True:
        a = x // y
        b = x % y
        str_out += str(b)
        if a == 0:
            break
        else:
            x = a
    print(str_out[::-1])


if __name__ == '__main__':
    func()
