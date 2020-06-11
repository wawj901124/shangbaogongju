

zonghe_list = [['03 10 00 00 00 12 24 1B 50 44 4B FC EF 44 53 8C 3C 44 56 C0 00 44 55 E6 BB 44 50 39 F8 44 4C B5 42 44 46 E0 97 44 4D 59 69 44 4F 66 86', False, '03 10 00 00 00 12 41 E6', '812.42,847.95', True],
               ['03 10 00 00 00 12 24 1B 50 44 4B 1B 50 44 4B 1B 50 44 4B C0 00 44 55 E6 BB 44 50 39 F8 44 4C B5 42 44 46 E0 97 44 4D 59 69 44 4F 66 86',
                   False, '03 10 00 00 00 12 41 E6', '812.42,847.95', True]]

def foo(zonghe_list):
    for zonghe_list_one in zonghe_list:
        yield zonghe_list_one

z = foo(zonghe_list)
print(z)
for i in z:
    print(i)

# for i in range(5):
#     print(next(foo(zonghe_list)))





