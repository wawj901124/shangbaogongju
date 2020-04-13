f=open("wenjian.txt","r",encoding="utf8")
#查看多少行
# print(len(f.read().split("\n")))

qianzui = "new_udd."
houzui = "qs_one."
for i in f:

    gong = """
    sd_%s_list = Spider%s.objects.filter(%s=%s_save)
    for sd_%s in sd_%s_list:
        spiderdata.%s.add(sd_%s)
    """%(i,i,i,i,i,i,i,i)
    print("%s"%(gong,))

    # gong = gong.strip()
    # print("%s%s=%s%s"% (qianzui,gong,houzui,gong))
#     gong_list = gong.split(" ")
#     gong_list_len = len(gong_list)
#     if gong_list_len>1:
#         gong = "_".join(gong_list)
#     # gong = gong.strip()
#     # gong = gong.split(" ")
#     gong = """
# %s(){
#         ss -an|grep "^tcp" |grep "%s"|wc -l   #使用ss命令获取以tcp开头的内容且包含LISTEN 的行数
# }
#     """ % (gong,gong)
#     print("%s" % gong)





