#脚本说明：
# 1.根据一个因子dev配置文件生成29个因子dev配置文件；
# 2.因子值都是偏移量
# 3.偏移值从3开始
# 4.因子值的长度都是4

f=open("yinzi.txt","r",encoding="utf8")   #打开yinzi.txt文件，编码为utf8
offset_num = 3  #设置初始偏移量
len_guding_num = 4  #设置固定长度
for i in f:   #遍历读取因子文件中的每一行
    yinzi_code = i.strip()   #使用strip函数去掉每行内容的前后空格和换行符
    moban = """<factor factorCode="%s" findMode="OFFSET" offset="%s" mark="" len="%s" decodeType="decode4" operator="*" operand="1"/>"""%(yinzi_code,str(offset_num),str(len_guding_num))  #一条数据的模板
    offset_num = offset_num+len_guding_num
    print(moban)











