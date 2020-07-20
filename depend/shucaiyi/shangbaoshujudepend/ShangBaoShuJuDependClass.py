# ----------------------------------------------------------------------
import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wanwenyc.settings")
django.setup()
# ----------------------------------------------------------------------
#独运行某一个py文件时会出现如下错误：django.core.exceptions.AppRegistryNotReady: Apps aren't loaded yet.，以上内容可以解决此问题,加载django中的App


class ShangBaoShuJuDepend(object):

    def makeShangBaoShuJu(self,depend_id):
        ftp_up_load_file_list = []
        from shangbaoshuju.models import ShangBaoShuJu
        shangbaogongju_list = ShangBaoShuJu.objects.filter(id=depend_id)
        shangbaogongju_list_count = shangbaogongju_list.count()
        if shangbaogongju_list_count==0:
            pass
        else:
            for shangbaogongju_one in shangbaogongju_list:

                sbyzid = shangbaogongju_one.id
                shujuduan_st = shangbaogongju_one.shujuduan_st
                shujuduan_cn = shangbaogongju_one.shujuduan_cn
                shujuduan_pw= shangbaogongju_one.shujuduan_pw
                shujuduan_mn = shangbaogongju_one.shujuduan_mn
                shujuduan_flag =shangbaogongju_one.shujuduan_flag
                is_check_crc = shangbaogongju_one.is_check_crc
                shujuduan_cp_datatime_type = shangbaogongju_one.shujuduan_cp_datatime_type


                from depend.shangbaogongjudepend.shangbaoyinzi import ShangBaoYinZi
                from WWSBGJTest.util.shangBaoGongju import TongXinXieYi



                # 获取因子串
                # 第一次上报数据
                sbyz = ShangBaoYinZi()
                yinzi_list = sbyz.shangbaoyinzi(sbyzid)
                CPyinzi = ''.join(yinzi_list)
                print(CPyinzi)
                # CPyinzi ="w01001-Rtd=63.0, w01001-Flag=N; w01003-Rtd =63.0,w01003-Flag=N;"
                txxy = TongXinXieYi(ST=shujuduan_st, CN=shujuduan_cn, PW=shujuduan_pw,
                                    MN=shujuduan_mn, Flag=shujuduan_flag, invert=is_check_crc,
                                    CPtime=shujuduan_cp_datatime_type, CPyinzi=CPyinzi)

                shangbaoshuju = txxy.shujuMain()
                print("上报数据：")
                print(shangbaoshuju)


shangbaoshujudepend = ShangBaoShuJuDepend()

if __name__ == '__main__':
    shangbaoshujudepend.makeShangBaoShuJu('1')





