select_jian_kong_yin_zi_list = ["w80004","w80001","w80002"]

xinzeng_first_xpath = "/html/body/div[1]/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[2]/div/div/div[1]/ul/li[2]/div[1]/div/div[1]/input"
xinzeng_first_select_ul_xpath = "/html/body/div[4]/div[1]/div[1]/ul"

def get_auto_xinzeng_yinzi_xpath_list(xinzeng_first_xpath,select_jian_kong_yin_zi_list):
    auto_xinzeng_yinzi_xpath_list = []
    xinzeng_yinzi_xpath_list = xinzeng_first_xpath.split("ul/")
    xinzeng_yinzi_xpath_list_one = xinzeng_yinzi_xpath_list[1]
    xinzeng_yinzi_xpath_list_one_list = xinzeng_yinzi_xpath_list_one.split("]/")
    xinzeng_yinzi_xpath_list_one_list_zero = xinzeng_yinzi_xpath_list_one_list[0]
    xinzeng_yinzi_xpath_list_one_list_zero_list = xinzeng_yinzi_xpath_list_one_list_zero.split("[")
    xinzeng_yinzi_xpath_li_num_yuan = xinzeng_yinzi_xpath_list_one_list_zero_list[1]
    print(xinzeng_yinzi_xpath_list)
    print(xinzeng_yinzi_xpath_list_one)
    print(xinzeng_yinzi_xpath_list_one_list)
    print(xinzeng_yinzi_xpath_list_one_list_zero)
    print(xinzeng_yinzi_xpath_list_one_list_zero_list)
    print(xinzeng_yinzi_xpath_li_num_yuan)

    select_jian_kong_yin_zi_list_len = len(select_jian_kong_yin_zi_list)

    for addnum in range(0,select_jian_kong_yin_zi_list_len):
        auto_xinzeng_yinzi_xpath_li_num = int(xinzeng_yinzi_xpath_li_num_yuan)+addnum
        xinzeng_yinzi_xpath_list_one_list_zero_list[1] = str(auto_xinzeng_yinzi_xpath_li_num)
        auto_xinzeng_yinzi_xpath_list_one_list_zero = "[".join(xinzeng_yinzi_xpath_list_one_list_zero_list)
        xinzeng_yinzi_xpath_list_one_list[0] = auto_xinzeng_yinzi_xpath_list_one_list_zero
        auto_xinzeng_yinzi_xpath_list_one = "]/".join(xinzeng_yinzi_xpath_list_one_list)
        xinzeng_yinzi_xpath_list[1] = auto_xinzeng_yinzi_xpath_list_one
        auto_yinzi_xpath = "ul/".join(xinzeng_yinzi_xpath_list)
        print(auto_yinzi_xpath)
        auto_xinzeng_yinzi_xpath_list.append(auto_yinzi_xpath)
    print("新增因子xpath列表：")
    print(auto_xinzeng_yinzi_xpath_list)
    return auto_xinzeng_yinzi_xpath_list


def get_auto_xinzeng_yinzi_select_ul_xpath_list(xinzeng_first_select_ul_xpath,select_jian_kong_yin_zi_list):
    auto_xinzeng_yinzi_select_ul_xpath_list = []

    xinzeng_yinzi_select_ul_xpath_list = xinzeng_first_select_ul_xpath.split("div[")
    xinzeng_yinzi_select_ul_xpath_list_one = xinzeng_yinzi_select_ul_xpath_list[1]
    xinzeng_yinzi_select_ul_xpath_list_one_list = xinzeng_yinzi_select_ul_xpath_list_one.split("]")
    xinzeng_yinzi_select_ul_xpath_list_one_list_zero = xinzeng_yinzi_select_ul_xpath_list_one_list[0]

    print(xinzeng_yinzi_select_ul_xpath_list)
    print(xinzeng_yinzi_select_ul_xpath_list_one_list)
    print(xinzeng_yinzi_select_ul_xpath_list_one_list_zero)

    select_jian_kong_yin_zi_list_len = len(select_jian_kong_yin_zi_list)
    for addnum in range(0, select_jian_kong_yin_zi_list_len):
        auto_xinzeng_yinzi_select_ul_xpath_list_one_list_zero = int(xinzeng_yinzi_select_ul_xpath_list_one_list_zero)+addnum
        xinzeng_yinzi_select_ul_xpath_list_one_list[0] = str(auto_xinzeng_yinzi_select_ul_xpath_list_one_list_zero)
        auto_xinzeng_yinzi_select_ul_xpath_list_one = "]".join(xinzeng_yinzi_select_ul_xpath_list_one_list)
        xinzeng_yinzi_select_ul_xpath_list[1] = auto_xinzeng_yinzi_select_ul_xpath_list_one
        auto_xinzeng_yinzi_select_ul_xpath = "div[".join(xinzeng_yinzi_select_ul_xpath_list)
        auto_xinzeng_yinzi_select_ul_xpath_list.append(auto_xinzeng_yinzi_select_ul_xpath)

    print("新增因子列表选项Xpath：")
    print(auto_xinzeng_yinzi_select_ul_xpath_list)
    return auto_xinzeng_yinzi_select_ul_xpath_list




if __name__ == '__main__':
    # get_auto_xinzeng_yinzi_xpath_list(xinzeng_first_xpath, select_jian_kong_yin_zi_list)
    get_auto_xinzeng_yinzi_select_ul_xpath_list(xinzeng_first_select_ul_xpath, select_jian_kong_yin_zi_list)



