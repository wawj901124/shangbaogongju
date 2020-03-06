f=open("wenjian.txt","r",encoding="utf8")
#查看多少行
# print(len(f.read().split("\n")))
qianzui = "new_udd."
houzui = "qs_one."
for i in f:
    gong = i.split("=")[0]
    print("%s%s=%s%s"% (qianzui,gong,houzui,gong))





