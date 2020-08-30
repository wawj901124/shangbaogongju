f=open("wenjian.txt","r",encoding="utf8")
#查看多少行
# print(len(f.read().split("\n")))

qianzui = "new_udd."
houzui = "qs_one."
expect_list = []
yuqi = ""
num_count = 0
for i in f:
    # tup_one = ()
    lie_list = i.split("=")
    # print(lie_list)
    ziduan = lie_list[0].strip()
    # print(ziduan)
    #
    yuqi = """%s = updatedbdata.%s""" % (ziduan,ziduan)
    # num_count = num_count+1
    # # print(yuqi)
    print(yuqi)


    # yuqi = "(%s, %s)"%(ziduan,hanzi)
    # print(yuqi)

#     expect_list.append(ziduan)
# print(expect_list)



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










