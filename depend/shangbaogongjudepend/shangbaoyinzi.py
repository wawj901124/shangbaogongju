# ----------------------------------------------------------------------
import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wanwenyc.settings")
django.setup()
# ----------------------------------------------------------------------
#独运行某一个py文件时会出现如下错误：django.core.exceptions.AppRegistryNotReady: Apps aren't loaded yet.，以上内容可以解决此问题,加载django中的App
import random

from WWSBGJTest.util.autoMakeString import AutoMakeString

class ShangBaoYinZi(object):
    #去掉首位的0的递归
    def delelezoro(self,shuzhi):
        if shuzhi[0] == '0':
            shuzhi = shuzhi[1:]
            self.delelezoro(shuzhi)
        print(shuzhi)
        return shuzhi

    #位数等于下限位数时，生成数据(上下限位数不同)
    def dengyuxiaxianweishu(self,yzxszfc):
        aut = AutoMakeString()
        shuju_down = yzxszfc
        shuju_down_len = len(yzxszfc)
        dengyuxiaxian_shouwei_string_type_list = []
        # print("88888888888888888888888888888888888888888888")
        # print(int(shuju_down[0]))
        # print("88888888888888888888888888888888888888888888")
        for i in range(int(shuju_down[0]), 10):
            dengyuxiaxian_shouwei_string_type_list.append(str(i))
        dengyuxiaxian_shouwei_string_type = "".join(dengyuxiaxian_shouwei_string_type_list)
        # print("---------------------------------------")
        # print(dengyuxiaxian_shouwei_string_type)
        # print("---------------------------------------")
        dengyuxiaxian_shouwei = aut.getBaseString(dengyuxiaxian_shouwei_string_type, 1)
        # print("999999999999999999999999999999")
        # print("第ji次首位" )
        # print(dengyuxiaxian_shouwei)
        # print("999999999999999999999999999999")

        shouwei = dengyuxiaxian_shouwei
        if int(dengyuxiaxian_shouwei) == int(shuju_down[0]):
                yzxszfc = yzxszfc[1:]
                # print("&&&&&&&&&&&&&&&&&&&&&&")
                # print(yzxszfc)
                # print("&&&&&&&&&&&&&&&&&&&&&&")
                if len(yzxszfc)>0:
                    shouwei = dengyuxiaxian_shouwei+self.dengyuxiaxianweishu(yzxszfc) #再进行第二位生成，按照生成首位的方法
        else:
            if shuju_down_len-1 > 0:
                shuju_zs_hou = aut.getDigits(shuju_down_len-1)
                shouwei = shouwei+shuju_zs_hou

        return shouwei

    #位数等于上限位数时，生成数据（上下限位数不同）
    def dengyushangxianweishu(self,yzxszfc):

        aut = AutoMakeString()
        shuju_up = yzxszfc
        shuju_up_len = len(yzxszfc)
        dengyushangxian_shouwei_string_type_list = []
        # print("88888888888888888888888888888888888888888888")
        # print(int(shuju_up[0]))
        # print("88888888888888888888888888888888888888888888")
        for i in range(0,int(shuju_up[0])):
            dengyushangxian_shouwei_string_type_list.append(str(i))
        dengyushangxian_shouwei_string_type = "".join(dengyushangxian_shouwei_string_type_list)
        # print("---------------------------------------")
        # print(dengyushangxian_shouwei_string_type)
        # print("---------------------------------------")
        dengyushangxian_shouwei = aut.getBaseString(dengyushangxian_shouwei_string_type, 1)
        # print("999999999999999999999999999999")
        # print("第ji次首位" )
        # print(dengyushangxian_shouwei)
        # print("999999999999999999999999999999")

        shouwei = dengyushangxian_shouwei
        if int(dengyushangxian_shouwei) == int(shuju_up[0]):
                yzxszfc = yzxszfc[1:]
                # print("&&&&&&&&&&&&&&&&&&&&&&")
                # print(yzxszfc)
                # print("&&&&&&&&&&&&&&&&&&&&&&")
                if len(yzxszfc)>0:
                    shouwei = dengyushangxian_shouwei+self.dengyushangxianweishu(yzxszfc) #再进行第二位生成，按照生成首位的方法
        else:
            if shuju_up_len-1 > 0:
                shuju_zs_hou = aut.getDigits(shuju_up_len-1)
                shouwei = shouwei+shuju_zs_hou

        return shouwei

    #位数等于上下限位数时，生成数据(上下限位数相同)
    def dengyushangxiaxianweishu(self,xiayzxszfc,shangyzxszfc):
        aut = AutoMakeString()
        shuju_down = xiayzxszfc
        shuju_down_len = len(xiayzxszfc)
        shuju_up = shangyzxszfc
        shuju_up_len = len(shangyzxszfc)
        dengyuxiaxian_shouwei_string_type_list = []
        # print("88888888888888888888888888888888888888888888")
        # print(int(shuju_down[0]))
        # print("88888888888888888888888888888888888888888888")
        for i in range(int(shuju_down[0]), int(shuju_up[0])+1):
            dengyuxiaxian_shouwei_string_type_list.append(str(i))
        dengyuxiaxian_shouwei_string_type = "".join(dengyuxiaxian_shouwei_string_type_list)
        # print("---------------------------------------")
        # print(dengyuxiaxian_shouwei_string_type)
        # print("---------------------------------------")
        dengyuxiaxian_shouwei = aut.getBaseString(dengyuxiaxian_shouwei_string_type, 1)
        # print("999999999999999999999999999999")
        # print("第ji次首位" )
        # print(dengyuxiaxian_shouwei)
        # print("999999999999999999999999999999")

        shouwei = dengyuxiaxian_shouwei
        if int(dengyuxiaxian_shouwei) == int(shuju_down[0]) or  int(dengyuxiaxian_shouwei) == int(shuju_up[0]):
                xiayzxszfc = xiayzxszfc[1:]
                shangyzxszfc = shangyzxszfc[1:]
                print("&&&&&&&&&&&&&&&&&&&&&&")
                print(xiayzxszfc)
                print("&&&&&&&&&&&&&&&&&&&&&&")
                if len(xiayzxszfc)>0:
                    shouwei = dengyuxiaxian_shouwei+self.dengyushangxiaxianweishu(xiayzxszfc,shangyzxszfc) #再进行第二位生成，按照生成首位的方法
        else:
            if shuju_down_len-1 > 0:
                shuju_zs_hou = aut.getDigits(shuju_down_len-1)
                shouwei = shouwei+shuju_zs_hou

        return shouwei



    #生成一个随机数
    def makeoneshuju(self,shuju_down,shuju_up,shuju_xiaoshuweishu):
        aut = AutoMakeString()

        shuju_up = str(shuju_up)
        shuju_up = self.delelezoro(shuju_up)  # 上限去首位0
        shuju_up_len = len(shuju_up)  # 获取上限的位数

        shuju_down = str(shuju_down)
        shuju_down = self.delelezoro(shuju_down)  # 下限去首位0
        shuju_down_len = len(shuju_down)  # 获取下限的位数
        shuju_xiaoshuweishu = int(shuju_xiaoshuweishu)  #小数位数

        # 根据上下限生成整数部分start
        if shuju_up_len > shuju_down_len:
            # 如果上限位数大于下限位数
            shuju_zhengshuweishu_list = random.sample(range(shuju_down_len, (shuju_up_len + 1)), 1)
            shuju_zhengshuweishu_str = shuju_zhengshuweishu_list[0]
            shuju_zhengshuweishu = int(shuju_zhengshuweishu_str)
            # print("fsfssdfdfssssssssssssssssssssssssssssssssssssssssssssssssssssssssss")
            # print(shuju_zhengshuweishu)
            # print(type(shuju_zhengshuweishu))
            # print("fsfssdfdfssssssssssssssssssssssssssssssssssssssssssssssssssssssssss")
            # shuju_zhengshuweishu = 3

            if shuju_zhengshuweishu == shuju_down_len:
                # 如果是等于下限值的位数，则随机数有数值限制
                shuju_zs = self.dengyuxiaxianweishu(shuju_down)

            elif shuju_zhengshuweishu == shuju_up_len:
                # 如果是等于上限值的位数，则随机数有数值限制
                # 首位大于0小于等于上限第一位
                dengyushangxian_shouwei_string_type_list = []
                for i in range(1, int(shuju_up[0]) + 1):
                    dengyushangxian_shouwei_string_type_list.append(str(i))
                dengyushangxian_shouwei_string_type = "".join(dengyushangxian_shouwei_string_type_list)
                dengyushangxian_shouwei = aut.getBaseString(dengyushangxian_shouwei_string_type, 1)
                # 生成首位完成
                print(dengyushangxian_shouwei)
                if dengyushangxian_shouwei == int(shuju_up[0]):
                    # 如果上限首位等于上限值首位，则进行后续位数判断
                    shuju_up = shuju_up[1:]
                    shuju_zs_hou = self.dengyushangxianweishu(shuju_up)
                else:
                    # 否则，后续位由0到9组成
                    # 之后位每个位随机0到9
                    shuju_zs_hou = ""
                    if shuju_zhengshuweishu - 1 > 0:
                        shuju_zs_hou = aut.getDigits(shuju_zhengshuweishu - 1)

                shuju_zs = dengyushangxian_shouwei + shuju_zs_hou
            else:
                ############################################################
                # 如果大于下限位数小于上限位数，则第一位不能为0，其他位数0到9随机
                # 首位随机1到9
                zhijian_shouwei_string_type = "123456789"
                zhijian_shouwei = aut.getBaseString(zhijian_shouwei_string_type, 1)
                # 之后位每个位随机0到9
                shuju_zs_hou = ""
                if shuju_zhengshuweishu - 1 > 0:
                    shuju_zs_hou = aut.getDigits(shuju_zhengshuweishu - 1)
                shuju_zs = zhijian_shouwei + shuju_zs_hou
        elif shuju_up_len == shuju_down_len:
            shuju_zs = self.dengyushangxiaxianweishu(shuju_down, shuju_down)
        else:
            print("下限位数不得大于上限位数")
            shuju_zs = None
        # 根据上下限制生成整数部分end

            # 根据小数位数随机生成指定位数的小数位数的数据start
        if shuju_up == shuju_down:
            if shuju_xiaoshuweishu == 0:
                shuju_xs = ""
            else:
                shuju_xs = ""
                for i in range(0, shuju_xiaoshuweishu):
                    shuju_xs = shuju_xs + "0"
        else:
            if shuju_xiaoshuweishu == 0:
                shuju_xs = ""
            else:
                shuju_xs = aut.getDigits(shuju_xiaoshuweishu)
        # 根据小数位数随机生成指定位数的小数位数的数据end
        if shuju_xiaoshuweishu == 0:
            yinzi_rtd = "%s" % shuju_zs
        else:
            yinzi_rtd = "%s.%s" % (shuju_zs, shuju_xs)

        print(yinzi_rtd)
        return  yinzi_rtd

    def makeonetiaoshuju(self, shuju_down, shuju_up, shuju_xiaoshuweishu,shuju_count):
        yinzi_rtd_list = []
        shuju_count = int(shuju_count)
        for i in range(0,shuju_count):
            yinzi_rtd = self.makeoneshuju(shuju_down, shuju_up, shuju_xiaoshuweishu)
            yinzi_rtd_list.append(yinzi_rtd)
        print(yinzi_rtd_list)
        return yinzi_rtd_list




    def shangbaoyinzi(self,sbyzid):

        yinzi_list = []
        from shangbaoshuju.models import ShuJuYinZi
        shujuyinzis = ShuJuYinZi.objects.filter(shangbaoshuju_id=int(sbyzid))
        if str(shujuyinzis) != "<QuerySet []>":
            print(u"找到依赖数据")
            for shujuyinzi in shujuyinzis:
                #一个因子生成"w01001-Rtd=63.0,w01001-Flag=N;"形式
                #根据上限和下限及小数位数生成数据
                shuju_down = shujuyinzi.yinzi_rtd_down
                shuju_up= shujuyinzi.yinzi_rtd_up
                shuju_xiaoshuweishu = shujuyinzi.yinzi_rtd_xiaoshuwei
                shuju_count = shujuyinzi.yinzi_rtd_count

                yinzi_rtd_list = self.makeonetiaoshuju(shuju_down,shuju_up,shuju_xiaoshuweishu,shuju_count)
                one_yinzi = "%s-Rtd=%s,%s-Flag=%s;" % (
                    shujuyinzi.yinzi_code, yinzi_rtd_list[0], shujuyinzi.yinzi_code, shujuyinzi.yinzi_flag)
                yinzi_list.append(one_yinzi)

        else:
            print(u"没有找到依赖id[%s]对应的数据！" % sbyzid)


        return yinzi_list



shangbaoyinzi = ShangBaoYinZi()

if __name__ == '__main__':
    print("hello world")
    yinzi_list =shangbaoyinzi.shangbaoyinzi(2)
    print(yinzi_list)
    CPyinzi = ''.join(yinzi_list)
    print(CPyinzi)
    # s = shangbaoyinzi.shouweixiangdeng("11")
    # print(s)
    # import random

    # print(random.sample(range(100, 900),10))
    #
    #
    # j = 10
    # #
    # # id_list = []
    # id_list = ''.join(str(i) for i in random.sample(range(100, 900), j))  # sample(seq, n) 从序列seq中选择n个随机且独立的元素；
    # print(id_list)
    # a = "000010"
    # shangbaoyinzi.delelezoro(a)
    # shuju_zhengshuweishu = 2
    # aut = AutoMakeString()
    # zhijian_shouwei_string_type = "123456789"
    # zhijian_shouwei = aut.getBaseString(zhijian_shouwei_string_type, 1)
    # shuju_xs_hou = ""
    # if shuju_zhengshuweishu - 1 > 0:
    #     shuju_xs_hou = aut.getDigits(shuju_zhengshuweishu - 1)
    #
    # shuju_xs = zhijian_shouwei + shuju_xs_hou
    # print("---------------------")
    # print(shuju_xs)
    # print("---------------------")
    # aut.getDigits(100)
    # import random
    #
    # one_wei = random.sample(range(1, 3), 1)
    # print(one_wei)
    # shuju_down = "110"
    #
    #
    # dengyuxiaxian_shouwei_string_type_list = []
    # for i in range(int(shuju_down[0]), 10):
    #     dengyuxiaxian_shouwei_string_type_list.append(str(i))
    #
    # dengyuxiaxian_shouwei_string_type = "".join(dengyuxiaxian_shouwei_string_type_list)
    # print(dengyuxiaxian_shouwei_string_type)


