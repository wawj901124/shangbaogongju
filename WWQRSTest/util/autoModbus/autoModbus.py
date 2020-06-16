from selenium import webdriver   #导入驱动
import  os
import time
import datetime
from selenium.webdriver.support.select import Select   #导入Select

from WWQRSTest.util.autoModbus.depend.startSCYXieYi import TelnetClient
from WWQRSTest.util.autoModbus.depend.comReceiveAndSend import ComThread
from WWQRSTest.util.autoModbus.depend.myftp_get_file import MyFTP
from WWQRSTest.util.autoModbus.depend.modbusCrc import ModbusCrc
from WWQRSTest.util.autoModbus.depend.tcpServerReceive import TcpServerReceive
from WWQRSTest.util.autoModbus.depend.handleTxt import HandleTxt
from WWQRSTest.util.autoModbus.depend.mysqlite import MySqlite
from WWQRSTest.util.myLogs import MyLogs



class AutoModbus(object):
    def __init__(self,telnet_host_ip =None,
                        telnet_username =None,
                        telnet_password =None,
                        xieyi_bin_dir=None,
                        xieyi_name =None,
                        xieyi_test_port =None,
                        xieyi_db=None,
                        xieyi_db_remote_path =None,
                        xieyi_db_table_name =None,
                        xieyi_device_id = None,
                        com_port =None,
                        com_baudrate =None,
                        com_bytesize =None,
                        com_parity =None,
                        com_stopbits =None,
                        com_send_date =None,
                        com_expect_date =None,
                        com_send_date_list =None,
                        is_need_expect_list = None,
                        com_expect_date_list=None,
                        xieyi_jiexi_expect_result_list =None,
                        tcp_server_ip =None,
                        tcp_server_port =None,
                        is_telnet_client_close_default_start_xieyi =None,
                        is_telnet_client_rstart_xieyi =None,
                        is_com_recive_and_send =None,
                        is_ftp_get_file =None,
                        is_assert_file_success =None,
                        is_ftp_get_remote_db_file =None,
                        is_assert_real_db_success =None,
                        is_tcp_server_receive =None,
                        is_assert_tcp_server_receive_success =None):

        self.telnet_host_ip = telnet_host_ip
        self.telnet_username = telnet_username
        self.telnet_password = telnet_password

        self.xieyi_bin_dir = xieyi_bin_dir
        self.xieyi_name = xieyi_name
        self.xieyi_test_port = xieyi_test_port  #数采仪端端口号
        self.xieyi_device_id = xieyi_device_id  #数采仪下发或接收指令的设备ID号或站地址
        self.xieyi_txt_file_name = '%s_%s.txt'%(self.xieyi_name,self.xieyi_test_port)
        self.xieyi_db = xieyi_db
        self.xieyi_db_remote_path = xieyi_db_remote_path
        self.xieyi_db_table_name = xieyi_db_table_name
        self.com_port = com_port   #设置端口号(电脑端)
        self.com_baudrate = com_baudrate  # 设置波特率
        self.com_bytesize = com_bytesize  # 设置数据位
        self.com_parity = com_parity  # 设置校验位  N(无校验)、O（奇校验）、E（偶校验）0、1
        self.com_stopbits = com_stopbits  # 设置停止位
        self.com_timeout = 2   #超时设置

        self.com_send_date = com_send_date
        self.com_expect_date = com_expect_date

        self.com_send_date_list = com_send_date_list

        self.xieyi_jiexi_expect_result_list = xieyi_jiexi_expect_result_list

        self.tcp_server_ip = tcp_server_ip
        self.tcp_server_port = tcp_server_port


        self.is_telnet_client_close_default_start_xieyi = is_telnet_client_close_default_start_xieyi
        self.is_telnet_client_rstart_xieyi = is_telnet_client_rstart_xieyi
        self.is_com_recive_and_send = is_com_recive_and_send
        self.is_ftp_get_file = is_ftp_get_file
        self.is_assert_file_success = is_assert_file_success
        self.is_ftp_get_remote_db_file = is_ftp_get_remote_db_file
        self.is_assert_real_db_success = is_assert_real_db_success
        self.is_tcp_server_receive = is_tcp_server_receive
        self.is_assert_tcp_server_receive_success = is_assert_tcp_server_receive_success


        self.telnet_clicent_object = None
        self.ftp_client_object = None


        self.com_send_date_yinzi_num = '1'  #回复数据中因子个数
        self.com_send_date_yinzi_num_is_auto_make = False # 回复数据中因子个数是否根据配置文件自动生成
        self.com_send_date_yinzi_hex_str_is_auto_make = False # 回复数据中因子16进制字符串是否自动生成
        self.com_send_date_yinzi_hex_str_list = ['F8 00 3F AC']  # 回复数据中因子16进制字符串非自动生成时，需要再此处传入
        # # self.com_send_date = '01 03 02 00 EA'
        # # self.com_expect_date = '01 03 12 2D 00 01 11 7B'
        # self.com_expect_date_bytes = self.handle_Hexstr_to_bytes(self.com_expect_date)
        # # self.com_send_date_list = ['01 03 02 18 75','01 03 02 18 75','01 03 02 18 75']
        # # self.com_send_date_bytes = self.handle_send_data()
        # self.com_send_date_list_bytes = self.handle_Hexstr_list_to_bytes_list(self.com_send_date_list)
        # # self.xieyi_jiexi_expect_result = '9.55'  #协议解析预期结果
        # # self.xieyi_jiexi_expect_result_list = ['0.234']  # 协议解析预期结果.列表值
        self.xieyi_cfg_protocol = ""
        self.xieyi_cfg_idNum = "11"
        self.xieyi_cfg_startAddress = "0000"
        self.xieyi_cfg_functionCode = "03"
        self.xieyi_cfg_registerNum = "01"
        self.xieyi_cfg_DataLen = ""
        self.xieyi_cfg_dataLen = "2"
        self.xieyi_cfg_dataType = "12"

        # self.tcp_server_ip = "192.168.101.123"
        # self.tcp_server_port = 63503
        self.tcp_server_file_name = 'tcp_server_receive.txt'
        self.tcp_server_object = None

        self.is_ftp_get_modbus_cfg = False
        self.is_check_modbus_xieyi_cfg = False
        self.is_get_modbus_cfg_main = False

        self.is_set_com_send_date = False
        self.is_write_device = False
        self.write_device_reatart_time = 40  #以秒计算
        # self.is_telnet_client_close_default_start_xieyi = False
        # self.is_telnet_client_rstart_xieyi = False
        # self.is_com_recive_and_send =True
        # self.is_ftp_get_file = False
        # self.is_assert_file_success = False
        # self.is_ftp_get_remote_db_file = False
        # self.is_assert_real_db_success = False
        # self.is_tcp_server_receive = False
        # self.is_assert_tcp_server_receive_success = False


    #延时函数
    def time_delay(self,deletime):
        self.outPutMyLog("即将等待%s秒" % str(deletime))
        time.sleep(int(deletime))
        self.outPutMyLog("等待%s秒结束" % str(deletime))

    def get_time_str(self):
        now_time = datetime.datetime.now()
        timestr = now_time.strftime('%Y%m%d%H%M%S')
        timestr = str(timestr)
        # self.outPutMyLog("当前时间：%s"% now_time)
        # self.outPutMyLog("时间串：%s"% timestr)
        return timestr

    def outPutMyLog(self,context):
        mylog = MyLogs(context)
        mylog.runMyLog()


    def outPutErrorMyLog(self,context):
        mylog = MyLogs(context)
        mylog.runErrorLog()

    #ftp连接
    def ftp_connnect(self):
        host = self.telnet_host_ip
        username = self.telnet_username
        password = self.telnet_password
        ftp_client = MyFTP(host, username, password)
        return ftp_client

    #ftp下载远程路径文件
    def run_ftp_down(self,remote_file,local_file):
        if self.ftp_client_object == None:
            self.ftp_client_object = self.ftp_connnect()
        else:
            self.ftp_client_object = self.ftp_client_object

        remote_file = remote_file
        local_file = local_file
        #先删除现有文件
        ht = HandleTxt(file_name=local_file)
        ht.delete_file()
        #再下载新文件
        self.ftp_client_object.ftp_download(remote_file, local_file)
        self.time_delay(3)
        # self.outPutMyLog(self.ftp_client_object)

    #ftp上传文件
    def run_ftp_up(self,remote_file,local_file):
        #上传文件之前将远程文件先备份

        if self.ftp_client_object == None:
            self.ftp_client_object = self.ftp_connnect()
        else:
            self.ftp_client_object = self.ftp_client_object
        remote_file = remote_file
        local_file = local_file
        self.ftp_client_object.ftp_upload(remote_file,local_file)
        self.time_delay(3)

    #读取本地文件并解析内容,查看是否存在
    def run_handle_text_read_is_exist(self,local_file,expect_name):
        flag = False
        ht = HandleTxt(file_name=local_file)
        all_content_list = ht.read_all_content_list()
        self.outPutMyLog(all_content_list)
        for one_content in all_content_list:
            one = one_content.strip("\n")  #去掉换行符
            self.outPutMyLog(one)
            if expect_name == one:
                flag = True
                break
            self.outPutMyLog("***************************")
            self.outPutMyLog(one_content)
            self.outPutMyLog(flag)
            self.outPutMyLog("***************************")
        return flag

    def run_ftp_up_load_file_list(self,ftp_up_load_file_list):
        for ftp_up_load_file_list_one in ftp_up_load_file_list:
            remote_file_path_one = ftp_up_load_file_list_one[0]
            local_file_path_one = ftp_up_load_file_list_one[1]
            remote_file_path_one_list = remote_file_path_one.split('/')
            self.outPutMyLog(remote_file_path_one_list)
            remote_file_path_new_list = remote_file_path_one_list[0:-1]  # 获取除最后一项
            self.outPutMyLog(remote_file_path_new_list)
            # 远程目录
            remote_file_path_dir = '/'.join(remote_file_path_new_list)
            self.outPutMyLog("远程文件路径：")
            self.outPutMyLog(remote_file_path_dir)
            # 远程文件
            remote_file_name = remote_file_path_one_list[-1]
            self.outPutMyLog("远程文件：")
            self.outPutMyLog(remote_file_name)
            ls_result = 'ls_%s_result.txt' % remote_file_name

            # 1-1.上传配置文件之前先修改远程文件名称为备份文件名
            # 查看服务器中是否存在远程文件
            mycommad_list = []
            mycommad_one = 'cd %s' % remote_file_path_dir
            mycommad_two = 'ls | grep %s >%s' % (remote_file_name, ls_result)
            mycommad_list.append(mycommad_one)
            mycommad_list.append(mycommad_two)
            mycommad_result_list = self.run_telnet_command_list(mycommad_list)
            self.outPutMyLog(mycommad_result_list)

            down_remote_file = remote_file_path_dir + '/' + ls_result
            self.outPutMyLog(down_remote_file)
            down_local_file = ls_result
            # 将ls文件down下来
            self.run_ftp_down(remote_file=down_remote_file, local_file=down_local_file)
            # 判断是否存在
            is_exist = self.run_handle_text_read_is_exist(local_file=down_local_file, expect_name=remote_file_name)
            if is_exist:  # 如果存在
                # 则修改原文件名字为备份文件
                timestr = self.get_time_str()
                mycommad_list = []
                mycommad_one = 'cd %s' % remote_file_path_dir
                mycommad_two = 'mv %s %s.bak.%s ' % (remote_file_name, remote_file_name, timestr)
                mycommad_list.append(mycommad_one)
                mycommad_list.append(mycommad_two)
                mycommad_result_list = self.run_telnet_command_list(mycommad_list)
                self.outPutMyLog(mycommad_result_list)

            # 上传文件
            self.run_ftp_up(remote_file=remote_file_path_one, local_file=local_file_path_one)
            # 更改文件权限
            mycommad_list = []
            mycommad_one = 'cd %s' % remote_file_path_dir
            mycommad_two = 'chmod a+x %s' % remote_file_name
            mycommad_list.append(mycommad_one)
            mycommad_list.append(mycommad_two)
            mycommad_result_list = self.run_telnet_command_list(mycommad_list)
            self.outPutMyLog(mycommad_result_list)


    #获取modbus.cfg文件，查看是否存在相应的协议配置内容，
    # 如果不存在则添加，如果存在，则获取到内容看配置是否正确
    def ftp_get_modbus_cfg(self):
        if self.ftp_client_object == None:
            self.ftp_client_object = self.ftp_connnect()
        else:
            self.ftp_client_object = self.ftp_client_object

        remote_file = '/usr/app_install/protocol/cfg/modbus.cfg'
        local_file = 'modbus.cfg'
        #先删除现有文件
        ht = HandleTxt(file_name=local_file)
        ht.delete_file()
        #再下载新文件
        self.ftp_client_object.ftp_download(remote_file, local_file)
        self.time_delay(3)
        self.outPutMyLog(self.ftp_client_object)

    def read_modbus_cfg(self):
        with open('modbus.cfg', "r") as f:
            modbus_cfg_list = f.readlines()
        return modbus_cfg_list


    #查找协议在配置文件中的配置内容
    def check_modbus_xieyi_cfg(self):
        xieyi_cfg_list = []
        modbus_cfg_list = self.read_modbus_cfg()
        for one_line in modbus_cfg_list:
            if self.xieyi_name in one_line:
                self.outPutMyLog(one_line)
                #解析每一行的内容
                one_line_list = one_line.split(";")
                self.outPutMyLog(one_line_list)
                for one_line_list_one in one_line_list:
                    if self.xieyi_name in one_line_list_one:
                        self.outPutMyLog(one_line_list_one)
                        one_line_list_one_list = one_line_list_one.split("=")
                        self.outPutMyLog(one_line_list_one_list)
                        for one_line_list_one_list_one in one_line_list_one_list:
                            if self.xieyi_name in one_line_list_one_list_one:
                                self.outPutMyLog(one_line_list_one_list_one)
                                if self.xieyi_name == one_line_list_one_list_one:
                                    # 如果modbus.cfg文件中的配置名和需要的协议名字一致，则
                                    #添加改行内容到xieyi_cfg_list数组中
                                    xieyi_cfg_list.append(one_line)
                                    self.outPutMyLog("退出one_line_list_one_list循环")
                                    break   #退出循环、
                        self.outPutMyLog("退出one_line_list循环")
                        break #退出循环
        self.outPutMyLog(xieyi_cfg_list)
        return xieyi_cfg_list

    #根据
    def get_Datalen_from_registerNum(self,registerNum):
        #传入的registerNum为16进制文本
        registerNum = registerNum
        registerNum_int = int(registerNum, 16)  # 字符串转为16进制整数,其实就是按照16进制，转为整数如'0F'转为15
        self.outPutMyLog("16进制整数：")
        self.outPutMyLog(registerNum_int)
        DataLen_from_registerNum = registerNum_int * 2
        DataLen_from_registerNum_hex = hex(DataLen_from_registerNum)  # 10进制数转为16进制数
        self.outPutMyLog(DataLen_from_registerNum_hex)
        self.outPutMyLog("查看类型：")
        self.outPutMyLog(type(DataLen_from_registerNum_hex))
        DataLen_from_registerNum_hex_list = DataLen_from_registerNum_hex.split("x")
        self.outPutMyLog("查看列表：")
        self.outPutMyLog(DataLen_from_registerNum_hex_list)
        DataLen_from_registerNum_hex_list_get = DataLen_from_registerNum_hex_list[1]
        self.outPutMyLog(DataLen_from_registerNum_hex_list_get)
        DataLen_from_registerNum_hex_list_get_str = str(DataLen_from_registerNum_hex_list_get)
        DataLen_from_registerNum_hex_list_get_str_len = len(DataLen_from_registerNum_hex_list_get_str)
        if DataLen_from_registerNum_hex_list_get_str_len == 1:
            DataLen_from_registerNum_hex_list_get_str = "0%s" % DataLen_from_registerNum_hex_list_get_str
            com_send_date_shujuquzongchandu = DataLen_from_registerNum_hex_list_get_str.upper()
        elif DataLen_from_registerNum_hex_list_get_str_len == 2:
            DataLen_from_registerNum_hex_list_get_str = DataLen_from_registerNum_hex_list_get_str
            com_send_date_shujuquzongchandu = DataLen_from_registerNum_hex_list_get_str.upper()
        DataLen= com_send_date_shujuquzongchandu
        return DataLen

    #更给modbus.cfg为modbus.cfg.bak
    def set_modbus_cfg_to_modbus_cfg_bak(self):
        host_ip = self.telnet_host_ip
        username = self.telnet_username
        password = self.telnet_password
        xieyi_name = self.xieyi_name
        test_port = self.xieyi_test_port  #协议测试端口
        txt_file_name = self.xieyi_txt_file_name
        # command1 = 'cd /usr/app_install/db/database/'
        # command2 = 'cd /usr/app_install/protocol/bin'
        command3 = 'cd /usr/app_install/protocol/cfg/'    #进入目录
        command4 = 'mv modbus.cfg modbus.cfg.bak &>/dev/null &'  #修改文件modbus.cfg为modbus.cfg.bak
        if self.telnet_clicent_object == None:
            self.telnet_clicent_object = TelnetClient()
        else:
            self.telnet_clicent_object = self.telnet_clicent_object
        # 如果登录结果返加True，则执行命令，然后退出
        if self.telnet_clicent_object.login_host(host_ip, username, password):
            # telnet_client.execute_some_command(command1)
            # self.telnet_clicent_object.execute_some_command(command2)
            self.telnet_clicent_object.execute_some_command(command3)
            result = self.telnet_clicent_object.execute_some_command(command4)

    #上传本地modbus.cfg到远程/usr/app_install/protocol/cfg/modbus.cfg
    def ftp_up_modbus_cfg(self):
        pass

    #根据参数生成配置文件
    def set_xieyi_cfg(self):
        xieyi_cfg_dict={}
        protocol = self.xieyi_name
        xieyi_cfg_dict['protocol']= protocol
        idNum = self.xieyi_cfg_idNum
        xieyi_cfg_dict['idNum']= idNum
        startAddress = self.xieyi_cfg_startAddress
        xieyi_cfg_dict['startAddress']= startAddress
        functionCode = self.xieyi_cfg_functionCode
        xieyi_cfg_dict['functionCode']= functionCode
        registerNum = self.xieyi_cfg_registerNum
        xieyi_cfg_dict['registerNum']= registerNum
        DataLen = self.get_Datalen_from_registerNum(registerNum)
        xieyi_cfg_dict['DataLen']= DataLen
        dataLen = self.xieyi_cfg_dataLen
        xieyi_cfg_dict['dataLen']= dataLen
        dataType = self.xieyi_cfg_dataType
        xieyi_cfg_dict['dataType']= dataType
        self.outPutMyLog("协议字典：")
        self.outPutMyLog(xieyi_cfg_dict)
        #字典转为字符串数据
        xieyi_cfg_str = ''
        for key, value in xieyi_cfg_dict.items():
            one = key + '=' + value+';'
            self.outPutMyLog(one)
            xieyi_cfg_str=xieyi_cfg_str+one
        xieyi_cfg_str = xieyi_cfg_str
        self.outPutMyLog("****************************************")
        self.outPutMyLog(xieyi_cfg_str)
        self.outPutMyLog("****************************************")

        # 写入modbus.cfg文件
        hs = HandleTxt('modbus.cfg')
        hs.add_content(xieyi_cfg_str)
        again_modbus_content = self.read_modbus_cfg()
        self.outPutMyLog(again_modbus_content)

        #FTP 上传之前先更改原配置文件为备份文件名
        self.set_modbus_cfg_to_modbus_cfg_bak()

        #FTP上传modbus.cfg到远程位置
        self.ftp_up_modbus_cfg()


    #根据协议配置文件内容模拟出数据
    def get_xieyi_cfg(self):
        ji_shi_list = []
        shi_shi_list = []
        all_cfg_list = []
        xieyi_cfg_list = self.check_modbus_xieyi_cfg()
        xieyi_cfg_list_len = len(xieyi_cfg_list)
        if xieyi_cfg_list_len == 0:  #如果长度为0,说明没有配置文件
            #没有配置文件
            self.outPutMyLog("modbus.cfg文件中没有相关【%s】协议配置文件" % self.xieyi_name)
            self.outPutMyLog("需要进行配置！！！")
            xieyi_cfg_str = self.set_xieyi_cfg()
            hs = HandleTxt('modbus.cfg')
            hs.add_content(xieyi_cfg_str)
            again_modbus_content = self.read_modbus_cfg
            self.outPutMyLog(again_modbus_content)

        else:
            for i in range(0,xieyi_cfg_list_len):  #遍历配置内容
                if "instantSampleCmd" in  xieyi_cfg_list[i]:
                    self.outPutMyLog("存在及使采样配置：")
                    self.outPutMyLog(xieyi_cfg_list[i])
                    ji_shi_list.append(xieyi_cfg_list[i])
                else:
                    self.outPutMyLog("存在实时采样配置：")
                    self.outPutMyLog(xieyi_cfg_list[i])
                    shi_shi_list.append(xieyi_cfg_list[i])
            all_cfg_list.append(shi_shi_list)  #第一项为实时采样配置
            all_cfg_list.append(ji_shi_list)   #第二项为及时采样配置
        return all_cfg_list

    #根据实时采样配置获取相关内容
    def get_shi_shi_cfg(self,shi_shi_list):
        # 如果配置文件存在
        # 则根据配置文件得出
        shi_shi_list_len = len(shi_shi_list)
        if shi_shi_list_len != 1:
            self.outPutMyLog("获取到的配置条数有且应该只有1条，而实际为【%s】:" )
            self.outPutMyLog(shi_shi_list)
            return None
        else:
            shi_shi_cfg_dict = {}
            self.outPutMyLog("获取到1条配置信息，开始分解获取相关内容...")
            for shi_shi_list_one in shi_shi_list:
                #根据实时采样配置得出相应的内容
                #遍历列表项，看有几条相关配置
                #理论上有且只能有一条
                shi_shi_list_one_list = shi_shi_list_one.split(";")
                self.outPutMyLog(shi_shi_list_one_list)
                for shi_shi_list_one_list_one in shi_shi_list_one_list:
                    if 'protocol' in shi_shi_list_one_list_one:
                        shi_shi_list_one_list_one_list = shi_shi_list_one_list_one.split("=")
                        self.outPutMyLog("协议名称：")
                        protocol = shi_shi_list_one_list_one_list[1]
                        self.outPutMyLog(protocol)
                        shi_shi_cfg_dict['protocol']=protocol
                    if 'idNum' in shi_shi_list_one_list_one:
                        shi_shi_list_one_list_one_list = shi_shi_list_one_list_one.split("=")
                        self.outPutMyLog("设备ID：")
                        idNum = shi_shi_list_one_list_one_list[1]
                        self.outPutMyLog(idNum)
                        idNum_len = len(idNum)
                        if idNum_len == 1:
                            idNum = '0%s' % idNum
                            com_send_date_shebeiid = idNum.upper()
                        elif idNum_len > 1:
                            idNum = idNum
                            com_send_date_shebeiid = idNum.upper()
                        shi_shi_cfg_dict['idNum'] = com_send_date_shebeiid

                    if 'startAddress' in shi_shi_list_one_list_one:
                        shi_shi_list_one_list_one_list = shi_shi_list_one_list_one.split("=")
                        self.outPutMyLog("寄存器开始地址：")
                        startAddress = shi_shi_list_one_list_one_list[1]
                        self.outPutMyLog(startAddress)
                        shi_shi_cfg_dict['startAddress'] = startAddress

                    if 'functionCode' in shi_shi_list_one_list_one:
                        shi_shi_list_one_list_one_list = shi_shi_list_one_list_one.split("=")
                        self.outPutMyLog("功能码：")
                        functionCode = shi_shi_list_one_list_one_list[1]
                        self.outPutMyLog(functionCode)
                        functionCode_len = len(functionCode)
                        if functionCode_len == 1:
                            functionCode = '0%s' % functionCode
                            com_send_date_gongnengma = functionCode.upper()
                        elif functionCode_len > 1:
                            functionCode = functionCode
                            com_send_date_gongnengma = functionCode.upper()
                        shi_shi_cfg_dict['functionCode'] = com_send_date_gongnengma

                    if 'registerNum' in shi_shi_list_one_list_one:
                        shi_shi_list_one_list_one_list = shi_shi_list_one_list_one.split("=")
                        self.outPutMyLog("寄存器长度（或者个数）：")
                        registerNum = shi_shi_list_one_list_one_list[1]
                        self.outPutMyLog(registerNum)
                        shi_shi_cfg_dict['registerNum'] = registerNum
                        registerNum_int = int(registerNum, 16)  # 字符串转为16进制整数,其实就是按照16进制，转为整数如'0F'转为15
                        self.outPutMyLog("16进制整数：")
                        self.outPutMyLog(registerNum_int)
                        DataLen_from_registerNum = registerNum_int * 2
                        DataLen_from_registerNum_hex = hex(DataLen_from_registerNum)  # 10进制数转为16进制数
                        self.outPutMyLog(DataLen_from_registerNum_hex)
                        self.outPutMyLog("查看类型：")
                        self.outPutMyLog(type(DataLen_from_registerNum_hex))
                        DataLen_from_registerNum_hex_list = DataLen_from_registerNum_hex.split("x")
                        self.outPutMyLog("查看列表：")
                        self.outPutMyLog(DataLen_from_registerNum_hex_list)
                        DataLen_from_registerNum_hex_list_get = DataLen_from_registerNum_hex_list[1]
                        self.outPutMyLog(DataLen_from_registerNum_hex_list_get)
                        DataLen_from_registerNum_hex_list_get_str = str(DataLen_from_registerNum_hex_list_get)
                        DataLen_from_registerNum_hex_list_get_str_len = len(DataLen_from_registerNum_hex_list_get_str)
                        if DataLen_from_registerNum_hex_list_get_str_len == 1:
                            DataLen_from_registerNum_hex_list_get_str = "0%s" % DataLen_from_registerNum_hex_list_get_str
                            com_send_date_shujuquzongchandu = DataLen_from_registerNum_hex_list_get_str.upper()
                        elif DataLen_from_registerNum_hex_list_get_str_len == 2:
                            DataLen_from_registerNum_hex_list_get_str = DataLen_from_registerNum_hex_list_get_str
                            com_send_date_shujuquzongchandu = DataLen_from_registerNum_hex_list_get_str.upper()
                        shi_shi_cfg_dict['DataLen'] = com_send_date_shujuquzongchandu

                    if 'DataLen' in shi_shi_list_one_list_one:
                        shi_shi_list_one_list_one_list = shi_shi_list_one_list_one.split("=")
                        self.outPutMyLog("回复数据区总长度（一个寄存器占两个字节，所以数据区总长度能且只能为寄存器长度的2倍：）：")
                        self.outPutMyLog(shi_shi_list_one_list_one_list[1])
                        # self.outPutMyLog("（配置DataLen为registerNum的2倍，则配置正确；）")
                        # self.outPutMyLog("（未配置DataLen，DataLen的值默认为registerNum的2倍；）")
                        # self.outPutMyLog("（如果配置了DataLen，但是DataLen的值不是registerNum的2倍，则配置不正确；）")
                    if 'dataLen' in shi_shi_list_one_list_one:
                        shi_shi_list_one_list_one_list = shi_shi_list_one_list_one.split("=")
                        self.outPutMyLog("一个实时值长度（不是数据总长度，一个或多个实时值的长度加起来应该小于总长度）：")
                        dataLen = shi_shi_list_one_list_one_list[1]
                        self.outPutMyLog(dataLen)
                        # self.outPutMyLog("（总长度为实时值长度的整倍数）")
                        # self.outPutMyLog("（一个实时值的长度只能为2或4）")
                        # self.outPutMyLog("一个实时值的长度为2时，数据为短整数")
                        # self.outPutMyLog("一个实时值的长度为4时，数据为整数（无符号或有符号）或者单精度浮点数")
                        # self.outPutMyLog("例如配置多个因子值：一个实时值的长度为4时，要2个因子，则回复数据区总长度即DataLen的值必须为8，"
                        #       "而registerNum的值必须为4")
                        shi_shi_cfg_dict['dataLen'] = dataLen
                    if 'dataType' in shi_shi_list_one_list_one:
                        shi_shi_list_one_list_one_list = shi_shi_list_one_list_one.split("=")
                        self.outPutMyLog("数据类型（实际作用为字节序）：")
                        dataType = shi_shi_list_one_list_one_list[1]
                        self.outPutMyLog(dataType)
                        com_send_data_danyinzizhi_zijiexu = dataType
                        # self.outPutMyLog("""
                        # dataLen=2时：短整型数据
                        #     dataType=120、121、210、211四种类型，前两位表示字节序，末位0表示无符号短整型，末位1表示有符号短整型；
                        # dataLen=4时：
                        #     dataType=12340、43210、12341、43211等五位数表示数据类型为整型，前四个数字表示字节序，末位是0表无符号整型，末位是1表示有符号整型。
                        #     dataType=0时将前端设备回复的数据按照字节序为12340进行解析，解析出来的数是无符号整形数
                        #     dataType的值为四位数1234,、4321、1342、1423、等等时：此时dataType表示数据区的字节序，会将前端设备回复的数据按照设定的字节序，解析成对应的单精度浮点数，也就是解析成float型的数。
                        # 当dataLen不等于4时：不解析 """)
                        # self.outPutMyLog("(dataLen=2时,dataType只能为120、121、210、211、12、21，其中12等于120,21等于210)")
                        # self.outPutMyLog("(dataLen=4时,dataType只能是五位的、四位的、0)")
                        # self.outPutMyLog("(当dataType只能为五位的、四位的、0时，若dataLen不等于4，则不进行数据解析)")
                        shi_shi_cfg_dict['dataType'] = com_send_data_danyinzizhi_zijiexu

                break  # 只循环一次
            self.outPutMyLog("获取到的实时采样配置信息：")
            self.outPutMyLog(shi_shi_cfg_dict)
            return shi_shi_cfg_dict

    #根据数据区中长度和单因子实时值长度计算返回因子个数
    def get_com_send_date_yinzi_num_from_modbus_cfg(self,com_send_date_shujuquzongchandu,
                                                    com_send_date_danyinzizhi_long):
        #根据数据区总长度和单因子长度计算根据配置得出的因子个数
        com_send_date_shujuquzongchandu_int = int(com_send_date_shujuquzongchandu, 16)  # 字符串转换成16进制整数
        self.outPutMyLog(com_send_date_shujuquzongchandu_int)
        com_send_date_danyinzizhi_long_int = int(com_send_date_danyinzizhi_long)  # 字符串转换成10进制整数
        self.outPutMyLog(com_send_date_danyinzizhi_long_int)
        com_send_date_yinzi_num_int = com_send_date_shujuquzongchandu_int // com_send_date_danyinzizhi_long_int  # 只获取整数部分
        self.outPutMyLog(com_send_date_yinzi_num_int)
        com_send_date_yinzi_num = str(com_send_date_yinzi_num_int)
        self.outPutMyLog(com_send_date_yinzi_num)
        return com_send_date_yinzi_num


    #获取modbus.cfg一个主流程
    def get_modbus_cfg_main(self):
        if self.is_ftp_get_modbus_cfg:
            self.ftp_get_modbus_cfg()   #从数采仪中获取modbus.cfg到本地
        # xieyi_cfg_list = self.check_modbus_xieyi_cfg()   #读取modbus.cfg文件，查看是否有相关配置
        all_cfg_list = self.get_xieyi_cfg()  # 获取协议相关配置，包含xieyi_cfg_list = self.check_modbus_xieyi_cfg()
        self.outPutMyLog(all_cfg_list)
        shi_shi_list = all_cfg_list[0]
        shi_shi_cfg_dict = self.get_shi_shi_cfg(shi_shi_list)  #获取协议配置
        self.outPutMyLog("【%s】协议配置："%self.xieyi_name)
        self.outPutMyLog(shi_shi_cfg_dict)
        #根据传入的因子个数校验并修改配置
        com_send_date_shebeiid = shi_shi_cfg_dict['idNum']  # 设备ID
        com_send_date_gongnengma = shi_shi_cfg_dict['functionCode']  # 功能码
        com_send_date_shujuquzongchandu = shi_shi_cfg_dict['DataLen']  # 数据区总长度
        com_send_data_danyinzizhi_zijiexu = shi_shi_cfg_dict['dataType']  # 字节序

        # 单因子实时值长度
        com_send_date_danyinzizhi_long = shi_shi_cfg_dict['dataLen']

        #根据数据区总长度和单因子长度计算根据配置得出的因子个数
        com_send_date_yinzi_num = self.get_com_send_date_yinzi_num_from_modbus_cfg(com_send_date_shujuquzongchandu,
                                                                                   com_send_date_danyinzizhi_long)
        com_send_date_yinzi_num_int = int(com_send_date_yinzi_num)
        self.outPutMyLog("从配置文件中获取计算得出的因子个数为:")
        self.outPutMyLog(com_send_date_yinzi_num_int)
        if int(self.com_send_date_yinzi_num) == com_send_date_yinzi_num_int:
            self.outPutMyLog("从配置文件中获取计算得出的因子个数与传入的因子个数一致，都为【%s】，无需更改配置" % self.com_send_date_yinzi_num)
        else:
            self.outPutMyLog("从配置文件中获取计算得出的因子个数为:%s"% com_send_date_yinzi_num)
            self.outPutMyLog("传入的因子个数为:%s" % self.com_send_date_yinzi_num)
            self.outPutMyLog("从配置文件中获取计算得出的因子个数与传入的因子个数不一致")
            self.outPutMyLog("正在配置为传入的因子个数...")
            modbus_cfg_list = self.read_modbus_cfg()
            self.outPutMyLog(modbus_cfg_list)



    #自动生成两位16进制字符串
    def get_two_hex_str(self):
        from WWQRSTest.util.autoModbus.depend.autoMakeString import AutoMakeString
        ams = AutoMakeString()
        string_type = '0123456789ABCDEF'
        two_hex_str = ams.getBaseString(string_type,2)
        self.outPutMyLog(two_hex_str)
        return two_hex_str

    #根据单因子实时值长度自动生成单因子16进制字符串
    def auto_make_danyinzi_hex_str(self,danyinzizhi_long):
        danyinzizhi_long_int = int(danyinzizhi_long)
        danyinzizhi_hex_str_list=[]
        for i in range(0,danyinzizhi_long_int):
            two_hex_str = self.get_two_hex_str()
            danyinzizhi_hex_str_list.append(two_hex_str)
        self.outPutMyLog(danyinzizhi_hex_str_list)
        danyinzizhi_hex_str = ' '.join(danyinzizhi_hex_str_list)
        self.outPutMyLog(danyinzizhi_hex_str)
        return danyinzizhi_hex_str

    #根据单因子16进制字符串和字节序生成单因子浮点型预期结果
    #根据字节序获取到单精度浮点型的数值
    def get_danyinzi_expect_result(self,danyinzizhi_hex_str,danyinzizhi_zijiexu):
        # 根据字节序获取到单精度浮点型的数值
        danyinzi_zijiexu_list = []  # 字节序字符串转为列表要保存的内容
        self.outPutMyLog("单因子字节序：")
        self.outPutMyLog(danyinzizhi_zijiexu)
        danyinzizhi_zijiexu_len = len(danyinzizhi_zijiexu)
        self.outPutMyLog(danyinzizhi_zijiexu_len)
        # 如果dataType的值为4位（字符串长度为4）：
        if danyinzizhi_zijiexu_len == 4:
            # 将单因子字节序字符串转存到danyinzi_zijiexu_list中
            for i in danyinzizhi_zijiexu:
                danyinzi_zijiexu_list.append(i)
        self.outPutMyLog("字节序列表")
        self.outPutMyLog(danyinzi_zijiexu_list)  # 打印字节序列表

        danyinzizhi_hex_str_list = danyinzizhi_hex_str.split(" ")
        self.outPutMyLog(danyinzizhi_hex_str_list)
        danyinzizhi_hex_str_list_len = len(danyinzizhi_hex_str_list)
        danyinzizhi_zhengxu_hex_str_list = []
        for i in range(0, danyinzizhi_hex_str_list_len):
            danyinzizhi_hex_str_zhengxu = danyinzizhi_hex_str_list[int(danyinzi_zijiexu_list[i]) - 1]
            danyinzizhi_zhengxu_hex_str_list.append(danyinzizhi_hex_str_zhengxu)
        self.outPutMyLog("单因子（16进制文件）正序后的列表：")
        self.outPutMyLog(danyinzizhi_zhengxu_hex_str_list)

        # 单因子十六进制文件正确顺序值
        danyinzizhi_zhengxu_hex_str = ''.join(danyinzizhi_zhengxu_hex_str_list)
        self.outPutMyLog(danyinzizhi_zhengxu_hex_str)
        # 单因子十六进制字符串转为16进制数值
        hex_pre = r'0x'
        danyinzizhi_zhengxu_hex = hex_pre + danyinzizhi_zhengxu_hex_str.lower()
        # 打印单因子十六进制字符串转为16进制数值的值
        self.outPutMyLog(danyinzizhi_zhengxu_hex)
        from WWQRSTest.util.autoModbus.depend.floutOrHex import hex_to_float
        # 单因子16进制数值转为浮点型数据
        danyinzizhi_shuzizhi_float = hex_to_float(danyinzizhi_zhengxu_hex)
        # 打印得到的浮点数值
        self.outPutMyLog(danyinzizhi_shuzizhi_float)  # 得到十六进制文件解析出的数值
        # 将浮点数据保存六位小数（四舍五入规则）
        danyinzizhi_shuzizhi_float_with_six = '%3f' % danyinzizhi_shuzizhi_float  # 默认保留小数6个
        #转为字符串类型
        danyinzizhi_shuzizhi_float_with_six_str = str(danyinzizhi_shuzizhi_float_with_six)
        # 打印带6位小数点的浮点数
        self.outPutMyLog(danyinzizhi_shuzizhi_float_with_six_str)  # 默认保留小数6个
        return danyinzizhi_shuzizhi_float_with_six_str

    # 根据因子个数自动生成多个因子16进制字符串列表数据
    def auto_make_duoyinzi_hex_str_list(self,yinzigeshu,danyinzizhi_long):
        yinzigeshu_int = int(yinzigeshu)
        duoyinzizhi_hex_str_list = []
        for i in range(0, yinzigeshu_int):
            #自动生成单因子16进制字符串
            danyinzizhi_hex_str = self.auto_make_danyinzi_hex_str(danyinzizhi_long)
            duoyinzizhi_hex_str_list.append(danyinzizhi_hex_str)
        self.outPutMyLog("自动生成的多因子16进制文件列表：")
        self.outPutMyLog(duoyinzizhi_hex_str_list)
        return duoyinzizhi_hex_str_list


    #根据多个因子16进制字符串列表数据和获取期望得到的浮点型数据
    def get_expect_result_from_duoyinzi_hex_str(self, duoyinzizhi_hex_str_list,danyinzizhi_zijiexu):
        yinzigeshu_int = len(duoyinzizhi_hex_str_list)
        duoyinzizhi_expect_result_list = []
        duoyinzizhi_hex_str_and_expect_result_list = []
        for i in range(0,yinzigeshu_int):
            #单因子16进制字符串
            danyinzizhi_hex_str = duoyinzizhi_hex_str_list[i]
            self.outPutMyLog(danyinzizhi_hex_str)
            #根据字节序获取到单精度浮点型的数值
            danyinzizhi_shuzizhi_float_with_six_str = \
                self.get_danyinzi_expect_result(danyinzizhi_hex_str=danyinzizhi_hex_str,
                                                danyinzizhi_zijiexu=danyinzizhi_zijiexu)
            #将预期数值（带6位小数点的浮点数）放到预期数组中
            duoyinzizhi_expect_result_list.append(danyinzizhi_shuzizhi_float_with_six_str)
        #多因子16进制文件
        self.outPutMyLog("多因子16进制文件列表：")
        self.outPutMyLog(duoyinzizhi_hex_str_list)
        #按照字节序得到的浮点数据
        self.outPutMyLog("按照字节序得到的相应浮点数字的列表：")
        #打印预期数组
        self.outPutMyLog(duoyinzizhi_expect_result_list)
        duoyinzizhi_hex_str_and_expect_result_list.append(duoyinzizhi_hex_str_list)
        duoyinzizhi_hex_str_and_expect_result_list.append(duoyinzizhi_expect_result_list)
        return duoyinzizhi_hex_str_and_expect_result_list


    #根据获得的配置
    #如果有配置则生成数据
    #如果没有配置则设置配置
    def set_com_send_date(self):
        all_cfg_list = self.get_xieyi_cfg()
        self.outPutMyLog(all_cfg_list)
        self.outPutMyLog("实时采样配置：")
        self.outPutMyLog(all_cfg_list[0])
        self.outPutMyLog("及使采样配置：")
        self.outPutMyLog(all_cfg_list[1])
        shi_shi_list = all_cfg_list[0]
        shi_shi_list_len = len(shi_shi_list)

        if shi_shi_list != '':
            #如果配置文件存在
            #则根据配置文件得出
            shi_shi_cfg_dict = self.get_shi_shi_cfg(shi_shi_list)
            com_send_date_shebeiid = shi_shi_cfg_dict['idNum']   #设备ID
            com_send_date_gongnengma = shi_shi_cfg_dict['functionCode']  #功能码
            com_send_date_shujuquzongchandu = shi_shi_cfg_dict['DataLen']   #数据区总长度
            com_send_data_danyinzizhi_zijiexu = shi_shi_cfg_dict['dataType']   #字节序

            #单因子实时值长度
            com_send_date_danyinzizhi_long = shi_shi_cfg_dict['dataLen']

            #因子个数，是否根根据配置文件自动生成因子个数
            if self.com_send_date_yinzi_num_is_auto_make:
                #根据配置文件自动生成
                com_send_date_shujuquzongchandu_int = int(com_send_date_shujuquzongchandu, 16)  # 字符串转换成16进制整数
                self.outPutMyLog(com_send_date_shujuquzongchandu_int)
                com_send_date_danyinzizhi_long_int = int(com_send_date_danyinzizhi_long)  # 字符串转换成10进制整数
                self.outPutMyLog(com_send_date_danyinzizhi_long_int)
                com_send_date_yinzi_num_int = com_send_date_shujuquzongchandu_int//com_send_date_danyinzizhi_long_int  #只获取整数部分
                self.outPutMyLog(com_send_date_yinzi_num_int)
                com_send_date_yinzi_num = str(com_send_date_yinzi_num_int)
                self.outPutMyLog(com_send_date_yinzi_num)
            else:
                com_send_date_yinzi_num = self.com_send_date_yinzi_num

            auto_make_duoyinzi_hex_str_list = \
                self.auto_make_duoyinzi_hex_str_list(yinzigeshu=com_send_date_yinzi_num,
                                                     danyinzizhi_long=com_send_date_danyinzizhi_long)

             #是否自动生成
            if self.com_send_date_yinzi_hex_str_is_auto_make:
                duoyinzi_hex_str_list = auto_make_duoyinzi_hex_str_list    #自动生成的因子16进制字符串
            else:
                duoyinzi_hex_str_list =self.com_send_date_yinzi_hex_str_list  #直接传入的因子16进制字符串

            duoyinzizhi_hex_str_and_expect_result_list = \
                self.get_expect_result_from_duoyinzi_hex_str(duoyinzizhi_hex_str_list=duoyinzi_hex_str_list,
                                                             danyinzizhi_zijiexu=com_send_data_danyinzizhi_zijiexu)

            com_send_date_duoyinzizhi_hex_str_list = duoyinzizhi_hex_str_and_expect_result_list[0]
            self.outPutMyLog(com_send_date_duoyinzizhi_hex_str_list)
            com_send_date_duoyinzizhi_expect_result_list = duoyinzizhi_hex_str_and_expect_result_list[1]
            self.outPutMyLog(com_send_date_duoyinzizhi_expect_result_list)
            self.outPutMyLog("原期望数值列表：")
            self.outPutMyLog(self.xieyi_jiexi_expect_result_list)
            self.xieyi_jiexi_expect_result_list = com_send_date_duoyinzizhi_expect_result_list
            self.outPutMyLog("重设期望数值列表：")
            self.outPutMyLog(self.xieyi_jiexi_expect_result_list)

            com_send_date_duoyinzizhi_hex_str = ' '.join(com_send_date_duoyinzizhi_hex_str_list)
            self.outPutMyLog("多因子16进制字符串：")
            self.outPutMyLog(com_send_date_duoyinzizhi_hex_str)
            com_send_date = com_send_date_shebeiid+' '+com_send_date_gongnengma+' '+ com_send_date_shujuquzongchandu + ' '+com_send_date_duoyinzizhi_hex_str
            self.outPutMyLog(com_send_date)
            self.outPutMyLog("原发送数据：")
            self.outPutMyLog(self.com_send_date )
            self.com_send_date = com_send_date  #重置发送数据
            self.outPutMyLog("重设发送数据：")
            self.outPutMyLog(self.com_send_date)


    #web后台，写入设备
    def write_device(self):
        try:
            self.chromedriver = webdriver.Chrome()
            #登录web后台config
            self.chromedriver.get("http://192.168.101.104/")
            account_ele = self.chromedriver.find_element_by_xpath("/html/body/div/div/div/form/table/tbody/tr[2]/td[2]/input")
            account_ele.send_keys("config")
            password_ele = self.chromedriver.find_element_by_xpath("/html/body/div/div/div/form/table/tbody/tr[3]/td[2]/input")
            password_ele.send_keys("config")
            login_ele = self.chromedriver.find_element_by_xpath("/html/body/div/div/div/form/table/tbody/tr[4]/td/input[1]")
            login_ele.click()
            self.time_delay(6)

            #配置串口

            #点击写入设备
            frame_ele = self.chromedriver.find_element_by_xpath("/html/frameset/frameset/frame[1]")
            self.chromedriver.switch_to.frame(frame_ele)
            chuankoucanshupeizhi_ele = self.chromedriver.find_element_by_xpath("/html/body/div/div[4]/input")
            chuankoucanshupeizhi_ele.click()
            self.time_delay(3)
            self.chromedriver.switch_to.default_content()  # 退出frame

            #获取js弹窗
            alert = self.chromedriver.switch_to.alert
            # self.outPutMyLog(alert.text)
            # alert.accept()
        except Exception as e:
            self.outPutMyLog("问题：")
            self.outPutMyLog(e)

        self.time_delay(int(self.write_device_reatart_time))  #等该30秒

    #telnet_clicent连接
    def telnet_clicent(self):
        host_ip = self.telnet_host_ip
        username = self.telnet_username
        password = self.telnet_password
        telnet_client = TelnetClient()
        return telnet_client

    #运行telnet命令列表中每一条命令
    def run_telnet_command_list(self,mycommad_list):
        if self.telnet_clicent_object == None:
            self.telnet_clicent_object = TelnetClient()
        else:
            self.telnet_clicent_object = self.telnet_clicent_object

        #命令执行结果
        command_result_list = []
        # 如果登录结果返加True，则执行命令，然后退出
        if self.telnet_clicent_object.login_host(host_ip=self.telnet_host_ip,
                                                 username=self.telnet_username,
                                                 password=self.telnet_password):
            for mycommad in mycommad_list:
                result = self.telnet_clicent_object.execute_some_command(mycommad)
                command_result_list.append(result)
        return command_result_list

    # 关闭默认启动协议进程_写死通用
    def telnet_client_close_default_start_xieyi_common(self):
        mycommad_list = []
        mycommad_one = "stop_guard &"   #关闭守护进程，如果有的话
        mycommad_two = "cd %s" % self.xieyi_bin_dir  # 进入到协议二进制程序的bin目录下
        mycommad_three = "./Debug_scrip.sh %s&>/dev/null & " % self.xieyi_name  # 关闭自启动协议
        mycommad_four = "ps aux | grep %s | xargs kill -9 &>/dev/null &" % self.xieyi_name  #杀死协议进程
        mycommad_list.append(mycommad_one)
        mycommad_list.append(mycommad_two)
        mycommad_list.append(mycommad_three)
        mycommad_list.append(mycommad_four)
        self.run_telnet_command_list(mycommad_list)
        print("执行语句：")
        print(mycommad_list)
        self.time_delay(15)

    #关闭默认启动协议进程
    def telnet_client_close_default_start_xieyi(self,mycommad_list):
        self.run_telnet_command_list(mycommad_list)
        self.time_delay(15)

    #关闭默认启动协议进程后，重新启动协议_写死通用
    def telnet_client_rstart_xieyi_common(self):
        mycommad_list = []
        mycommad_one = "cd %s" % self.xieyi_bin_dir  # 进入到协议二进制程序的bin目录下
        mycommad_two = "rm -rf %s&>/dev/null &" % self.xieyi_txt_file_name  # 删除已有txt文件
        mycommad_three = "./%s --id=com%s_%s --log_level=develop &>%s &" % (self.xieyi_name,self.xieyi_test_port,self.xieyi_device_id ,self.xieyi_txt_file_name)  # 或启动程序
        mycommad_list.append(mycommad_one)
        mycommad_list.append(mycommad_two)
        mycommad_list.append(mycommad_three)
        self.run_telnet_command_list(mycommad_list)
        print("执行语句：")
        print(mycommad_list)
        self.time_delay(3)

    #关闭默认启动协议进程后，重新启动协议
    def telnet_client_rstart_xieyi(self,mycommad_list):
        self.run_telnet_command_list(mycommad_list)
        self.time_delay(3)
        # host_ip = self.telnet_host_ip
        # username = self.telnet_username
        # password = self.telnet_password
        # xieyi_name = self.xieyi_name
        # test_port = self.xieyi_test_port  #协议测试端口
        # txt_file_name = self.xieyi_txt_file_name
        # # command1 = 'cd /usr/app_install/db/database/'
        # # command2 = 'cd /usr/app_install/protocol/bin'
        # command2 = 'cd /usr/app_install/protocol/bin'
        # command3 = 'rm -rf %s &' % txt_file_name
        # command4 = './%s %s &>%s &' %(xieyi_name,test_port,txt_file_name)
        # # command4 = './%s %s &>/dev/nul &' %(xieyi_name,test_port)
        # if self.telnet_clicent_object == None:
        #     self.telnet_clicent_object = TelnetClient()
        # else:
        #     self.telnet_clicent_object = self.telnet_clicent_object
        # # 如果登录结果返加True，则执行命令，然后退出
        # if self.telnet_clicent_object.login_host(host_ip, username, password):
        #     # telnet_client.execute_some_command(command1)
        #     self.telnet_clicent_object.execute_some_command(command2)
        #     self.telnet_clicent_object.execute_some_command(command3)
        #     result=self.telnet_clicent_object.execute_some_command(command4)
        #     with open('result.txt','w') as f:
        #         f.write(result)
        #     # result = self.telnet_clicent_object.execute_some_command(command4)

    #处理发送的二进制数据
    def handle_Hexstr_to_bytes(self,HexDate):
        send_data_hex_str = HexDate
        send_data_hex_str_list = send_data_hex_str.split(' ')
        self.outPutMyLog(send_data_hex_str_list )
        send_data_bytes = b''
        for i in send_data_hex_str_list:
            str_hex_to_bytes = bytes.fromhex(i)  # 十六进制字符串转二进制
            self.outPutMyLog(str_hex_to_bytes)
            send_data_bytes = send_data_bytes + str_hex_to_bytes
        self.outPutMyLog(send_data_bytes)
        return send_data_bytes

    #处理发送的二进制数据
    def handle_Hexstr_list_to_bytes_list(self,HexDateList):
        send_data_bytes_list = []
        for HexDate in HexDateList:
            send_data_hex_str = HexDate
            send_data_hex_str_list = send_data_hex_str.split(' ')
            self.outPutMyLog(send_data_hex_str_list )
            send_data_bytes = b''
            for i in send_data_hex_str_list:
                str_hex_to_bytes = bytes.fromhex(i)  # 十六进制字符串转二进制
                self.outPutMyLog(str_hex_to_bytes)
                send_data_bytes = send_data_bytes + str_hex_to_bytes
            self.outPutMyLog(send_data_bytes)
            send_data_bytes_list.append(send_data_bytes)
        return send_data_bytes_list

    #处理发送的二进制数据
    def handle_send_data(self):
        #进行CRC16位低位在前校验
        mc = ModbusCrc()
        send_data_hex_str = mc.crc16Add_di(self.com_send_date)  #16进制字符串,进行CRC校验后
        self.outPutMyLog(send_data_hex_str)
        send_data_bytes = self.handle_Hexstr_to_bytes(send_data_hex_str)
        return send_data_bytes

    # 开启COM模拟接收和发送数据
    def com_recive_and_send(self):
        Port = self.com_port
        Baudrate = int(self.com_baudrate)
        Bytesize = int(self.com_bytesize)
        Parity = self.com_parity
        Stopbits = int(self.com_stopbits)
        # Senddate =self.com_send_date_bytes
        Senddate = None
        # Senddatelist =self.com_send_date_list_bytes
        # ExpectDateBytes=self.com_expect_date_bytes
        Senddatelist =None
        ExpectDateBytes=None
        rt = ComThread(Port=Port,Baudrate=Baudrate,Bytesize=Bytesize,Parity =Parity,Stopbits=Stopbits,
                       ExpectDateBytes=ExpectDateBytes,Senddate=Senddate,Senddatelist=Senddatelist)
        try:
            if rt.start():
                self.outPutMyLog(rt.l_serial.name)
                rt.waiting()
                self.outPutMyLog("The data is:%s,The Id is:%s" % (rt.data, rt.ID))
                rt.stop()
            else:
                pass
        except Exception as se:
            self.outPutMyLog(str(se))
        if rt.alive:
            rt.stop()
        self.outPutMyLog('')
        self.outPutMyLog('End OK .')
        del rt
        self.time_delay(30)  #等待30秒


    #解析收到的数据sender_hex_data_order_list的数据为一条一条可收发的二进制
    def get_sender_hex_data_order_list_bytes_list(self,sender_hex_data_order_list):
        print("sender_hex_data_order_list:")
        print(sender_hex_data_order_list)
        sender_hex_data_order_list_len = len(sender_hex_data_order_list)
        sender_hex_data_order_list_bytes = []
        for i in range(0,sender_hex_data_order_list_len):
            sender_hex_data_order_list_bytes_one = []
            is_send_hex = sender_hex_data_order_list[i][6]
            if is_send_hex:   #如果是16进制
                com_send_date_one_bytes = self.handle_Hexstr_to_bytes(sender_hex_data_order_list[i][0])
            else:  #否则为ASCII
                from WWQRSTest.util.autoModbus.depend.floutOrHex import strtobytes
                com_send_date_one_bytes = strtobytes(sender_hex_data_order_list[i][0])
            is_need_expect = sender_hex_data_order_list[i][1]

            if sender_hex_data_order_list[i][2]==None:
                com_expect_date_bytes = None
            else:
                is_receive_hex = sender_hex_data_order_list[i][7]
                if is_receive_hex:  #如果是16进制
                    com_expect_date_bytes = self.handle_Hexstr_to_bytes(sender_hex_data_order_list[i][2])
                else:  #否则为ASCII
                    from WWQRSTest.util.autoModbus.depend.floutOrHex import strtobytes
                    com_expect_date_bytes = strtobytes(sender_hex_data_order_list[i][2])
            is_need_after_expect = sender_hex_data_order_list[i][4]
            is_just_one = sender_hex_data_order_list[i][5]
            sender_hex_data_order_list_bytes_one.append(com_send_date_one_bytes)
            sender_hex_data_order_list_bytes_one.append(is_need_expect)
            sender_hex_data_order_list_bytes_one.append(com_expect_date_bytes)
            sender_hex_data_order_list_bytes_one.append(is_need_after_expect)
            sender_hex_data_order_list_bytes_one.append(is_just_one)
            sender_hex_data_order_list_bytes.append(sender_hex_data_order_list_bytes_one)
        print("sender_hex_data_order_list_bytes:")
        print(sender_hex_data_order_list_bytes)
        return sender_hex_data_order_list_bytes

    # 开启COM模拟接收和发送数据_使用参数
    def com_recive_and_send_with_params(self,sender_hex_data_order_list):

        Port = self.com_port
        Baudrate = int(self.com_baudrate)
        Bytesize = int(self.com_bytesize)
        Parity = self.com_parity
        Stopbits = int(self.com_stopbits)
        # Senddate =self.com_send_date_bytes
        Senddate = None
        Senddatelist =None
        ExpectDateBytes=None
        SenderHexDataOrderBytesList = self.get_sender_hex_data_order_list_bytes_list(sender_hex_data_order_list)
        rt = ComThread(Port=Port,Baudrate=Baudrate,Bytesize=Bytesize,Parity =Parity,Stopbits=Stopbits,
                       SenderHexDataOrderBytesList = SenderHexDataOrderBytesList,
                       ExpectDateBytes=ExpectDateBytes,Senddate=Senddate,Senddatelist=Senddatelist)
        try:
            if rt.start():
                self.outPutMyLog(rt.l_serial.name)
                rt.waiting()
                self.outPutMyLog("The data is:%s,The Id is:%s" % (rt.data, rt.ID))
                rt.stop()
            else:
                pass
        except Exception as se:
            self.outPutMyLog(str(se))
        if rt.alive:
            rt.stop()
        self.outPutMyLog('')
        self.outPutMyLog('End OK .')
        del rt
        self.time_delay(30)  #等待30秒

    #ftp获取串口解析文件_通用函数
    def ftp_down_xieyi_file_commom(self):
        xieyi_remote_file = self.xieyi_bin_dir + '/' + self.xieyi_txt_file_name
        xieyi_local_file = self.xieyi_txt_file_name
        self.time_delay(60)
        self.run_ftp_down(remote_file=xieyi_remote_file, local_file=xieyi_local_file)


    #ftp获取串口解析文件
    def ftp_get_file(self):
        if self.ftp_client_object == None:
            self.ftp_client_object = self.ftp_connnect()
        else:
            self.ftp_client_object = self.ftp_client_object

        remote_file = '/usr/app_install/protocol/bin/%s' % self.xieyi_txt_file_name
        local_file = self.xieyi_txt_file_name
        self.ftp_client_object.ftp_download(remote_file, local_file)
        self.time_delay(3)

    #判断文件中存在正确的解析值
    def assert_file_success(self):
        local_file = self.xieyi_txt_file_name
        with open(local_file, "r", encoding='utf-8') as f:
            result = f.read()
            self.outPutMyLog("获取到文件【%s】中的内容为：" % str(local_file))
            self.outPutMyLog(result)
        expect_result_list = self.xieyi_jiexi_expect_result_list
        for expect_result in expect_result_list:
        # expect_result = self.xieyi_jiexi_expect_result
            if expect_result in result:
                self.outPutMyLog("查到解析结果：%s" % expect_result)
                self.outPutMyLog("解析数据正确")
                assert True
            else:
                self.outPutErrorMyLog("解析数据失败！！！")
                assert False

    #ftp获取串口解析文件
    def ftp_get_remote_db_file(self):
        if self.ftp_client_object == None:
            self.ftp_client_object = self.ftp_connnect()
        else:
            self.ftp_client_object = self.ftp_client_object

        remote_file = self.xieyi_db_remote_path
        local_file = self.xieyi_db
        self.ftp_client_object.ftp_download(remote_file, local_file)
        self.time_delay(3)

    #验证远程/tmp/real.db中的实时数据是否与解析值一致：
    def assert_real_db_success(self):
        local_db = self.xieyi_db
        table_name = self.xieyi_db_table_name
        ms = MySqlite(sql_name=local_db,table_name=table_name)
        table_content_list = ms.get_table_content()
        self.outPutMyLog("表的内容：")
        self.outPutMyLog(table_content_list)
        # 循环遍历预期结果
        expect_result_list = self.xieyi_jiexi_expect_result_list
        message_list = []
        for expect_result_one in expect_result_list:
            self.outPutMyLog("遍历数据：")
            self.outPutMyLog(expect_result_one)
            assert_result_flag = False
            #遍历数据库查看预期结果是否在数据库中：
            for table_content_one in table_content_list:
                self.outPutMyLog("遍历表：")
                self.outPutMyLog(table_content_one)
                self.outPutMyLog(table_content_one)
                #遍历一条数据的字段值，如果存在字段值则停止本次验证
                for one_ziduan_value in table_content_one:
                    #如果值在里面，则打印
                    if expect_result_one in str(one_ziduan_value):
                        message_one = "验证值【%s】在实际值【%s】中。"%(expect_result_one,one_ziduan_value)
                        message_list.append(message_one)
                        self.outPutMyLog("退出从一条数据中查找一个预期结果的循环")
                        assert_result_flag = True
                        break  #退出本次循环
                self.outPutMyLog("退出遍历一个表中的每条数据的循环")
                if assert_result_flag:
                    break
            self.outPutMyLog("开始进入下一个预期结果值的查找的循环")
        if assert_result_flag :
            self.outPutMyLog("查找结果信息：")
            self.outPutMyLog(message_list)
        else:
            self.outPutErrorMyLog("没有在数据库【%s】中的【%s】表中查找到【%s】" % (local_db,table_name,str(expect_result_list)))
        return assert_result_flag




    #处理tcp_server接受数据
    def tcp_server_receive(self):
        self.tcp_server_object = TcpServerReceive(ip=self.tcp_server_ip,
                                                  port=int(self.tcp_server_port),
                                                  file_name=self.tcp_server_file_name)
        self.tcp_server_object.tcp_server_receive()
        self.tcp_server_object.tcp_server_close()

    #断言tcp_server接受到上报的数据
    def assert_tcp_server_receive_success(self):
        local_file = self.tcp_server_file_name
        with open(local_file, "r", encoding='utf-8') as f:
            result = f.read()
            self.outPutMyLog("获取的内容：")
            self.outPutMyLog(result)
        expect_result_list = self.xieyi_jiexi_expect_result_list
        for expect_result in expect_result_list:
        # expect_result = self.xieyi_jiexi_expect_result
            if expect_result in result:
                self.outPutMyLog("查到上报结果：%s" % expect_result)
                self.outPutMyLog("上报数据正确")
                assert True
            else:
                self.outPutErrorMyLog("上报数据失败！！！")
                assert False


    #一些善后工作
    def end_work(self):
        if self.telnet_clicent_object != None:
            self.telnet_clicent_object.logout_host()  #如果telnet连接则退出
        if self.ftp_client_object != None:
            self.ftp_client_object.ftp_close()   #如果tfp连接，则退出


    def run_test(self):
        # # 0-1获取配置文件信息，如果存在则查看，不存在则配置
        # if self.is_ftp_get_modbus_cfg:
        #     self.ftp_get_modbus_cfg()
        # # 0-2查看有没有相应的程序，有则显示，无则上传
        # if  self.is_check_modbus_xieyi_cfg:
        #     self.check_modbus_xieyi_cfg()
        # if  self.is_set_com_send_date:
        #     self.set_com_send_date()
        #
        # if self.is_get_modbus_cfg_main:
        #     self.get_modbus_cfg_main()

        #0-1.ftp上传协议二进制文件和配置文件

        #1.web后台，写入设备
        if self.is_write_device:
            self.write_device()
        #2.关闭默认启动协议进程
        if self.is_telnet_client_close_default_start_xieyi:
            self.telnet_client_close_default_start_xieyi()
        #3.关闭默认启动协议进程后，重新启动协议
        if self.is_telnet_client_rstart_xieyi:
            self.telnet_client_rstart_xieyi()
        #4.开启COM模拟接收和发送数据
        if self.is_com_recive_and_send:
            self.com_recive_and_send()
        #5.ftp获取串口解析文件
        if self.is_ftp_get_file:
            self.ftp_get_file()
        #6.判断文件中存在正确的解析值
        if self.is_assert_file_success:
            self.assert_file_success()

        #5.ftp获取实时数据库文件
        if self.is_ftp_get_remote_db_file:
            self.ftp_get_remote_db_file()
        #6.判断实时数据库文件中存在正确的解析值
        if self.is_assert_real_db_success:
            self.assert_real_db_success()

        #7.是否查看上报平台数据
        if self.is_tcp_server_receive:
            self.tcp_server_receive()

        #8.检查上报数据中存在解析后的数值或上报的数值
        if self.is_assert_tcp_server_receive_success:
            self.assert_tcp_server_receive_success()

        #7善后工作
        self.end_work()

if __name__ == '__main__':
    am = AutoModbus()
    am.run_test()
    # am.auto_make_duoyinzi_hex_str(4,4)
    # am.get_modbus_cfg_main()
    # am.set_xieyi_cfg()
