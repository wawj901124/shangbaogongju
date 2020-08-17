# ----------------------------------------------------------------------
import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wanwenyc.settings")
django.setup()
# ----------------------------------------------------------------------
#独运行某一个py文件时会出现如下错误：django.core.exceptions.AppRegistryNotReady: Apps aren't loaded yet.，以上内容可以解决此问题,加载django中的App

import random

from WWSBGJTest.util.autoMakeString import AutoMakeString



class HandleYinZiXianZhi(object):

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
            if shuju_up >= shuju_down:
                #如果上限值大于等于下限
                shuju_zs = self.dengyushangxiaxianweishu(shuju_down, shuju_up)
            else:
                print("下限值不得大于上限值")
                shuju_zs = None
        else:
            print("下限位数不得大于上限位数")
            shuju_zs = None
        # 根据上下限制生成整数部分end

        # 根据小数位数随机生成指定位数的小数位数的数据start
        if shuju_up == shuju_down:  #如果上限等于下限
            if shuju_xiaoshuweishu == 0:  #小数位数为0是，不带小数位
                shuju_xs = ""
            else:
                shuju_xs = ""
                for i in range(0, shuju_xiaoshuweishu):  #小数位数不为0时，则小数位全部为0
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

    #根据数据个数生成一个随机数据列表
    def makeonetiaoshuju(self, shuju_down, shuju_up, shuju_xiaoshuweishu,shuju_count):
        yinzi_rtd_list = []
        shuju_count = int(shuju_count)
        for i in range(0,shuju_count):
            yinzi_rtd = self.makeoneshuju(shuju_down, shuju_up, shuju_xiaoshuweishu)
            yinzi_rtd_list.append(yinzi_rtd)
        print(yinzi_rtd_list)
        return yinzi_rtd_list


if __name__ == '__main__':
    hyzxz = HandleYinZiXianZhi()
    shuju_down = 100
    shuju_up = 234
    shuju_xiaoshuweishu = 6
    shuju_list = []
    for i in range(100):
        one = hyzxz.makeoneshuju(shuju_down,shuju_up,shuju_xiaoshuweishu)
        shuju_list.append(one)

    print("生成的随机数：")
    print(shuju_list)
    for one in shuju_list:
        print(one)
