import random

class AutoMakePhoneNumber(object):
    """
    电信号段：133/153/180/181/189/177;
    联通号段：130/131/132/155/156/185/186/145/175;
    移动号段：134/135/136/137/138/138/150/151/152/154/157/158/159/182/183/184/187/188/147/178;
    第一位：1；
    第二位：3，4，5，7，8
    第三位：
    3：【0，9】
    4：【5，7】
    5：【0，9】 ！4
    7：【6，7，8】
    8：【0-9】
    """

    def creat_phone(self):
        # 第二位数
        second = [3, 4, 5, 7, 8][random.randint(0, 4)]
        # 第三位数
        third = {
            3: random.randint(0, 9),
            4: [5, 7][random.randint(0, 1)],
            5: [i for i in range(0, 10) if i != 4][random.randint(0, 8)],
            7: [6, 7, 8][random.randint(0, 2)],
            8: random.randint(0, 9)
        }[second]
        # 后八位数
        suffix = ''
        for j in range(0, 8):
            suffix = suffix + str(random.randint(0, 9))

        phone_number = "1{}{}{}".format(second, third, suffix)
        print(phone_number )
        return phone_number


    def create_phone_count(self):
        """
        获取生成手机号的个数
        :return:
        """
        output = int(input("请输入需要获取电话号码的个数："))
        phone_list = []
        for i in range(output):
            phone_list.append(self.creat_phone())

        print(phone_list)
        return phone_list

automakephonenumber = AutoMakePhoneNumber()

if __name__ == '__main__':
    print("hello world")
    automakephonenumber = AutoMakePhoneNumber()
    automakephonenumber.creat_phone()
    # automakephonenumber.create_phone_count()


