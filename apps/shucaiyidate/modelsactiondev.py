from django.db import models
from datetime import datetime
from wanwenyc.settings import DJANGO_SERVER_YUMING
from django.contrib.auth import  get_user_model  #导入get_user_model
from testupdatadb.models import UpdateDbData

#第三个就是我们自己创建的包
User = get_user_model()  #get_user_model() 函数直接返回User类，找的是settings.AUTH_USER_MODEL变量的值

class ActionDevTag(models.Model):

    original_file_name = models.CharField(max_length=100, default="", null=True, blank=True, verbose_name=u"原有dev文件路径")
    config_project = models.CharField(max_length=100, default="", null=True, blank=True, verbose_name=u"入库的项目名称")
    root_name = models.CharField(max_length=100, default="", null=True, blank=True, verbose_name=u"入库的根节点名称")
    export_root_num = models.CharField(max_length=100, default="", null=True, blank=True, verbose_name=u"导出的数据库根节点ID号")
    new_file_name = models.CharField(max_length=100, default="", null=True, blank=True, verbose_name=u"导出的新的dev文件路径")
    is_read_original_dev = models.BooleanField(default=False, verbose_name=u"是否从原dev文件导入数据到数据库")
    is_create_new_dev = models.BooleanField(default=False, verbose_name=u"是否导出数据库中的节点数据到新的dev文件中")

    write_user = models.ForeignKey(User, null=True, blank=True, verbose_name=u"用户名", on_delete=models.PROTECT)
    add_time = models.DateTimeField(null=True, blank=True,auto_now_add=True,
                                    verbose_name=u"添加时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间,auto_now_add=True是指定在数据新增时, 自动写入时间
    update_time = models.DateTimeField(default=datetime.now, null=True, blank=True,
                                    verbose_name=u"更新时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间，auto_now=True是无论新增还是更新数据, 此字段都会更新为当前时间

    class Meta:
        verbose_name = u"节点数据入库和出库"
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.config_project