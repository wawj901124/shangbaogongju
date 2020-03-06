from django.db import models
from datetime import datetime
from wanwenyc.settings import DJANGO_SERVER_YUMING
from django.contrib.auth import  get_user_model  #导入get_user_model
from testupdatadb.models import UpdateDbData

#第三个就是我们自己创建的包
User = get_user_model()  #get_user_model() 函数直接返回User类，找的是settings.AUTH_USER_MODEL变量的值



class ShangBaoShuJu(models.Model):
    test_project = models.CharField(max_length=100, default="", verbose_name=u"测试项目")
    test_module = models.CharField(max_length=100, default="", verbose_name=u"测试模块")
    test_page =  models.CharField(max_length=100, default="", verbose_name=u"测试页面")
    test_case_title = models.CharField(max_length=100, default="", verbose_name=u"测试内容的名称")
    forcount = models.CharField(max_length=100, default="", verbose_name=u"循环次数")
    time_delay = models.CharField(max_length=100, default="", verbose_name=u"次数间上报间隔（单位：秒）")
    is_check_crc = models.BooleanField(default=True, verbose_name=u"是否进行CRC校验")

    shujuduan_st = models.CharField(max_length=100, default="21",null=True, blank=True, verbose_name=u"数据段_系统编码ST",help_text = "请输入ST")
    shujuduan_cn = models.CharField(max_length=100, default="2011",null=True, blank=True, verbose_name=u"数据段_命令编码CN",help_text = "请输入CN")
    shujuduan_pw = models.CharField(max_length=100, default="123456",null=True, blank=True, verbose_name=u"数据段_访问密码PW",help_text = "请输入PW")
    mn_type = models.CharField(max_length=10,null=True, blank=True,
                                     choices=(("P0", u"输入MN"), ("P1", u"SQL语句获取MN") , ("P2", u"输入范围值自动生成MN")),
                                     default="P0",
                                     verbose_name=u"获取MN类型")
    shujuduan_mn = models.CharField(max_length=100, default="A220582_0001",null=True, blank=True, verbose_name=u"数据段_站点唯一标识MN",help_text = "请输入MN")
    mn_sql =  models.ForeignKey(UpdateDbData, null=True, blank=True, verbose_name=u"获取MN依赖的数据库SQL语句场景", on_delete=models.PROTECT,related_name='sbsj_mn_sql')
    mn_auto_make_base = models.CharField(max_length=100, default="",null=True, blank=True, verbose_name=u"自动生成MN_连续固定部分")
    mn_auto_make_down = models.CharField(max_length=100, default="",null=True, blank=True, verbose_name=u"自动生成MN_下限")
    mn_auto_make_up = models.CharField(max_length=100, default="",null=True, blank=True, verbose_name=u"自动生成MN_上限")
    mn_auto_make_interval = models.CharField(max_length=100, default="1", null=True, blank=True, verbose_name=u"自动生成MN_间隔")

    shujuduan_flag = models.CharField(max_length=100, default="9",null=True, blank=True, verbose_name=u"数据段_应答标志Flag",help_text = "请输入Flag")
    shujuduan_cp_datatime_type = models.CharField(max_length=100, default="shishi",null=True, blank=True,
                                                  verbose_name=u"数据段_指令参数CP的DataTime类型",
                                                  help_text = "如果模拟上报实时数据，请输入“shishi”；如果模拟小时数据，请输入“xiaoshi”")

    #在一个表中多次引用某同一个外键表，需要为各个字段指定唯一不同的releated_name
    actual_data_sql = models.ForeignKey(UpdateDbData, null=True, blank=True, verbose_name=u"获取目标数据库中因子值依赖的SQL场景", on_delete=models.PROTECT,related_name='sbsj_actual_data_sql')
    dele_zidian = models.CharField(max_length=1000, default="",null=True, blank=True,
                                   verbose_name=u"获取目标数据库中因子值对应表所有字段中需要删除的字段",
                                   help_text = "多个字段之间以英文半角逗号(,)隔开")
    actual_data_count = models.CharField(max_length=100, default="2", verbose_name=u"目标数据库中接收到报文需要进行报文的次数",
                                         help_text = "例如上报一条数据，则目标数据库中会出现上报的报文，此处应该填写1；"
                                                     "若上报一条数据后需要再上报一条数据，然后目标数据库中才会出现第一次上报的报文，"
                                                     "则此处应该填写2；依次类推...")
    actual_data_delay_time = models.CharField(max_length=100, default="60", verbose_name=u"上报数据到数据库录入数据预估耗时（单位：秒）")

    tcp_host = models.CharField(max_length=100, default="192.168.8.205", verbose_name=u"tcp主机IP")
    tcp_post = models.CharField(max_length=100, default="57001", verbose_name=u"tcp主机端口号")

    write_user = models.ForeignKey(User, null=True, blank=True, verbose_name=u"用户名", on_delete=models.PROTECT)
    add_time = models.DateTimeField(null=True, blank=True,auto_now_add=True,
                                    verbose_name=u"添加时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间,auto_now_add=True是指定在数据新增时, 自动写入时间
    update_time = models.DateTimeField(default=datetime.now, null=True, blank=True,
                                    verbose_name=u"更新时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间，auto_now=True是无论新增还是更新数据, 此字段都会更新为当前时间

    class Meta:
        verbose_name = u"模拟上报数据工具"
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.test_case_title


class ShuJuYinZi(models.Model):
    shangbaoshuju = models.ForeignKey(ShangBaoShuJu, null=True, blank=True, verbose_name=u"依赖的模拟上报数据工具", on_delete=models.PROTECT)
    yinzi_code = models.CharField(max_length=100, default="", verbose_name=u"因子编码")
    yinzi_rtd_up = models.CharField(max_length=100, default="", verbose_name=u"因子数值_上限")
    yinzi_rtd_down = models.CharField(max_length=100, default="", verbose_name=u"因子数值_下限")
    yinzi_rtd_xiaoshuwei = models.CharField(max_length=100, default="1", verbose_name=u"因子数值_小数位数")
    yinzi_rtd_count = models.CharField(max_length=100, default="1", verbose_name=u"因子数值个数")

    yinzi_flag = models.CharField(max_length=100, default="", verbose_name=u"因子标识")

    write_user = models.ForeignKey(User, null=True, blank=True, verbose_name=u"用户名", on_delete=models.PROTECT)
    add_time = models.DateTimeField(null=True, blank=True,auto_now_add=True,
                                    verbose_name=u"添加时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间,auto_now_add=True是指定在数据新增时, 自动写入时间
    update_time = models.DateTimeField(default=datetime.now, null=True, blank=True,
                                    verbose_name=u"更新时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间，auto_now=True是无论新增还是更新数据, 此字段都会更新为当前时间

    class Meta:
        verbose_name = u"数据段_指令参数CP的因子"
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.yinzi_code


class StoreSBShuJu(models.Model):
    test_project = models.CharField(max_length=100, default="", verbose_name=u"测试项目")
    test_module = models.CharField(max_length=100, default="", verbose_name=u"测试模块")
    test_page =  models.CharField(max_length=100, default="", verbose_name=u"测试页面")
    test_case_title = models.CharField(max_length=100, default="", verbose_name=u"测试内容的名称")
    test_start_time = models.CharField(max_length=100, default="", verbose_name=u"开始运行时间")
    forcount = models.CharField(max_length=100, default="", verbose_name=u"循环次数")
    time_delay = models.CharField(max_length=100, default="", verbose_name=u"次数间上报间隔（单位：秒）")
    is_check_crc = models.BooleanField(default=True, verbose_name=u"是否进行CRC校验")

    shujuduan_mn = models.CharField(max_length=100, default="", null=True, blank=True, verbose_name=u"数据段_站点唯一标识MN")
    sb_yinzi = models.CharField(max_length=5000,default="", verbose_name=u"上报因子字符串")
    sb_shuju = models.CharField(max_length=5000,default="", verbose_name=u"上报数据字符串")
    sb_ret = models.CharField(max_length=5000,default="", verbose_name=u"tcp响应数据")

    write_user = models.ForeignKey(User, null=True, blank=True, verbose_name=u"用户名", on_delete=models.PROTECT)
    add_time = models.DateTimeField(null=True, blank=True,auto_now_add=True,
                                    verbose_name=u"添加时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间,auto_now_add=True是指定在数据新增时, 自动写入时间
    update_time = models.DateTimeField(default=datetime.now, null=True, blank=True,
                                    verbose_name=u"更新时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间，auto_now=True是无论新增还是更新数据, 此字段都会更新为当前时间

    class Meta:
        verbose_name = u"模拟上报数据记录"
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.test_case_title

