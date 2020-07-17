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


#RDM日志统计配置
class RdmConfig(models.Model):
    rdm_url = models.CharField(max_length=1000, default="http://192.168.8.98:2000/main.do", verbose_name=u"RDM网址")
    rdm_account = models.CharField(max_length=50, default="", verbose_name=u"RDM登录账号")
    rdm_password = models.CharField(max_length=50, default="", verbose_name=u"RDM登录密码")
    recode_year = models.CharField(max_length=50, default="", verbose_name=u"获取RDM日志年限")

    add_time = models.DateTimeField(null=True, blank=True,auto_now_add=True,
                                    verbose_name=u"添加时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间,auto_now_add=True是指定在数据新增时, 自动写入时间
    update_time = models.DateTimeField(null=True, blank=True,auto_now=True,
                                    verbose_name=u"更新时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间，auto_now=True是无论新增还是更新数据, 此字段都会更新为当前时间

    class Meta:
        verbose_name = u"RDM日志统计配置"
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.rdm_url

    def go_to(self):   #定义点击后跳转到某一个地方（可以加html代码）
        from django.utils.safestring import mark_safe   #调用mark_safe这个函数，django可以显示成一个文本，而不是html代码
        auto_make = "<a href='{}/rdmrecode/rdmconfig/{}/'>自动获取RDM日志</a>&nbsp;&nbsp;</br>".format(
            DJANGO_SERVER_YUMING, self.id)

        return mark_safe(auto_make)

    go_to.short_description = u"操作"   #为go_to函数名个名字


#RDM日志统计查看
class RdmStatic(models.Model):
    people_name = models.CharField(max_length=50, default="", verbose_name=u"人员")
    rdm_year = models.CharField(max_length=50, default="", verbose_name=u"日志年限")
    rdm_data_range = models.CharField(max_length=50, default="", verbose_name=u"日志周时间范围")
    is_week =  models.BooleanField(default=False,verbose_name=u"是否周记")
    day_date = models.CharField(max_length=50, default="", verbose_name=u"日志日期")
    day_task_name = models.CharField(max_length=1000, default="", verbose_name=u"日志任务名称")
    day_task_desc = models.TextField(default="", verbose_name=u"日志任务详情")
    day_task_quse = models.TextField(default="", verbose_name=u"日志问题详情")
    week_task_deck = models.TextField(default="", verbose_name=u"周任务简述")
    add_time = models.DateTimeField(null=True, blank=True,auto_now_add=True,
                                    verbose_name=u"添加时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间,auto_now_add=True是指定在数据新增时, 自动写入时间
    update_time = models.DateTimeField(null=True, blank=True,auto_now=True,
                                    verbose_name=u"更新时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间，auto_now=True是无论新增还是更新数据, 此字段都会更新为当前时间

    class Meta:
        verbose_name = u"RDM日志统计"
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.people_name



    def html_show_week_decs(self):
        from django.utils.safestring import mark_safe  # 调用mark_safe这个函数，django可以显示成一个文本，而不是html代码
        return mark_safe(self.week_task_deck)

    html_show_week_decs.short_description = u"周任务简述"   #为go_to函数名个名字

    def html_show_task_decs(self):
        from django.utils.safestring import mark_safe  # 调用mark_safe这个函数，django可以显示成一个文本，而不是html代码
        return mark_safe(self.day_task_desc)

    html_show_task_decs.short_description = u"日任务详情"   #为go_to函数名个名字

    def html_show_quest_decs(self):
        from django.utils.safestring import mark_safe  # 调用mark_safe这个函数，django可以显示成一个文本，而不是html代码
        return mark_safe(self.day_task_quse)

    html_show_quest_decs.short_description = u"日问题详情"   #为go_to函数名个名字


class CopyRdmStatic(RdmStatic):

    class Meta:
        verbose_name = u"RDM日志统计（去掉空内容）"
        verbose_name_plural = verbose_name
        proxy = True  #将proxy设置为True,不会再生成一张表，如果不设置为True,就会再生成一张表

                        #将proxy设置为True,不会再生成一张表，同时具有model的属性

    def __str__(self):
        return self.people_name


#RDM日志统计查看
class RdmAutoStatic(models.Model):
    people_name = models.CharField(max_length=50, default="", verbose_name=u"人员")
    start_date = models.DateField(null=True, blank=True,verbose_name=u"起始日期")
    end_date = models.DateField(null=True, blank=True, verbose_name=u"结束日期")
    all_task_name = models.TextField(default="", null=True, blank=True, verbose_name=u"所有任务名称")
    all_task_desc = models.TextField(default="", null=True, blank=True, verbose_name=u"所有任务详情")
    all_task_quse = models.TextField(default="", null=True, blank=True, verbose_name=u"所有问题详情")
    add_time = models.DateTimeField(null=True, blank=True,auto_now_add=True,
                                    verbose_name=u"添加时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间,auto_now_add=True是指定在数据新增时, 自动写入时间
    update_time = models.DateTimeField(null=True, blank=True,auto_now=True,
                                    verbose_name=u"更新时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间，auto_now=True是无论新增还是更新数据, 此字段都会更新为当前时间

    class Meta:
        verbose_name = u"RDM日志自动统计某个时段间的任务"
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.people_name

    def go_to(self):   #定义点击后跳转到某一个地方（可以加html代码）
        from django.utils.safestring import mark_safe   #调用mark_safe这个函数，django可以显示成一个文本，而不是html代码
        auto_make = "<a href='{}/rdmrecode/rdmautostatic/{}/'>自动生成简报</a>&nbsp;&nbsp;</br>".format(
            DJANGO_SERVER_YUMING, self.id)

        return mark_safe(auto_make)
        # return  "<a href='http://192.168.212.194:9002/testcase/{}/'>跳转</a>".format(self.id)

    go_to.short_description = u"操作"   #为go_to函数名个名字

    def html_show_all_task_name(self):
        from django.utils.safestring import mark_safe  # 调用mark_safe这个函数，django可以显示成一个文本，而不是html代码
        all_html = ""
        all_task_name_list = eval(self.all_task_name)
        for all_task_name_one in all_task_name_list:
            one_html = "<span>%s</span><br/>"% all_task_name_one
            all_html = all_html+one_html

        return mark_safe(all_html)

    html_show_all_task_name.short_description = u"所有任务名称"   #为go_to函数名个名字

    def html_show_all_task_desc(self):
        from django.utils.safestring import mark_safe  # 调用mark_safe这个函数，django可以显示成一个文本，而不是html代码
        all_html = ""
        all_task_name_list = eval(self.all_task_desc)
        for all_task_name_one in all_task_name_list:
            one_html = "<span>%s</span><br/>"% all_task_name_one
            all_html = all_html+one_html

        return mark_safe(all_html)

    html_show_all_task_desc.short_description = u"所有任务详情"   #为go_to函数名个名字

    def html_show_all_task_quse(self):
        from django.utils.safestring import mark_safe  # 调用mark_safe这个函数，django可以显示成一个文本，而不是html代码
        all_html = ""
        all_task_name_list = eval(self.all_task_quse)
        for all_task_name_one in all_task_name_list:
            one_html = "<span>%s</span><br/>"% all_task_name_one
            all_html = all_html+one_html

        return mark_safe(all_html)

    html_show_all_task_quse.short_description = u"所有问题详情"   #为go_to函数名个名字







