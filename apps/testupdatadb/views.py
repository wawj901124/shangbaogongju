from django.shortcuts import render
from django.views.generic import View   #导入View


from .models import UpdateDbData,User
from wanwenyc.settings import DJANGO_SERVER_YUMING

from .forms import UpdateDbDataForm



# Create your views here.
#添加场景的view
class  UpdateDbDataView(View):  #继承View
    """
    测试数据复制编写页面处理
    """
    def get(self,request,testupdatadb_id):
        if request.user.username == 'check':
            return render(request, "canNotAddupdatedbdata.html",{
                "django_server_yuming":DJANGO_SERVER_YUMING
            })
        elif request.user.is_active:
            updatedbdata = UpdateDbData.objects.get(id=int(testupdatadb_id))   #获取用例
            updatedbdata_all = UpdateDbData.objects.all().order_by("-id")
            return render(request,"updatedbdata/updatedbdata.html",
                          {"updatedbdata":updatedbdata,
                           "updatedbdata_all":updatedbdata_all,
                           "django_server_yuming": DJANGO_SERVER_YUMING,
                           })
        else:
            return render(request,"addContentError.html",{
                "django_server_yuming": DJANGO_SERVER_YUMING
            })

    def post(self, request,testupdatadb_id):
        username = request.user.username
        updatedbdata_all = UpdateDbData.objects.all().order_by("-id")
        updatedbdata_form = UpdateDbDataForm(request.POST)  # 实例化updatedbdataForm()
        updatedbdata = UpdateDbData.objects.get(id=int(testupdatadb_id))  # 获取用例

        if updatedbdata_form.is_valid():  # is_valid()判断是否有错

            updatedbdata_form.save(commit=True)  # 将信息保存到数据库中

            zj = UpdateDbData.objects.all().order_by('-add_time')[:1][0]  # 根据添加时间查询最新的
            user = User.objects.get(username=username)
            zj.write_user_id = user.id
            zj.save()

            updatedbdataid = zj.id
            updatedbdataadd = UpdateDbData.objects.get(id=int(updatedbdataid))  # 获取用例
            return render(request, "updatedbdata/updatedbdata.html", {
                "updatedbdata": updatedbdataadd,
                "updatedbdata_all": updatedbdata_all,
                "sumsg":u"添加测试用例---【{}】---成功,请继续添加".format(updatedbdataadd.test_case_title),
                "django_server_yuming": DJANGO_SERVER_YUMING,
            })
        else:
            return render(request, 'updatedbdata/updatedbdataForm.html', {
                "updatedbdata": updatedbdata,
                "updatedbdata_all": updatedbdata_all,
                "updatedbdataform": updatedbdata_form,
                "errmsg":u"添加失败，请重新添加，添加时请检查各个字段是否填写",
                "django_server_yuming": DJANGO_SERVER_YUMING,
            })  # 返回页面，回填信息
