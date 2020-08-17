# ----------------------------------------------------------------------
import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wanwenyc.settings")
django.setup()
# ----------------------------------------------------------------------
#独运行某一个py文件时会出现如下错误：django.core.exceptions.AppRegistryNotReady: Apps aren't loaded yet.，以上内容可以解决此问题,加载django中的App

from WWSBGJTest.util.autoMakeString import AutoMakeString
from depend.senddatadepend.handleyinzixianzhi import HandleYinZiXianZhi
from depend.senddatadepend.floutOrHex import *


class GetSendData(object):
    def __init__(self,denpendid):
        self.denpend_id = int(denpendid)


    def getSendData(self):
        from shucaiyidate.modelsautodata import XieYiAutoData
        xyad = XieYiAutoData.objects.get(id=self.denpend_id)
        device_id = xyad.shebeiid
        gong_neng_ma = xyad.gongnengma
        shu_ju_chang_du = xyad.shujuchangdu

        from shucaiyidate.modelsautodata import XieYiOneData
        xyod_list = XieYiOneData.objects.filter(xieyiautodata_id=self.denpend_id)
        xyod_list_len = len(xyod_list)
        if xyod_list_len >=1:
            all_yinzi_data = ""
            for xyod_one in xyod_list:
                #处理一个因子的16进制
                #获取字节序
                zix = xyod_one.yinzi_zijiexu
                if zix == "1234":
                    #如果字节序是1234，则按照1234转为16进制文件
                    #数值上限
                    shuju_down = xyod_one.yinzi_rtd_down  #数值下限
                    shuju_up = xyod_one.yinzi_rtd_up  #数值上限
                    shuju_xiaoshuweishu = xyod_one.yinzi_rtd_xiaoshuwei  #小数位数
                    hyzxz = HandleYinZiXianZhi()
                    shijishuzhi = hyzxz.makeoneshuju(shuju_down, shuju_up, shuju_xiaoshuweishu)
                    print("数值：")
                    print(shijishuzhi)
                    print(type(shijishuzhi))
                    #数值转为16进制
                    shijishuzhi_f = float(shijishuzhi)
                    shijishuzhi_16 = float_to_hex(shijishuzhi_f)
                    print("16进制数值：")
                    print(shijishuzhi_16)

                    print("16进制数值字符串(大写)：")
                    shijishuzhi_str_upper = str(shijishuzhi_16).upper()
                    print(shijishuzhi_str_upper)
                    shijishuzhi_str_upper_len = len(shijishuzhi_str_upper)
                    print(shijishuzhi_str_upper_len)
                    shijishuzhi_str_upper_len_2_beishu = shijishuzhi_str_upper_len//2
                    print(shijishuzhi_str_upper_len_2_beishu)
                    print("16进制数值字符串(大写),两两一组：")
                    shijishuzhi_list = []
                    shijishuzhi_list_zero = shijishuzhi_str_upper[:2]
                    print(shijishuzhi_list_zero)



        else:
            print("没有因子数据")


if __name__ == '__main__':
    denpendid = '1'
    gsd = GetSendData(denpendid=denpendid)
    gsd.getSendData()


