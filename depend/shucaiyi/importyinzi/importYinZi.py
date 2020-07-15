# ----------------------------------------------------------------------
import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wanwenyc.settings")
django.setup()
# ----------------------------------------------------------------------
#独运行某一个py文件时会出现如下错误：django.core.exceptions.AppRegistryNotReady: Apps aren't loaded yet.，以上内容可以解决此问题,加载django中的App


class AutoImportYinZi(object):

    def autoimportyinzi(self,biaoming,guobiao):
        f = open("all_yinzi.txt", "r", encoding="utf8")
        data_id_list = []
        data_id_dict = {}
        num_count = 0
        for i in f:
            lie_list = i.split(" ")
            print(lie_list)
            national_standard = guobiao
            table_name = biaoming
            yinzi_code = lie_list[0]
            yinzi_name = lie_list[1]
            yinzi_original_code = lie_list[2]
            yinzi_company_concentration = lie_list[3]
            yinzi_company_emissions = lie_list[4]
            yinzi_data_type_concentration = lie_list[5]
            lie_list_len = len(lie_list)
            from shucaiyidate.modelscode import YinZiCode
            fil_list = YinZiCode.objects.filter(yinzi_code=yinzi_code).filter(table_name=table_name).filter(yinzi_name=yinzi_name)
            fil_list_count = fil_list.count()
            if fil_list_count == 0:  #如果有则不保存
                new_yinzicode = YinZiCode()
                new_yinzicode.national_standard = national_standard
                new_yinzicode.table_name = table_name
                new_yinzicode.yinzi_code = yinzi_code
                new_yinzicode.yinzi_name = yinzi_name
                new_yinzicode.yinzi_original_code = yinzi_original_code
                new_yinzicode.yinzi_company_concentration = yinzi_company_concentration
                new_yinzicode.yinzi_company_emissions = yinzi_company_emissions
                new_yinzicode.yinzi_data_type_concentration = yinzi_data_type_concentration
                if lie_list_len > 6:
                    yinzi_des = lie_list[6]
                    new_yinzicode.yinzi_des = yinzi_des
                new_yinzicode.save()
            else:
                # print("已经存在：%s" % yinzi_code)
                for fil_one in fil_list :
                    print("对应数据ID：%s" % str(fil_one.id))
                    data_id_list.append(str(fil_one.id))
                    break

            num_count = num_count+1
        print("总数：%s"%str(num_count))

        #原list
        print(data_id_list)
        data_id_list_set = set(data_id_list)  #set()函数列表去重
        print(data_id_list_set)
        for data_one in data_id_list_set:
            data_id_dict[data_one]=data_id_list.count(data_one)   #count()函数统计列表中某个元素的个数

        print(data_id_dict)

        for key,value in data_id_dict.items():
            if value !=1:
                print("不是1个的元素：【%s】,而是【%s】个" % (str(key),str(value)))




autoimportyinzi = AutoImportYinZi()

if __name__ == '__main__':
    guobiao = "标准HJ212-2017"
    # biaoming = "表 B.1 水监测因子编码表（引用 HJ 525-2009）"
    # biaoming = '表 B.2 气监测因子编码表（引用 HJ 524-2009）'
    # biaoming = '表 B.3 声环境监测因子编码表 '
    # biaoming = '表 B.5 污水排放过程（工况）监控监测因子编码表  '
    # biaoming = '表 B.7 烟气排放过程（工况）监控监测因子编码表 '
    biaoming = '表 B.10 现场端信息编码表 '
    autoimportyinzi.autoimportyinzi(biaoming=biaoming,guobiao=guobiao)

