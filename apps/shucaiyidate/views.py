from django.shortcuts import render
from django.views.generic import View   #导入View

from wanwenyc.settings import DJANGO_SERVER_YUMING


from .modelsdev import TagContent,User,TagAttrib

from .forms import TagContentForm


class TagContentView(View):
    """
    节点配置复制编写页面处理
    """

    def get(self, request, tagcontent_id):
        if request.user.username == 'check':
            return render(request, "canNotAddclickAndBack.html", {
                "django_server_yuming": DJANGO_SERVER_YUMING
            })
        elif request.user.is_active:
            tagcontent = TagContent.objects.get(id=int(tagcontent_id))  # 获取数据
            is_with_relevance = 1
            depend_all = TagContent.objects.all().order_by("-id")   #依赖数据

            depend_tagattrib = TagAttrib.objects.filter(tagcontent_id=int(tagcontent_id)).order_by("-id")  #获取属性数据库内容
            depend_tagattrib_num = depend_tagattrib.count()

            return render(request, "tagcontent/TagContent.html",
                          {"tagcontent": tagcontent,
                           "depend_all":depend_all,
                           "depend_tagattrib":depend_tagattrib,
                           "depend_tagattrib_num":depend_tagattrib_num,
                           "django_server_yuming": DJANGO_SERVER_YUMING,
                           "is_withRelevance": is_with_relevance,
                           })
        else:
            return render(request, "addContentError.html", {
                "django_server_yuming": DJANGO_SERVER_YUMING
            })


    def post(self, request,tagcontent_id):
        username = request.user.username
        depend_all = TagContent.objects.all().order_by("-id")  # 依赖数据

        tagcontent_form = TagContentForm(request.POST)  # 实例化NewAddAndCheckForm()
        tagcontent = TagContent.objects.get(id=int(tagcontent_id))  # 获取内容

        # 处理附带复制内容
        is_with_relevance = request.POST.get('is_withRelevance', '')
        print("is_withRelevance:%s" % is_with_relevance)
        print("is_withRelevance类型:%s" % type(is_with_relevance))
        is_with_relevance =int(is_with_relevance)
        print("is_withRelevance:%s" % is_with_relevance)
        print("is_withRelevance类型:%s" % type(is_with_relevance))
        # 结束处理

        if tagcontent_form.is_valid():  # is_valid()判断是否有错

            tagcontent_form.save(commit=True)  # 将信息保存到数据库中

            zj = TagContent.objects.all().order_by('-add_time')[:1][0]  # 根据添加时间查询最新的
            user = User.objects.get(username=username)
            zj.write_user_id = user.id
            zj.save()

            tagcontentid = zj.id
            tagcontentadd = TagContent.objects.get(id=int(tagcontentid))  # 获取用例

            # 如果增加附带
            if is_with_relevance == 1:
                print("处理附带内容")
                #处理添加数据的节点属性依赖
                tagattrib_old_all = TagAttrib.objects.filter(tagcontent_id=tagcontent_id).order_by("id")
                tagattrib_old_all_count =  tagattrib_old_all.count()
                if tagattrib_old_all_count != 0:
                    for tagattrib_old in tagattrib_old_all:
                        tagattrib_new = TagAttrib()
                        tagattrib_new.tagcontent_id = zj.id
                        tagattrib_new.tag_value_name = tagattrib_old.tag_value_name
                        tagattrib_new.tag_value_text = tagattrib_old.tag_value_text
                        tagattrib_new.write_user_id = user.id
                        tagattrib_new.save()


            return render(request, "tagcontent/TagContent.html", {
                "tagcontent": tagcontentadd,
                "depend_all": depend_all,
                "sumsg":u"添加数据---【{}】---成功,请继续添加".format(tagcontentadd.tag_name),
                "django_server_yuming": DJANGO_SERVER_YUMING,
            })
        else:
            return render(request, 'tagcontent/TagContentForm.html', {
                "tagcontent": tagcontent,
                "depend_all": depend_all,
                "tagcontentform": tagcontent_form ,
                "errmsg":u"添加失败，请重新添加，添加时请检查各个字段是否填写",
                "django_server_yuming": DJANGO_SERVER_YUMING,
            })  # 返回页面，回填信息
