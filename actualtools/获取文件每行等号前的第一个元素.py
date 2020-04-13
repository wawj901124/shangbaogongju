f=open("wenjian.txt","r",encoding="utf8")
#查看多少行
# print(len(f.read().split("\n")))

qianzui = "new_udd."
houzui = "qs_one."
for i in f:

    gong = """
    from spiderdata.models import Spider%s

    %s_save = direcotr_and_studio_and_label_list[0][0]
    is_exist_%s_count = Spider%s.objects.filter(%s=%s_save).count()
    if is_exist_%s_count != 0:
        print("导演已经存在")
    else:
        spider%s = Spider%s()
        spider%s.%s = %s_save
        spider%s.%s_url = direcotr_and_studio_and_label_list[0][1]
        spider%s.save()
        print("已经成功保存导演到相应数据库中")
    """%(i,i,i,i,i,i,i,i,i,i,i,i,i,i,i)
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





