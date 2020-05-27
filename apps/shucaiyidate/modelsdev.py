from django.db import models
from datetime import datetime
from wanwenyc.settings import DJANGO_SERVER_YUMING
from django.contrib.auth import  get_user_model  #导入get_user_model
from testupdatadb.models import UpdateDbData

#第三个就是我们自己创建的包
User = get_user_model()  #get_user_model() 函数直接返回User类，找的是settings.AUTH_USER_MODEL变量的值


class TagContent(models.Model):
    config_project = models.CharField(max_length=100, default="", null=True, blank=True, verbose_name=u"项目名称")
    tag_level = models.CharField(max_length=100, default="", null=True, blank=True, verbose_name=u"节点层数",
                                 help_text="节点层数，根目录层数为1，根目录下层数为2，依次往下为3、4、5等等")
    tag_name = models.CharField(max_length=100, default="", null=True, blank=True, verbose_name=u"节点名字")
    is_root = models.BooleanField(default=False, verbose_name=u"是否根节点")
    tag_text = models.CharField(max_length=100, default="", null=True, blank=True, verbose_name=u"节点文本内容")
    tag_father = models.ForeignKey('self', null=True, blank=True, verbose_name=u"依赖的父节点", on_delete=models.PROTECT)

    write_user = models.ForeignKey(User, null=True, blank=True, verbose_name=u"用户名", on_delete=models.PROTECT)
    add_time = models.DateTimeField(null=True, blank=True,auto_now_add=True,
                                    verbose_name=u"添加时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间,auto_now_add=True是指定在数据新增时, 自动写入时间
    update_time = models.DateTimeField(default=datetime.now, null=True, blank=True,
                                    verbose_name=u"更新时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间，auto_now=True是无论新增还是更新数据, 此字段都会更新为当前时间

    class Meta:
        verbose_name = u"节点配置"
        verbose_name_plural=verbose_name

    def __str__(self):
        return "{}-【{}】-{}-{}".format(self.id,self.config_project,self.tag_level,self.tag_name)

    def go_to(self):   #定义点击后跳转到某一个地方（可以加html代码）
        from django.utils.safestring import mark_safe   #调用mark_safe这个函数，django可以显示成一个文本，而不是html代码
        return mark_safe("<a href='{}/shucaiyidate/tagcontent/{}/'>复制新加</a>".format(DJANGO_SERVER_YUMING,self.id))
        # return  "<a href='http://192.168.212.194:9002/testcase/{}/'>跳转</a>".format(self.id)

    go_to.short_description = u"复制新加"   #为go_to函数名个名字

    def node_first_attrib(self):   #定义点击后跳转到某一个地方（可以加html代码）
        from django.utils.safestring import mark_safe   #调用mark_safe这个函数，django可以显示成一个文本，而不是html代码
        html_all = ""
        node_attrib_all = self.tagattrib_set.all().order_by('id')

        for node_attrib_one in node_attrib_all:
            html_one = "<span>{}：{}</span></br>".format(node_attrib_one.tag_value_name,node_attrib_one.tag_value_text)
            html_all = "%s%s" % (html_all, html_one)
            # break   #循环一次
        return mark_safe(html_all)

    node_first_attrib.short_description = u"节点属性及其值"  # 为go_to函数名个名字


class TagAttrib(models.Model):
    tagcontent = models.ForeignKey(TagContent,default="", null=True, blank=True,
                                   verbose_name=u"依赖的节点",on_delete=models.PROTECT)
    tag_value_name = models.CharField(max_length=100, default="", null=True, blank=True, verbose_name=u"节点属性名字")

    tag_value_text = models.CharField(max_length=100, default="", null=True, blank=True, verbose_name=u"节点属性值")

    write_user = models.ForeignKey(User, null=True, blank=True, verbose_name=u"用户名", on_delete=models.PROTECT)
    add_time = models.DateTimeField(null=True, blank=True,auto_now_add=True,
                                    verbose_name=u"添加时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间,auto_now_add=True是指定在数据新增时, 自动写入时间
    update_time = models.DateTimeField(default=datetime.now, null=True, blank=True,
                                    verbose_name=u"更新时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间，auto_now=True是无论新增还是更新数据, 此字段都会更新为当前时间

    class Meta:
        verbose_name = u"节点属性"
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.tag_value_name


