from datetime import datetime   #系统的包放在最上面

from django.db import models   #第二个级别的就是第三方包
from django.contrib.auth import  get_user_model  #导入get_user_model

from wanwenyc.settings import DJANGO_SERVER_YUMING

#第三个就是我们自己创建的包
User = get_user_model()  #get_user_model() 函数直接返回User类，找的是settings.AUTH_USER_MODEL变量的值
# Create your models here.


class ApiRequestData(models.Model):#继承django的Model模块
    """
    接口数据
    """
    test_project = models.CharField(max_length=100, default="", verbose_name=u"测试项目")
    test_module = models.CharField(max_length=100, default="",null=True, blank=True, verbose_name=u"测试模块")
    test_page = models.CharField(max_length=100, default="",null=True, blank=True, verbose_name=u"测试页面")
    case_priority = models.CharField(max_length=10,null=True, blank=True,
                                     choices=(("P0", u"冒烟用例"), ("P1", u"系统的重要功能用例") , ("P2", u"系统的一般功能用例"), ("P3", "极低级别的用例")),
                                     default="P1",
                                     verbose_name=u"用例优先级")
    test_case_title = models.CharField(max_length=200, default="", verbose_name=u"测试内容的名称")
    is_run_case = models.BooleanField(default=True,verbose_name=u"是否运行")
    depend_case = models.ForeignKey('self', default="", null=True, blank=True,
                                   verbose_name=u"依赖的接口的用例",on_delete=models.PROTECT)


    request_url = models.CharField(max_length=1000, default="xpath",null=True, blank=True,verbose_name=u"请求的url")

    is_auto_get_cookies = models.BooleanField(default=True,verbose_name=u"是否自动获取cookies")

    is_use_cache = models.BooleanField(default=True, verbose_name=u"是否使用缓存cookies")


    is_post = models.BooleanField(default=True,verbose_name=u"是否Post请求")

    is_json = models.BooleanField(default=False, verbose_name=u"是否JSON串")


    case_counts = models.IntegerField(default="1",verbose_name="循环次数",help_text=u"循环次数，请填写数字，"
                                                                   u"例如：1、2、3")
    write_user = models.ForeignKey(User,null=True, blank=True,verbose_name=u"添加人", on_delete=models.PROTECT)

    # datetime.now记录实例化时间，datetime.now()记录模型创建时间,auto_now_add=True是指定在数据新增时, 自动写入时间
    add_time = models.DateTimeField(null=True, blank=True, auto_now_add=True,verbose_name=u"添加时间")
    # datetime.now记录实例化时间，datetime.now()记录模型创建时间，auto_now=True是无论新增还是更新数据, 此字段都会更新为当前时间
    update_time = models.DateTimeField(default=datetime.now, null=True, blank=True,verbose_name=u"更新时间")

    class Meta:
        verbose_name = u"接口数据"
        verbose_name_plural = verbose_name

    def __str__(self):#重载函数
        return self.test_case_title

    def go_to(self):   #定义点击后跳转到某一个地方（可以加html代码）
        from django.utils.safestring import mark_safe   #调用mark_safe这个函数，django可以显示成一个文本，而不是html代码
        return mark_safe("<a href='{}/testapidatas/apirequestdatacopy/{}/'>复制新加</a>".format(DJANGO_SERVER_YUMING,self.id))
        # return  "<a href='http://192.168.212.194:9002/testcase/{}/'>跳转</a>".format(self.id)

    go_to.short_description = u"复制新加"   #为go_to函数名个名字


class RequestHeaders(models.Model):
    """
    接口数据依赖的请求Headers内容模型
    """
    apirequestdata = models.ForeignKey(ApiRequestData,default="", null=True, blank=True,
                                   verbose_name=u"依赖的接口用例",on_delete=models.PROTECT)

    request_key = models.CharField(max_length=100, default="request_key",null=True, blank=True,
                                      verbose_name=u"键值对的键")

    # is_auto_input = models.BooleanField(default=False, verbose_name=u"是否自动输入键值对的值")
    # auto_input_type = models.CharField(choices=(('1','数字'),('2','字母'),('3','数字和字母'),('4','数字和字母和特殊符号'),('5','数字和字母和特殊符号和转义字符'),('6','汉字')),
    #                                    null=True, blank=True,
    #                                    max_length=10,default='6',verbose_name="自动输入字符的类型")
    # auto_input_long = models.CharField(max_length=100,default="300",null=True, blank=True,
    #                                       verbose_name="自动输入的字符的个数",help_text=u"字符的个数，请填写数字，"
    #                                                                u"例如：1、2、3")

    request_value = models.CharField(max_length=1000, default="",null=True, blank=True,
                                                         verbose_name=u"键值对的值")

    # is_with_time = models.BooleanField(default=True,verbose_name=u"是否带时间串")
    # is_check = models.BooleanField(default=True,verbose_name=u"是否进行验证")
    # datetime.now记录实例化时间，datetime.now()记录模型创建时间,auto_now_add=True是指定在数据新增时, 自动写入时间
    add_time = models.DateTimeField(null=True, blank=True, auto_now_add=True,verbose_name=u"添加时间")
    # datetime.now记录实例化时间，datetime.now()记录模型创建时间，auto_now=True是无论新增还是更新数据, 此字段都会更新为当前时间
    update_time = models.DateTimeField(default=datetime.now, null=True, blank=True,verbose_name=u"更新时间")

    class Meta:
        verbose_name = u"请求Headers相关内容"
        verbose_name_plural = verbose_name

    def __str__(self):#重载函数
        return self.request_key


class RequestCookies(models.Model):
    """
    接口数据依赖的请求Cookies内容模型
    """
    apirequestdata = models.ForeignKey(ApiRequestData,default="", null=True, blank=True,
                                   verbose_name=u"依赖的接口用例",on_delete=models.PROTECT)

    request_key = models.CharField(max_length=100, default="request_key",null=True, blank=True,
                                      verbose_name=u"键值对的键")

    is_auto_input = models.BooleanField(default=False, verbose_name=u"是否自动输入键值对的值")
    auto_input_type = models.CharField(choices=(('1','数字'),('2','字母'),('3','数字和字母'),('4','数字和字母和特殊符号'),('5','数字和字母和特殊符号和转义字符'),('6','汉字')),
                                       null=True, blank=True,
                                       max_length=10,default='6',verbose_name="自动输入字符的类型")
    auto_input_long = models.CharField(max_length=100,default="300",null=True, blank=True,
                                          verbose_name="自动输入的字符的个数",help_text=u"字符的个数，请填写数字，"
                                                                   u"例如：1、2、3")

    request_value = models.CharField(max_length=1000, default="",null=True, blank=True,
                                                         verbose_name=u"键值对的值")

    is_with_time = models.BooleanField(default=True,verbose_name=u"是否带时间串")
    is_check = models.BooleanField(default=True,verbose_name=u"是否进行验证")
    # datetime.now记录实例化时间，datetime.now()记录模型创建时间,auto_now_add=True是指定在数据新增时, 自动写入时间
    add_time = models.DateTimeField(null=True, blank=True, auto_now_add=True,verbose_name=u"添加时间")
    # datetime.now记录实例化时间，datetime.now()记录模型创建时间，auto_now=True是无论新增还是更新数据, 此字段都会更新为当前时间
    update_time = models.DateTimeField(default=datetime.now, null=True, blank=True,verbose_name=u"更新时间")

    class Meta:
        verbose_name = u"请求Cookies相关内容"
        verbose_name_plural = verbose_name

    def __str__(self):#重载函数
        return self.request_key


class RequestDatas(models.Model):
    """
    接口数据依赖的请求data或urldata内容模型
    """
    apirequestdata = models.ForeignKey(ApiRequestData,default="", null=True, blank=True,
                                   verbose_name=u"依赖的接口用例",on_delete=models.PROTECT)

    request_key = models.CharField(max_length=100, default="request_key",null=True, blank=True,
                                      verbose_name=u"键值对的键")

    is_auto_input = models.BooleanField(default=False, verbose_name=u"是否自动输入键值对的值")
    auto_input_type = models.CharField(choices=(('1','数字'),('2','字母'),('3','数字和字母'),('4','数字和字母和特殊符号'),('5','数字和字母和特殊符号和转义字符'),('6','汉字')),
                                       null=True, blank=True,
                                       max_length=10,default='6',verbose_name="自动输入字符的类型")
    auto_input_long = models.CharField(max_length=100,default="300",null=True, blank=True,
                                          verbose_name="自动输入的字符的个数",help_text=u"字符的个数，请填写数字，"
                                                                   u"例如：1、2、3")

    request_value = models.CharField(max_length=1000, default="",null=True, blank=True,
                                                         verbose_name=u"键值对的值")

    sql_assert = models.CharField(max_length=100, default="request_key", null=True, blank=True,
                                  verbose_name=u"查询数据库相应值语句")

    is_with_time = models.BooleanField(default=False,verbose_name=u"是否带时间串")
    is_check = models.BooleanField(default=False,verbose_name=u"是否进行验证")
    # datetime.now记录实例化时间，datetime.now()记录模型创建时间,auto_now_add=True是指定在数据新增时, 自动写入时间
    add_time = models.DateTimeField(null=True, blank=True, auto_now_add=True,verbose_name=u"添加时间")
    # datetime.now记录实例化时间，datetime.now()记录模型创建时间，auto_now=True是无论新增还是更新数据, 此字段都会更新为当前时间
    update_time = models.DateTimeField(default=datetime.now, null=True, blank=True,verbose_name=u"更新时间")

    class Meta:
        verbose_name = u"请求bodyData相关内容"
        verbose_name_plural = verbose_name

    def __str__(self):#重载函数
        return self.request_key

class RequestUrlDatas(models.Model):
    """
    接口数据依赖的url参数
    """
    apirequestdata = models.ForeignKey(ApiRequestData,default="", null=True, blank=True,
                                   verbose_name=u"依赖的接口用例",on_delete=models.PROTECT)

    request_key = models.CharField(max_length=100, default="request_key",null=True, blank=True,
                                      verbose_name=u"键值对的键")

    is_auto_input = models.BooleanField(default=False, verbose_name=u"是否自动输入键值对的值")
    auto_input_type = models.CharField(choices=(('1','数字'),('2','字母'),('3','数字和字母'),('4','数字和字母和特殊符号'),('5','数字和字母和特殊符号和转义字符'),('6','汉字')),
                                       null=True, blank=True,
                                       max_length=10,default='6',verbose_name="自动输入字符的类型")
    auto_input_long = models.CharField(max_length=100,default="300",null=True, blank=True,
                                          verbose_name="自动输入的字符的个数",help_text=u"字符的个数，请填写数字，"
                                                                   u"例如：1、2、3")

    request_value = models.CharField(max_length=1000, default="",null=True, blank=True,
                                                         verbose_name=u"键值对的值")

    is_with_time = models.BooleanField(default=False,verbose_name=u"是否带时间串")
    is_check = models.BooleanField(default=False,verbose_name=u"是否进行验证")
    # datetime.now记录实例化时间，datetime.now()记录模型创建时间,auto_now_add=True是指定在数据新增时, 自动写入时间
    add_time = models.DateTimeField(null=True, blank=True, auto_now_add=True,verbose_name=u"添加时间")
    # datetime.now记录实例化时间，datetime.now()记录模型创建时间，auto_now=True是无论新增还是更新数据, 此字段都会更新为当前时间
    update_time = models.DateTimeField(default=datetime.now, null=True, blank=True,verbose_name=u"更新时间")

    class Meta:
        verbose_name = u"请求UrlData相关内容"
        verbose_name_plural = verbose_name

    def __str__(self):#重载函数
        return self.request_key


class RequestAssert(models.Model):
    """
    接口数据断言
    """
    apirequestdata = models.ForeignKey(ApiRequestData,default="", null=True, blank=True,
                                   verbose_name=u"依赖的接口用例",on_delete=models.PROTECT)

    request_assert_type = models.CharField(max_length=100, default="request_key",null=True, blank=True,
                                      verbose_name=u"断言类型")
    input_assert = models.CharField(max_length=100, default="request_key",null=True, blank=True,
                                      verbose_name=u"输入预期断言内容")
    sql_assert = models.CharField(max_length=100, default="request_key",null=True, blank=True,
                                      verbose_name=u"数据库语句断言")
    code_assert = models.CharField(max_length=100, default="request_key",null=True, blank=True,
                                      verbose_name=u"状态码断言")
    time_assert = models.CharField(max_length=100, default="request_key",null=True, blank=True,
                                   verbose_name=u"响应时间断言（单位：毫秒）",
                                   help_text="断言小于等于输入的毫秒数则通过")

    is_auto_input = models.BooleanField(default=False, verbose_name=u"是否自动输入键值对的值")
    auto_input_type = models.CharField(choices=(('1','数字'),('2','字母'),('3','数字和字母'),('4','数字和字母和特殊符号'),('5','数字和字母和特殊符号和转义字符'),('6','汉字')),
                                       null=True, blank=True,
                                       max_length=10,default='6',verbose_name="自动输入字符的类型")
    auto_input_long = models.CharField(max_length=100,default="300",null=True, blank=True,
                                          verbose_name="自动输入的字符的个数",help_text=u"字符的个数，请填写数字，"
                                                                   u"例如：1、2、3")

    request_value = models.CharField(max_length=1000, default="",null=True, blank=True,
                                                         verbose_name=u"键值对的值")

    is_with_time = models.BooleanField(default=False,verbose_name=u"是否带时间串")
    is_check = models.BooleanField(default=False,verbose_name=u"是否进行验证")
    # datetime.now记录实例化时间，datetime.now()记录模型创建时间,auto_now_add=True是指定在数据新增时, 自动写入时间
    add_time = models.DateTimeField(null=True, blank=True, auto_now_add=True,verbose_name=u"添加时间")
    # datetime.now记录实例化时间，datetime.now()记录模型创建时间，auto_now=True是无论新增还是更新数据, 此字段都会更新为当前时间
    update_time = models.DateTimeField(default=datetime.now, null=True, blank=True,verbose_name=u"更新时间")

    class Meta:
        verbose_name = u"断言内容"
        verbose_name_plural = verbose_name

    def __str__(self):#重载函数
        return str(self.request_assert_type)



