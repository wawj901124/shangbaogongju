from django.db import models
from datetime import datetime
from wanwenyc.settings import DJANGO_SERVER_YUMING

from django.contrib.auth import  get_user_model  #导入get_user_model
#第三个就是我们自己创建的包
User = get_user_model()  #get_user_model() 函数直接返回User类，找的是settings.AUTH_USER_MODEL变量的值

# Create your models here.
class Report(models.Model):
    testproject = models.CharField(max_length=50, default="", verbose_name=u"测试项目")
    testmodule = models.CharField(max_length=50, default="", verbose_name=u"项目模块")
    reportname = models.CharField(max_length=20, default="", verbose_name=u"测试执行开始时间串")
    reportfile = models.FileField(upload_to="report/%Y%m" , verbose_name=u"报告文件", max_length=1000)
    # reportimage = models.ImageField(upload_to="report/%Y%m/screenshots/",verbose_name=u"报告中错误截图",max_length=1000,height_field="image_height",width_field="image_width")   #图片类型，可以定义宽度（width_field）和高度（height_field）
    # image_height = models.PositiveIntegerField(null=True, blank=True, editable=False, default="50")  #设置图片高度field
    # image_width = models.PositiveIntegerField(null=True, blank=True, editable=False, default="50")   #设置图片宽度field
    add_time = models.DateTimeField(null=True, blank=True,auto_now_add=True,
                                    verbose_name=u"添加时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间,auto_now_add=True是指定在数据新增时, 自动写入时间
    update_time = models.DateTimeField(null=True, blank=True,auto_now=True,
                                    verbose_name=u"更新时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间，auto_now=True是无论新增还是更新数据, 此字段都会更新为当前时间

    class Meta:
        verbose_name = u"报告记录"
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.reportname

    def go_to(self):   #定义点击后跳转到某一个地方（可以加html代码）
        from django.utils.safestring import mark_safe   #调用mark_safe这个函数，django可以显示成一个文本，而不是html代码
        return mark_safe("<a href='{}/media/{}'>{}</a>".format(DJANGO_SERVER_YUMING,self.reportfile,self.reportfile))
        # return  "<a href='http://192.168.212.194:9002/testcase/{}/'>跳转</a>".format(self.id)

    go_to.short_description = u"报告文件"   #为go_to函数名个名字



class RequestReport(models.Model):
    testproject = models.CharField(max_length=100, default="", verbose_name=u"测试项目")
    testmodule = models.CharField(max_length=100, default="", verbose_name=u"测试模块")
    testpage =  models.CharField(max_length=100, default="", verbose_name=u"测试页面")
    testcasetitle = models.CharField(max_length=100, default="", verbose_name=u"测试内容的名称")
    teststarttime = models.CharField(max_length=100, default="", verbose_name=u"开始运行时间")
    forcount = models.CharField(max_length=100, default="", verbose_name=u"第几次循环")
    test_result = models.CharField(max_length=10,null=True, blank=True,
                                     choices=(("P0", u"通过"), ("P1", u"失败")),
                                     default="",
                                     verbose_name=u"接口测试结果")

    response_status_code = models.CharField(max_length=100, default="",null=True, blank=True, verbose_name=u"接口响应status_code")
    response_text = models.TextField(default="",null=True, blank=True, verbose_name=u"接口响应text")
    response_content = models.TextField(default="",null=True, blank=True, verbose_name=u"接口响应content")
    response_json = models.TextField(default="",null=True, blank=True, verbose_name=u"接口响应json")
    response_elapsed = models.CharField(max_length=100, default="",null=True, blank=True, verbose_name=u"接口响应elapsed")
    response_elapsed_microseconds = models.CharField(max_length=100, default="",null=True, blank=True, verbose_name=u"接口响应elapsed_microseconds(单位：毫秒)")
    response_headers = models.TextField(default="",null=True, blank=True, verbose_name=u"接口响应headers")
    response_cookies =models.TextField(default="",null=True, blank=True, verbose_name=u"接口响应cookies")

    add_time = models.DateTimeField(null=True, blank=True,auto_now_add=True,
                                    verbose_name=u"添加时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间,auto_now_add=True是指定在数据新增时, 自动写入时间
    update_time = models.DateTimeField(default=datetime.now, null=True, blank=True,
                                    verbose_name=u"更新时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间，auto_now=True是无论新增还是更新数据, 此字段都会更新为当前时间

    class Meta:
        verbose_name = u"接口测试结果统计"
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.testcasetitle


class PageLoadTimeReport(models.Model):
    testproject = models.CharField(max_length=100, default="", verbose_name=u"测试项目")
    testmodule = models.CharField(max_length=100, default="", verbose_name=u"测试模块")
    testpage =  models.CharField(max_length=100, default="", verbose_name=u"测试页面")
    testcasetitle = models.CharField(max_length=100, default="", verbose_name=u"测试内容的名称")
    teststarttime = models.CharField(max_length=100, default="", verbose_name=u"开始运行时间")
    forcount = models.CharField(max_length=100, default="", verbose_name=u"第几次循环")


    page_load_time_no_catch = models.CharField(max_length=100, default="",null=True, blank=True, verbose_name=u"页面加载时间（单位：毫秒）")
    dom_load_time_no_catch = models.CharField(max_length=100, default="",null=True, blank=True, verbose_name=u"DOM加载时间（单位：毫秒）")
    page_load_time_with_catch = models.CharField(max_length=100, default="",null=True, blank=True, verbose_name=u"有缓存时页面加载时间（单位：毫秒）")
    dom_load_time_with_catch = models.CharField(max_length=100, default="",null=True, blank=True, verbose_name=u"有缓存时DOM加载时间（单位：毫秒）")

    write_user = models.ForeignKey(User,null=True, blank=True,verbose_name=u"用户名", on_delete=models.PROTECT)
    add_time = models.DateTimeField(null=True, blank=True,auto_now_add=True,
                                    verbose_name=u"添加时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间,auto_now_add=True是指定在数据新增时, 自动写入时间
    update_time = models.DateTimeField(default=datetime.now, null=True, blank=True,
                                    verbose_name=u"更新时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间，auto_now=True是无论新增还是更新数据, 此字段都会更新为当前时间

    class Meta:
        verbose_name = u"页面加载时间统计"
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.testcasetitle



