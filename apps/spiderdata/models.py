from django.db import models
from datetime import datetime
from wanwenyc.settings import DJANGO_SERVER_YUMING
from django.contrib.auth import  get_user_model  #导入get_user_model
from testupdatadb.models import UpdateDbData

#第三个就是我们自己创建的包
User = get_user_model()  #get_user_model() 函数直接返回User类，找的是settings.AUTH_USER_MODEL变量的值

# Create your models here.
class SpiderDate(models.Model):
    splider_title = models.CharField(max_length=100, default="爬取数据",null=True, blank=True, verbose_name=u"数据标题")
    img_height = models.CharField(max_length=100, default=75, verbose_name=u"封面图高度")
    img_width = models.CharField(max_length=100, default=75, verbose_name=u"封面图宽度")
    front_cover_img = models.ImageField(upload_to="report/%Y%m/screenshots/" , null=True, blank=True,verbose_name=u"封面图片", height_field='img_height',width_field='img_width')
    video = models.CharField(max_length=100, default="",null=True, blank=True, verbose_name=u"视频连接")
    down_load = models.CharField(max_length=1500, default="", null=True, blank=True,verbose_name=u"下载连接")


    write_user = models.ForeignKey(User, null=True, blank=True, verbose_name=u"用户名", on_delete=models.PROTECT)
    add_time = models.DateTimeField(null=True, blank=True,auto_now_add=True,
                                    verbose_name=u"添加时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间,auto_now_add=True是指定在数据新增时, 自动写入时间
    update_time = models.DateTimeField(default=datetime.now, null=True, blank=True,
                                    verbose_name=u"更新时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间，auto_now=True是无论新增还是更新数据, 此字段都会更新为当前时间

    def image_data(self):   #定义点击后跳转到某一个地方（可以加html代码）
        from django.utils.safestring import mark_safe   #调用mark_safe这个函数，django可以显示成一个文本，而不是html代码
        return mark_safe("<a href='{}'> <img src='{}' style='width:75px;height:75px;'/></a>".format(self.front_cover_img.url,self.front_cover_img.url))
        # return  "<a href='http://192.168.212.194:9002/testcase/{}/'>跳转</a>".format(self.id)

    image_data.short_description = u"封面图片"   #为go_to函数名个名字

    def video_link(self):   #定义点击后跳转到某一个地方（可以加html代码）
        from django.utils.safestring import mark_safe   #调用mark_safe这个函数，django可以显示成一个文本，而不是html代码
        return mark_safe("<a href='{}'>{}</a>".format(self.video,self.video))
        # return  "<a href='http://192.168.212.194:9002/testcase/{}/'>跳转</a>".format(self.id)

    video_link.short_description = u"视频地址连接"   #为go_to函数名个名字

    def down_load_link(self):   #定义点击后跳转到某一个地方（可以加html代码）
        from django.utils.safestring import mark_safe   #调用mark_safe这个函数，django可以显示成一个文本，而不是html代码
        return mark_safe("<a href='{}'>{}</a>".format(self.down_load,self.down_load))
        # return  "<a href='http://192.168.212.194:9002/testcase/{}/'>跳转</a>".format(self.id)

    down_load_link.short_description = u"下载地址连接"   #为go_to函数名个名字

    class Meta:
        verbose_name = u"爬取数据查询"
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.splider_title