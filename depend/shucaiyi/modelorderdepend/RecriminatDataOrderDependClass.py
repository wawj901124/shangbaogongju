# ----------------------------------------------------------------------
import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wanwenyc.settings")
django.setup()
# ----------------------------------------------------------------------
#独运行某一个py文件时会出现如下错误：django.core.exceptions.AppRegistryNotReady: Apps aren't loaded yet.，以上内容可以解决此问题,加载django中的App


class RecriminatDataOrderDepend(object):

    def makeRecriminatDataOrderList(self,depend_id):
        recriminat_data_order_list = []

        from shucaiyidate.modelsorder import RecriminatDataOrder
        RecriminatDataOrder_list = RecriminatDataOrder.objects.filter(xieyitestcase_id=depend_id)
        RecriminatDataOrder_list_count = RecriminatDataOrder_list.count()
        if RecriminatDataOrder_list_count==0:
            pass
        else:
            for RecriminatDataOrder_one in RecriminatDataOrder_list:
                recriminat_data_order_one_list = []
                recriminat_data_order_one_list.append(RecriminatDataOrder_one.send_wait_time)
                recriminat_data_order_one_list.append(RecriminatDataOrder_one.com_send_date)
                # recriminat_data_order_one_list.append(RecriminatDataOrder_one.is_need_expect)
                expect_data_str= RecriminatDataOrder_one.com_expect_date
                print("原数据：%s" % expect_data_str)
                # expect_data_bytes =bytes(expect_data_str,'utf-8')
                # print("原数据字节：")
                # print(expect_data_bytes)
                # expect_data_bytes_to_str = str(expect_data_bytes, encoding="utf-8")
                # print("原数据字节转为字符串：")
                # print(expect_data_bytes_to_str)
                # expect_data_bytes_to_str_with_huiche = expect_data_bytes_to_str+r"\r\n"  #字符串组合回车换行
                # print("原数据字节转为字符串带回车换行：")
                # print(expect_data_bytes_to_str_with_huiche)

                if expect_data_str == None:
                    recriminat_data_order_one_list.append(expect_data_str)
                else:
                    #有双斜杠转发单斜杠
                    expect_data_str_new = expect_data_str.encode("gbk").decode("unicode_escape")  #将字符串先编码后解码，解决单斜杠，变为双斜杠问题
                    print("双斜杠变为单斜杠的数据：%s" % expect_data_str_new)
                    recriminat_data_order_one_list.append(expect_data_str_new)

                recriminat_data_order_list.append(recriminat_data_order_one_list)

        print("recriminat_data_order_list:")
        print(recriminat_data_order_list)
        return recriminat_data_order_list


recriminatdataorderdepend = RecriminatDataOrderDepend()

if __name__ == '__main__':
    my_list = recriminatdataorderdepend.makeRecriminatDataOrderList("15")
    print(my_list[0][1])




