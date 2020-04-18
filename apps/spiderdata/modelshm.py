from django.db import models
from datetime import datetime
from wanwenyc.settings import DJANGO_SERVER_YUMING
from django.contrib.auth import  get_user_model  #导入get_user_model
from testupdatadb.models import UpdateDbData

#第三个就是我们自己创建的包
User = get_user_model()  #get_user_model() 函数直接返回User类，找的是settings.AUTH_USER_MODEL变量的值


#地区
class SpiderHMArea(models.Model):
    hm_area = models.CharField(max_length=100, default="", null=True, blank=True, verbose_name=u"地区")
    hm_area_url = models.CharField(max_length=1500, default="", null=True, blank=True,verbose_name=u"地区外部链接")
    write_user = models.ForeignKey(User, null=True, blank=True, verbose_name=u"用户名", on_delete=models.PROTECT)
    add_time = models.DateTimeField(null=True, blank=True,auto_now_add=True,
                                    verbose_name=u"添加时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间,auto_now_add=True是指定在数据新增时, 自动写入时间
    update_time = models.DateTimeField(default=datetime.now, null=True, blank=True,
                                    verbose_name=u"更新时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间，auto_now=True是无论新增还是更新数据, 此字段都会更新为当前时间

    class Meta:
        verbose_name = u"地区"
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.hm_area

#类型
class SpiderHMTag(models.Model):
    hm_tag = models.CharField(max_length=100, default="", null=True, blank=True, verbose_name=u"类型")
    hm_tag_url = models.CharField(max_length=1500, default="", null=True, blank=True,verbose_name=u"类型外部链接")
    write_user = models.ForeignKey(User, null=True, blank=True, verbose_name=u"用户名", on_delete=models.PROTECT)
    add_time = models.DateTimeField(null=True, blank=True,auto_now_add=True,
                                    verbose_name=u"添加时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间,auto_now_add=True是指定在数据新增时, 自动写入时间
    update_time = models.DateTimeField(default=datetime.now, null=True, blank=True,
                                    verbose_name=u"更新时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间，auto_now=True是无论新增还是更新数据, 此字段都会更新为当前时间

    class Meta:
        verbose_name = u"类型"
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.hm_tag

#书名
class SpiderHMBook(models.Model):
    splider_url = models.CharField(max_length=1500, default="",null=True, blank=True,verbose_name=u"爬取数据URL")  #unique=True,表示设置此字段为主键，唯一
    splider_title = models.CharField(max_length=1000, default="爬取漫画数据",null=True, blank=True, verbose_name=u"数据标题")
    img_height = models.CharField(max_length=100, default=75,null=True, blank=True, verbose_name=u"封面图高度")
    img_width = models.CharField(max_length=100, default=75, null=True, blank=True,verbose_name=u"封面图宽度")
    front_cover_img = models.ImageField(upload_to="hanman/fengmian/" , null=True, blank=True,verbose_name=u"封面图片", height_field='img_height',width_field='img_width',max_length=2000)

    chapter_count = models.CharField(max_length=100, default="", null=True, blank=True, verbose_name=u"章节数")

    is_love = models.BooleanField(default=False,verbose_name=u"喜爱")
    is_check = models.BooleanField(default=False,verbose_name=u"检查封面")

    #对于ManyToManyField，没有null参数，如果加上会报警告如：spiderdata.SpiderData.genre: (fields.W340) null has no effect on ManyToManyField.
    hm_area = models.ManyToManyField(SpiderHMArea,default="", blank=True,verbose_name=u"地区")
    hm_tag = models.ManyToManyField(SpiderHMTag,default="",blank=True,verbose_name=u"类型")

    write_user = models.ForeignKey(User, null=True, blank=True, verbose_name=u"用户名", on_delete=models.PROTECT)
    add_time = models.DateTimeField(null=True, blank=True,auto_now_add=True,
                                    verbose_name=u"添加时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间,auto_now_add=True是指定在数据新增时, 自动写入时间
    update_time = models.DateTimeField(default=datetime.now, null=True, blank=True,
                                    verbose_name=u"更新时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间，auto_now=True是无论新增还是更新数据, 此字段都会更新为当前时间

    def front_cover_img_data(self):   #定义点击后跳转到某一个地方（可以加html代码）
        from django.utils.safestring import mark_safe   #调用mark_safe这个函数，django可以显示成一个文本，而不是html代码
        return mark_safe("<a href='{}'><span>{}<span></a><br/><a href='{}/media/{}'> <img src='{}/media/{}' style='width:75px;height:75px;'/></a>".
                         format(self.splider_url,self.chapter_count,DJANGO_SERVER_YUMING,self.front_cover_img,DJANGO_SERVER_YUMING,self.front_cover_img))
        # return  "<a href='http://192.168.212.194:9002/testcase/{}/'>跳转</a>".format(self.id)

    front_cover_img_data.short_description = u"封面图片"   #为go_to函数名个名字

    def all_chapter(self):
        from django.utils.safestring import mark_safe  # 调用mark_safe这个函数，django可以显示成一个文本，而不是html代码
        html_all = ""
        chapter_list = self.spiderhmchapterdata_set.all().order_by("chapter_num")
        for chapter_one in  chapter_list:
            html_chapter_one = "<span>{}</span><br/>".format(chapter_one.splider_title)
            html_all = "%s%s" % (html_all, html_chapter_one)
            chapter_image_list = chapter_one.spiderhmchapterimage_set.all().order_by("chapter_image_num")
            for chapter_image_one in chapter_image_list:
                html_chapter_image_one = "<a href='{}/media/{}'> <img src='{}/media/{}' style='width:75px;height:75px;'/></a><br/>".format(
                    DJANGO_SERVER_YUMING,chapter_image_one.content_img, DJANGO_SERVER_YUMING,chapter_image_one.content_img
                )
                html_all = "%s%s" % (html_all, html_chapter_image_one)

        return mark_safe(html_all)

    all_chapter.short_description = u"已经存在章节"  # 为go_to函数名个名字

    class Meta:
        verbose_name = u"爬取的漫画书"
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.splider_title


# 爬取漫画数据
class SpiderHMChapterData(models.Model):
    spiderhmbook = models.ForeignKey(SpiderHMBook,null=True, blank=True, verbose_name=u"书目", on_delete=models.PROTECT)
    splider_url = models.CharField(max_length=1500, default="",null=True, blank=True,verbose_name=u"爬取数据URL")  #unique=True,表示设置此字段为主键，唯一
    splider_title = models.CharField(max_length=1000, default="爬取漫画数据",null=True, blank=True, verbose_name=u"数据标题")
    chapter_num = models.IntegerField(null=True, blank=True,verbose_name=u"章节数")
    # img_height = models.CharField(max_length=100, default=75,null=True, blank=True, verbose_name=u"封面图高度")
    # img_width = models.CharField(max_length=100, default=75, null=True, blank=True,verbose_name=u"封面图宽度")
    # back_front_cover_img = models.ImageField(upload_to="" , null=True, blank=True,verbose_name=u"补传封面图片", height_field='img_height',width_field='img_width',max_length=2000)
    # front_cover_img = models.CharField(max_length=1500, null=True, blank=True,verbose_name=u"封面图片")
    # prenum = models.CharField(max_length=100, default="", null=True, blank=True, verbose_name=u"编号")
    # long_time = models.CharField(max_length=100, default="", null=True, blank=True, verbose_name=u"时长（分钟）")
    # is_love = models.BooleanField(default=False,verbose_name=u"喜爱")
    # is_check = models.BooleanField(default=False,verbose_name=u"检查封面")

    # #对于ManyToManyField，没有null参数，如果加上会报警告如：spiderdata.SpiderData.genre: (fields.W340) null has no effect on ManyToManyField.
    # hm_area = models.ManyToManyField(SpiderHMArea,default="", blank=True,verbose_name=u"地区")
    # hm_tag = models.ManyToManyField(SpiderHMTag,default="",blank=True,verbose_name=u"类型")

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
        verbose_name = u"爬取漫画数据查询"
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.splider_title


class SpiderHMChapterImage(models.Model):
    spiderhmchapterdata = models.ForeignKey(SpiderHMChapterData,null=True, blank=True, verbose_name=u"章节", on_delete=models.PROTECT)
    img_title = models.CharField(max_length=1000, default=75,null=True, blank=True, verbose_name=u"图片标题")
    img_height = models.CharField(max_length=100, default=75,null=True, blank=True, verbose_name=u"图片高度")
    img_width = models.CharField(max_length=100, default=75, null=True, blank=True,verbose_name=u"图片宽度")
    content_img = models.ImageField(upload_to="hanman/content/" , null=True, blank=True,verbose_name=u"图片", height_field='img_height',width_field='img_width',max_length=2000)
    chapter_image_num = models.IntegerField(null=True, blank=True,verbose_name=u"图片编号")
    write_user = models.ForeignKey(User, null=True, blank=True, verbose_name=u"用户名", on_delete=models.PROTECT)
    add_time = models.DateTimeField(null=True, blank=True,auto_now_add=True,
                                    verbose_name=u"添加时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间,auto_now_add=True是指定在数据新增时, 自动写入时间
    update_time = models.DateTimeField(default=datetime.now, null=True, blank=True,
                                    verbose_name=u"更新时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间，auto_now=True是无论新增还是更新数据, 此字段都会更新为当前时间
    class Meta:
        verbose_name = u"漫画内容"
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.img_title