from django.db import models
from datetime import datetime
from wanwenyc.settings import DJANGO_SERVER_YUMING
from django.contrib.auth import  get_user_model  #导入get_user_model
from testupdatadb.models import UpdateDbData

#第三个就是我们自己创建的包
User = get_user_model()  #get_user_model() 函数直接返回User类，找的是settings.AUTH_USER_MODEL变量的值

#类别
class XieyiConfigDateOrder(models.Model):
    test_project = models.CharField(max_length=100, default="", verbose_name=u"配置名称")
    # test_module = models.CharField(max_length=100, default="",null=True, blank=True, verbose_name=u"测试模块")
    # test_page = models.CharField(max_length=100, default="", verbose_name=u"测试页面")
    # case_priority = models.CharField(max_length=10,null=True, blank=True,
    #                                  choices=(("P0", u"冒烟用例"), ("P1", u"系统的重要功能用例") , ("P2", u"系统的一般功能用例"), ("P3", "极低级别的用例")),
    #                                  default="P1",
    #                                  verbose_name=u"用例优先级")
    # test_case_title = models.CharField(max_length=200, default="", verbose_name=u"测试内容的名称")
    # is_run_case = models.BooleanField(default=True,verbose_name=u"是否运行")
    web_type = models.CharField(max_length=10,null=True, blank=True,
                                     choices=(("P0", u"V5"), ("P1", u"V6")),
                                     default="P0",
                                     verbose_name=u"系统类型")
    is_web_modify_xieyi = models.BooleanField(default=True,verbose_name=u"是否通过web端修改协议")

    web_xieyi_name =  models.CharField(max_length=100, default="",  null=True, blank=True,verbose_name=u"web端选择的协议名称")
    web_xieyi_yinzi = models.CharField(max_length=100, default="",  null=True, blank=True,verbose_name=u"web端添加的监控因子",
                                       help_text=u"web端添加的监控因子，多个因子之间以半角逗号隔开")

    telnet_host_ip = models.CharField(max_length=100, default="192.168.101.133", verbose_name=u"数采仪IP地址")
    telnet_username = models.CharField(max_length=100, default="root", verbose_name=u"登录数采仪的用户名")
    telnet_password = models.CharField(max_length=100, default="wwyc8888", verbose_name=u"登录数采仪的密码")
    is_ftp_upload =  models.BooleanField(default=False,verbose_name=u"是否上传配置文件")
    # is_close_xieyi =  models.BooleanField(default=True,verbose_name=u"是否关闭开机自启动时启动的协议")
    # is_restart_xieyi = models.BooleanField(default=True,verbose_name=u"是否重新启动协议")
    # xieyi_bin_dir =  models.CharField(max_length=100, default="/usr/app_install/collect/bin", verbose_name=u"数采仪存放协议二进制文件的bin目录")
    xieyi_name =  models.CharField(max_length=100, default="11020", verbose_name=u"协议二进制文件的名字")
    xieyi_test_port  =  models.CharField(max_length=100, default="4", verbose_name=u"数采仪协议串口号",help_text=u"请填写数字，"
                                                                   u"例如串口为COM4，则填写4")
    xieyi_device_id = models.CharField(max_length=100, default="1",  null=True, blank=True,verbose_name=u"设备ID号",
                                 help_text=u"下发或接收指令的设备ID号或站地址")

    is_com_recive_and_send =  models.BooleanField(default=True,verbose_name=u"是否进行数据接收和发送")

    com_port = models.CharField(max_length=100, default="COM3", verbose_name=u"电脑与数采仪连接的USB口",
                                help_text=u"电脑与数采仪连接的USB口，例如USB口为COM4，则填写COM4")

    com_baudrate = models.CharField(max_length=100, default="9600", verbose_name=u"协议波特率",
                                    help_text=u"协议波特率，一般有4800/9600/19200/38400bps，"
                                              u"如协议使用波特率为9600bps，则此处填写9600")

    com_bytesize = models.CharField(max_length=100, default="8", verbose_name=u"协议数据位",
                                    help_text=u"协议数据位，一般有6、7、8，如协议使用数据位为8，则此处填写8")
    com_parity =  models.CharField(max_length=100, default="N", verbose_name=u"协议校验位",
                                   help_text=u"协议校验位，一般有N(无校验)、O（奇校验）、E（偶校验）0、1，"
                                             u"若协议使用无校验，则此处填写大写的N；"
                                             u"若协议使用奇校验，则此处填写大写的O；"
                                             u"若协议使用偶校验，则此处填写大写的E；")

    com_stopbits =  models.CharField(max_length=100, default="1", verbose_name=u"协议停止位",
                                    help_text=u"协议停止位，一般有1、1.5、2，如协议使用停止位为1，则此处填写1")

    # com_send_date =  models.CharField(max_length=1000, default="01 03 02 00 EA 39 CB", verbose_name=u"回复指令中的全部内容",
    #                                 help_text=u"回复指令中的全部内容，如回复的全部数据为：01 03 02 00 EA 39 CB，则此处填写01 03 02 00 EA 39 CB；"
    #                                           u"如需要发送多条指令，则每条指令之间以半角逗号隔开，")
    # com_expect_date = models.CharField(max_length=100, default="01 03 12 2D 00 01 11 7B", verbose_name=u"预期接收到的指令的内容",
    #                                 help_text=u"预期接收到的指令的内容，如预期接收到的指令的内容为：01 03 12 2D 00 01 11 7B，则此处填写01 03 12 2D 00 01 11 7B")

    # is_ftp_down_xieyi_file = models.BooleanField(default=True,verbose_name=u"是否ftp下载获取解析文件")
    is_with_code_assert = models.BooleanField(default=True,verbose_name=u"断言结果是否带因子代码")
    is_assert_file_success = models.BooleanField(default=True,verbose_name=u"是否断言协议预期解析结果在协议解析文件中")

    # xieyi_jiexi_expect_result = models.CharField(max_length=1000, default="0.234", verbose_name=u"协议解析预期结果",
    #                                 help_text=u"协议解析预期结果，如预期结果为0.234，则此处填写0.234，如有多个预期结果，每个结果之间以半角逗号隔开，如:0.234,9.55")

    # is_ftp_get_remote_db_file =  models.BooleanField(default=False,verbose_name=u"是否ftp下载远程数据库文件")
    is_assert_real_db_success = models.BooleanField(default=False,verbose_name=u"是否断言协议预期解析结果在实时数据库的表中")

    # xieyi_db =  models.CharField(max_length=100, default="real.db", null=True, blank=True, verbose_name=u"协议实时数据存放的数据库名字")
    # xieyi_db_remote_path =  models.CharField(max_length=100, default="/tmp/real.db", null=True, blank=True, verbose_name=u"协议实时数据存放的数据库在数采仪中的路径",
    #                                          help_text=u"如数据库路径为'/tmp/real.db',则填写'/tmp/real.db'")
    # xieyi_db_table_name = models.CharField(max_length=100, default="rttable", null=True, blank=True, verbose_name=u"协议实时数据存放的数据的数据表")

    # is_tcp_server_receive = models.BooleanField(default=False,verbose_name=u"是否接收平台报文")
    is_assert_tcp_server_receive_success = models.BooleanField(default=False,verbose_name=u"是否断言协议预期解析结果在接收的报文中")

    tcp_server_ip = models.CharField(max_length=100, default="192.168.101.123", null=True, blank=True,verbose_name=u"数据上报平台的IP地址")
    tcp_server_port = models.CharField(max_length=100, default="63503", null=True, blank=True,verbose_name=u"数据上报平台的端口号")
    tcp_receive_delay_min = models.CharField(max_length=100, default="10", null=True, blank=True,verbose_name=u"tcp服务接收的数据为当前时间后延的时间（以分钟为单位）")


    # case_counts = models.IntegerField(default="1",verbose_name="循环次数",help_text=u"循环次数，请填写数字，"
    #                                                                u"例如：1、2、3")
    write_user = models.ForeignKey(User, null=True, blank=True, verbose_name=u"用户名", on_delete=models.PROTECT)
    add_time = models.DateTimeField(null=True, blank=True,auto_now_add=True,
                                    verbose_name=u"添加时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间,auto_now_add=True是指定在数据新增时, 自动写入时间
    update_time = models.DateTimeField(default=datetime.now, null=True, blank=True,
                                    verbose_name=u"更新时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间，auto_now=True是无论新增还是更新数据, 此字段都会更新为当前时间

    class Meta:
        verbose_name = u"协议测试之依赖配置"
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.test_project

    def go_to(self):   #定义点击后跳转到某一个地方（可以加html代码）
        from django.utils.safestring import mark_safe   #调用mark_safe这个函数，django可以显示成一个文本，而不是html代码
        return mark_safe("<a href='{}/shucaiyidate/xieyiconfigdate/{}/'>复制新加</a>".format(DJANGO_SERVER_YUMING,self.id))

    go_to.short_description = u"复制新加"   #为go_to函数名个名字



class XieyiTestCase(models.Model):
    test_project = models.CharField(max_length=100, default="", verbose_name=u"测试项目")
    test_module = models.CharField(max_length=100, default="",null=True, blank=True, verbose_name=u"测试模块")
    test_page = models.CharField(max_length=100, default="", verbose_name=u"测试页面")
    case_priority = models.CharField(max_length=10,null=True, blank=True,
                                     choices=(("P0", u"冒烟用例"), ("P1", u"系统的重要功能用例") , ("P2", u"系统的一般功能用例"), ("P3", "极低级别的用例")),
                                     default="P1",
                                     verbose_name=u"用例优先级")
    test_case_title = models.CharField(max_length=200, default="", verbose_name=u"测试内容的名称")
    is_run_case = models.BooleanField(default=True,verbose_name=u"是否运行")

    depend_config = models.ForeignKey(XieyiConfigDateOrder, null=True, blank=True, verbose_name=u"依赖的测试配置", on_delete=models.PROTECT)


    case_counts = models.IntegerField(default="1",verbose_name="循环次数",help_text=u"循环次数，请填写数字，"
                                                                   u"例如：1、2、3")
    write_user = models.ForeignKey(User, null=True, blank=True, verbose_name=u"用户名", on_delete=models.PROTECT)
    add_time = models.DateTimeField(null=True, blank=True,auto_now_add=True,
                                    verbose_name=u"添加时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间,auto_now_add=True是指定在数据新增时, 自动写入时间
    update_time = models.DateTimeField(default=datetime.now, null=True, blank=True,
                                    verbose_name=u"更新时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间，auto_now=True是无论新增还是更新数据, 此字段都会更新为当前时间

    class Meta:
        verbose_name = u"协议测试之测试用例"
        verbose_name_plural=verbose_name

    def __str__(self):
        return "{}-【{}】-{}".format(self.id,self.test_project,self.test_case_title)

    def go_to(self):   #定义点击后跳转到某一个地方（可以加html代码）
        from django.utils.safestring import mark_safe   #调用mark_safe这个函数，django可以显示成一个文本，而不是html代码
        return mark_safe("<a href='{}/shucaiyidate/xieyitestcase/{}/'>复制新加</a>".format(DJANGO_SERVER_YUMING,self.id))

    go_to.short_description = u"复制新加"   #为go_to函数名个名字

class FtpUploadFileOrder(models.Model):
    xieyiconfigdateorder = models.ForeignKey(XieyiConfigDateOrder,default="", null=True, blank=True,
                                        verbose_name=u"依赖的协议测试",on_delete=models.PROTECT)
    up_remote_file = models.CharField(max_length=1000, default="",null=True, blank=True, verbose_name=u"远程路径文件")
    up_local_file = models.CharField(max_length=1000, default="", null=True, blank=True, verbose_name=u"本地路径文件")
    write_user = models.ForeignKey(User, null=True, blank=True, verbose_name=u"用户名", on_delete=models.PROTECT)
    add_time = models.DateTimeField(null=True, blank=True,auto_now_add=True,
                                    verbose_name=u"添加时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间,auto_now_add=True是指定在数据新增时, 自动写入时间
    update_time = models.DateTimeField(default=datetime.now, null=True, blank=True,
                                    verbose_name=u"更新时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间，auto_now=True是无论新增还是更新数据, 此字段都会更新为当前时间

    class Meta:
        verbose_name = u"FTP上传文件"
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.up_remote_file


class CloseXieYiCommandOrder(models.Model):
    xieyiconfigdateorder = models.ForeignKey(XieyiConfigDateOrder,default="", null=True, blank=True,
                                        verbose_name=u"依赖的协议测试",on_delete=models.PROTECT)
    close_command = models.CharField(max_length=1000, default="",null=True, blank=True, verbose_name=u"关闭协议命令")
    write_user = models.ForeignKey(User, null=True, blank=True, verbose_name=u"用户名", on_delete=models.PROTECT)
    add_time = models.DateTimeField(null=True, blank=True,auto_now_add=True,
                                    verbose_name=u"添加时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间,auto_now_add=True是指定在数据新增时, 自动写入时间
    update_time = models.DateTimeField(default=datetime.now, null=True, blank=True,
                                    verbose_name=u"更新时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间，auto_now=True是无论新增还是更新数据, 此字段都会更新为当前时间

    class Meta:
        verbose_name = u"关闭协议命令"
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.close_command


class RestartXieYiCommandOrder(models.Model):
    xieyiconfigdateorder = models.ForeignKey(XieyiConfigDateOrder,default="", null=True, blank=True,
                                        verbose_name=u"依赖的协议测试",on_delete=models.PROTECT)
    restart_command = models.CharField(max_length=1000, default="",null=True, blank=True, verbose_name=u"关闭协议命令")
    write_user = models.ForeignKey(User, null=True, blank=True, verbose_name=u"用户名", on_delete=models.PROTECT)
    add_time = models.DateTimeField(null=True, blank=True,auto_now_add=True,
                                    verbose_name=u"添加时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间,auto_now_add=True是指定在数据新增时, 自动写入时间
    update_time = models.DateTimeField(default=datetime.now, null=True, blank=True,
                                    verbose_name=u"更新时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间，auto_now=True是无论新增还是更新数据, 此字段都会更新为当前时间

    class Meta:
        verbose_name = u"重启协议命令"
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.restart_command


class SenderHexDataOrder(models.Model):
    xieyitestcase = models.ForeignKey(XieyiTestCase,default="", null=True, blank=True,
                                        verbose_name=u"依赖的协议测试用例",on_delete=models.PROTECT)
    # sender_hex_data = models.CharField(max_length=1000, default="",null=True, blank=True, verbose_name=u"发送数据命令")
    is_send_hex = models.BooleanField(default=True,verbose_name=u"发送的数据是否为16进制",help_text="选中则表示发送的数据为16进制，否则表示发送的数据为ASCII字符")
    send_wait_time = models.CharField(max_length=1000, default="0", verbose_name=u"发送数据前等待时间（单位秒）")
    com_send_date =  models.CharField(max_length=1000, default="01 03 02 00 EA 39 CB", verbose_name=u"回复指令中的全部内容",
                                    help_text=u"回复指令中的全部内容，如回复的全部数据为：01 03 02 00 EA 39 CB，则此处填写01 03 02 00 EA 39 CB；")
    is_need_expect = models.BooleanField(default=False,verbose_name=u"发送数据前是否需要先接收到指令")
    is_need_after_expect = models.BooleanField(default=False, verbose_name=u"发送数据后是否需要接收到指令")
    is_just_one =  models.BooleanField(default=True, verbose_name=u"是否只发送一次数据")
    is_receive_hex = models.BooleanField(default=True, verbose_name=u"接收的数据是否为16进制",
                                      help_text="选中则表示接收的数据为16进制，否则表示接收的数据为ASCII字符")
    com_expect_date = models.CharField(max_length=1000, default="01 03 12 2D 00 01 11 7B",null=True, blank=True, verbose_name=u"预期接收到的指令的内容",
                                    help_text=u"预期接收到的指令的内容，如预期接收到的指令的内容为：01 03 12 2D 00 01 11 7B，则此处填写01 03 12 2D 00 01 11 7B")
    is_assert_expect = models.BooleanField(default=True,verbose_name=u"是否断言预期结果")
    xieyi_jiexi_expect_result = models.CharField(max_length=1000, default="0.234",null=True, blank=True, verbose_name=u"协议解析预期结果",
                                    help_text=u"协议解析预期结果，如预期结果为0.234，则此处填写0.234；如需多个预期值，则多个预期值之间以半角逗号隔开，例如：0.234,0.506")

    write_user = models.ForeignKey(User, null=True, blank=True, verbose_name=u"用户名", on_delete=models.PROTECT)
    add_time = models.DateTimeField(null=True, blank=True,auto_now_add=True,
                                    verbose_name=u"添加时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间,auto_now_add=True是指定在数据新增时, 自动写入时间
    update_time = models.DateTimeField(default=datetime.now, null=True, blank=True,
                                    verbose_name=u"更新时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间，auto_now=True是无论新增还是更新数据, 此字段都会更新为当前时间

    class Meta:
        verbose_name = u"协议测试之测试数据"
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.xieyi_jiexi_expect_result


