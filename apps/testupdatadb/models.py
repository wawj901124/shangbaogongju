from datetime import datetime   #系统的包放在最上面

from django.db import models   #第二个级别的就是第三方包
from django.contrib.auth import  get_user_model  #导入get_user_model

from wanwenyc.settings import DJANGO_SERVER_YUMING
#第三个就是我们自己创建的包
User = get_user_model()  #get_user_model() 函数直接返回User类，找的是settings.AUTH_USER_MODEL变量的值


#Create your models here.
class UpdateDbData(models.Model):#继承django的Model模块
    """
    批量修改或替换数据库中表中某字段的内容模型
    """
    test_project = models.CharField(max_length=100, default="", verbose_name=u"测试项目")
    test_module = models.CharField(max_length=100, default="",null=True, blank=True, verbose_name=u"测试模块")
    test_page = models.CharField(max_length=100, default="", verbose_name=u"测试页面")
    case_priority = models.CharField(max_length=10,null=True, blank=True,
                                     choices=(("P0", u"冒烟用例"), ("P1", u"系统的重要功能用例") , ("P2", u"系统的一般功能用例"), ("P3", "极低级别的用例")),
                                     default="P1",
                                     verbose_name=u"用例优先级")
    test_case_title = models.CharField(max_length=200, default="", verbose_name=u"测试内容的名称")
    is_run_case = models.BooleanField(default=True,verbose_name=u"是否运行")
    depend_case = models.ForeignKey('self', default="", null=True, blank=True,
                                   verbose_name=u"依赖的前置用例",on_delete=models.PROTECT)

    db_host = models.CharField(max_length=100, default="192.168.100.198",null=True, blank=True, verbose_name=u"数据库IP")
    db_port = models.CharField(max_length=100, default="3306",null=True, blank=True, verbose_name=u"数据库端口")
    db_user = models.CharField(max_length=100, default="lepus_user",null=True, blank=True, verbose_name=u"数据库用户名")
    db_password = models.CharField(max_length=100, default="123456",null=True, blank=True, verbose_name=u"数据库密码")
    db_database = models.CharField(max_length=100, default="testconn",null=True, blank=True, verbose_name=u"数据库库名")
    db_charset = models.CharField(max_length=100, default="utf8",null=True, blank=True, verbose_name=u"数据库编码格式")

    db_biao= models.CharField(max_length=1000, default="testdatas_clickandback",null=True, blank=True, verbose_name=u"数据库中的表",
                              help_text="多个表之间以英文半角逗号(,)隔开")
    db_ziduan= models.CharField(max_length=1000, default="current_page_click_ele_find_value",null=True, blank=True, verbose_name=u"数据库中的表的字段名",
                                help_text="多个字段之间以英文半角逗号(,)隔开，全部字段请输入*")
    db_xiugaiqiandezhi= models.CharField(max_length=1000, default="/html/body/",null=True, blank=True, verbose_name=u"数据库中的表的字段替换前的值")
    db_xiugaihoudezhi= models.CharField(max_length=1000, default="修改后的油烟餐饮",null=True, blank=True, verbose_name=u"数据库中的表的字段替换后的值")
    db_tiaojianziduan= models.CharField(max_length=100, default="id",null=True, blank=True, verbose_name=u"where条件字段名",
                                        help_text="多个条件字段之间以英文半角逗号(,)隔开")
    db_tiaojianzhi = models.CharField(max_length=1000, default="10",null=True, blank=True, verbose_name=u"where条件字段值",
                                      help_text="多个条件字段值之间以英文半角逗号(,)隔开，如果是遍历所有，请填写'all'")

    db_paixuziduan =models.CharField(max_length=1000, default="",null=True, blank=True, verbose_name=u"排序字段名")
    is_daoxu = models.BooleanField(default=True,verbose_name=u"是否倒序")
    db_qianjiwei = models.CharField(max_length=1000, default="",null=True, blank=True, verbose_name=u"获取前几行数据")

    case_counts = models.IntegerField(default="1",verbose_name="用例循环次数",help_text=u"用例循环次数，请填写数字，"
                                                                   u"例如：1、2、3")
    write_user = models.ForeignKey(User,null=True, blank=True,verbose_name=u"添加人", on_delete=models.PROTECT)

    # datetime.now记录实例化时间，datetime.now()记录模型创建时间,auto_now_add=True是指定在数据新增时, 自动写入时间
    add_time = models.DateTimeField(null=True, blank=True, auto_now_add=True,verbose_name=u"添加时间")
    # datetime.now记录实例化时间，datetime.now()记录模型创建时间，auto_now=True是无论新增还是更新数据, 此字段都会更新为当前时间
    update_time = models.DateTimeField(default=datetime.now, null=True, blank=True,verbose_name=u"更新时间")

    class Meta:
        verbose_name = u"批量替换数据库中表中某字段的内容"
        verbose_name_plural = verbose_name

    def __str__(self):#重载函数
        return self.test_case_title

    def go_to(self):   #定义点击后跳转到某一个地方（可以加html代码）
        from django.utils.safestring import mark_safe   #调用mark_safe这个函数，django可以显示成一个文本，而不是html代码
        return mark_safe("<a href='{}/testupdatadb/testupdatadbcopy/{}/'>复制新加</a>".format(DJANGO_SERVER_YUMING,self.id))
        # return  "<a href='http://192.168.212.194:9002/testcase/{}/'>跳转</a>".format(self.id)

    go_to.short_description = u"复制新加"   #为go_to函数名个名字
