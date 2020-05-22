import random
import string

class AutoMakeString(object):

    """
    可以利用string类和random模块
    string类
    whitespace = ' \t\n\r\v\f'   #转义字符
    ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'   #小写字母
    ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'    #大写字母
    ascii_letters = ascii_lowercase + ascii_uppercase   #小写字母和大写字母
    digits = '0123456789'    #十进制数字
    hexdigits = digits + 'abcdef' + 'ABCDEF'    #十六进制数字
    octdigits = '01234567'    #八进制数字
    punctuation = "!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"     #特殊字符
    """

    def getBaseString(self,string_type,num_count):
        """
        自动生成指定位数的随机字符串
        :param string_type:
        :param num_count:
        :return:
        """
        #除数
        num_count_int = int(num_count)
        #除以50后的值
        divisor_result = num_count_int//10
        #余数
        remainder = num_count_int%10
        # print("divisor_result:%s"%divisor_result)
        # print("remainder:%s"%remainder)
        result_list_all = []
        for i in range(0,divisor_result):
            result_list = random.sample(string_type,10)  # 生成数组
            result_list_all.append(result_list)

        result_list_remainder = random.sample(string_type,remainder)  # 生成数组
        result_list_all.append(result_list_remainder)

        result_list_all_long = len(result_list_all)
        # print("result_list_all:%s"% result_list_all)
        # print("result_list_all_long:%s"% result_list_all_long)
        result_string = ""
        for i in range(0,result_list_all_long):
            result_list_all_i = result_list_all[i]
            # print("result_list_all_i:%s" % result_list_all_i)
            result_string = result_string + "".join(result_list_all[i])  # 将数组转换为字符串

        print(result_string)
        print(len(result_string))
        return result_string    #返回字符串


    def getAsciiLowercase(self,num_count):
        """
        自动生成指定位数的小写字母组成的随机字符串
        :param num_count:
        :return:
        """
        result_string = self.getBaseString(string_type=string.ascii_lowercase,num_count=num_count)
        print("自动生成指定%s位数的小写字母组成的随机字符串:%s" % (num_count,result_string))
        return result_string

    def getAsciiUppercase(self,num_count):
        """
        自动生成指定位数的大写字母组成的随机字符串
        :param num_count:
        :return:
        """
        result_string = self.getBaseString(string_type=string.ascii_uppercase,num_count=num_count)
        print("自动生成指定%s位数的大写字母组成的随机字符串:%s" % (num_count, result_string))
        return result_string

    def getDigits(self,num_count):
        """
        自动生成指定位数的0~9数字的随机字符串
        :param num_count:
        :return:
        """
        result_string = self.getBaseString(string_type=string.digits,num_count=num_count)
        print("自动生成指定%s位数的0~9数字的随机字符串:%s" % (num_count, result_string))
        return result_string

    def getSymbols(self,num_count):
        """
        自动生成指定位数的特殊符号的随机字符串
        :param num_count:
        :return:
        """
        result_string = self.getBaseString(string_type=string.punctuation,num_count=num_count)
        print("自动生成指定%s位数的特殊符号的随机字符串:%s" % (num_count, result_string))
        return result_string

    def getWhitespace(self,num_count):
        """
        自动生成指定位数的空白字符类型的随机字符串
        :param num_count:
        :return:
        """
        result_string = self.getBaseString(string_type=string.punctuation,num_count=num_count)
        print("自动生成指定%s位数的空白字符类型的随机字符串:%s" % (num_count, result_string))
        return result_string


    def getAsciiLetters(self,num_count):
        """
        自动生成指定位数的小写字母和大写字母组成的随机字符串
        :param num_count:
        :return:
        """
        result_string = self.getBaseString(string_type=string.ascii_letters,num_count=num_count)
        print("自动生成指定%s位数的小写字母和大写字母组成的随机字符串:%s" % (num_count, result_string))
        return result_string

    def getLowercaseAndDigits(self,num_count):
        """
        自动生成指定位数的0~9数字和小写字母组成的随机字符串
        :param num_count:
        :return:
        """
        result_string = self.getBaseString(string.ascii_lowercase+string.digits,num_count=num_count)
        print("自动生成指定%s位数的0~9数字和小写字母组成的随机字符串:%s" % (num_count, result_string))
        return result_string

    def getUppercaseAndDigits(self,num_count):
        """
        自动生成指定位数的0~9数字和大写字母组成的随机字符串
        :param num_count:
        :return:
        """
        result_string = self.getBaseString(string.ascii_uppercase+string.digits,num_count=num_count)
        print("自动生成指定%s位数的0~9数字和大写字母组成的随机字符串:%s" % (num_count, result_string))
        return result_string


    def getLettersAndDigits(self,num_count):
        """
        自动生成指定位数的0~9数字和字母组成的随机字符串
        :param num_count:
        :return:
        """
        result_string = self.getBaseString(string.ascii_letters+string.digits,num_count=num_count)
        print("自动生成指定%s位数的0~9数字和大小写字母组成的随机字符串:%s" % (num_count, result_string))
        return result_string

    def getLetterAndDigitsAndSymbols(self,num_count):
        """
        自动生成指定位数的0~9数字和字母和特殊字符组成的随机字符串
        :param num_count:
        :return:
        """
        result_string = self.getBaseString(string.ascii_letters+string.digits+string.punctuation,num_count=num_count)
        print("自动生成指定%s位数的0~9数字和大小写字母和特殊字符组成的随机字符串:%s" % (num_count, result_string))
        return result_string

    def getLetterAndDigitsAndSymbolsAndWhitespace(self,num_count):
        """
        自动生成指定位数的0~9数字和字母和特殊字符和转义符号组成的随机字符串
        :param num_count:
        :return:
        """
        result_string = self.getBaseString(string.printable,num_count=num_count)
        print("自动生成指定%s位数的0~9数字和大小写字母和特殊字符和空白字符组成的随机字符串:%s" % (num_count, result_string))
        return result_string

    # 直接基于unicode码生成
    # 在unicode码中，汉字范围是(0x4E00, 0x9FBF)
    def unicode_zh(self):
        # 随机生成一个汉字码
        zh = random.randint(0x4E00, 0x9FBF)
        # 转换下,返回
        return chr(zh)

    # 基于gbk2312码生成
    # 在gbk2312码中，字符的编码采用两个字节组合
    # 汉字第一个字节范围是(0xB0, 0xF7)
    # 汉字第二个字节范围是(0xA1, 0xFE)
    def gbk2312_zh(self):
        # 生成第一个字节
        first = random.randint(0xB0, 0xF7)
        # 生成第二个字节
        last = random.randint(0xA1, 0xFE)
        # 组合一下
        s = f'{first:x}{last:x}'
        # 转换成汉字
        zh = bytes.fromhex(s).decode('gb2312')
        # 返回
        return zh

    def getUnicodeZh(self,num_count):
        word_list = []
        result_string = ""
        for _ in range(int(num_count)):
            word = self.unicode_zh()
            word_list.append(word)

        result_string = result_string + "".join(word_list)  # 将数组转换为字符串
        print(result_string)
        print(len(result_string))
        return result_string

    def getGbk2312Zh(self,num_count):
        word_list = []
        result_string = ""
        for _ in range(int(num_count)):
            word = self.gbk2312_zh()
            word_list.append(word)

        # print(word_list)
        result_string = result_string + "".join(word_list)  # 将数组转换为字符串
        print(result_string)
        print(len(result_string))
        return result_string

automakestring = AutoMakeString()



if __name__ == "__main__":
    auto = AutoMakeString()
    auto.getAsciiLowercase(100)  #小写字母
    auto.getAsciiUppercase(100)   #大写字母
    auto.getDigits(151)         #0~9数字
    auto.getSymbols(100)        #特殊字符
    auto.getWhitespace(50)      #空白符

    auto.getAsciiLetters(100)  #大小写字母
    auto.getLowercaseAndDigits(20) #小写字母和0~9数字
    auto.getUppercaseAndDigits(35)   #大写字母和0~9数字
    auto.getLettersAndDigits(199) #大小写和数字0`9
    auto.getLetterAndDigitsAndSymbols(250)   #大小写字母和数字0~9和特殊符号
    auto.getLetterAndDigitsAndSymbolsAndWhitespace(66)   #大小写字母和数字0~9和特殊符号和空白符号
    # auto.getUnicodeZh(600)
    # auto.getGbk2312Zh(600)

