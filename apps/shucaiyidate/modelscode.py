from django.db import models
from datetime import datetime
from wanwenyc.settings import DJANGO_SERVER_YUMING
from django.contrib.auth import  get_user_model  #导入get_user_model

#第三个就是我们自己创建的包
User = get_user_model()  #get_user_model() 函数直接返回User类，找的是settings.AUTH_USER_MODEL变量的值

#类别
class YinZiCode(models.Model):
    national_standard = models.CharField(max_length=100, default="标准HJ212-2017", verbose_name=u"国标标准")
    table_name =  models.CharField(max_length=100, default="",  null=True, blank=True,verbose_name=u"表名")
    yinzi_code = models.CharField(max_length=100, default="", null=True, blank=True, verbose_name=u"编码")
    yinzi_name = models.CharField(max_length=100, default="", null=True, blank=True, verbose_name=u"中文名称")
    yinzi_original_code = models.CharField(max_length=100, default="", null=True, blank=True, verbose_name=u"原编码")
    yinzi_company_concentration = models.CharField(max_length=100, default="", null=True, blank=True, verbose_name=u"缺省计量单位（浓度）")
    yinzi_company_emissions = models.CharField(max_length=100, default="", null=True, blank=True, verbose_name=u"缺省计量单位（排放量）")
    yinzi_data_type_concentration = models.CharField(max_length=100, default="", null=True, blank=True, verbose_name=u"缺省数据类型（浓度")


    write_user = models.ForeignKey(User, null=True, blank=True, verbose_name=u"用户名", on_delete=models.PROTECT)
    add_time = models.DateTimeField(null=True, blank=True,auto_now_add=True,
                                    verbose_name=u"添加时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间,auto_now_add=True是指定在数据新增时, 自动写入时间
    update_time = models.DateTimeField(default=datetime.now, null=True, blank=True,
                                    verbose_name=u"更新时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间，auto_now=True是无论新增还是更新数据, 此字段都会更新为当前时间

    class Meta:
        verbose_name = u"因子及编码查询"
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.yinzi_code

    # def go_to(self):   #定义点击后跳转到某一个地方（可以加html代码）
    #     from django.utils.safestring import mark_safe   #调用mark_safe这个函数，django可以显示成一个文本，而不是html代码
    #     return mark_safe("<a href='{}/shucaiyidate/xieyiconfigdate/{}/'>复制新加</a>".format(DJANGO_SERVER_YUMING,self.id))
    #
    # go_to.short_description = u"复制新加"   #为go_to函数名个名字
