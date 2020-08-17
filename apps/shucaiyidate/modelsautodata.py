from django.db import models
from datetime import datetime
from wanwenyc.settings import DJANGO_SERVER_YUMING
from django.contrib.auth import  get_user_model  #导入get_user_model

#第三个就是我们自己创建的包
User = get_user_model()  #get_user_model() 函数直接返回User类，找的是settings.AUTH_USER_MODEL变量的值

#自动生成
class XieYiAutoData(models.Model):
    test_project = models.CharField(max_length=100, default="", verbose_name=u"测试项目")
    test_module = models.CharField(max_length=100, default="", verbose_name=u"测试模块")
    test_page =  models.CharField(max_length=100, default="", verbose_name=u"测试页面")
    test_case_title = models.CharField(max_length=100, default="", verbose_name=u"测试内容的名称")
    forcount = models.CharField(max_length=100, default="", verbose_name=u"循环次数")
    time_delay = models.CharField(max_length=100, default="", verbose_name=u"次数间上报间隔（单位：秒）")
    is_check_crc = models.BooleanField(default=True, verbose_name=u"是否进行CRC校验")

    shebeiid = models.CharField(max_length=100, default="01",null=True, blank=True, verbose_name=u"设备ID",help_text = "请输入设备ID")
    gongnengma = models.CharField(max_length=100, default="03",null=True, blank=True, verbose_name=u"功能码",help_text = "请输入功能码")
    shujuchangdu = models.CharField(max_length=100, default="04",null=True, blank=True, verbose_name=u"数据长度",help_text = "请输入数据长度")


    write_user = models.ForeignKey(User, null=True, blank=True, verbose_name=u"用户名", on_delete=models.PROTECT)
    add_time = models.DateTimeField(null=True, blank=True,auto_now_add=True,
                                    verbose_name=u"添加时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间,auto_now_add=True是指定在数据新增时, 自动写入时间
    update_time = models.DateTimeField(default=datetime.now, null=True, blank=True,
                                    verbose_name=u"更新时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间，auto_now=True是无论新增还是更新数据, 此字段都会更新为当前时间

    class Meta:
        verbose_name = u"模拟下发16进制数据工具"
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.test_case_title

    # def go_to(self):   #定义点击后跳转到某一个地方（可以加html代码）
    #     from django.utils.safestring import mark_safe   #调用mark_safe这个函数，django可以显示成一个文本，而不是html代码
    #     return mark_safe("<a href='{}/shucaiyidate/xieyiconfigdateorder/{}/'>复制新加</a>".format(DJANGO_SERVER_YUMING,self.id))
    #
    # go_to.short_description = u"复制新加"   #为go_to函数名个名字


class XieYiOneData(models.Model):
    xieyiautodata = models.ForeignKey(XieYiAutoData, null=True, blank=True, verbose_name=u"模拟下发16进制数据工具", on_delete=models.PROTECT)
    yinzi_code = models.CharField(max_length=100, default="",null=True, blank=True, verbose_name=u"因子编码")
    yinzi_rtd_down = models.CharField(max_length=100, default="", verbose_name=u"因子数值_下限")
    yinzi_rtd_up = models.CharField(max_length=100, default="", verbose_name=u"因子数值_上限")
    yinzi_rtd_xiaoshuwei = models.CharField(max_length=100, default="6", verbose_name=u"因子数值_小数位数",
                                            help_text=u"浮点型数据固定设置为：6；整数设置为：0；")
    yinzi_rtd_count = models.CharField(max_length=100, default="1", verbose_name=u"因子数值个数")
    yinzi_zijiexu = models.CharField(max_length=100, default="1234", verbose_name=u"字节序")
    # yinzi_flag = models.CharField(max_length=100, default="", verbose_name=u"因子标识")

    write_user = models.ForeignKey(User, null=True, blank=True, verbose_name=u"用户名", on_delete=models.PROTECT)
    add_time = models.DateTimeField(null=True, blank=True,auto_now_add=True,
                                    verbose_name=u"添加时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间,auto_now_add=True是指定在数据新增时, 自动写入时间
    update_time = models.DateTimeField(default=datetime.now, null=True, blank=True,
                                    verbose_name=u"更新时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间，auto_now=True是无论新增还是更新数据, 此字段都会更新为当前时间

    class Meta:
        verbose_name = u"协议单个数据"
        verbose_name_plural=verbose_name

    def __str__(self):
        return str(self.yinzi_code)

