from django.db import models
from datetime import datetime
from wanwenyc.settings import DJANGO_SERVER_YUMING
from django.contrib.auth import  get_user_model  #导入get_user_model
from testupdatadb.models import UpdateDbData

#第三个就是我们自己创建的包
User = get_user_model()  #get_user_model() 函数直接返回User类，找的是settings.AUTH_USER_MODEL变量的值

#类别
class SpiderGenre(models.Model):
    genre =models.CharField(max_length=100, default="",null=True, blank=True, verbose_name=u"类别")
    genre_url = models.CharField(max_length=1500, default="", null=True, blank=True,verbose_name=u"类别外部链接")
    write_user = models.ForeignKey(User, null=True, blank=True, verbose_name=u"用户名", on_delete=models.PROTECT)
    add_time = models.DateTimeField(null=True, blank=True,auto_now_add=True,
                                    verbose_name=u"添加时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间,auto_now_add=True是指定在数据新增时, 自动写入时间
    update_time = models.DateTimeField(default=datetime.now, null=True, blank=True,
                                    verbose_name=u"更新时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间，auto_now=True是无论新增还是更新数据, 此字段都会更新为当前时间

    class Meta:
        verbose_name = u"类别"
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.genre

#演员
class SpiderStar(models.Model):
    star =models.CharField(max_length=100, default="",null=True, blank=True, verbose_name=u"演员")
    star_photo = models.CharField(max_length=1500, default="", null=True, blank=True,verbose_name=u"演员头像")
    img_height = models.CharField(max_length=100, default=75, null=True, blank=True, verbose_name=u"封面图高度")
    img_width = models.CharField(max_length=100, default=75, null=True, blank=True, verbose_name=u"封面图宽度")
    #上传图像路径，如果以/开头，表示在根目录下的文件夹下，如/update,表示在根目录（即项目目录下wanwenys）下的update文件夹
    #如果不以/开头，表示相对路径是在django配置的media路径下,如update,表示在配置的media目录（即项目目录下wanwenys的文件夹media文件夹下的）下的update文件夹
    #此处为空，表示存在项目目录下wanwenys的文件夹media文件夹下
    back_start_photo = models.ImageField(upload_to="", null=True, blank=True, verbose_name=u"补传演员头像",
                                             height_field='img_height', width_field='img_width', max_length=2000)

    star_url = models.CharField(max_length=1500, default="", null=True, blank=True,verbose_name=u"演员外部链接")
    write_user = models.ForeignKey(User, null=True, blank=True, verbose_name=u"用户名", on_delete=models.PROTECT)
    add_time = models.DateTimeField(null=True, blank=True,auto_now_add=True,
                                    verbose_name=u"添加时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间,auto_now_add=True是指定在数据新增时, 自动写入时间
    update_time = models.DateTimeField(default=datetime.now, null=True, blank=True,
                                    verbose_name=u"更新时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间，auto_now=True是无论新增还是更新数据, 此字段都会更新为当前时间

    class Meta:
        verbose_name = u"演员"
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.star

#发行商
class SpiderLabel(models.Model):
    label = models.CharField(max_length=100, default="", null=True, blank=True, verbose_name=u"发行商")
    label_url = models.CharField(max_length=1500, default="", null=True, blank=True,verbose_name=u"发行商外部链接")
    write_user = models.ForeignKey(User, null=True, blank=True, verbose_name=u"用户名", on_delete=models.PROTECT)
    add_time = models.DateTimeField(null=True, blank=True,auto_now_add=True,
                                    verbose_name=u"添加时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间,auto_now_add=True是指定在数据新增时, 自动写入时间
    update_time = models.DateTimeField(default=datetime.now, null=True, blank=True,
                                    verbose_name=u"更新时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间，auto_now=True是无论新增还是更新数据, 此字段都会更新为当前时间

    class Meta:
        verbose_name = u"发行商"
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.label

#制作商
class SpiderStudio(models.Model):
    studio = models.CharField(max_length=100, default="", null=True, blank=True, verbose_name=u"制作商")
    studio_url = models.CharField(max_length=1500, default="", null=True, blank=True,verbose_name=u"制作商外部链接")
    write_user = models.ForeignKey(User, null=True, blank=True, verbose_name=u"用户名", on_delete=models.PROTECT)
    add_time = models.DateTimeField(null=True, blank=True,auto_now_add=True,
                                    verbose_name=u"添加时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间,auto_now_add=True是指定在数据新增时, 自动写入时间
    update_time = models.DateTimeField(default=datetime.now, null=True, blank=True,
                                    verbose_name=u"更新时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间，auto_now=True是无论新增还是更新数据, 此字段都会更新为当前时间

    class Meta:
        verbose_name = u"制作商"
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.studio

#导演
class SpiderDirector(models.Model):
    director = models.CharField(max_length=100, default="", null=True, blank=True, verbose_name=u"导演")
    director_url = models.CharField(max_length=1500, default="", null=True, blank=True,verbose_name=u"制作商外部链接")
    write_user = models.ForeignKey(User, null=True, blank=True, verbose_name=u"用户名", on_delete=models.PROTECT)
    add_time = models.DateTimeField(null=True, blank=True,auto_now_add=True,
                                    verbose_name=u"添加时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间,auto_now_add=True是指定在数据新增时, 自动写入时间
    update_time = models.DateTimeField(default=datetime.now, null=True, blank=True,
                                    verbose_name=u"更新时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间，auto_now=True是无论新增还是更新数据, 此字段都会更新为当前时间

    class Meta:
        verbose_name = u"导演"
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.director


#系列
class SpiderSeries(models.Model):
    series = models.CharField(max_length=100, default="", null=True, blank=True, verbose_name=u"系列")
    series_url = models.CharField(max_length=1500, default="", null=True, blank=True,verbose_name=u"系列外部链接")
    write_user = models.ForeignKey(User, null=True, blank=True, verbose_name=u"用户名", on_delete=models.PROTECT)
    add_time = models.DateTimeField(null=True, blank=True,auto_now_add=True,
                                    verbose_name=u"添加时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间,auto_now_add=True是指定在数据新增时, 自动写入时间
    update_time = models.DateTimeField(default=datetime.now, null=True, blank=True,
                                    verbose_name=u"更新时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间，auto_now=True是无论新增还是更新数据, 此字段都会更新为当前时间

    class Meta:
        verbose_name = u"系列"
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.series

# 爬取数据
class SpiderData(models.Model):
    splider_url = models.CharField(max_length=1500, default="",null=True, blank=True,verbose_name=u"爬取数据URL")  #unique=True,表示设置此字段为主键，唯一
    splider_title = models.CharField(max_length=1000, default="爬取数据",null=True, blank=True, verbose_name=u"数据标题")
    img_height = models.CharField(max_length=100, default=75,null=True, blank=True, verbose_name=u"封面图高度")
    img_width = models.CharField(max_length=100, default=75, null=True, blank=True,verbose_name=u"封面图宽度")
    back_front_cover_img = models.ImageField(upload_to="" , null=True, blank=True,verbose_name=u"补传封面图片", height_field='img_height',width_field='img_width',max_length=2000)
    front_cover_img = models.CharField(max_length=1500, null=True, blank=True,verbose_name=u"封面图片")
    prenum = models.CharField(max_length=100, default="", null=True, blank=True, verbose_name=u"编号")
    long_time = models.CharField(max_length=100, default="", null=True, blank=True, verbose_name=u"时长（分钟）")
    is_love = models.BooleanField(default=False,verbose_name=u"喜爱")
    is_check = models.BooleanField(default=False,verbose_name=u"检查封面")

    #对于ManyToManyField，没有null参数，如果加上会报警告如：spiderdata.SpiderData.genre: (fields.W340) null has no effect on ManyToManyField.
    genre = models.ManyToManyField(SpiderGenre,default="", blank=True,verbose_name=u"类别")
    star = models.ManyToManyField(SpiderStar,default="",blank=True,verbose_name=u"演员")
    label = models.ManyToManyField(SpiderLabel,default="",blank=True,verbose_name=u"发行商")
    studio = models.ManyToManyField(SpiderStudio,default="",blank=True,verbose_name=u"制作商")
    director = models.ManyToManyField(SpiderDirector,default="",blank=True,verbose_name=u"导演")
    series = models.ManyToManyField(SpiderSeries,default="",blank=True,verbose_name=u"系列")

    write_user = models.ForeignKey(User, null=True, blank=True, verbose_name=u"用户名", on_delete=models.PROTECT)
    add_time = models.DateTimeField(null=True, blank=True,auto_now_add=True,
                                    verbose_name=u"添加时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间,auto_now_add=True是指定在数据新增时, 自动写入时间
    update_time = models.DateTimeField(default=datetime.now, null=True, blank=True,
                                    verbose_name=u"更新时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间，auto_now=True是无论新增还是更新数据, 此字段都会更新为当前时间

    def image_data(self):   #定义点击后跳转到某一个地方（可以加html代码）
        from django.utils.safestring import mark_safe   #调用mark_safe这个函数，django可以显示成一个文本，而不是html代码
        return mark_safe("<a href='{}'> <img src='{}' style='width:75px;height:75px;'/></a>".format(self.front_cover_img,self.front_cover_img))
        # return  "<a href='http://192.168.212.194:9002/testcase/{}/'>跳转</a>".format(self.id)

    image_data.short_description = u"封面图片"   #为go_to函数名个名字

    def back_image_data(self):   #定义点击后跳转到某一个地方（可以加html代码）
        from django.utils.safestring import mark_safe   #调用mark_safe这个函数，django可以显示成一个文本，而不是html代码
        return mark_safe("<a href='{}'><span>{}<span></a><br/><a href='{}/media/{}'> <img src='{}/media/{}' style='width:75px;height:75px;'/></a>".
                         format(self.splider_url,self.prenum,DJANGO_SERVER_YUMING,self.back_front_cover_img,DJANGO_SERVER_YUMING,self.back_front_cover_img))
        # return  "<a href='http://192.168.212.194:9002/testcase/{}/'>跳转</a>".format(self.id)

    back_image_data.short_description = u"补传封面图片"   #为go_to函数名个名字

    def video_link(self):   #定义点击后跳转到某一个地方（可以加html代码）
        from django.utils.safestring import mark_safe   #调用mark_safe这个函数，django可以显示成一个文本，而不是html代码
        return mark_safe("<a href='{}'>{}</a>".format(self.video,self.video))
        # return  "<a href='http://192.168.212.194:9002/testcase/{}/'>跳转</a>".format(self.id)

    video_link.short_description = u"视频地址连接"   #为go_to函数名个名字

    def down_load_link(self):   #定义点击后跳转到某一个地方（可以加html代码）
        from django.utils.safestring import mark_safe   #调用mark_safe这个函数，django可以显示成一个文本，而不是html代码
        html_all = ""
        down_load_list = self.spiderdownload_set.all()
        for down_load in down_load_list:
            html_one = "<a href='{}'>{}</a><br/>".format(down_load.down_load,down_load.down_load)
            html_all = "%s%s"%(html_all,html_one)
        return mark_safe(html_all)
        # return  "<a href='http://192.168.212.194:9002/testcase/{}/'>跳转</a>".format(self.id)

    down_load_link.short_description = u"下载地址连接"   #为go_to函数名个名字

    class Meta:
        verbose_name = u"爬取数据查询"
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.splider_title



#下载链接，关联作品
class SpiderDownLoad(models.Model):
    spiderdata = models.ForeignKey(SpiderData,null=True, blank=True, verbose_name=u"作品", on_delete=models.PROTECT)
    down_load = models.CharField(max_length=1500, default="", null=True, blank=True,verbose_name=u"下载连接")
    write_user = models.ForeignKey(User, null=True, blank=True, verbose_name=u"用户名", on_delete=models.PROTECT)
    add_time = models.DateTimeField(null=True, blank=True,auto_now_add=True,
                                    verbose_name=u"添加时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间,auto_now_add=True是指定在数据新增时, 自动写入时间
    update_time = models.DateTimeField(default=datetime.now, null=True, blank=True,
                                    verbose_name=u"更新时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间，auto_now=True是无论新增还是更新数据, 此字段都会更新为当前时间

    class Meta:
        verbose_name = u"下载链接"
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.down_load

#视频链接，关联作品
class SpiderVideo(models.Model):
    spiderdata = models.ForeignKey(SpiderData,null=True, blank=True, verbose_name=u"作品", on_delete=models.PROTECT)
    video = models.CharField(max_length=100, default="",null=True, blank=True, verbose_name=u"视频连接")
    write_user = models.ForeignKey(User, null=True, blank=True, verbose_name=u"用户名", on_delete=models.PROTECT)
    add_time = models.DateTimeField(null=True, blank=True,auto_now_add=True,
                                    verbose_name=u"添加时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间,auto_now_add=True是指定在数据新增时, 自动写入时间
    update_time = models.DateTimeField(default=datetime.now, null=True, blank=True,
                                    verbose_name=u"更新时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间，auto_now=True是无论新增还是更新数据, 此字段都会更新为当前时间

    class Meta:
        verbose_name = u"视频链接"
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.video