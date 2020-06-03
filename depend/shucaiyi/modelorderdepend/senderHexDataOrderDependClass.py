# ----------------------------------------------------------------------
import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wanwenyc.settings")
django.setup()
# ----------------------------------------------------------------------
#独运行某一个py文件时会出现如下错误：django.core.exceptions.AppRegistryNotReady: Apps aren't loaded yet.，以上内容可以解决此问题,加载django中的App


class SenderHexDataOrderDepend(object):

    def makeSenderHexDataOrderList(self,depend_id):
        sender_hex_data_order_list = []

        from shucaiyidate.modelsorder import SenderHexDataOrder
        SenderHexDataOrder_list = SenderHexDataOrder.objects.filter(xieyitestcase_id=depend_id)
        SenderHexDataOrder_list_count = SenderHexDataOrder_list.count()
        if SenderHexDataOrder_list_count==0:
            pass
        else:
            for SenderHexDataOrder_one in SenderHexDataOrder_list:
                sender_hex_data_order_one_list = []
                sender_hex_data_order_one_list.append(SenderHexDataOrder_one.com_send_date)
                sender_hex_data_order_one_list.append(SenderHexDataOrder_one.is_need_expect)
                sender_hex_data_order_one_list.append(SenderHexDataOrder_one.com_expect_date)
                sender_hex_data_order_one_list.append(SenderHexDataOrder_one.xieyi_jiexi_expect_result)
                sender_hex_data_order_list.append(sender_hex_data_order_one_list)

        print("sender_hex_data_order_list:")
        print(sender_hex_data_order_list)
        return sender_hex_data_order_list


senderhexdataorderdepend = SenderHexDataOrderDepend()

if __name__ == '__main__':
    senderhexdataorderdepend.makeSenderHexDataOrderList("1")



