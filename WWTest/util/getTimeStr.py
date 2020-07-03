import datetime
import os

from WWTest.util.myLogs import MyLogs


class GetTimeStr:

    def getTimeStr(self):
        now_time = datetime.datetime.now()
        timestr = now_time.strftime('%Y%m%d%H%M%S')
        self.outPutMyLog("当前时间：%s"% now_time)
        self.outPutMyLog("时间串：%s"% timestr)
        return timestr

    def getTimeStrNY(self):
        now_time = datetime.datetime.now()
        timestr = now_time.strftime('%Y%m')
        self.outPutMyLog("当前时间：%s"% now_time)
        self.outPutMyLog("时间串年月：%s"% timestr)
        return timestr

    def outPutMyLog(self,context):
        mylog = MyLogs(context)
        mylog.runMyLog()

    def writeText(self,filename,var):
        with open(filename, 'w') as f:  # 打开test.txt   如果文件不存在，创建该文件。
            f.write(str(var))  # 把变量getid写入createactivityid.txt。这里var必须是str格式，如果不是，则可以转一下。
            self.outPutMyLog("将[%s]写入文件[%s]" % (var,filename))

    def readText(self,filename):
        with open(filename,"r+") as f1:
            for line in f1:
                sxhdmcinputtext =line
                self.outPutMyLog("将文件[%s]中第一行内容【%s】返回" % (filename,sxhdmcinputtext))
                return sxhdmcinputtext

    #创建目录
    def createdir(self,filedir):
        filelist = filedir.split("/")
        long = len(filelist)
        zuhefiledir = filelist[0]
        for i in range(1,long):
            zuhefiledir = zuhefiledir+"/"+filelist[i]
            if os.path.exists(zuhefiledir):
                self.outPutMyLog("已经存在目录：%s" % zuhefiledir)
            else:
                os.mkdir(zuhefiledir)
                self.outPutMyLog("已经创建目录：%s" % zuhefiledir)

    #处理以半角逗号为分隔符，且去掉列表各项的前后空格
    def getListFromStr(self,handlestr,splitstr):
        str_list = handlestr.split(splitstr)
        str_list_len = len(str_list)
        for i in range(0, str_list_len):
            str_list[i] = str_list[i].strip()
        self.outPutMyLog("转换得出的列表内容：%s" %str(str_list))
        return str_list

    #判断字符串是否只包含在“0123456789.”中
    def is_only_num(self,prestr):
        num_str = "0123456789."
        if prestr == "":
            self.outPutMyLog("字符串【%s】为空字符串." % prestr)
            return False
        prestr_strip = prestr.strip()  #去掉字符前后空格
        if prestr == "":
            self.outPutMyLog("字符串【%s】去掉前后空格后为空字符串." % prestr_strip)
            return False

        for prestr_one in prestr:
            if prestr_one not in num_str:
                self.outPutMyLog("字符串【%s】不是纯数字型字符串，包含有【%s】." % (prestr,prestr_one))
                return False
        self.outPutMyLog("字符串【%s】是纯数字型字符串." % prestr)
        return True

    # 获取当前时间N分钟之后的时间串-分钟(后延分钟数为传入的分钟数)
    def get_now_time_after_param_minute(self,delay_min):
        now_time = datetime.datetime.now()
        delay_time = int(delay_min)
        now_plus_n = now_time + datetime.timedelta(minutes=delay_time)
        timestr = now_plus_n.strftime('%Y%m%d%H%M')
        print("当前时间%s分钟后的时间：%s" % (str(delay_time), now_plus_n))
        print("时间串：%s" % timestr)
        timestr_after_n_minute = '%s00' % timestr
        print("当前时间%s分钟后的时间串（分钟）：%s" % (str(delay_time), timestr_after_n_minute))
        return timestr_after_n_minute

    #比较两个时间串大小
    def compare_time_str(self, timestrone, timestrtwo):
        if timestrone >= timestrtwo:  # 大于等于
            print("【%s】大于等于【%s】" % (timestrone, timestrtwo))
            return True
        else:
            print("【%s】小于【%s】" % (timestrone, timestrtwo))
            return False


if __name__  == '__main__':
    gettimestr = GetTimeStr()
    gettimestr.writeText("1.txt",'1')
    gettimestr.readText("1.txt")