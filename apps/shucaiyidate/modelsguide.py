from django.db import models
from datetime import datetime
from wanwenyc.settings import DJANGO_SERVER_YUMING,MEDIA_ROOT
from django.contrib.auth import  get_user_model  #导入get_user_model
from testupdatadb.models import UpdateDbData

from .definehelptext import definehelptext


#第三个就是我们自己创建的包
User = get_user_model()  #get_user_model() 函数直接返回User类，找的是settings.AUTH_USER_MODEL变量的值


def getTimeStrN():
    now_time = datetime.now()
    timestrn = now_time.strftime('%Y')
    return timestrn


def getTimeStrNY():
    now_time = datetime.now()
    timestrny = now_time.strftime('%Y%m')
    return timestrny


def getTimeStrNYR():
    now_time = datetime.now()
    timestrnyr = now_time.strftime('%Y%m%d')
    return timestrnyr

#让上传的文件路径动态地与config_project的名字有关
def upload_guide_file_path(instance, filename):  #instance代表模式示例，filename代表上传文件的名字
    file_path = '/'.join(["Guide","{2}/{3}/{4}/{0}_{1}".format(instance.id, instance.guide_project,getTimeStrN(),getTimeStrNY(),getTimeStrNYR()), filename])   #带年月日
    print(file_path)
    return  file_path


class GuideHelp(models.Model):
    guide_project = models.CharField(max_length=100, default="", null=True, blank=True, verbose_name=u"指导文件名称")

    guide_file = models.FileField(upload_to=upload_guide_file_path,  blank=True, null=True,verbose_name="上传指导文件")

    write_user = models.ForeignKey(User, null=True, blank=True, verbose_name=u"上传人员", on_delete=models.PROTECT)
    add_time = models.DateTimeField(null=True, blank=True,auto_now_add=True,
                                    verbose_name=u"添加时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间,auto_now_add=True是指定在数据新增时, 自动写入时间
    update_time = models.DateTimeField(default=datetime.now, null=True, blank=True,
                                    verbose_name=u"更新时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间，auto_now=True是无论新增还是更新数据, 此字段都会更新为当前时间

    class Meta:
        verbose_name = u"使用指导文档"
        verbose_name_plural=verbose_name

    def __str__(self):
        return "{}-【{}】".format(self.id,self.guide_project)

    def go_to(self):   #定义点击后跳转到某一个地方（可以加html代码）
        from django.utils.safestring import mark_safe   #调用mark_safe这个函数，django可以显示成一个文本，而不是html代码
        all_html = ""
        if self.guide_file:   #如果有则显示
            open_dev_html = "<a href='{}{}'>下载查看指导文件</a>".format(DJANGO_SERVER_YUMING,self.guide_file.url)
        else:
            open_dev_html = "<span>无指导文件</span>"

        all_html = all_html + open_dev_html

        return mark_safe(all_html)
        # return  "<a href='http://192.168.212.194:9002/testcase/{}/'>跳转</a>".format(self.id)

    go_to.short_description = u"操作"   #为go_to函数名个名字

