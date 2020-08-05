from django.db import models
from datetime import datetime
from wanwenyc.settings import DJANGO_SERVER_YUMING
from django.contrib.auth import  get_user_model  #导入get_user_model
from testupdatadb.models import UpdateDbData
from .modelsnewdev import NodeConfig

#第三个就是我们自己创建的包
User = get_user_model()  #get_user_model() 函数直接返回User类，找的是settings.AUTH_USER_MODEL变量的值

#协议对照表
class VSixXieYiDuiZhao(models.Model):
    v6_xiyihao = models.CharField(max_length=100, default="", verbose_name=u"协议号")
    v6_jianceleixing = models.CharField(max_length=100, default="",null=True, blank=True, verbose_name=u"监测类型")
    v6_yiqifenlei = models.CharField(max_length=100, default="",null=True, blank=True, verbose_name=u"仪器分类")
    v6_zhenglihouxieyimingcheng = models.CharField(max_length=100, default="",null=True, blank=True, verbose_name=u"整理后协议名称")
    v6_yuanxieyimingcheng = models.CharField(max_length=100, default="",null=True, blank=True, verbose_name=u"原协议名称")
    v6_syybxydcjyqxh = models.CharField(max_length=100, default="",null=True, blank=True, verbose_name=u"适用于本协议的厂家仪器型号")
    v6_status = models.CharField(max_length=100, default="", null=True, blank=True,verbose_name=u"状态")
    v6_yuanshucaiyiduiyingxieyihao = models.CharField(max_length=100,null=True, blank=True, default="", verbose_name=u"原数采仪对应协议号")
    # v6_shujuzhiling = models.CharField(max_length=2000, default="",null=True, blank=True, verbose_name=u"数据指令")
    v6_shujuzhiling = models.TextField(max_length=2000, default="",null=True, blank=True, verbose_name=u"数据指令")
    # v6_zhuangtaicanshuzhiling = models.CharField(max_length=2000, default="",null=True, blank=True, verbose_name=u"状态参数指令")
    v6_zhuangtaicanshuzhiling = models.TextField(max_length=2000, default="",null=True, blank=True, verbose_name=u"状态参数指令")
    v6_erjinzhimingcheng = models.CharField(max_length=100, default="", null=True, blank=True,verbose_name=u"二进制名称")
    # v6_teshupeizhiwenjian = models.CharField(max_length=2000, default="", null=True, blank=True,verbose_name=u"特殊配置文件")
    v6_teshupeizhiwenjian = models.TextField(max_length=2000, default="", null=True, blank=True,verbose_name=u"特殊配置文件")
    v6_shifoucaijizhuangtai = models.CharField(max_length=100, default="",null=True, blank=True, verbose_name=u"是否采集状态")
    v6_yijifenlei = models.CharField(max_length=100, default="",null=True, blank=True, verbose_name=u"一级分类")
    v6_shiyongquyu = models.CharField(max_length=100, default="",null=True, blank=True, verbose_name=u"使用区域")
    v6_jiekouleixing = models.CharField(max_length=100, default="",null=True, blank=True, verbose_name=u"接口类型")
    v6_chengxuleixing = models.CharField(max_length=100, default="",null=True, blank=True, verbose_name=u"程序类型")
    v6_kaifaren = models.CharField(max_length=100, default="",null=True, blank=True, verbose_name=u"开发人")
    v6_ceshiren = models.CharField(max_length=100, default="",null=True, blank=True, verbose_name=u"测试人")
    v6_xiugaineirong = models.CharField(max_length=100, default="",null=True, blank=True, verbose_name=u"修改内容")
    v6_guidangshijian = models.CharField(max_length=100, default="",null=True, blank=True, verbose_name=u"归档时间")
    v6_gengxinren = models.CharField(max_length=100, default="",null=True, blank=True, verbose_name=u"更新人")



    write_user = models.ForeignKey(User, null=True, blank=True, verbose_name=u"用户名", on_delete=models.PROTECT)
    add_time = models.DateTimeField(null=True, blank=True,auto_now_add=True,
                                    verbose_name=u"添加时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间,auto_now_add=True是指定在数据新增时, 自动写入时间
    update_time = models.DateTimeField(default=datetime.now, null=True, blank=True,
                                    verbose_name=u"更新时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间，auto_now=True是无论新增还是更新数据, 此字段都会更新为当前时间

    class Meta:
        verbose_name = u"采集协议V6对照表"
        verbose_name_plural=verbose_name

    def __str__(self):
        return str(self.v6_xiyihao)

    # def go_to(self):   #定义点击后跳转到某一个地方（可以加html代码）
    #     from django.utils.safestring import mark_safe   #调用mark_safe这个函数，django可以显示成一个文本，而不是html代码
    #     return mark_safe("<a href='{}/shucaiyidate/xieyiconfigdateorder/{}/'>复制新加</a>".format(DJANGO_SERVER_YUMING,self.id))
    #
    # go_to.short_description = u"复制新加"   #为go_to函数名个名字


