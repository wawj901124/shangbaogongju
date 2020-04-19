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

            spiderhmchapterdata_list = SpiderHMChapterData.objects.filter(spiderhmbook_id=spiderhmchapterdata.spiderhmbook_id).order_by("chapter_num")
            current_chapter_num = spiderhmchapterdata.chapter_num
            chapter_num_list = []
            for i in spiderhmchapterdata_list:
                chapter_num_list.append(i.chapter_num)
            print("chapter_num_list:")
            print(chapter_num_list)
            current_chapter_num_index = chapter_num_list.index(current_chapter_num)
            chapter_num_list_len = len(chapter_num_list)
            if current_chapter_num_index == chapter_num_list_len-1:
                next_chapter_num_index = current_chapter_num_index
            else:
                next_chapter_num_index = current_chapter_num_index+1
            next_chapter_num = chapter_num_list[next_chapter_num_index]
            next_spiderhmchapterdata = SpiderHMChapterData.objects.get(chapter_num=next_chapter_num)

            return render(request, "spiderhmchapterimage/SpiderHMChapterImage.html",
                          {"spiderhmchapterdata":  spiderhmchapterdata,
                           "nextspiderhmchapterdata":next_spiderhmchapterdata,
                           "spiderhmchapterimage_list":  spiderhmchapterimage_list,
                           "django_server_yuming": DJANGO_SERVER_YUMING,
                           "is_withRelevance": is_with_relevance,
                           })
        else:
            return render(request, "addContentError.html", {
                "django_server_yuming": DJANGO_SERVER_YUMING
            })
