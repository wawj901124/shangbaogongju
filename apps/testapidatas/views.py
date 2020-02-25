from django.shortcuts import render
from django.views.generic import View   #导入View


from .models import ApiRequestData,User   #ApiRequestData
from .forms import ApiRequestDataForm  #导入QSClickAndBackForm
from wanwenyc.settings import DJANGO_SERVER_YUMING

# Create your views here.
#接口数据的view
class  ApiRequestDataView(View):  #继承View
    """
    测试数据复制编写页面处理
    """
    def get(self,request,apirequestdata_id):
        if request.user.username == 'check':
            return render(request, "canNotAddclickAndBack.html",{
                "django_server_yuming":DJANGO_SERVER_YUMING
            })
        elif request.user.is_active:
            apirequestdata = ApiRequestData.objects.get(id=int(apirequestdata_id))   #获取用例
            apirequestdata_all = ApiRequestData.objects.all().order_by("-id")
            return render(request,"apirequestdata/apiRequestData.html",
                          {"apirequestdata":apirequestdata,
                           "apirequestdata_all":apirequestdata_all,
                           "django_server_yuming": DJANGO_SERVER_YUMING,
                           })
        else:
            return render(request,"addContentError.html",{
                "django_server_yuming": DJANGO_SERVER_YUMING
            })

    def post(self, request,apirequestdata_id):
        username = request.user.username
        apirequestdata_all = ApiRequestData.objects.all().order_by("-id")
        apirequestdata_form = ApiRequestDataForm(request.POST)  # 实例化ApiRequestDataForm()
        apirequestdata = ApiRequestData.objects.get(id=int(apirequestdata_id))  # 获取用例

        if apirequestdata_form.is_valid():  # is_valid()判断是否有错

            apirequestdata_form.save(commit=True)  # 将信息保存到数据库中

            zj = ApiRequestData.objects.all().order_by('-add_time')[:1][0]  # 根据添加时间查询最新的
            user = User.objects.get(username=username)
            zj.write_user_id = user.id
            zj.save()

            apirequestdataid = zj.id
            apirequestdataadd = ApiRequestData.objects.get(id=int(apirequestdataid))  # 获取用例
            return render(request, "apirequestdata/apiRequestData.html", {
                "apirequestdata": apirequestdataadd,
                "apirequestdata_all": apirequestdata_all,
                "sumsg":u"添加测试用例---【{}】---成功,请继续添加".format(apirequestdataadd.test_case_title),
                "django_server_yuming": DJANGO_SERVER_YUMING,
            })
        else:
            return render(request, 'apirequestdata/apiRequestDataForm.html', {
                "apirequestdata": apirequestdata,
                "apirequestdata_all": apirequestdata_all,
                "apirequestdataform": apirequestdata_form,
                "errmsg":u"添加失败，请重新添加，添加时请检查各个字段是否填写",
                "django_server_yuming": DJANGO_SERVER_YUMING,
            })  # 返回页面，回填信息