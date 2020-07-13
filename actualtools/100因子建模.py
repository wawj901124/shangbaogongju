f=open("100因子.txt","r",encoding="utf8")
#查看多少行
# print(len(f.read().split("\n")))

qianzui = "new_udd."
houzui = "qs_one."
expect_list = []
yuqi = ""
chushizhi = 3
yinzi_list = []
for i in f:
    lie_list = i.split("|")
    ziduan = lie_list[2].strip()
    if ziduan not in yinzi_list:
        yinzi_list.append(ziduan)
    # ziduanzhi = chushizhi

    # yuqi = """<factor factorCode="%s" findMode="OFFSET" offset="%s" mark="" len="4" decodeType="decode2" operator="*" operand="1"/>"""%(str(ziduan),str(ziduanzhi))
    # print(yuqi)
    #
    # chushizhi=chushizhi+4

    # expect_list.append(ziduan)
print(len(yinzi_list))
for one in yinzi_list:
    # print(one)
    ziduan=one
    ziduanzhi = chushizhi
    yuqi = """<factor factorCode="%s" findMode="OFFSET" offset="%s" mark="" len="4" decodeType="decode2" operator="*" operand="1"/>"""%(str(ziduan),str(ziduanzhi))
    print(yuqi)
    chushizhi = chushizhi + 4

chu_str = "01 03 E4"
for one in yinzi_list:
    one_str = " 41 A4 00 00"
    chu_str = chu_str+one_str

print(chu_str)







# for i in f:
#     lie_list = i.split("=")
#     lei_one = lie_list[0]
#     lei_one = lei_one.strip()
#     lei_two = lie_list[1]
#     lei_two = lei_two.strip()
#     lei = """
#         <tr>
#             <td>
#                 <label>%s:</label>
#             </td>
#             <td>
#                 <input id="%s" name="%s" type="text" value="{{ xieyiconfigdate.%s|default:""  }}"/>
#             </td>
#         </tr>
#     """ %(lei_two,lei_one,lei_one,lei_one)
#     # lei = """
#     #     <tr>
#     #         <td>
#     #             <label>%s:</label>
#     #         </td>
#     #         <td>
#     #             <input type="radio" id="%s" name="%s"  value="true"  {%% if xieyiconfigdate.%s == 1 %%} checked="checked"{%% endif %%}>是
#     #             <input type="radio" id="%s" name="%s"  value="false" {%% if xieyiconfigdate.%s == 0 %%} checked="checked"{%% endif %%}>否
#     #         </td>
#     #     </tr>
#     # """ %(lei_two,lei_one,lei_one,lei_one,lei_one,lei_one,lei_one)
#     print(lei)










