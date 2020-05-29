f=open("wenjian.txt","r",encoding="utf8")
#查看多少行
# print(len(f.read().split("\n")))


qianzui = "new_udd."
houzui = "qs_one."
expect_list = []
for i in f:
    lie_list = i.split("\t")
    # print(lie_list)
    lie_list_one = lie_list[0]
    expect_list.append(lie_list)
    print(lie_list_one)

    # for lie_one in lie_list:
    #     lie_one = lie_one.strip("\t")
    #     expect_list.append(lie_one)

print(expect_list)
print(len(expect_list))

yinzi = "a01016"
expect_list_len =len(expect_list)
for i in range(0,expect_list_len):
    if yinzi in expect_list[i]:
        print(i)
        print(expect_list[i])
    # else:
    #     print("不存在因子：%s" % yinzi)