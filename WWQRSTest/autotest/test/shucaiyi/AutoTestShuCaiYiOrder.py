import unittest
import datetime
# ----------------------------------------------------------------------
import os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wanwenyc.settings")
django.setup()
# ----------------------------------------------------------------------
# 独运行某一个py文件时会出现如下错误：django.core.exceptions.AppRegistryNotReady: Apps aren't loaded yet.，以上内容可以解决此问题,加载django中的App

from WWTest.util.getTimeStr import GetTimeStr


from WWQRSTest.util.autoModbus.autoModbus import AutoModbus


class TestShuCaiYiClass(unittest.TestCase):  # 创建测试类

    @classmethod  # 类方法，只执行一次，但必须要加注解@classmethod,且名字固定为setUpClass
    def setUpClass(cls):
        pass

    @classmethod  # 类方法，只执行一次，但必须要加注解@classmethod,且名字固定为tearDownClass
    def tearDownClass(cls):
        # cls.activeweb.closeBrowse()
        pass

    def setUp(self):  # 每条用例执行测试之前都要执行此方法
        pass

    def tearDown(self):  # 每条用例执行测试之后都要执行此方法
        pass

    def defineshucaiyi(self,
                           case_id,
                           depend_config_id
                        ):

        #通过协议配置模块获取配置相关信息
        from shucaiyidate.modelsorder import XieyiConfigDateOrder
        xieyiconfigdateorder = XieyiConfigDateOrder.objects.filter(id=depend_config_id)
        xieyiconfigdateorder_count = xieyiconfigdateorder.count()
        if xieyiconfigdateorder_count == 0:
            print("测试用例没有选择相关配置依赖，请选择相关配置依赖")
            assert False
        else:
            #获取配置信息
            for xieyiconfigdateorder_one in xieyiconfigdateorder:
                is_web_modify_xieyi = xieyiconfigdateorder_one.is_web_modify_xieyi
                web_type = xieyiconfigdateorder_one.web_type
                web_xieyi_name = xieyiconfigdateorder_one.web_xieyi_name
                web_xieyi_yinzi = xieyiconfigdateorder_one.web_xieyi_yinzi
                is_upload_dev_config_file = xieyiconfigdateorder_one.is_upload_dev_config_file
                nodeconfig_id = xieyiconfigdateorder_one.nodeconfig_id
                dev_config_name = xieyiconfigdateorder_one.dev_config_name
                telnet_host_ip = xieyiconfigdateorder_one.telnet_host_ip
                telnet_username = xieyiconfigdateorder_one.telnet_username
                telnet_password = xieyiconfigdateorder_one.telnet_password
                xieyi_name = xieyiconfigdateorder_one.xieyi_name
                xieyi_test_port = xieyiconfigdateorder_one.xieyi_test_port
                xieyi_device_id = xieyiconfigdateorder_one.xieyi_device_id
                com_port = xieyiconfigdateorder_one.com_port
                com_baudrate = xieyiconfigdateorder_one.com_baudrate
                com_bytesize = xieyiconfigdateorder_one.com_bytesize
                com_parity = xieyiconfigdateorder_one.com_parity
                com_stopbits = xieyiconfigdateorder_one.com_stopbits
                is_recriminat_recive_and_send = xieyiconfigdateorder_one.is_recriminat_recive_and_send
                tcp_server_ip = xieyiconfigdateorder_one.tcp_server_ip
                tcp_server_port = xieyiconfigdateorder_one.tcp_server_port
                tcp_server_xieyi = xieyiconfigdateorder_one.tcp_server_xieyi
                tcp_receive_delay_min = xieyiconfigdateorder_one.tcp_receive_delay_min
                is_ftp_upload = xieyiconfigdateorder_one.is_ftp_upload
                is_com_recive_and_send = xieyiconfigdateorder_one.is_com_recive_and_send
                is_with_code_assert = xieyiconfigdateorder_one.is_with_code_assert
                is_assert_file_success = xieyiconfigdateorder_one.is_assert_file_success
                is_assert_real_db_success = xieyiconfigdateorder_one.is_assert_real_db_success
                is_assert_tcp_server_receive_success = xieyiconfigdateorder_one.is_assert_tcp_server_receive_success
                break



            #通过发送和接收数据部分获取发送和接收的数据以及预期结果的list
            from depend.shucaiyi.modelorderdepend.senderHexDataOrderDependClass import senderhexdataorderdepend
            sender_hex_data_order_list = senderhexdataorderdepend.makeSenderHexDataOrderList(case_id)

            xieyi_jiexi_expect_result_list = []
            for sender_hex_data_order_list_one in sender_hex_data_order_list:
                is_assert_expect = sender_hex_data_order_list_one[9]
                if is_assert_expect:  #如果进行结果断言
                    gts = GetTimeStr()
                    expect_one_list =gts.getListFromStr(sender_hex_data_order_list_one[3], ",")
                    for expect_one in expect_one_list:
                        xieyi_jiexi_expect_result_list.append(expect_one)  #添加断言结果到预期校验数据列表中
            print("预期校验数据：")
            print(xieyi_jiexi_expect_result_list)



            print("web_type:")
            print(web_type)

            select_xie_yi = web_xieyi_name
            if web_xieyi_yinzi !=None:
                gts = GetTimeStr()
                select_jian_kong_yin_zi_list = gts.getListFromStr(web_xieyi_yinzi,",")


            #是否通过web修改协议
            if is_web_modify_xieyi:   #如果是，则需要通过web修改协议
                if web_type =="P1":  #如果是V6,则走V6的web程序
                    from depend.shucaiyi.dependwebconfig.webConfigClass import WebVSixConfig
                    wc = WebVSixConfig(select_xie_yi=select_xie_yi,
                                       select_jian_kong_yin_zi_list=select_jian_kong_yin_zi_list,
                                       ip=telnet_host_ip,
                                       service_ip=tcp_server_ip,
                                       service_port=tcp_server_port,
                                       device_id=xieyi_device_id,
                                       select_shangbao_xieyi=tcp_server_xieyi)
                    is_web_success = wc.run()
                elif web_type =="P0" : #如果是V5,则走V5web程序
                    from depend.shucaiyi.dependwebconfig.webOldConfigClass import WebOldConfig
                    wc = WebOldConfig(select_xie_yi=select_xie_yi,
                                      select_jian_kong_yin_zi_list=select_jian_kong_yin_zi_list,
                                      ip=telnet_host_ip,
                                      service_ip=tcp_server_ip,
                                      service_port=tcp_server_port,
                                      device_id=xieyi_device_id,
                                      select_shangbao_xieyi=tcp_server_xieyi)
                    is_web_success = wc.run()
                elif web_type =="P2" : #如果是V5.1,则走V5.1web程序
                    from depend.shucaiyi.dependwebconfig.webV51ConfigClass import WebVFiveOneConfig
                    wc = WebVFiveOneConfig(select_xie_yi=select_xie_yi,
                                           select_jian_kong_yin_zi_list=select_jian_kong_yin_zi_list,
                                           ip=telnet_host_ip,
                                           service_ip=tcp_server_ip,
                                           service_port=tcp_server_port,
                                           device_id=xieyi_device_id,
                                           select_shangbao_xieyi=tcp_server_xieyi)
                    is_web_success = wc.run()
                elif web_type =="P3" : #如果是E4,则走E4web程序
                    from depend.shucaiyi.dependwebconfig.webE4ConfigClass import WebEFourConfig
                    wc = WebEFourConfig(select_xie_yi=select_xie_yi,
                                        select_jian_kong_yin_zi_list=select_jian_kong_yin_zi_list,
                                        ip=telnet_host_ip,
                                        service_ip=tcp_server_ip,
                                        service_port=tcp_server_port,
                                        device_id=xieyi_device_id)
                    is_web_success = wc.run()


                self.assertTrue(is_web_success,"web端修改协议失败，原因为：因子配置列表中没有全部的监控因子，需要进行添加，添加的因子请查看上面信息！！！")



            am = AutoModbus(
                telnet_host_ip=telnet_host_ip,
                telnet_username=telnet_username,
                telnet_password=telnet_password,
                # xieyi_bin_dir=xieyi_bin_dir,
                xieyi_name=xieyi_name,
                xieyi_test_port=xieyi_test_port,
                xieyi_device_id = xieyi_device_id,
                com_port=com_port,
                com_baudrate=com_baudrate,
                com_bytesize=com_bytesize,
                com_parity=com_parity,
                com_stopbits=com_stopbits,

                xieyi_jiexi_expect_result_list=xieyi_jiexi_expect_result_list,

                # xieyi_db=xieyi_db,
                # xieyi_db_remote_path=xieyi_db_remote_path,
                # xieyi_db_table_name=xieyi_db_table_name,

                tcp_server_ip=tcp_server_ip,
                tcp_server_port=tcp_server_port,
                tcp_receive_delay_min = tcp_receive_delay_min
            )

            if is_upload_dev_config_file:  # 如果上传配置文件，则上传配置文件
                # 根据 nodeconfig_id获取对应的配置文件
                print("nodeconfig_id:")
                print(nodeconfig_id)
                if nodeconfig_id != None:  # 如果不为空，则上传配置文件
                    # 根据依赖配置获取相应的配置文件
                    from shucaiyidate.modelsnewdev import NodeConfig
                    depend_node_config_list = NodeConfig.objects.filter(id=nodeconfig_id)
                    for depend_node_config_one in depend_node_config_list:
                        dev_path = depend_node_config_one.dev_file.path
                        print("本地dev配置文件的路径：")
                        print(dev_path)
                        break  # 退出循环

                    local_dev_path = dev_path
                    if web_type == "P1":  # 如果是V6,则走v6的关闭原有协议命令
                        xieyi_bin_dir_fixed_v6 = "/usr/app_install/collect/bin"
                        remote_dev_path = "%s/devices.cfg/%s" % (xieyi_bin_dir_fixed_v6, dev_config_name)
                    elif web_type == "P0" or web_type == "P2":  # 如果是V5,则走V5的关闭原有协议命令
                        xieyi_bin_dir_fixed_v5 = "/usr/app_install/protocol/bin"
                        remote_dev_path = "%s/devices.cfg/%s" % (xieyi_bin_dir_fixed_v5, dev_config_name)
                    dev_upload_file_list_all = []
                    dev_upload_file_list_one = []
                    dev_upload_file_list_one.append(remote_dev_path)
                    dev_upload_file_list_one.append(local_dev_path)
                    dev_upload_file_list_all.append(dev_upload_file_list_one)
                    # 处理本地文件上传到远程数采仪配置文件目录下
                    am.run_ftp_up_load_file_list(dev_upload_file_list_all)
                else:
                    print("没有依赖配置，请选择相应的dev配置依赖，如需要的话。")
            else:
                print("不上传国标配置文件。")

            #处理通用的文件上传
            ftp_up_load_file_list = [['/usr/app_install/collect/bin/text.txt','D:/pycharmproject/shangbaogongju/WWQRSTest/util/text.txt'],
                                     ['/usr/app_install/collect/bin/result1.txt','D:/pycharmproject/shangbaogongju/WWQRSTest/util/result1.txt']]
            from depend.shucaiyi.ftpUploadFileDependClass import ftpuploadfiledepend
            ftp_up_load_file_list = ftpuploadfiledepend.makeFtpUpliadFileList(depend_id=case_id)   #传入程序的id，获取上传文件列表
            #1.是否上传配置文件
            #1-1.上传配置文件之前先修改远程文件名称为备份文件名
            #1-2.上传配置文件
            #上传文件进行可执行命令
            #先分离远程文件目录，获取到目录和文件
            if ftp_up_load_file_list == []: #则说明没有填写上传文件路径，不进行文件上传
                pass
            else:
                if is_ftp_upload:   #如果需要上传文件
                    am.run_ftp_up_load_file_list(ftp_up_load_file_list)


            #如果需要验证数据库和平台上报数据，需要先删除原数据库中已经存在的内容
            #然后重启，运行后续操作
            # 是否验证实时数据
            if is_assert_real_db_success:  # 是否验证实时数据，是，则需要先删除远程实时数据库的内容

                am.telnet_client_delete_real_or_rtd_db()  #删除原有实时数据库

            #是否验证平台上报内容
            if is_assert_tcp_server_receive_success:  # 是否验证平台上报内容，是，则需要清除已经存在的平台数据库
                am.telnet_client_delete_upload_db()   #删除原有上报平台数据

            #如果验证数据库
            #验证平台接收数据
            #上传dev配置文件
            #都需要重启设备
            if is_assert_real_db_success or is_assert_tcp_server_receive_success or is_upload_dev_config_file:  #如果需要验证实时数据库中的数据或需要验证平台上报内容，则需要删除原有数据后，重启
                am.telnet_client_restart_scy()


            #是否在协议文件中找到相应的解析内容
            if is_assert_file_success:  # 是否在协议文件中找到相应的解析内容,是，则需要关闭原有协议,重新运行协议，并生成协议解析文件
                #关闭原有协议
                if web_type == "P1":  # 如果是V6,则走v6的关闭原有协议命令
                    xieyi_bin_dir_fixed_v6 = "/usr/app_install/collect/bin"
                    am.telnet_client_close_default_start_xieyi_common_with_param(xieyi_bin_dir=xieyi_bin_dir_fixed_v6)  # 执行关闭协议通用命令 V6版本协议
                elif web_type == "P0" or web_type == "P2" or web_type =="P3":  # 如果是V5,则走V5的关闭原有协议命令
                    xieyi_bin_dir_fixed_v5 = "/usr/app_install/protocol/bin"
                    am.telnet_client_close_default_start_xieyi_common_with_param(xieyi_bin_dir=xieyi_bin_dir_fixed_v5)  # 执行关闭协议通用命令 V5版本协议

                # 重新运行协议，并生成协议解析文件，v6版本与非v6版本重启的命令不同
                if web_type == "P1":  # 如果是V6,则走v6的重启协议命令
                    xieyi_bin_dir_fixed_v6 = "/usr/app_install/collect/bin"
                    am.telnet_client_rstart_xieyi_common_with_param(xieyi_bin_dir=xieyi_bin_dir_fixed_v6)  # 执行重启通用命令 V6版本协议
                elif web_type == "P0" or web_type == "P2" or web_type =="P3":  # 如果是V5,则走V5的重启协议命令
                    xieyi_bin_dir_fixed_v5 = "/usr/app_install/protocol/bin"
                    am.telnet_client_rstart_xieyi_common_not_v6_with_param(xieyi_bin_dir=xieyi_bin_dir_fixed_v5)  # 执行重启通用命令 非V6版本


            #是否发送数据
            if is_com_recive_and_send:
                am.com_recive_and_send_with_params(sender_hex_data_order_list)  #处理收发数据


            #是否在协议文件中找到相应的解析内容
            if is_assert_file_success:  #是否在协议文件中找到相应的解析内容,是，则需要下载解析文件
                # am.ftp_down_xieyi_file_commom()  #执行获取解析文件通用函数
                if web_type == "P1":  # 如果是V6,则走v6的解析文件函数
                    xieyi_bin_dir_fixed_v6 = "/usr/app_install/collect/bin"
                    am.ftp_down_xieyi_file_commom_with_param(xieyi_bin_dir_fixed_v6)  # 获取解析文件通用命令 V6版本协议
                elif web_type == "P0" or web_type == "P2" or web_type =="P3":  # 如果是V5,则走V5的重启协议命令
                    xieyi_bin_dir_fixed_v5 = "/usr/app_install/protocol/bin"
                    am.ftp_down_xieyi_file_commom_with_param(xieyi_bin_dir_fixed_v5)  # 获取解析文件通用命令 V5版本协议


            #是否ftp下载实时数据
            if is_assert_real_db_success: # 是否验证实时数据，是，则需要下载远程实时数据库
                # am.ftp_get_remote_db_file()
                if web_type == "P1":  # 如果是V6,则走v6的解析文件函数
                    xieyi_db_remote_path_fixed_v6 = "/tmp/database.d/rtd.db"
                    xieyi_db_fixed_v6 = "rtd.db"
                    am.ftp_get_remote_db_file_with_param(xieyi_db_remote_path=xieyi_db_remote_path_fixed_v6,
                                                         xieyi_db=xieyi_db_fixed_v6) # 获取远程实时数据库通用命令 V6版本协议
                elif web_type == "P0" or web_type == "P2" or web_type =="P3":  # 如果是V5,则走V5的重启协议命令
                    xieyi_db_remote_path_fixed_v5 = "/tmp/real.db"
                    xieyi_db_fixed_v5 = "real.db"
                    am.ftp_get_remote_db_file_with_param(xieyi_db_remote_path=xieyi_db_remote_path_fixed_v5,
                                                         xieyi_db=xieyi_db_fixed_v5) # 获取远程实时数据库通用命令 V5版本协议



            #是否上报平台
            # if is_tcp_server_receive:
            if is_assert_tcp_server_receive_success:  #是否验证平台上报内容，是，则需要接收上报平台数据
                is_receive_normal = am.tcp_server_receive()  #是否接受数据正常
                self.assertTrue(is_receive_normal, msg=u"平台接收数据失败")

            am.end_work()   #善后工作

            # 是否发送和接收反控报文
            if is_recriminat_recive_and_send:  #如果进行反控
                from WWQRSTest.util.autoModbus.depend.tcpServerReceive import TcpServerReceive
                now_time_str = str(datetime.datetime.now().strftime('%Y%m%d%H%M%S%f'))  # 格式化到毫秒
                file_name = "%s_tcp_service_receive.txt" % now_time_str
                tsr = TcpServerReceive(ip=tcp_server_ip, port=int(tcp_server_port), file_name=file_name,
                                       tcp_receive_delay_min=int(tcp_receive_delay_min))
                #反控数据接收和发送
                from depend.shucaiyi.modelorderdepend.RecriminatDataOrderDependClass import recriminatdataorderdepend
                recriminat_data_list = recriminatdataorderdepend.makeRecriminatDataOrderList(depend_id=case_id)

                # tsr.tcp_server_send(senddata=recriminat_send_date)  # 发送数据
                tsr.tcp_server_send_data_list(senddata_list=recriminat_data_list)
                tsr.tcp_server_receive()  # 接受数据
                tsr.tcp_server_close()  # 关闭tcp服务

                # 断言反控响应指令在报文中
                # 读取文件内容
                with open(file_name, "r", encoding='utf-8') as f:
                    result = f.read()
                    print("获取的内容：")
                    print(result)
                # 断言响应报文在接受的文件中
                for recriminat_data_one in  recriminat_data_list:
                    recriminat_send_date = recriminat_data_one[1]
                    recriminat_receive_date = recriminat_data_one[2]
                    self.assertIn(recriminat_receive_date, result, "反控响应内容不在报文中！！！")
                    print("反控发送的指令内容：%s" % str(recriminat_send_date))
                    print("反控响应的内容：%s" % str(recriminat_receive_date))


            #是否在协议文件中找到相应的解析内容
            if is_assert_file_success:
                if is_with_code_assert:  # 如果断言结果带有因子代码，则用监控因子和数据值拼接后断言
                    jiankongyinzi_list = select_jian_kong_yin_zi_list
                    shuju_list = xieyi_jiexi_expect_result_list
                    jiankongyinzi_list_len = len(jiankongyinzi_list)
                    shuju_list_len = len(shuju_list)
                    jiexi_expect_result_list = []
                    if jiankongyinzi_list_len == shuju_list_len:
                        # 将因子与数据拼接形成断言内容：
                        for i in range(0,jiankongyinzi_list_len):
                            if web_type == "P1" or web_type == "P2":  # 如果是V6,则走v6的日志拼接
                                jiexi_expect_result_one = "code:%s, rtd:%s" % (
                                str(jiankongyinzi_list[i]), str(shuju_list[i]))
                            elif web_type == "P0" or web_type =="P3":  # 如果是V5,则走V5的日志拼接
                                jiexi_expect_result_one = "Save factor(%s) raw value(%s" % (
                                str(jiankongyinzi_list[i]), str(shuju_list[i]))

                            jiexi_expect_result_list.append(jiexi_expect_result_one)

                        print("jiexi_expect_result_list:")
                        print(jiexi_expect_result_list)
                        is_in_file = am.assert_file_success_with_param(
                            expect_result_list=jiexi_expect_result_list)  # 带参数的断言
                    else:
                        self.assertTrue(False, "解析数据断言失败,监控因子与预期验证数据值个数需要相同，而实际不同，请修改保证两者个数相等且互相对应！！！")
                        is_in_file = False
                else:
                    is_in_file = am.assert_file_success()
                self.assertTrue(is_in_file, "解析数据断言失败")

            #是否验证实时数据
            if is_assert_real_db_success:
                if web_type == "P1":  # 如果是V6,则走v6的解析文件函数
                    xieyi_db_fixed_v6 = "rtd.db"
                    xieyi_db_table_name_fixed_v6 = "tb_rtd"
                    assert_result_flag_result = am.assert_real_db_success_with_param(xieyi_db=xieyi_db_fixed_v6,
                                                                              xieyi_db_table_name=xieyi_db_table_name_fixed_v6)# 验证远程数据库中的实时数据是否与解析值一致通用命令 V6版本协议
                    self.assertTrue(assert_result_flag_result, msg=u"数据库断言失败")
                elif web_type == "P0" or web_type == "P2" or web_type =="P3":  # 如果是V5,则走V5的重启协议命令
                    xieyi_db_fixed_v5 = "real.db"
                    xieyi_db_table_name_fixed_v5 = "rttable"
                    assert_result_flag_result = am.assert_real_db_success_with_param(xieyi_db=xieyi_db_fixed_v5,
                                                                              xieyi_db_table_name=xieyi_db_table_name_fixed_v5)# 验证远程数据库中的实时数据是否与解析值一致通用命令 V5版本协议
                    self.assertTrue(assert_result_flag_result,msg=u"数据库断言失败")

            #是否验证平台上报内容
            if is_assert_tcp_server_receive_success:
                if is_with_code_assert:  #如果断言结果带有因子代码，则用监控因子和数据值拼接后断言
                    jiankongyinzi_list = select_jian_kong_yin_zi_list
                    shuju_list = xieyi_jiexi_expect_result_list
                    tcp_expect_result_list = []
                    #将因子与数据拼接形成断言内容：
                    jiankongyinzi_list_len = len(jiankongyinzi_list)
                    shuju_list_len = len(shuju_list)
                    if jiankongyinzi_list_len ==shuju_list_len:
                        for i in range(0,jiankongyinzi_list_len):
                            tcp_expect_result_one = "%s-Rtd=%s" %(str(jiankongyinzi_list[i]),str(shuju_list[i]))
                            tcp_expect_result_list.append(tcp_expect_result_one)

                        print("tcp_expect_result_list:")
                        print(tcp_expect_result_list)
                        is_in_tcp = am.assert_tcp_server_receive_success_with_param(
                            expect_result_list=tcp_expect_result_list)  # 带参数的断言
                    else:
                        self.assertTrue(False, "平台上报数据断言失败,监控因子与预期验证数据值个数需要相同，而实际不同，请修改保证两者个数相等且互相对应！！！")
                        is_in_tcp = False

                else:  #否则，没有监控因子，只以数据断言
                    is_in_tcp = am.assert_tcp_server_receive_success()  #不带参数的断言

                self.assertTrue(is_in_tcp,"平台上报数据断言失败")

            if not is_recriminat_recive_and_send:  # 如果不是反控，则打印串口收发数据信息
                #如果三个断言中没有一个断言启动，则测试用例断言失败
                if is_assert_file_success or is_assert_real_db_success or is_assert_tcp_server_receive_success :
                    self.assertTrue(True)
                else:
                    self.assertTrue(False,u"测试用例为协议测试用例，没有断言，请至少添加一种断言（解析内容断言、实时数据库断言、平台上报内容断言）")


                for sender_hex_data_order_list_one in sender_hex_data_order_list:
                    am.outPutMyLog("="*50)
                    am.outPutMyLog("接收的数据：%s"% str(sender_hex_data_order_list_one[2]))
                    am.outPutMyLog("发送的数据：%s" % str(sender_hex_data_order_list_one[0]))
                    if sender_hex_data_order_list_one[9]:  #如果不断言结果，则不写预期结果
                        am.outPutMyLog("预期的解析结果：%s" %str(sender_hex_data_order_list_one[3]))
                    am.outPutMyLog("=" * 50)
            else:  #如果是反控，则打印反控数据信息
                pass




    @staticmethod  # 根据不同的参数生成测试用例
    def getTestFunc(case_id,depend_config_id):

        def func(self):
            self.defineshucaiyi(case_id,depend_config_id)

        return func


def __generateTestCases():
    from shucaiyidate.modelsorder import XieyiTestCase

    xieyitestcase_all = XieyiTestCase.objects.filter(is_run_case=True).order_by('id')

    for xieyitestcase in xieyitestcase_all:
        forcount = xieyitestcase.case_counts
        starttime = GetTimeStr().getTimeStr()
        if len(str(xieyitestcase.id)) == 1:
            xieyitestcaseid = '0000%s' % xieyitestcase.id
        elif len(str(xieyitestcase.id)) == 2:
            xieyitestcaseid = '000%s' % xieyitestcase.id
        elif len(str(xieyitestcase.id)) == 3:
            xieyitestcaseid = '00%s' % xieyitestcase.id
        elif len(str(xieyitestcase.id)) == 4:
            xieyitestcaseid = '0%s' % xieyitestcase.id
        elif len(str(xieyitestcase.id)) == 5:
            xieyitestcaseid = '%s' % xieyitestcase.id
        else:
            xieyitestcaseid = 'Id已经超过5位数，请重新定义'

        for i in range(1, forcount + 1):  # 循环，从1开始
            if len(str(i)) == 1:
                forcount_i = '0000%s' % i
            elif len(str(i)) == 2:
                forcount_i = '000%s' % i
            elif len(str(i)) == 3:
                forcount_i = '00%s' % i
            elif len(str(i)) == 4:
                forcount_i = '0%s' % i
            elif len(str(i)) == 5:
                forcount_i = '%s' % i
            else:
                forcount_i = 'Id已经超过5位数，请重新定义'
                forcount_i = i

            args = []
            args.append(xieyitestcase.id)
            args.append(xieyitestcase.depend_config_id)

            setattr(TestShuCaiYiClass,
                    'test_func_%s_%s_%s' % (
                    xieyitestcaseid, xieyitestcase.test_case_title, forcount_i),
                    TestShuCaiYiClass.getTestFunc(*args))  # 通过setattr自动为TestCase类添加成员方法，方法以“test_func_”开头


__generateTestCases()

if __name__ == '__main__':
    ts = TestShuCaiYiClass()
    ts.defineshucaiyi()












