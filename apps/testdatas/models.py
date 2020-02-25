from datetime import datetime   #系统的包放在最上面

from django.db import models   #第二个级别的就是第三方包
from django.contrib.auth import  get_user_model  #导入get_user_model

from wanwenyc.settings import DJANGO_SERVER_YUMING

#第三个就是我们自己创建的包
User = get_user_model()  #get_user_model() 函数直接返回User类，找的是settings.AUTH_USER_MODEL变量的值
#Create your models here.
class LoginAndCheck(models.Model):#继承django的Model模块
    """
    登录场景
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

    login_url = models.CharField(max_length=1000, default="",null=True, blank=True,
                                                         verbose_name=u"登录页的url")

    is_auto_input_code = models.BooleanField(default=False,verbose_name=u"是否自动输入验证码")

    code_image_xpath = models.CharField(max_length=1000, default="",null=True, blank=True,
                                                         verbose_name=u"验证码xpath路径")

    code_type = models.CharField(max_length=10, default="n4",null=True, blank=True,verbose_name=u"验证码类型",
                                 help_text=u"验证码类型：n4(4位纯数字)、n5(5位纯数字)、n6（6位纯数字）、"
                                           u"e4（4位纯英文）、e5（5位纯英文）、e6（6位纯英文）、"
                                           u"ne4（4位英文数字）、ne5（5位英文数字）、ne6（6位英文数字)" )

    code_input_ele_find = models.CharField(max_length=100, default="xpath",null=True, blank=True,
                                        verbose_name=u"验证码输入框查找风格",
                                        help_text=u"元素查找风格：id、name、class_name、tag_name、"
                                                  u"link_text、partial_link_text、css_selector、xpath")
    code_input_ele_find_value = models.CharField(max_length=1000, default="",null=True, blank=True,
                                                         verbose_name=u"验证码输入框查找风格的确切值")

    login_button_ele_find = models.CharField(max_length=100, default="xpath",null=True, blank=True,
                                        verbose_name=u"登录按钮查找风格",
                                        help_text=u"元素查找风格：id、name、class_name、tag_name、"
                                                  u"link_text、partial_link_text、css_selector、xpath")
    login_button_ele_find_value = models.CharField(max_length=1000, default="",null=True, blank=True,
                                                         verbose_name=u"登录按钮查找风格的确切值")
    click_login_button_delay_time = models.CharField(max_length=100, default="3", null=True, blank=True,
                                                verbose_name=u"点击登录按钮后的延时时长（单位秒）",
                                                help_text=u"点击登录按钮后的延时时长（单位秒），请填写数字，例如：1、2、3")


    case_counts = models.IntegerField(default="1",verbose_name="循环次数",help_text=u"循环次数，请填写数字，"
                                                                   u"例如：1、2、3")
    write_user = models.ForeignKey(User,null=True, blank=True,verbose_name=u"添加人", on_delete=models.PROTECT)

    # datetime.now记录实例化时间，datetime.now()记录模型创建时间,auto_now_add=True是指定在数据新增时, 自动写入时间
    add_time = models.DateTimeField(null=True, blank=True, auto_now_add=True,verbose_name=u"添加时间")
    # datetime.now记录实例化时间，datetime.now()记录模型创建时间，auto_now=True是无论新增还是更新数据, 此字段都会更新为当前时间
    update_time = models.DateTimeField(default=datetime.now, null=True, blank=True,verbose_name=u"更新时间")

    class Meta:
        verbose_name = u"登录场景"
        verbose_name_plural = verbose_name

    def __str__(self):#重载函数
        return self.test_case_title

    def go_to(self):   #定义点击后跳转到某一个地方（可以加html代码）
        from django.utils.safestring import mark_safe   #调用mark_safe这个函数，django可以显示成一个文本，而不是html代码
        return mark_safe("<a href='{}/testdatas/loginandcheckcopy/{}/'>复制新加</a>".format(DJANGO_SERVER_YUMING,self.id))
        # return  "<a href='http://192.168.212.194:9002/testcase/{}/'>跳转</a>".format(self.id)

    go_to.short_description = u"复制新加"   #为go_to函数名个名字


class ClickAndBack(models.Model):#继承django的Model模块
    """
    点击滑动返回测试场景测试数据
    """
    test_project = models.CharField(max_length=100, default="", verbose_name=u"测试项目")
    test_module = models.CharField(max_length=100, default="",null=True, blank=True, verbose_name=u"测试模块")
    test_page = models.CharField(max_length=100, default="", verbose_name=u"测试页面")
    test_case_title = models.CharField(max_length=200, default="", verbose_name=u"测试内容的名称")
    is_run_case = models.BooleanField(default=True,verbose_name=u"是否运行")
    is_static_load_page_time = models.BooleanField(default=False,verbose_name=u"是否统计页面加载时间")
    current_page_click_ele_find = models.CharField(max_length=100, default="xpath",
                                                    verbose_name=u"当前页面要点击元素查找风格",
                                                    help_text=u"元素查找风格：id、name、class_name、tag_name、"
                                                              u"link_text、partial_link_text、css_selector、xpath")
    current_page_click_ele_find_value = models.CharField(max_length=1000, default="",
                                                         verbose_name=u"当前页面要点击元素查找风格的确切值")
    is_new = models.BooleanField(default=False, verbose_name=u"是否新窗口")
    next_page_check_ele_find= models.CharField(max_length=100,
                                             default="xpath", verbose_name=u"下一页面标识元素查找风格",
                                             help_text=u"元素查找风格：id、name、class_name、tag_name、"
                                                       u"link_text、partial_link_text、css_selector、xpath")
    next_page_check_ele_find_value = models.CharField(max_length=1000, default="",
                                                         verbose_name=u"下一页面标识元素查找风格的确切值")
    case_counts = models.IntegerField(default="1",verbose_name="用例循环次数",help_text=u"用例循环次数，请填写数字，"
                                                                   u"例如：1、2、3")
    depend_case = models.ForeignKey('self', default="", null=True, blank=True,
                                   verbose_name=u"依赖的前置用例",on_delete=models.PROTECT)
    write_user = models.ForeignKey(User,related_name="writeuser",null=True, blank=True,
                                   verbose_name=u"添加用例人", on_delete=models.PROTECT)

    # datetime.now记录实例化时间，datetime.now()记录模型创建时间,auto_now_add=True是指定在数据新增时, 自动写入时间
    add_time = models.DateTimeField(null=True, blank=True, auto_now_add=True,verbose_name=u"添加时间")
    # datetime.now记录实例化时间，datetime.now()记录模型创建时间，auto_now=True是无论新增还是更新数据, 此字段都会更新为当前时间
    update_time = models.DateTimeField(default=datetime.now, null=True, blank=True,verbose_name=u"更新时间")

    class Meta:
        verbose_name = u"点击场景"
        verbose_name_plural = verbose_name

    def __str__(self):#重载函数
        return self.test_case_title

    def go_to(self):   #定义点击后跳转到某一个地方（可以加html代码）
        from django.utils.safestring import mark_safe   #调用mark_safe这个函数，django可以显示成一个文本，而不是html代码
        return mark_safe("<a href='{}/testdatas/clickandbackcopy/{}/'>复制新加</a>".format(DJANGO_SERVER_YUMING,self.id))
        # return  "<a href='http://192.168.212.194:9002/testcase/{}/'>跳转</a>".format(self.id)

    go_to.short_description = u"复制新加"   #为go_to函数名个名字


class NewAddAndCheck(models.Model):#继承django的Model模块
    """
    新增数据场景
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

    depend_new_add_and_check_case = models.ForeignKey('self', default="", null=True, blank=True,
                                   verbose_name=u"依赖的添加场景的用例",on_delete=models.PROTECT)

    depend_click_case = models.ForeignKey(ClickAndBack, default="", null=True, blank=True,
                                   verbose_name=u"依赖的点击场景的用例",on_delete=models.PROTECT)



    confirm_ele_find = models.CharField(max_length=100, default="xpath",null=True, blank=True,
                                        verbose_name=u"确定按钮查找风格",
                                        help_text=u"元素查找风格：id、name、class_name、tag_name、"
                                                  u"link_text、partial_link_text、css_selector、xpath")
    confirm_ele_find_value = models.CharField(max_length=1000, default="",null=True, blank=True,
                                                         verbose_name=u"确定按钮查找风格的确切值")
    click_confirm_delay_time = models.CharField(max_length=100, default="3", null=True, blank=True,
                                                verbose_name=u"点击确定按钮后的延时时长（单位秒）",
                                                help_text=u"点击确定按钮后的延时时长（单位秒），请填写数字，例如：1、2、3")

    is_click_cancel = models.BooleanField(default=False,verbose_name=u"是否点击取消按钮")
    cancel_ele_find = models.CharField(max_length=100, default="xpath", null=True, blank=True,
                                       verbose_name=u"取消按钮查找风格",
                                       help_text=u"元素查找风格：id、name、class_name、tag_name、"
                                                 u"link_text、partial_link_text、css_selector、xpath")
    cancel_ele_find_value = models.CharField(max_length=1000, default="",null=True, blank=True,
                                                         verbose_name=u"取消按钮查找风格的确切值")
    is_submit_success = models.BooleanField(default=True,verbose_name=u"是否添加成功")

    is_signel_page = models.BooleanField(default=False, verbose_name=u"是否单页面")

    page_number_xpath = models.CharField(max_length=1000, default="",null=True, blank=True,
                                                         verbose_name=u"页数层xpath路径值")

    result_table_ele_find = models.CharField(max_length=100, default="xpath",null=True, blank=True,
                                             verbose_name=u"结果表格查找风格",
                                             help_text=u"元素查找风格：id、name、class_name、tag_name、"
                                                       u"link_text、partial_link_text、css_selector、xpath")
    result_table_ele_find_value = models.CharField(max_length=1000, default="",null=True, blank=True,
                                                         verbose_name=u"结果表格查找风格的确切值")
    table_colnum_counts = models.CharField(max_length=100, default="", null=True, blank=True,
                                           verbose_name=u"结果表格总列数",help_text=u"结果表格总列数，请填写数字，"
                                                        u"例如：1、2、3")
    case_counts = models.IntegerField(default="1",verbose_name="循环次数",help_text=u"循环次数，请填写数字，"
                                                                   u"例如：1、2、3")
    write_user = models.ForeignKey(User,null=True, blank=True,verbose_name=u"添加人", on_delete=models.PROTECT)

    # datetime.now记录实例化时间，datetime.now()记录模型创建时间,auto_now_add=True是指定在数据新增时, 自动写入时间
    add_time = models.DateTimeField(null=True, blank=True, auto_now_add=True,verbose_name=u"添加时间")
    # datetime.now记录实例化时间，datetime.now()记录模型创建时间，auto_now=True是无论新增还是更新数据, 此字段都会更新为当前时间
    update_time = models.DateTimeField(default=datetime.now, null=True, blank=True,verbose_name=u"更新时间")

    class Meta:
        verbose_name = u"新增场景"
        verbose_name_plural = verbose_name

    def __str__(self):#重载函数
        return self.test_case_title

    def go_to(self):   #定义点击后跳转到某一个地方（可以加html代码）
        from django.utils.safestring import mark_safe   #调用mark_safe这个函数，django可以显示成一个文本，而不是html代码
        return mark_safe("<a href='{}/testdatas/newaddandcheckcopy/{}/'>复制新加不带关联</a>".format(DJANGO_SERVER_YUMING,self.id))
        # return  "<a href='http://192.168.212.194:9002/testcase/{}/'>跳转</a>".format(self.id)

    go_to.short_description = u"复制新加不带关联"   #为go_to函数名个名字

    def go_to_with_relevance(self):   #定义点击后跳转到某一个地方（可以加html代码）
        from django.utils.safestring import mark_safe   #调用mark_safe这个函数，django可以显示成一个文本，而不是html代码
        return mark_safe("<a href='{}/testdatas/newaddandcheckcopywithrelevance/{}/'>复制新加</a>".format(DJANGO_SERVER_YUMING,self.id))
        # return  "<a href='http://192.168.212.194:9002/testcase/{}/'>跳转</a>".format(self.id)

    go_to_with_relevance.short_description = u"复制新加"   #为go_to函数名个名字


class EditAndCheck(models.Model):#继承django的Model模块
    """
    修改数据场景
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

    depend_click_case = models.ForeignKey(ClickAndBack, default="", null=True, blank=True,
                                   verbose_name=u"依赖的点击场景的用例",on_delete=models.PROTECT)

    edit_ele_find = models.CharField(max_length=100, default="xpath",null=True, blank=True,
                                        verbose_name=u"被修改元素查找风格",
                                        help_text=u"元素查找风格：id、name、class_name、tag_name、"
                                                  u"link_text、partial_link_text、css_selector、xpath")
    edit_ele_find_value = models.CharField(max_length=1000, default="",null=True, blank=True,
                                                         verbose_name=u"被修改元素查找风格的确切值")

    edit_button_find = models.CharField(max_length=100, default="xpath",null=True, blank=True,
                                        verbose_name=u"修改按钮查找风格",
                                        help_text=u"元素查找风格：id、name、class_name、tag_name、"
                                                  u"link_text、partial_link_text、css_selector、xpath")
    edit_button_find_value = models.CharField(max_length=1000, default="",null=True, blank=True,
                                                         verbose_name=u"修改按钮查找风格的确切值")


    confirm_ele_find = models.CharField(max_length=100, default="xpath",null=True, blank=True,
                                        verbose_name=u"确定按钮查找风格",
                                        help_text=u"元素查找风格：id、name、class_name、tag_name、"
                                                  u"link_text、partial_link_text、css_selector、xpath")
    confirm_ele_find_value = models.CharField(max_length=1000, default="",null=True, blank=True,
                                                         verbose_name=u"确定按钮查找风格的确切值")
    click_confirm_delay_time = models.CharField(max_length=100, default="3", null=True, blank=True,
                                                verbose_name=u"点击确定按钮后的延时时长（单位秒）",
                                                help_text=u"点击确定按钮后的延时时长（单位秒），请填写数字，例如：1、2、3")

    is_click_cancel = models.BooleanField(default=False,verbose_name=u"是否点击取消按钮")
    cancel_ele_find = models.CharField(max_length=100, default="xpath", null=True, blank=True,
                                       verbose_name=u"取消按钮查找风格",
                                       help_text=u"元素查找风格：id、name、class_name、tag_name、"
                                                 u"link_text、partial_link_text、css_selector、xpath")
    cancel_ele_find_value = models.CharField(max_length=1000, default="",null=True, blank=True,
                                                         verbose_name=u"取消按钮查找风格的确切值")
    is_submit_success = models.BooleanField(default=True,verbose_name=u"是否添加成功")

    is_signel_page = models.BooleanField(default=True, verbose_name=u"是否单页面")

    page_number_xpath = models.CharField(max_length=1000, default="",null=True, blank=True,
                                                         verbose_name=u"页数层xpath路径值")

    result_table_ele_find = models.CharField(max_length=100, default="xpath",null=True, blank=True,
                                             verbose_name=u"结果表格查找风格",
                                             help_text=u"元素查找风格：id、name、class_name、tag_name、"
                                                       u"link_text、partial_link_text、css_selector、xpath")
    result_table_ele_find_value = models.CharField(max_length=1000, default="",null=True, blank=True,
                                                         verbose_name=u"结果表格查找风格的确切值")
    table_colnum_counts = models.CharField(max_length=100, default="", null=True, blank=True,
                                           verbose_name=u"结果表格总列数",help_text=u"结果表格总列数，请填写数字，"
                                                        u"例如：1、2、3")
    case_counts = models.IntegerField(default="1",verbose_name="循环次数",help_text=u"循环次数，请填写数字，"
                                                                   u"例如：1、2、3")
    write_user = models.ForeignKey(User,null=True, blank=True,verbose_name=u"添加人", on_delete=models.PROTECT)

    # datetime.now记录实例化时间，datetime.now()记录模型创建时间,auto_now_add=True是指定在数据新增时, 自动写入时间
    add_time = models.DateTimeField(null=True, blank=True, auto_now_add=True,verbose_name=u"添加时间")
    # datetime.now记录实例化时间，datetime.now()记录模型创建时间，auto_now=True是无论新增还是更新数据, 此字段都会更新为当前时间
    update_time = models.DateTimeField(default=datetime.now, null=True, blank=True,verbose_name=u"更新时间")

    class Meta:
        verbose_name = u"修改场景"
        verbose_name_plural = verbose_name

    def __str__(self):#重载函数
        return self.test_case_title

    def go_to(self):   #定义点击后跳转到某一个地方（可以加html代码）
        from django.utils.safestring import mark_safe   #调用mark_safe这个函数，django可以显示成一个文本，而不是html代码
        return mark_safe("<a href='{}/testdatas/editandcheckcopy/{}/'>复制新加</a>".format(DJANGO_SERVER_YUMING,self.id))
        # return  "<a href='http://192.168.212.194:9002/testcase/{}/'>跳转</a>".format(self.id)

    go_to.short_description = u"复制新加"   #为go_to函数名个名字



class InputTapInputText(models.Model):
    """
    新增数据场景依赖的文本输入框模型
    """
    loginandcheck = models.ForeignKey(LoginAndCheck,default="", null=True, blank=True,
                                   verbose_name=u"依赖的登录场景",on_delete=models.PROTECT)

    newaddandcheck = models.ForeignKey(NewAddAndCheck,default="", null=True, blank=True,
                                   verbose_name=u"依赖的添加场景",on_delete=models.PROTECT)
    editandcheck = models.ForeignKey(EditAndCheck,default="", null=True, blank=True,
                                   verbose_name=u"依赖的修改场景",on_delete=models.PROTECT)

    input_ele_find = models.CharField(max_length=100, default="xpath",null=True, blank=True,
                                      verbose_name=u"输入框查找风格",
                                      help_text=u"元素查找风格：id、name、class_name、tag_name、"
                                                u"link_text、partial_link_text、css_selector、xpath")
    input_ele_find_value = models.CharField(max_length=1000, default="",null=True, blank=True,
                                                         verbose_name=u"输入框查找风格的确切值")
    is_auto_input = models.BooleanField(default=False, verbose_name=u"是否自动输入")
    auto_input_type = models.CharField(choices=(('1','数字'),('2','字母（小写）'),
                                                ('3','字母（大写）'), ('4', '特殊符号'),
                                                ('5','数字和字母（小写）'),('6','数字和字母（大写）'),
                                                ('7', '字母（大小写）'),
                                                ('8','数字和字母（大小写）'),
                                                ('9', '数字和字母和特殊符号'),
                                                ('10','数字和字母和特殊符号和空白字符'),('11','汉字'),
                                                ('12','手机号'),('13','身份证号')),
                                       null=True, blank=True,
                                       max_length=10,default='11',verbose_name="自动输入字符的类型")
    auto_input_long = models.CharField(max_length=100,default="300",null=True, blank=True,
                                          verbose_name="自动输入的字符的个数",help_text=u"字符的个数，请填写数字，"
                                                                   u"例如：1、2、3")

    input_text = models.CharField(max_length=300,default="",null=True, blank=True,
                                  verbose_name=u"输入框中要输入的内容")
    is_with_time = models.BooleanField(default=True,verbose_name=u"是否带时间串")

    is_click_clear_icon = models.BooleanField(default=False,verbose_name=u"是否点击清空图标")

    clear_icon_find = models.CharField(max_length=100, default="xpath",null=True, blank=True,
                                      verbose_name=u"清空图标查找风格",
                                      help_text=u"元素查找风格：id、name、class_name、tag_name、"
                                                u"link_text、partial_link_text、css_selector、xpath")
    clear_icon_find_value = models.CharField(max_length=1000, default="",null=True, blank=True,
                                                         verbose_name=u"清空图标查找风格的确切值")

    is_check = models.BooleanField(default=True,verbose_name=u"是否进行验证")
    # datetime.now记录实例化时间，datetime.now()记录模型创建时间,auto_now_add=True是指定在数据新增时, 自动写入时间
    add_time = models.DateTimeField(null=True, blank=True, auto_now_add=True,verbose_name=u"添加时间")
    # datetime.now记录实例化时间，datetime.now()记录模型创建时间，auto_now=True是无论新增还是更新数据, 此字段都会更新为当前时间
    update_time = models.DateTimeField(default=datetime.now, null=True, blank=True,verbose_name=u"更新时间")

    class Meta:
        verbose_name = u"文本输入框相关内容"
        verbose_name_plural = verbose_name

    def __str__(self):#重载函数
        return self.input_ele_find



class InputTapInputFile(models.Model):
    """
    新增数据场景依赖的文件输入框模型
    """
    newaddandcheck = models.ForeignKey(NewAddAndCheck,default="", null=True, blank=True,
                                   verbose_name=u"依赖的添加场景",on_delete=models.PROTECT)
    editandcheck = models.ForeignKey(EditAndCheck,default="", null=True, blank=True,
                                   verbose_name=u"依赖的修改场景",on_delete=models.PROTECT)

    input_ele_find = models.CharField(max_length=100, default="xpath",null=True, blank=True,
                                      verbose_name=u"输入框查找风格",
                                      help_text=u"元素查找风格：id、name、class_name、tag_name、"
                                                u"link_text、partial_link_text、css_selector、xpath")
    input_ele_find_value = models.CharField(max_length=1000, default="",null=True, blank=True,
                                                         verbose_name=u"输入框查找风格的确切值")
    input_file = models.CharField(max_length=300,default="",null=True, blank=True,
                                  verbose_name=u"输入框中要输入的文件路径",
                                  help_text = u"多个文件路径之间以半角逗号隔开,例如“D:\\timg.jpg,/root/timg.jpg”，会获取第一个有效路径")
    input_class_name = models.CharField(max_length=300,default="",null=True, blank=True,
                                        verbose_name=u"隐藏输入框的类名")
    # datetime.now记录实例化时间，datetime.now()记录模型创建时间,auto_now_add=True是指定在数据新增时, 自动写入时间
    add_time = models.DateTimeField(null=True, blank=True, auto_now_add=True,verbose_name=u"添加时间")
    # datetime.now记录实例化时间，datetime.now()记录模型创建时间，auto_now=True是无论新增还是更新数据, 此字段都会更新为当前时间
    update_time = models.DateTimeField(default=datetime.now, null=True, blank=True,verbose_name=u"更新时间")

    class Meta:
        verbose_name = u"文件输入框相关内容"
        verbose_name_plural = verbose_name

    def __str__(self):#重载函数
        return self.input_ele_find


class InputTapInputDateTime(models.Model):
    """
    新增数据场景依赖的时间输入框模型
    """
    newaddandcheck = models.ForeignKey(NewAddAndCheck,default="", null=True, blank=True,
                                   verbose_name=u"依赖的添加场景",on_delete=models.PROTECT)
    editandcheck = models.ForeignKey(EditAndCheck,default="", null=True, blank=True,
                                   verbose_name=u"依赖的修改场景",on_delete=models.PROTECT)

    input_ele_find = models.CharField(max_length=100, default="xpath",null=True, blank=True,
                                      verbose_name=u"时间输入框查找风格",
                                      help_text=u"元素查找风格：id、name、class_name、tag_name、"
                                                u"link_text、partial_link_text、css_selector、xpath")
    input_ele_find_value = models.CharField(max_length=1000, default="",null=True, blank=True,
                                                         verbose_name=u"时间输入框查找风格的确切值")

    date_ele_find = models.CharField(max_length=100, default="xpath",null=True, blank=True,
                                      verbose_name=u"日期元素查找风格",
                                      help_text=u"元素查找风格：id、name、class_name、tag_name、"
                                                u"link_text、partial_link_text、css_selector、xpath")
    date_ele_find_value = models.CharField(max_length=1000, default="",null=True, blank=True,
                                                         verbose_name=u"日期元素查找风格的确切值")

    last_month_ele_find = models.CharField(max_length=100, default="xpath",null=True, blank=True,
                                      verbose_name=u"上一月按钮查找风格",
                                      help_text=u"元素查找风格：id、name、class_name、tag_name、"
                                                u"link_text、partial_link_text、css_selector、xpath")
    last_month_ele_find_value = models.CharField(max_length=1000, default="",null=True, blank=True,
                                                         verbose_name=u"上一月按钮查找风格的确切值")
    click_last_month_counts = models.CharField(max_length=100, default="", null=True, blank=True,
                                           verbose_name=u"点击上一月按钮的次数",help_text=u"点击上一月按钮的次数，请填写数字，"
                                                        u"例如：1、2、3")

    next_month_ele_find = models.CharField(max_length=100, default="xpath",null=True, blank=True,
                                      verbose_name=u"下一月按钮查找风格",
                                      help_text=u"元素查找风格：id、name、class_name、tag_name、"
                                                u"link_text、partial_link_text、css_selector、xpath")
    next_month_ele_find_value = models.CharField(max_length=1000, default="",null=True, blank=True,
                                                         verbose_name=u"下一月按钮查找风格的确切值")

    click_next_month_counts = models.CharField(max_length=100, default="", null=True, blank=True,
                                           verbose_name=u"点击下一月按钮的次数",help_text=u"点击下一月按钮的次数，请填写数字，"
                                                        u"例如：1、2、3")

    last_year_ele_find = models.CharField(max_length=100, default="xpath", null=True, blank=True,
                                           verbose_name=u"上一年按钮查找风格",
                                           help_text=u"元素查找风格：id、name、class_name、tag_name、"
                                                     u"link_text、partial_link_text、css_selector、xpath")
    last_year_ele_find_value = models.CharField(max_length=1000, default="", null=True, blank=True,
                                                 verbose_name=u"上一年按钮查找风格的确切值")
    click_last_year_counts = models.CharField(max_length=100, default="", null=True, blank=True,
                                           verbose_name=u"点击上一年按钮的次数",help_text=u"点击上一年按钮的次数，请填写数字，"
                                                        u"例如：1、2、3")

    next_year_ele_find = models.CharField(max_length=100, default="xpath", null=True, blank=True,
                                           verbose_name=u"下一年按钮查找风格",
                                           help_text=u"元素查找风格：id、name、class_name、tag_name、"
                                                     u"link_text、partial_link_text、css_selector、xpath")
    next_year_ele_find_value = models.CharField(max_length=1000, default="", null=True, blank=True,
                                                 verbose_name=u"下一年按钮查找风格的确切值")
    click_next_year_counts = models.CharField(max_length=100, default="", null=True, blank=True,
                                           verbose_name=u"点击下一年按钮的次数",help_text=u"点击下一年按钮的次数，请填写数字，"
                                                        u"例如：1、2、3")

    # datetime.now记录实例化时间，datetime.now()记录模型创建时间,auto_now_add=True是指定在数据新增时, 自动写入时间
    add_time = models.DateTimeField(null=True, blank=True, auto_now_add=True,verbose_name=u"添加时间")
    # datetime.now记录实例化时间，datetime.now()记录模型创建时间，auto_now=True是无论新增还是更新数据, 此字段都会更新为当前时间
    update_time = models.DateTimeField(default=datetime.now, null=True, blank=True,verbose_name=u"更新时间")

    class Meta:
        verbose_name = u"时间输入框相关内容"
        verbose_name_plural = verbose_name

    def __str__(self):#重载函数
        return self.input_ele_find


class RadioAndReelectionLabel(models.Model):
    """
    新增数据场景依赖的单选项和复选项模型
    """
    newaddandcheck = models.ForeignKey(NewAddAndCheck,default="", null=True, blank=True,
                                   verbose_name=u"依赖的添加场景",on_delete=models.PROTECT)
    editandcheck = models.ForeignKey(EditAndCheck,default="", null=True, blank=True,
                                   verbose_name=u"依赖的修改场景",on_delete=models.PROTECT)

    label_ele_find = models.CharField(max_length=100, default="xpath",null=True, blank=True,
                                      verbose_name=u"选项标签查找风格",
                                      help_text=u"元素查找风格：id、name、class_name、tag_name、"
                                                u"link_text、partial_link_text、css_selector、xpath")
    label_ele_find_value = models.CharField(max_length=1000, default="",null=True, blank=True,
                                                         verbose_name=u"选项标签查找风格的确切值")

    is_check = models.BooleanField(default=True,verbose_name=u"是否选中")
    checked_add_attribute = models.CharField(max_length=100, default="",null=True, blank=True,
                                         verbose_name=u"元素被选中后新增的属性")
    checked_add_attribute_value = models.CharField(max_length=100, default="",null=True, blank=True,
                                         verbose_name=u"元素被选中后新增的属性的值")
    # datetime.now记录实例化时间，datetime.now()记录模型创建时间,auto_now_add=True是指定在数据新增时, 自动写入时间
    add_time = models.DateTimeField(null=True, blank=True, auto_now_add=True,verbose_name=u"添加时间")
    # datetime.now记录实例化时间，datetime.now()记录模型创建时间，auto_now=True是无论新增还是更新数据, 此字段都会更新为当前时间
    update_time = models.DateTimeField(default=datetime.now, null=True, blank=True,verbose_name=u"更新时间")

    class Meta:
        verbose_name = u"单选项和复选项相关内容"
        verbose_name_plural = verbose_name

    def __str__(self):#重载函数
        return self.label_ele_find


class SelectTapSelectOption(models.Model):
    """
    新增数据场景依赖的选项框模型
    """
    newaddandcheck = models.ForeignKey(NewAddAndCheck,default="", null=True, blank=True,
                                   verbose_name=u"依赖的添加场景",on_delete=models.PROTECT)
    editandcheck = models.ForeignKey(EditAndCheck,default="", null=True, blank=True,
                                   verbose_name=u"依赖的修改场景",on_delete=models.PROTECT)

    is_multiple_choices = models.BooleanField(default=False,verbose_name=u"是否多选")

    select_ele_find = models.CharField(max_length=100, default="xpath",null=True, blank=True,
                                       verbose_name=u"选项框的查找风格",
                                       help_text=u"元素查找风格：id、name、class_name、tag_name、"
                                                 u"link_text、partial_link_text、css_selector、xpath")
    select_ele_find_value = models.CharField(max_length=1000, default="",null=True, blank=True,
                                                         verbose_name=u"选项框查找风格的确切值")
    select_option_ele_find = models.CharField(max_length=100, default="xpath",null=True, blank=True,
                                              verbose_name=u"选项的查找风格",
                                              help_text=u"元素查找风格：id、name、class_name、tag_name、"
                                                        u"link_text、partial_link_text、css_selector、xpath")
    select_option_ele_find_value = models.CharField(max_length=1000, default="",null=True, blank=True,
                                                         verbose_name=u"选项查找风格的确切值")

    is_click_clear_icon = models.BooleanField(default=False,verbose_name=u"是否点击清空图标")

    clear_icon_find = models.CharField(max_length=100, default="xpath",null=True, blank=True,
                                      verbose_name=u"清空图标查找风格",
                                      help_text=u"元素查找风格：id、name、class_name、tag_name、"
                                                u"link_text、partial_link_text、css_selector、xpath")
    clear_icon_find_value = models.CharField(max_length=1000, default="",null=True, blank=True,
                                                         verbose_name=u"清空图标查找风格的确切值")

    # datetime.now记录实例化时间，datetime.now()记录模型创建时间,auto_now_add=True是指定在数据新增时, 自动写入时间
    add_time = models.DateTimeField(null=True, blank=True, auto_now_add=True,verbose_name=u"添加时间")
    # datetime.now记录实例化时间，datetime.now()记录模型创建时间，auto_now=True是无论新增还是更新数据, 此字段都会更新为当前时间
    update_time = models.DateTimeField(default=datetime.now, null=True, blank=True,verbose_name=u"更新时间")

    class Meta:
        verbose_name = u"选项框相关内容"
        verbose_name_plural = verbose_name

    def __str__(self):#重载函数
        return self.select_ele_find


class SelectTapSelectText(models.Model):
    """
    为选项框及选项文本内容创建的模型，目前没用处
    """
    newaddandcheck = models.ForeignKey(NewAddAndCheck,default="", null=True, blank=True,
                                   verbose_name=u"依赖的添加场景",on_delete=models.PROTECT)
    editandcheck = models.ForeignKey(EditAndCheck,default="", null=True, blank=True,
                                   verbose_name=u"依赖的修改场景",on_delete=models.PROTECT)

    select_ele_find = models.CharField(max_length=100, default="xpath",null=True, blank=True,
                                       verbose_name=u"选项框的查找风格",
                                       help_text=u"元素查找风格：id、name、class_name、tag_name、"
                                                 u"link_text、partial_link_text、css_selector、xpath")
    select_ele_find_value = models.CharField(max_length=1000, default="",null=True, blank=True,
                                                         verbose_name=u"选项框查找风格的确切值")
    select_option_text = models.CharField(max_length=300,default="",null=True, blank=True,
                                          verbose_name=u"选项的文本的内容")
    # datetime.now记录实例化时间，datetime.now()记录模型创建时间,auto_now_add=True是指定在数据新增时, 自动写入时间
    add_time = models.DateTimeField(null=True, blank=True, auto_now_add=True,verbose_name=u"添加时间")
    # datetime.now记录实例化时间，datetime.now()记录模型创建时间，auto_now=True是无论新增还是更新数据, 此字段都会更新为当前时间
    update_time = models.DateTimeField(default=datetime.now, null=True, blank=True,verbose_name=u"更新时间")

    class Meta:
        verbose_name = u"选项框及选项文本内容"
        verbose_name_plural = verbose_name

    def __str__(self):#重载函数
        return self.select_ele_find


class AssertTipText(models.Model):
    """
    新增数据场景依赖的验证元素模型
    """
    loginandcheck = models.ForeignKey(LoginAndCheck,default="", null=True, blank=True,
                                   verbose_name=u"依赖的登录场景",on_delete=models.PROTECT)

    newaddandcheck = models.ForeignKey(NewAddAndCheck,default="", null=True, blank=True,
                                   verbose_name=u"依赖的添加场景",on_delete=models.PROTECT)

    editandcheck = models.ForeignKey(EditAndCheck,default="", null=True, blank=True,
                                   verbose_name=u"依赖的修改场景",on_delete=models.PROTECT)

    tip_ele_find = models.CharField(max_length=100, default="xpath",null=True, blank=True,
                                      verbose_name=u"验证元素查找风格",
                                      help_text=u"元素查找风格：id、name、class_name、tag_name、"
                                                u"link_text、partial_link_text、css_selector、xpath")
    tip_ele_find_value = models.CharField(max_length=1000, default="",null=True, blank=True,
                                                         verbose_name=u"验证元素查找风格的确切值")
    tip_text = models.CharField(max_length=300,default="",null=True, blank=True,
                                  verbose_name=u"验证元素文本信息内容")
    # datetime.now记录实例化时间，datetime.now()记录模型创建时间,auto_now_add=True是指定在数据新增时, 自动写入时间
    add_time = models.DateTimeField(null=True, blank=True, auto_now_add=True,verbose_name=u"添加时间")
    # datetime.now记录实例化时间，datetime.now()记录模型创建时间，auto_now=True是无论新增还是更新数据, 此字段都会更新为当前时间
    update_time = models.DateTimeField(default=datetime.now, null=True, blank=True,verbose_name=u"更新时间")

    class Meta:
        verbose_name = u"验证元素相关内容"
        verbose_name_plural = verbose_name

    def __str__(self):#重载函数
        return self.tip_ele_find


class IframeBodyInputText(models.Model):
    """
    新增数据场景依赖的富文本输入框模型
    """
    newaddandcheck = models.ForeignKey(NewAddAndCheck,default="", null=True, blank=True,
                                   verbose_name=u"依赖的添加场景",on_delete=models.PROTECT)

    editandcheck = models.ForeignKey(EditAndCheck,default="", null=True, blank=True,
                                   verbose_name=u"依赖的修改场景",on_delete=models.PROTECT)

    iframe_ele_find = models.CharField(max_length=100, default="xpath",null=True, blank=True,
                                      verbose_name=u"iframe查找风格",
                                      help_text=u"元素查找风格：id、name、class_name、tag_name、"
                                                u"link_text、partial_link_text、css_selector、xpath")
    iframe_ele_find_value = models.CharField(max_length=1000, default="", null=True, blank=True,
                                            verbose_name=u"iframe查找风格的确切值")

    input_ele_find = models.CharField(max_length=100, default="xpath",null=True, blank=True,
                                      verbose_name=u"输入框查找风格",
                                      help_text=u"元素查找风格：id、name、class_name、tag_name、"
                                                u"link_text、partial_link_text、css_selector、xpath")
    input_ele_find_value = models.CharField(max_length=1000, default="",null=True, blank=True,
                                                         verbose_name=u"输入框查找风格的确切值")
    is_auto_input = models.BooleanField(default=False, verbose_name=u"是否自动输入")
    auto_input_type = models.CharField(choices=(('1','数字'),('2','字母（小写）'),
                                                ('3','字母（大写）'), ('4', '特殊符号'),
                                                ('5','数字和字母（小写）'),('6','数字和字母（大写）'),
                                                ('7', '字母（大小写）'),
                                                ('8','数字和字母（大小写）'),
                                                ('9', '数字和字母和特殊符号'),
                                                ('10','数字和字母和特殊符号和空白字符'),('11','汉字'),
                                                ('12','手机号'),('13','身份证号')),
                                       null=True, blank=True,
                                       max_length=10,default='11',verbose_name="自动输入字符的类型")
    auto_input_long = models.CharField(max_length=100,default="300",null=True, blank=True,
                                          verbose_name="自动输入的字符的个数",help_text=u"字符的个数，请填写数字，"
                                                                   u"例如：1、2、3")

    input_text = models.CharField(max_length=300,default="",null=True, blank=True,
                                  verbose_name=u"输入框中要输入的内容")
    is_with_time = models.BooleanField(default=True,verbose_name=u"是否带时间串")
    is_check = models.BooleanField(default=True,verbose_name=u"是否进行验证")
    # datetime.now记录实例化时间，datetime.now()记录模型创建时间,auto_now_add=True是指定在数据新增时, 自动写入时间
    add_time = models.DateTimeField(null=True, blank=True, auto_now_add=True,verbose_name=u"添加时间")
    # datetime.now记录实例化时间，datetime.now()记录模型创建时间，auto_now=True是无论新增还是更新数据, 此字段都会更新为当前时间
    update_time = models.DateTimeField(default=datetime.now, null=True, blank=True,verbose_name=u"更新时间")

    class Meta:
        verbose_name = u"富文本输入框相关内容"
        verbose_name_plural = verbose_name

    def __str__(self):#重载函数
        return self.input_ele_find


class SearchAndCheck(models.Model):#继承django的Model模块
    """
    查询场景
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
    depend_click_case = models.ForeignKey(ClickAndBack, default="", null=True, blank=True,
                                   verbose_name=u"依赖的点击场景的用例",on_delete=models.PROTECT)



    search_ele_find = models.CharField(max_length=100, default="xpath",null=True, blank=True,
                                        verbose_name=u"查询按钮查找风格",
                                        help_text=u"元素查找风格：id、name、class_name、tag_name、"
                                                  u"link_text、partial_link_text、css_selector、xpath")
    search_ele_find_value = models.CharField(max_length=1000, default="",null=True, blank=True,
                                                         verbose_name=u"查询按钮查找风格的确切值")
    is_with_date = models.BooleanField(default=True, verbose_name=u"是否查询到数据")
    result_table_ele_find = models.CharField(max_length=100, default="xpath",null=True, blank=True,
                                             verbose_name=u"结果表格查找风格",
                                             help_text=u"元素查找风格：id、name、class_name、tag_name、"
                                                       u"link_text、partial_link_text、css_selector、xpath")
    result_table_ele_find_value = models.CharField(max_length=1000, default="",null=True, blank=True,
                                                         verbose_name=u"结果表格查找风格的确切值")

    case_counts = models.IntegerField(default="1",verbose_name="循环次数",help_text=u"循环次数，请填写数字，"
                                                                   u"例如：1、2、3")
    write_user = models.ForeignKey(User,null=True, blank=True,verbose_name=u"添加人", on_delete=models.PROTECT)

    # datetime.now记录实例化时间，datetime.now()记录模型创建时间,auto_now_add=True是指定在数据新增时, 自动写入时间
    add_time = models.DateTimeField(null=True, blank=True, auto_now_add=True,verbose_name=u"添加时间")
    # datetime.now记录实例化时间，datetime.now()记录模型创建时间，auto_now=True是无论新增还是更新数据, 此字段都会更新为当前时间
    update_time = models.DateTimeField(default=datetime.now, null=True, blank=True,verbose_name=u"更新时间")

    class Meta:
        verbose_name = u"查询场景"
        verbose_name_plural = verbose_name

    def __str__(self):#重载函数
        return self.test_case_title

    def go_to(self):   #定义点击后跳转到某一个地方（可以加html代码）
        from django.utils.safestring import mark_safe   #调用mark_safe这个函数，django可以显示成一个文本，而不是html代码
        return mark_safe("<a href='{}/testdatas/searchandcheckcopy/{}/'>复制新加不带关联</a>".format(DJANGO_SERVER_YUMING,self.id))
        # return  "<a href='http://192.168.212.194:9002/testcase/{}/'>跳转</a>".format(self.id)

    go_to.short_description = u"复制新加不带关联"   #为go_to函数名个名字

    def go_to_with_relevance(self):   #定义点击后跳转到某一个地方（可以加html代码）
        from django.utils.safestring import mark_safe   #调用mark_safe这个函数，django可以显示成一个文本，而不是html代码
        return mark_safe("<a href='{}/testdatas/searchandcheckcopywithrelevance/{}/'>复制新加</a>".format(DJANGO_SERVER_YUMING,self.id))
        # return  "<a href='http://192.168.212.194:9002/testcase/{}/'>跳转</a>".format(self.id)

    go_to_with_relevance.short_description = u"复制新加"   #为go_to函数名个名字


class SearchInputTapInputText(models.Model):
    """
    查询场景依赖的文本输入框模型
    """
    searchandcheck = models.ForeignKey(SearchAndCheck,default="", null=True, blank=True,
                                   verbose_name=u"依赖的搜素场景",on_delete=models.PROTECT)

    input_ele_find = models.CharField(max_length=100, default="xpath",null=True, blank=True,
                                      verbose_name=u"输入框查找风格",
                                      help_text=u"元素查找风格：id、name、class_name、tag_name、"
                                                u"link_text、partial_link_text、css_selector、xpath")
    input_ele_find_value = models.CharField(max_length=1000, default="",null=True, blank=True,
                                                         verbose_name=u"输入框查找风格的确切值")
    input_text = models.CharField(max_length=300,default="",null=True, blank=True,
                                  verbose_name=u"输入框中要输入的内容")
    search_result_colnum = models.CharField(max_length=100, default="", null=True, blank=True,
                                           verbose_name=u"在搜索结果表格中对应的列数",
                                            help_text=u"在搜索结果表格中对应的列数，请填写数字，例如：1、2、3;"
                                                      u"如果是多列，列数之间以半角逗号隔开，例如：3,4")
    # datetime.now记录实例化时间，datetime.now()记录模型创建时间,auto_now_add=True是指定在数据新增时, 自动写入时间
    add_time = models.DateTimeField(null=True, blank=True, auto_now_add=True,verbose_name=u"添加时间")
    # datetime.now记录实例化时间，datetime.now()记录模型创建时间，auto_now=True是无论新增还是更新数据, 此字段都会更新为当前时间
    update_time = models.DateTimeField(default=datetime.now, null=True, blank=True,verbose_name=u"更新时间")

    class Meta:
        verbose_name = u"文本输入框相关内容"
        verbose_name_plural = verbose_name

    def __str__(self):#重载函数
        return self.input_ele_find_value


class SearchSelectTapSelectOption(models.Model):
    """
    查询场景依赖的选项框模型
    """
    searchandcheck = models.ForeignKey(SearchAndCheck,default="", null=True, blank=True,
                                   verbose_name=u"依赖的搜素场景",on_delete=models.PROTECT)
    select_ele_find = models.CharField(max_length=100, default="xpath",null=True, blank=True,
                                       verbose_name=u"选项框的查找风格",
                                       help_text=u"元素查找风格：id、name、class_name、tag_name、"
                                                 u"link_text、partial_link_text、css_selector、xpath")
    select_ele_find_value = models.CharField(max_length=1000, default="",null=True, blank=True,
                                                         verbose_name=u"选项框查找风格的确切值")
    select_option_ele_find = models.CharField(max_length=100, default="xpath",null=True, blank=True,
                                              verbose_name=u"选项的查找风格",
                                              help_text=u"元素查找风格：id、name、class_name、tag_name、"
                                                        u"link_text、partial_link_text、css_selector、xpath")
    select_option_ele_find_value = models.CharField(max_length=1000, default="",null=True, blank=True,
                                                         verbose_name=u"选项查找风格的确切值")
    search_result_colnum = models.CharField(max_length=100, default="", null=True, blank=True,
                                           verbose_name=u"在搜索结果表格中对应的列数",
                                            help_text=u"在搜索结果表格中对应的列数，请填写数字，例如：1、2、3...")
    # datetime.now记录实例化时间，datetime.now()记录模型创建时间,auto_now_add=True是指定在数据新增时, 自动写入时间
    add_time = models.DateTimeField(null=True, blank=True, auto_now_add=True,verbose_name=u"添加时间")
    # datetime.now记录实例化时间，datetime.now()记录模型创建时间，auto_now=True是无论新增还是更新数据, 此字段都会更新为当前时间
    update_time = models.DateTimeField(default=datetime.now, null=True, blank=True,verbose_name=u"更新时间")

    class Meta:
        verbose_name = u"选项框相关内容"
        verbose_name_plural = verbose_name

    def __str__(self):#重载函数
        return self.select_ele_find_value



class DeleteAndCheck(models.Model):#继承django的Model模块
    """
    删除数据场景
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


    depend_click_case = models.ForeignKey(ClickAndBack, default="", null=True, blank=True,
                                   verbose_name=u"依赖的点击场景的用例",on_delete=models.PROTECT)

    delete_ele_find = models.CharField(max_length=100, default="xpath",null=True, blank=True,
                                        verbose_name=u"被删除元素查找风格",
                                        help_text=u"元素查找风格：id、name、class_name、tag_name、"
                                                  u"link_text、partial_link_text、css_selector、xpath")
    delete_ele_find_value = models.CharField(max_length=1000, default="",null=True, blank=True,
                                                         verbose_name=u"被删除元素查找风格的确切值")

    delete_button_find = models.CharField(max_length=100, default="xpath",null=True, blank=True,
                                        verbose_name=u"删除按钮查找风格",
                                        help_text=u"元素查找风格：id、name、class_name、tag_name、"
                                                  u"link_text、partial_link_text、css_selector、xpath")
    delete_button_find_value = models.CharField(max_length=1000, default="",null=True, blank=True,
                                                         verbose_name=u"删除按钮查找风格的确切值")

    confirm_ele_find = models.CharField(max_length=100, default="xpath",null=True, blank=True,
                                        verbose_name=u"删除弹框确定按钮查找风格",
                                        help_text=u"元素查找风格：id、name、class_name、tag_name、"
                                                  u"link_text、partial_link_text、css_selector、xpath")
    confirm_ele_find_value = models.CharField(max_length=1000, default="",null=True, blank=True,
                                                         verbose_name=u"删除弹框确定按钮查找风格的确切值")
    click_confirm_delay_time = models.CharField(max_length=100, default="3", null=True, blank=True,
                                                verbose_name=u"点击确定按钮后的延时时长（单位秒）",
                                                help_text=u"点击确定按钮后的延时时长（单位秒），请填写数字，例如：1、2、3")

    is_click_cancel = models.BooleanField(default=False,verbose_name=u"是否点击取消按钮")
    cancel_ele_find = models.CharField(max_length=100, default="xpath", null=True, blank=True,
                                       verbose_name=u"删除弹框取消按钮查找风格",
                                       help_text=u"元素查找风格：id、name、class_name、tag_name、"
                                                 u"link_text、partial_link_text、css_selector、xpath")
    cancel_ele_find_value = models.CharField(max_length=1000, default="",null=True, blank=True,
                                                         verbose_name=u"删除弹框取消按钮查找风格的确切值")

    is_submit_success = models.BooleanField(default=True,verbose_name=u"是否删除成功")

    popup_ele_find = models.CharField(max_length=100, default="xpath",null=True, blank=True,
                                      verbose_name=u"删除成功弹框中的某个元素查找风格",
                                      help_text=u"元素查找风格：id、name、class_name、tag_name、"
                                                u"link_text、partial_link_text、css_selector、xpath")
    popup_ele_find_value = models.CharField(max_length=1000, default="",null=True, blank=True,
                                                         verbose_name=u"删除成功弹框中的某个元素查找风格的确切值")

    popup_text = models.CharField(max_length=300,default="",null=True, blank=True,
                                  verbose_name=u"删除成功弹框中的某个元素文本信息内容")


    is_signel_page = models.BooleanField(default=True, verbose_name=u"是否单页面")

    page_number_xpath = models.CharField(max_length=1000, default="",null=True, blank=True,
                                                         verbose_name=u"页数层xpath路径值")

    result_table_ele_find = models.CharField(max_length=100, default="xpath",null=True, blank=True,
                                             verbose_name=u"结果表格查找风格",
                                             help_text=u"元素查找风格：id、name、class_name、tag_name、"
                                                       u"link_text、partial_link_text、css_selector、xpath")
    result_table_ele_find_value = models.CharField(max_length=1000, default="",null=True, blank=True,
                                                         verbose_name=u"结果表格查找风格的确切值")
    table_colnum_counts = models.CharField(max_length=100, default="", null=True, blank=True,
                                           verbose_name=u"结果表格总列数",help_text=u"结果表格总列数，请填写数字，"
                                                        u"例如：1、2、3")
    case_counts = models.IntegerField(default="1",verbose_name="循环次数",help_text=u"循环次数，请填写数字，"
                                                                   u"例如：1、2、3")
    write_user = models.ForeignKey(User,null=True, blank=True,verbose_name=u"添加人", on_delete=models.PROTECT)

    # datetime.now记录实例化时间，datetime.now()记录模型创建时间,auto_now_add=True是指定在数据新增时, 自动写入时间
    add_time = models.DateTimeField(null=True, blank=True, auto_now_add=True,verbose_name=u"添加时间")
    # datetime.now记录实例化时间，datetime.now()记录模型创建时间，auto_now=True是无论新增还是更新数据, 此字段都会更新为当前时间
    update_time = models.DateTimeField(default=datetime.now, null=True, blank=True,verbose_name=u"更新时间")

    class Meta:
        verbose_name = u"删除场景"
        verbose_name_plural = verbose_name

    def __str__(self):#重载函数
        return self.test_case_title

    def go_to(self):   #定义点击后跳转到某一个地方（可以加html代码）
        from django.utils.safestring import mark_safe   #调用mark_safe这个函数，django可以显示成一个文本，而不是html代码
        return mark_safe("<a href='{}/testdatas/deleteandcheckcopy/{}/'>复制新加</a>".format(DJANGO_SERVER_YUMING,self.id))
        # return  "<a href='http://192.168.212.194:9002/testcase/{}/'>跳转</a>".format(self.id)

    go_to.short_description = u"复制新加"   #为go_to函数名个名字












