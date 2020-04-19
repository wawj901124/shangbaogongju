from django.shortcuts import render
from django.views.generic import View   #导入View


from .modelshm import SpiderHMChapterImage,SpiderHMChapterData
from wanwenyc.settings import DJANGO_SERVER_YUMING


# Create your views here.
# 漫画图片显示
class SpiderHMChapterImageView(View):  # 继承View
    """
    漫画图片展示
    """

    def get(self, request, spiderhmchapterdata_id):
        if request.user.username == 'check':
            return render(request, "canNotAddclickAndBack.html", {
                "django_server_yuming": DJANGO_SERVER_YUMING
            })
        elif request.user.is_active:
            spiderhmchapterdata = SpiderHMChapterData.objects.get(id=int(spiderhmchapterdata_id))
            spiderhmchapterimage_list = SpiderHMChapterImage.objects.filter(spiderhmchapterdata_id=int(spiderhmchapterdata_id)).order_by("chapter_image_num")  # 获取实例对象
            is_with_relevance = 1
            return render(request, "spiderhmchapterimage/SpiderHMChapterImage.html",
                          {"spiderhmchapterdata":  spiderhmchapterdata,
                           "spiderhmchapterimage_list":  spiderhmchapterimage_list,
                           "django_server_yuming": DJANGO_SERVER_YUMING,
                           "is_withRelevance": is_with_relevance,
                           })
        else:
            return render(request, "addContentError.html", {
                "django_server_yuming": DJANGO_SERVER_YUMING
            })
