from django.db import models
from datetime import datetime
from wanwenyc.settings import DJANGO_SERVER_YUMING
from django.contrib.auth import  get_user_model  #导入get_user_model

#第三个就是我们自己创建的包
User = get_user_model()  #get_user_model() 函数直接返回User类，找的是settings.AUTH_USER_MODEL变量的值




class PageLoadTimeReportOneSecond(models.Model):
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

    write_user = models.ForeignKey(User, null=True, blank=True, verbose_name=u"用户名", on_delete=models.PROTECT)
    add_time = models.DateTimeField(null=True, blank=True,auto_now_add=True,
                                    verbose_name=u"添加时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间,auto_now_add=True是指定在数据新增时, 自动写入时间
    update_time = models.DateTimeField(default=datetime.now, null=True, blank=True,
                                    verbose_name=u"更新时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间，auto_now=True是无论新增还是更新数据, 此字段都会更新为当前时间

    class Meta:
        verbose_name = u"页面加载时间在1秒至2秒统计"
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.testcasetitle


class PageLoadTimeReportTwoSecond(models.Model):
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

    write_user = models.ForeignKey(User, null=True, blank=True, verbose_name=u"用户名", on_delete=models.PROTECT)
    add_time = models.DateTimeField(null=True, blank=True,auto_now_add=True,
                                    verbose_name=u"添加时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间,auto_now_add=True是指定在数据新增时, 自动写入时间
    update_time = models.DateTimeField(default=datetime.now, null=True, blank=True,
                                    verbose_name=u"更新时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间，auto_now=True是无论新增还是更新数据, 此字段都会更新为当前时间

    class Meta:
        verbose_name = u"页面加载时间在2秒至3秒统计"
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.testcasetitle


class PageLoadTimeReportThereSecond(models.Model):
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

    write_user = models.ForeignKey(User, null=True, blank=True, verbose_name=u"用户名", on_delete=models.PROTECT)
    add_time = models.DateTimeField(null=True, blank=True,auto_now_add=True,
                                    verbose_name=u"添加时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间,auto_now_add=True是指定在数据新增时, 自动写入时间
    update_time = models.DateTimeField(default=datetime.now, null=True, blank=True,
                                    verbose_name=u"更新时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间，auto_now=True是无论新增还是更新数据, 此字段都会更新为当前时间

    class Meta:
        verbose_name = u"页面加载时间在3秒至4秒统计"
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.testcasetitle


class PageLoadTimeReportFourSecond(models.Model):
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

    write_user = models.ForeignKey(User, null=True, blank=True, verbose_name=u"用户名", on_delete=models.PROTECT)
    add_time = models.DateTimeField(null=True, blank=True,auto_now_add=True,
                                    verbose_name=u"添加时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间,auto_now_add=True是指定在数据新增时, 自动写入时间
    update_time = models.DateTimeField(default=datetime.now, null=True, blank=True,
                                    verbose_name=u"更新时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间，auto_now=True是无论新增还是更新数据, 此字段都会更新为当前时间

    class Meta:
        verbose_name = u"页面加载时间在4秒至5秒统计"
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.testcasetitle


class PageLoadTimeReportFiveSecond(models.Model):
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

    write_user = models.ForeignKey(User, null=True, blank=True, verbose_name=u"用户名", on_delete=models.PROTECT)
    add_time = models.DateTimeField(null=True, blank=True,auto_now_add=True,
                                    verbose_name=u"添加时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间,auto_now_add=True是指定在数据新增时, 自动写入时间
    update_time = models.DateTimeField(default=datetime.now, null=True, blank=True,
                                    verbose_name=u"更新时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间，auto_now=True是无论新增还是更新数据, 此字段都会更新为当前时间

    class Meta:
        verbose_name = u"页面加载时间在5秒及其以上统计"
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.testcasetitle