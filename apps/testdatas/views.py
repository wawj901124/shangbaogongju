from django.shortcuts import render
from django.views.generic import View   #导入View


from .models import ClickAndBack,User,NewAddAndCheck,SearchAndCheck,DeleteAndCheck,EditAndCheck   #ClickAndBack
from .forms import ClickAndBackForm,NewAddAndCheckForm,SearchAndCheckForm,DeleteAndCheckForm,EditAndCheckForm  #导入QSClickAndBackForm
from wanwenyc.settings import DJANGO_SERVER_YUMING
from .models import InputTapInputText,InputTapInputFile,InputTapInputDateTime,\
    RadioAndReelectionLabel,SelectTapSelectOption,AssertTipText             #导入添加场景依赖模块
from .models import IframeBodyInputText   #导入添加场景依赖模块
from .models import SearchInputTapInputText,SearchSelectTapSelectOption   #导入查询场景依赖模块
from .models import LoginAndCheck
from .forms import LoginAndCheckForm



# Create your views here.
#登录场景的view
class LoginAndCheckView(View):  # 继承View
    """
    测试数据复制编写页面处理
    """

    def get(self, request, loginandcheck_id):
        if request.user.username == 'check':
            return render(request, "canNotAddclickAndBack.html", {
                "django_server_yuming": DJANGO_SERVER_YUMING
            })
        elif request.user.is_active:
            loginandcheck = LoginAndCheck.objects.get(id=int(loginandcheck_id))  # 获取用例
            is_with_relevance = 1
            return render(request, "loginandcheck/loginAndCheck.html",
                          {"loginandcheck": loginandcheck,
                           "django_server_yuming": DJANGO_SERVER_YUMING,
                           "is_withRelevance": is_with_relevance,
                           })
        else:
            return render(request, "addContentError.html", {
                "django_server_yuming": DJANGO_SERVER_YUMING
            })

    def post(self, request, loginandcheck_id):
        username = request.user.username
        loginandcheck_form = LoginAndCheckForm(request.POST)  # 实例化NewAddAndCheckForm()
        loginandcheck =  LoginAndCheck.objects.get(id=int(loginandcheck_id))  # 获取用例

        # 处理附带复制内容
        is_with_relevance = request.POST.get('is_withRelevance', '')
        print("is_withRelevance:%s" % is_with_relevance)
        print("is_withRelevance类型:%s" % type(is_with_relevance))
        is_with_relevance = int(is_with_relevance)
        print("is_withRelevance:%s" % is_with_relevance)
        print("is_withRelevance类型:%s" % type(is_with_relevance))
        # 结束处理

        if loginandcheck_form.is_valid():  # is_valid()判断是否有错

            loginandcheck_form.save(commit=True)  # 将信息保存到数据库中

            zj = LoginAndCheck.objects.all().order_by('-add_time')[:1][0]  # 根据添加时间查询最新的
            user = User.objects.get(username=username)
            zj.write_user_id = user.id
            zj.save()

            loginandcheckid = zj.id
            loginandcheckadd = LoginAndCheck.objects.get(id=int(loginandcheckid))  # 获取用例

            # 如果增加附带
            if is_with_relevance == 1:
                print("处理附带内容")
                # 处理新增数据场景依赖的文本输入框
                inputtapinputtext_old_all = InputTapInputText.objects.filter(
                    loginandcheck_id=loginandcheck_id).order_by("id")
                inputtapinputtext_old_all_count = inputtapinputtext_old_all.count()
                if inputtapinputtext_old_all_count != 0:
                    for inputtapinputtext_old in inputtapinputtext_old_all:
                        inputtapinputtext_new = InputTapInputText()
                        inputtapinputtext_new.loginandcheck_id = zj.id
                        inputtapinputtext_new.input_ele_find = inputtapinputtext_old.input_ele_find
                        inputtapinputtext_new.input_ele_find_value = inputtapinputtext_old.input_ele_find_value
                        inputtapinputtext_new.is_auto_input = inputtapinputtext_old.is_auto_input
                        inputtapinputtext_new.auto_input_type = inputtapinputtext_old.auto_input_type
                        inputtapinputtext_new.auto_input_long = inputtapinputtext_old.auto_input_long
                        inputtapinputtext_new.input_text = inputtapinputtext_old.input_text
                        inputtapinputtext_new.is_with_time = inputtapinputtext_old.is_with_time
                        inputtapinputtext_new.is_check = inputtapinputtext_old.is_check
                        inputtapinputtext_new.save()


                # 处理新增数据场景依赖的验证元素
                asserttiptext_old_all = AssertTipText.objects.filter(loginandcheck_id=loginandcheck_id).order_by("id")
                asserttiptext_old_all_count = asserttiptext_old_all.count()
                if asserttiptext_old_all_count != 0:
                    for asserttiptext_old in asserttiptext_old_all:
                        asserttiptext_new = AssertTipText()
                        asserttiptext_new.loginandcheck_id = zj.id
                        asserttiptext_new.tip_ele_find = asserttiptext_old.tip_ele_find
                        asserttiptext_new.tip_ele_find_value = asserttiptext_old.tip_ele_find_value
                        asserttiptext_new.tip_text = asserttiptext_old.tip_text
                        asserttiptext_new.save()


            return render(request, "loginandcheck/loginAndCheck.html", {
                "loginandcheck": loginandcheckadd,
                "sumsg": u"添加测试用例---【{}】---成功,请继续添加".format(loginandcheckadd.test_case_title),
                "django_server_yuming": DJANGO_SERVER_YUMING,
                "is_withRelevance": is_with_relevance,
            })
        else:
            return render(request, 'loginandcheck/loginAndCheckForm.html', {
                "loginandcheck": loginandcheck,
                "newaddandcheckform": loginandcheck_form,
                "errmsg": u"添加失败，请重新添加，添加时请检查各个字段是否填写",
                "django_server_yuming": DJANGO_SERVER_YUMING,
                "is_withRelevance": is_with_relevance,
            })  # 返回页面，回填信息


#添加场景的view
class  ClickAndBackView(View):  #继承View
    """
    测试数据复制编写页面处理
    """
    def get(self,request,clickandback_id):
        if request.user.username == 'check':
            return render(request, "canNotAddclickAndBack.html",{
                "django_server_yuming":DJANGO_SERVER_YUMING
            })
        elif request.user.is_active:
            clickandback = ClickAndBack.objects.get(id=int(clickandback_id))   #获取用例
            clickandback_all = ClickAndBack.objects.all().order_by("-id")
            return render(request,"clickAndBack.html",
                          {"clickandback":clickandback,
                           "clickandback_all":clickandback_all,
                           "django_server_yuming": DJANGO_SERVER_YUMING,
                           })
        else:
            return render(request,"addContentError.html",{
                "django_server_yuming": DJANGO_SERVER_YUMING
            })

    def post(self, request,clickandback_id):
        username = request.user.username
        clickandback_all = ClickAndBack.objects.all().order_by("-id")
        clickandback_form = ClickAndBackForm(request.POST)  # 实例化ClickAndBackForm()
        clickandback = ClickAndBack.objects.get(id=int(clickandback_id))  # 获取用例

        if clickandback_form.is_valid():  # is_valid()判断是否有错

            clickandback_form.save(commit=True)  # 将信息保存到数据库中

            zj = ClickAndBack.objects.all().order_by('-add_time')[:1][0]  # 根据添加时间查询最新的
            user = User.objects.get(username=username)
            zj.write_user_id = user.id
            zj.save()

            clickandbackid = zj.id
            clickandbackadd = ClickAndBack.objects.get(id=int(clickandbackid))  # 获取用例
            return render(request, "clickAndBack.html", {
                "clickandback": clickandbackadd,
                "clickandback_all": clickandback_all,
                "sumsg":u"添加测试用例---【{}】---成功,请继续添加".format(clickandbackadd.test_case_title),
                "django_server_yuming": DJANGO_SERVER_YUMING,
            })
        else:
            return render(request, 'clickAndBackForm.html', {
                "clickandback": clickandback,
                "clickandback_all": clickandback_all,
                "clickandbackform": clickandback_form,
                "errmsg":u"添加失败，请重新添加，添加时请检查各个字段是否填写",
                "django_server_yuming": DJANGO_SERVER_YUMING,
            })  # 返回页面，回填信息

#新增场景的view
class  NewAddAndCheckView(View):  #继承View
    """
    测试数据复制编写页面处理
    """
    def get(self,request,newaddandcheck_id):
        if request.user.username == 'check':
            return render(request, "canNotAddclickAndBack.html",{
                "django_server_yuming":DJANGO_SERVER_YUMING
            })
        elif request.user.is_active:
            newaddandcheck = NewAddAndCheck.objects.get(id=int(newaddandcheck_id))   #获取用例
            clickandback_all = ClickAndBack.objects.all().order_by("-id")
            return render(request,"newaddandcheck/newAddAndCheck.html",
                          {"newaddandcheck":newaddandcheck,
                           "clickandback_all":clickandback_all,
                           "django_server_yuming": DJANGO_SERVER_YUMING,
                           })
        else:
            return render(request,"addContentError.html",{
                "django_server_yuming": DJANGO_SERVER_YUMING
            })

    def post(self, request,newaddandcheck_id):
        username = request.user.username
        clickandback_all = ClickAndBack.objects.all().order_by("-id")
        newaddandcheck_form = NewAddAndCheckForm(request.POST)  # 实例化NewAddAndCheckForm()
        newaddandcheck = NewAddAndCheck.objects.get(id=int(newaddandcheck_id))  # 获取用例

        if newaddandcheck_form.is_valid():  # is_valid()判断是否有错

            newaddandcheck_form.save(commit=True)  # 将信息保存到数据库中

            zj = NewAddAndCheck.objects.all().order_by('-add_time')[:1][0]  # 根据添加时间查询最新的
            user = User.objects.get(username=username)
            zj.write_user_id = user.id
            zj.save()

            newaddandcheckid = zj.id
            newaddandcheckadd = NewAddAndCheck.objects.get(id=int(newaddandcheckid))  # 获取用例
            return render(request, "newaddandcheck/newAddAndCheck.html", {
                "newaddandcheck": newaddandcheckadd,
                "clickandback_all": clickandback_all,
                "sumsg":u"添加测试用例---【{}】---成功,请继续添加".format(newaddandcheckadd.test_case_title),
                "django_server_yuming": DJANGO_SERVER_YUMING,
            })
        else:
            return render(request, 'newaddandcheck/newAddAndCheckForm.html', {
                "newaddandcheck": newaddandcheck,
                "clickandback_all": clickandback_all,
                "newaddandcheckform": newaddandcheck_form,
                "errmsg":u"添加失败，请重新添加，添加时请检查各个字段是否填写",
                "django_server_yuming": DJANGO_SERVER_YUMING,
            })  # 返回页面，回填信息


#新增场景的view（带有关联数据库的新增）
class  NewAddAndCheckWithRelevanceView(View):  #继承View
    """
    测试数据复制编写页面处理
    """
    def get(self,request,newaddandcheck_id):
        if request.user.username == 'check':
            return render(request, "canNotAddclickAndBack.html",{
                "django_server_yuming":DJANGO_SERVER_YUMING
            })
        elif request.user.is_active:
            newaddandcheck = NewAddAndCheck.objects.get(id=int(newaddandcheck_id))   #获取用例
            clickandback_all = ClickAndBack.objects.all().order_by("-id")
            is_with_relevance = 1
            return render(request,"newaddandcheckwithrelevance/newAddAndCheckWithRelevance.html",
                          {"newaddandcheck":newaddandcheck,
                           "clickandback_all":clickandback_all,
                           "django_server_yuming": DJANGO_SERVER_YUMING,
                           "is_withRelevance": is_with_relevance,
                           })
        else:
            return render(request,"addContentError.html",{
                "django_server_yuming": DJANGO_SERVER_YUMING
            })

    def post(self, request,newaddandcheck_id):
        username = request.user.username
        clickandback_all = ClickAndBack.objects.all().order_by("-id")
        newaddandcheck_form = NewAddAndCheckForm(request.POST)  # 实例化NewAddAndCheckForm()
        newaddandcheck = NewAddAndCheck.objects.get(id=int(newaddandcheck_id))  # 获取用例

        # 处理附带复制内容
        is_with_relevance = request.POST.get('is_withRelevance', '')
        print("is_withRelevance:%s" % is_with_relevance)
        print("is_withRelevance类型:%s" % type(is_with_relevance))
        is_with_relevance =int(is_with_relevance)
        print("is_withRelevance:%s" % is_with_relevance)
        print("is_withRelevance类型:%s" % type(is_with_relevance))
        # 结束处理

        if newaddandcheck_form.is_valid():  # is_valid()判断是否有错

            newaddandcheck_form.save(commit=True)  # 将信息保存到数据库中

            zj = NewAddAndCheck.objects.all().order_by('-add_time')[:1][0]  # 根据添加时间查询最新的
            user = User.objects.get(username=username)
            zj.write_user_id = user.id
            zj.save()


            newaddandcheckid = zj.id
            newaddandcheckadd = NewAddAndCheck.objects.get(id=int(newaddandcheckid))  # 获取用例

            #如果增加附带
            if is_with_relevance == 1:
                print("处理附带内容")
                #处理新增数据场景依赖的文本输入框
                inputtapinputtext_old_all = InputTapInputText.objects.filter(newaddandcheck_id=newaddandcheck_id).order_by("id")
                inputtapinputtext_old_all_count = inputtapinputtext_old_all.count()
                if inputtapinputtext_old_all_count != 0 :
                    for inputtapinputtext_old in inputtapinputtext_old_all:
                        inputtapinputtext_new = InputTapInputText()
                        inputtapinputtext_new.newaddandcheck_id = zj.id
                        inputtapinputtext_new.input_ele_find = inputtapinputtext_old.input_ele_find
                        inputtapinputtext_new.input_ele_find_value = inputtapinputtext_old.input_ele_find_value
                        inputtapinputtext_new.is_auto_input = inputtapinputtext_old.is_auto_input
                        inputtapinputtext_new.auto_input_type = inputtapinputtext_old.auto_input_type
                        inputtapinputtext_new.auto_input_long = inputtapinputtext_old.auto_input_long
                        inputtapinputtext_new.input_text = inputtapinputtext_old.input_text
                        inputtapinputtext_new.is_with_time = inputtapinputtext_old.is_with_time
                        inputtapinputtext_new.is_check  = inputtapinputtext_old.is_check
                        inputtapinputtext_new.save()

                #处理新增数据场景依赖的文件输入框
                inputtapinputfile_old_all = InputTapInputFile.objects.filter(newaddandcheck_id=newaddandcheck_id).order_by("id")
                inputtapinputfile_old_all_count = inputtapinputfile_old_all.count()
                if inputtapinputfile_old_all_count != 0 :
                    for inputtapinputfile_old in inputtapinputfile_old_all:
                        inputtapinputfile_new = InputTapInputFile()
                        inputtapinputfile_new.newaddandcheck_id = zj.id
                        inputtapinputfile_new.input_ele_find = inputtapinputfile_old.input_ele_find
                        inputtapinputfile_new.input_ele_find_value = inputtapinputfile_old.input_ele_find_value
                        inputtapinputfile_new.input_file = inputtapinputfile_old.input_file
                        inputtapinputfile_new.input_class_name = inputtapinputfile_old.input_class_name
                        inputtapinputfile_new.save()


                #处理新增数据场景依赖的时间输入框
                inputtapinputdatetime_old_all = InputTapInputDateTime.objects.filter(newaddandcheck_id=newaddandcheck_id).order_by("id")
                inputtapinputdatetime_old_all_count = inputtapinputdatetime_old_all.count()
                if inputtapinputdatetime_old_all_count != 0 :
                    for inputtapinputdatetime_old in inputtapinputdatetime_old_all:
                        inputtapinputdatetime_new = InputTapInputDateTime()
                        inputtapinputdatetime_new.newaddandcheck_id = zj.id
                        inputtapinputdatetime_new.input_ele_find = inputtapinputdatetime_old.input_ele_find
                        inputtapinputdatetime_new.input_ele_find_value = inputtapinputdatetime_old.input_ele_find_value
                        inputtapinputdatetime_new.date_ele_find = inputtapinputdatetime_old.date_ele_find
                        inputtapinputdatetime_new.date_ele_find_value = inputtapinputdatetime_old.date_ele_find_value
                        inputtapinputdatetime_new.last_month_ele_find = inputtapinputdatetime_old.last_month_ele_find
                        inputtapinputdatetime_new.last_month_ele_find_value = inputtapinputdatetime_old.last_month_ele_find_value
                        inputtapinputdatetime_new.click_last_month_counts = inputtapinputdatetime_old.click_last_month_counts
                        inputtapinputdatetime_new.next_month_ele_find  = inputtapinputdatetime_old.next_month_ele_find
                        inputtapinputdatetime_new.next_month_ele_find_value = inputtapinputdatetime_old.next_month_ele_find_value
                        inputtapinputdatetime_new.click_next_month_counts = inputtapinputdatetime_old.click_next_month_counts
                        inputtapinputdatetime_new.last_year_ele_find = inputtapinputdatetime_old.last_year_ele_find
                        inputtapinputdatetime_new.last_year_ele_find_value = inputtapinputdatetime_old.last_year_ele_find_value
                        inputtapinputdatetime_new.click_last_year_counts = inputtapinputdatetime_old.click_last_year_counts
                        inputtapinputdatetime_new.next_year_ele_find = inputtapinputdatetime_old.next_year_ele_find
                        inputtapinputdatetime_new.next_year_ele_find_value  = inputtapinputdatetime_old.next_year_ele_find_value
                        inputtapinputdatetime_new.click_next_year_counts = inputtapinputdatetime_old.click_next_year_counts
                        inputtapinputdatetime_new.save()


                #处理新增数据场景依赖的单选项和复选项
                radioandreelectionlabel_old_all = RadioAndReelectionLabel.objects.filter(newaddandcheck_id=newaddandcheck_id).order_by("id")
                radioandreelectionlabel_old_all_count = radioandreelectionlabel_old_all.count()
                if radioandreelectionlabel_old_all_count != 0 :
                    for radioandreelectionlabel_old in radioandreelectionlabel_old_all:
                        radioandreelectionlabel_new = RadioAndReelectionLabel()
                        radioandreelectionlabel_new.newaddandcheck_id = zj.id
                        radioandreelectionlabel_new.label_ele_find = radioandreelectionlabel_old.label_ele_find
                        radioandreelectionlabel_new.label_ele_find_value = radioandreelectionlabel_old.label_ele_find_value
                        radioandreelectionlabel_new.is_check = radioandreelectionlabel_old.is_check
                        radioandreelectionlabel_new.checked_add_attribute = radioandreelectionlabel_old.checked_add_attribute
                        radioandreelectionlabel_new.checked_add_attribute_value = radioandreelectionlabel_old.checked_add_attribute_value
                        radioandreelectionlabel_new.save()


                #处理新增数据场景依赖的选项框
                selecttapselectoption_old_all = SelectTapSelectOption.objects.filter(newaddandcheck_id=newaddandcheck_id).order_by("id")
                selecttapselectoption_old_all_count = selecttapselectoption_old_all.count()
                if selecttapselectoption_old_all_count != 0 :
                    for selecttapselectoption_old in selecttapselectoption_old_all:
                        selecttapselectoption_new = SelectTapSelectOption()
                        selecttapselectoption_new.newaddandcheck_id = zj.id
                        selecttapselectoption_new.select_ele_find = selecttapselectoption_old.select_ele_find
                        selecttapselectoption_new.select_ele_find_value = selecttapselectoption_old.select_ele_find_value
                        selecttapselectoption_new.select_option_ele_find = selecttapselectoption_old.select_option_ele_find
                        selecttapselectoption_new.select_option_ele_find_value = selecttapselectoption_old.select_option_ele_find_value
                        selecttapselectoption_new.save()


                #处理新增数据场景依赖的验证元素
                asserttiptext_old_all = AssertTipText.objects.filter(newaddandcheck_id=newaddandcheck_id).order_by("id")
                asserttiptext_old_all_count = asserttiptext_old_all.count()
                if asserttiptext_old_all_count != 0 :
                    for asserttiptext_old in asserttiptext_old_all:
                        asserttiptext_new = AssertTipText()
                        asserttiptext_new.newaddandcheck_id = zj.id
                        asserttiptext_new.tip_ele_find = asserttiptext_old.tip_ele_find
                        asserttiptext_new.tip_ele_find_value = asserttiptext_old.tip_ele_find_value
                        asserttiptext_new.tip_text = asserttiptext_old.tip_text
                        asserttiptext_new.save()

                # 处理新增数据场景依赖的富文本输入框
                iframebodyinputtext_old_all = IframeBodyInputText.objects.filter(newaddandcheck_id=newaddandcheck_id).order_by("id")
                iframebodyinputtext_old_all_count = iframebodyinputtext_old_all.count()
                if iframebodyinputtext_old_all_count !=0:
                    for iframebodyinputtext_old in iframebodyinputtext_old_all:
                        iframebodyinputtext_new = IframeBodyInputText()
                        iframebodyinputtext_new.newaddandcheck_id = zj.id
                        iframebodyinputtext_new.iframe_ele_find = iframebodyinputtext_old.iframe_ele_find
                        iframebodyinputtext_new.iframe_ele_find_value = iframebodyinputtext_old.iframe_ele_find_value
                        iframebodyinputtext_new.input_ele_find = iframebodyinputtext_old.input_ele_find
                        iframebodyinputtext_new.input_ele_find_value = iframebodyinputtext_old.input_ele_find_value
                        iframebodyinputtext_new.is_auto_input = iframebodyinputtext_old.is_auto_input
                        iframebodyinputtext_new.auto_input_type = iframebodyinputtext_old.auto_input_type
                        iframebodyinputtext_new.auto_input_long = iframebodyinputtext_old.auto_input_long
                        iframebodyinputtext_new.input_text = iframebodyinputtext_old.input_text
                        iframebodyinputtext_new.is_with_time = iframebodyinputtext_old.is_with_time
                        iframebodyinputtext_new.is_check  = iframebodyinputtext_old.is_check
                        iframebodyinputtext_new.save()


                
            return render(request, "newaddandcheckwithrelevance/newAddAndCheckWithRelevance.html", {
                "newaddandcheck": newaddandcheckadd,
                "clickandback_all": clickandback_all,
                "sumsg":u"添加测试用例---【{}】---成功,请继续添加".format(newaddandcheckadd.test_case_title),
                "django_server_yuming": DJANGO_SERVER_YUMING,
                "is_withRelevance": is_with_relevance,
            })
        else:
            return render(request, 'newaddandcheckwithrelevance/newAddAndCheckWithRelevanceForm.html', {
                "newaddandcheck": newaddandcheck,
                "clickandback_all": clickandback_all,
                "newaddandcheckform": newaddandcheck_form,
                "errmsg":u"添加失败，请重新添加，添加时请检查各个字段是否填写",
                "django_server_yuming": DJANGO_SERVER_YUMING,
                "is_withRelevance": is_with_relevance,
            })  # 返回页面，回填信息

#查询场景的view
class  SearchAndCheckView(View):  #继承View
    """
    测试数据复制编写页面处理
    """
    def get(self,request,searchandcheck_id):
        if request.user.username == 'check':
            return render(request, "canNotAddclickAndBack.html",{
                "django_server_yuming":DJANGO_SERVER_YUMING
            })
        elif request.user.is_active:
            searchandcheck = SearchAndCheck.objects.get(id=int(searchandcheck_id))   #获取用例
            clickandback_all = ClickAndBack.objects.all().order_by("-id")
            return render(request,"searchandcheck/searchAndCheck.html",
                          {"searchandcheck":searchandcheck,
                           "clickandback_all":clickandback_all,
                           "django_server_yuming": DJANGO_SERVER_YUMING,
                           })
        else:
            return render(request,"addContentError.html",{
                "django_server_yuming": DJANGO_SERVER_YUMING
            })

    def post(self, request,searchandcheck_id):
        username = request.user.username
        clickandback_all = ClickAndBack.objects.all().order_by("-id")
        searchandcheck_form = SearchAndCheckForm(request.POST)  # 实例化SearchAndCheckForm()
        searchandcheck = SearchAndCheck.objects.get(id=int(searchandcheck_id))  # 获取用例

        if searchandcheck_form.is_valid():  # is_valid()判断是否有错

            searchandcheck_form.save(commit=True)  # 将信息保存到数据库中

            zj = SearchAndCheck.objects.all().order_by('-add_time')[:1][0]  # 根据添加时间查询最新的
            user = User.objects.get(username=username)
            zj.write_user_id = user.id
            zj.save()

            searchandcheckid = zj.id
            searchandcheckadd = SearchAndCheck.objects.get(id=int(searchandcheckid))  # 获取用例
            return render(request, "searchandcheck/searchAndCheck.html", {
                "searchandcheck": searchandcheckadd,
                "clickandback_all": clickandback_all,
                "sumsg":u"添加测试用例---【{}】---成功,请继续添加".format(searchandcheckadd.test_case_title),
                "django_server_yuming": DJANGO_SERVER_YUMING,
            })
        else:
            return render(request, 'searchandcheck/searchAndCheckForm.html', {
                "searchandcheck": searchandcheck,
                "clickandback_all": clickandback_all,
                "searchandcheckform": searchandcheck_form,
                "errmsg":u"添加失败，请重新添加，添加时请检查各个字段是否填写",
                "django_server_yuming": DJANGO_SERVER_YUMING,
            })  # 返回页面，回填信息


#查询场景的view（带有关联数据库的新增）
class  SearchAndCheckWithRelevanceView(View):  #继承View
    """
    测试数据复制编写页面处理
    """
    def get(self,request,searchandcheck_id):
        if request.user.username == 'check':
            return render(request, "canNotAddclickAndBack.html",{
                "django_server_yuming":DJANGO_SERVER_YUMING
            })
        elif request.user.is_active:
            searchandcheck = SearchAndCheck.objects.get(id=int(searchandcheck_id))   #获取用例
            clickandback_all = ClickAndBack.objects.all().order_by("-id")
            is_with_relevance = 1
            return render(request,"searchandcheckwithrelevance/searchAndCheckWithRelevance.html",
                          {"searchandcheck":searchandcheck,
                           "clickandback_all":clickandback_all,
                           "django_server_yuming": DJANGO_SERVER_YUMING,
                           "is_withRelevance": is_with_relevance,
                           })
        else:
            return render(request,"addContentError.html",{
                "django_server_yuming": DJANGO_SERVER_YUMING
            })

    def post(self, request,searchandcheck_id):
        username = request.user.username
        clickandback_all = ClickAndBack.objects.all().order_by("-id")
        searchandcheck_form = SearchAndCheckForm(request.POST)  # 实例化SearchAndCheckForm()
        searchandcheck = SearchAndCheck.objects.get(id=int(searchandcheck_id))  # 获取用例

        # 处理附带复制内容
        is_with_relevance = request.POST.get('is_withRelevance', '')
        print("is_withRelevance:%s" % is_with_relevance)
        print("is_withRelevance类型:%s" % type(is_with_relevance))
        is_with_relevance =int(is_with_relevance)
        print("is_withRelevance:%s" % is_with_relevance)
        print("is_withRelevance类型:%s" % type(is_with_relevance))
        # 结束处理

        if searchandcheck_form.is_valid():  # is_valid()判断是否有错

            searchandcheck_form.save(commit=True)  # 将信息保存到数据库中

            zj = SearchAndCheck.objects.all().order_by('-add_time')[:1][0]  # 根据添加时间查询最新的
            user = User.objects.get(username=username)
            zj.write_user_id = user.id
            zj.save()

            searchandcheckid = zj.id
            searchandcheckadd = SearchAndCheck.objects.get(id=int(searchandcheckid))  # 获取用例

            #如果增加附带
            if is_with_relevance == 1:
                print("处理附带内容")
                #处理查询场景依赖的文本输入框模型
                searchinputtapinputtext_old_all = SearchInputTapInputText.objects.filter(searchandcheck_id=searchandcheck_id).order_by("id")
                searchinputtapinputtext_old_all_count = searchinputtapinputtext_old_all.count()
                if searchinputtapinputtext_old_all_count != 0 :
                    for searchinputtapinputtext_old in searchinputtapinputtext_old_all:
                        searchinputtapinputtext_new = SearchInputTapInputText()
                        searchinputtapinputtext_new.searchandcheck_id = zj.id
                        searchinputtapinputtext_new.input_ele_find = searchinputtapinputtext_old.input_ele_find
                        searchinputtapinputtext_new.input_ele_find_value = searchinputtapinputtext_old.input_ele_find_value
                        searchinputtapinputtext_new.input_text = searchinputtapinputtext_old.input_text
                        searchinputtapinputtext_new.search_result_colnum = searchinputtapinputtext_old.search_result_colnum
                        searchinputtapinputtext_new.save()

                #处理查询场景依赖的选项框模型
                searchselecttapselectoption_old_all = SearchSelectTapSelectOption.objects.filter(searchandcheck_id=searchandcheck_id).order_by("id")
                searchselecttapselectoption_old_all_count = searchselecttapselectoption_old_all.count()
                if searchselecttapselectoption_old_all_count != 0 :
                    for searchselecttapselectoption_old in searchselecttapselectoption_old_all:
                        searchselecttapselectoption_new = SearchSelectTapSelectOption()
                        searchselecttapselectoption_new.searchandcheck_id = zj.id
                        searchselecttapselectoption_new.select_ele_find = searchselecttapselectoption_old.select_ele_find
                        searchselecttapselectoption_new.select_ele_find_value = searchselecttapselectoption_old.select_ele_find_value
                        searchselecttapselectoption_new.select_option_ele_find = searchselecttapselectoption_old.select_option_ele_find
                        searchselecttapselectoption_new.select_option_ele_find_value = searchselecttapselectoption_old.select_option_ele_find_value
                        searchselecttapselectoption_new.search_result_colnum = searchselecttapselectoption_old.search_result_colnum
                        searchselecttapselectoption_new.save()



            return render(request, "searchandcheckwithrelevance/searchAndCheckWithRelevance.html", {
                "searchandcheck": searchandcheckadd,
                "clickandback_all": clickandback_all,
                "sumsg":u"添加测试用例---【{}】---成功,请继续添加".format(searchandcheckadd.test_case_title),
                "django_server_yuming": DJANGO_SERVER_YUMING,
                "is_withRelevance": is_with_relevance,
            })
        else:
            return render(request, 'searchandcheckwithrelevance/searchAndCheckWithRelevanceForm.html', {
                "searchandcheck": searchandcheck,
                "clickandback_all": clickandback_all,
                "searchandcheckform": searchandcheck_form,
                "errmsg":u"添加失败，请重新添加，添加时请检查各个字段是否填写",
                "django_server_yuming": DJANGO_SERVER_YUMING,
                "is_withRelevance": is_with_relevance,
            })  # 返回页面，回填信息


#删除场景的view
class  DeleteAndCheckView(View):  #继承View
    """
    测试数据复制编写页面处理
    """
    def get(self,request,deleteandcheck_id):
        if request.user.username == 'check':
            return render(request, "canNotAddclickAndBack.html",{
                "django_server_yuming":DJANGO_SERVER_YUMING
            })
        elif request.user.is_active:
            deleteandcheck = DeleteAndCheck.objects.get(id=int(deleteandcheck_id))   #获取用例
            clickandback_all = ClickAndBack.objects.all().order_by("-id")
            return render(request,"deleteandcheck/deleteAndCheck.html",
                          {"deleteandcheck":deleteandcheck,
                           "clickandback_all":clickandback_all,
                           "django_server_yuming": DJANGO_SERVER_YUMING,
                           })
        else:
            return render(request,"addContentError.html",{
                "django_server_yuming": DJANGO_SERVER_YUMING
            })

    def post(self, request,deleteandcheck_id):
        username = request.user.username
        clickandback_all = ClickAndBack.objects.all().order_by("-id")
        deleteandcheck_form = DeleteAndCheckForm(request.POST)  # 实例化DeleteAndCheckForm()
        deleteandcheck = NewAddAndCheck.objects.get(id=int(deleteandcheck_id))  # 获取用例

        if deleteandcheck_form.is_valid():  # is_valid()判断是否有错

            deleteandcheck_form.save(commit=True)  # 将信息保存到数据库中

            zj = DeleteAndCheck.objects.all().order_by('-add_time')[:1][0]  # 根据添加时间查询最新的
            user = User.objects.get(username=username)
            zj.write_user_id = user.id
            zj.save()

            deleteandcheckid = zj.id
            deleteandcheckadd = DeleteAndCheck.objects.get(id=int(deleteandcheckid))  # 获取用例
            return render(request, "deleteandcheck/deleteAndCheck.html", {
                "deleteandcheck": deleteandcheckadd,
                "clickandback_all": clickandback_all,
                "sumsg":u"添加测试用例---【{}】---成功,请继续添加".format(deleteandcheckadd.test_case_title),
                "django_server_yuming": DJANGO_SERVER_YUMING,
            })
        else:
            return render(request, 'deleteandcheck/deleteAndCheckForm.html', {
                "deleteandcheck": deleteandcheck,
                "clickandback_all": clickandback_all,
                "deleteandcheckform": deleteandcheck_form,
                "errmsg":u"添加失败，请重新添加，添加时请检查各个字段是否填写",
                "django_server_yuming": DJANGO_SERVER_YUMING,
            })  # 返回页面，回填信息


# 修改场景的view（带有关联数据库的新增）
class EditAndCheckView(View):  # 继承View
    """
    测试数据复制编写页面处理
    """

    def get(self, request, editandcheck_id):
        if request.user.username == 'check':
            return render(request, "canNotAddclickAndBack.html", {
                "django_server_yuming": DJANGO_SERVER_YUMING
            })
        elif request.user.is_active:
            editandcheck = EditAndCheck.objects.get(id=int(editandcheck_id))  # 获取用例
            clickandback_all = ClickAndBack.objects.all().order_by("-id")
            is_with_relevance = 1
            return render(request, "editandcheck/editAndCheck.html",
                          {"editandcheck": editandcheck,
                           "clickandback_all": clickandback_all,
                           "django_server_yuming": DJANGO_SERVER_YUMING,
                           "is_withRelevance": is_with_relevance,
                           })
        else:
            return render(request, "addContentError.html", {
                "django_server_yuming": DJANGO_SERVER_YUMING
            })

    def post(self, request, editandcheck_id):
        username = request.user.username
        clickandback_all = ClickAndBack.objects.all().order_by("-id")
        editandcheck_form = EditAndCheckForm(request.POST)  # 实例化NewAddAndCheckForm()
        editandcheck = EditAndCheck.objects.get(id=int(editandcheck_id))  # 获取用例

        # 处理附带复制内容
        is_with_relevance = request.POST.get('is_withRelevance', '')
        print("is_withRelevance:%s" % is_with_relevance)
        print("is_withRelevance类型:%s" % type(is_with_relevance))
        is_with_relevance = int(is_with_relevance)
        print("is_withRelevance:%s" % is_with_relevance)
        print("is_withRelevance类型:%s" % type(is_with_relevance))
        # 结束处理

        if editandcheck_form.is_valid():  # is_valid()判断是否有错

            editandcheck_form.save(commit=True)  # 将信息保存到数据库中

            zj = EditAndCheck.objects.all().order_by('-add_time')[:1][0]  # 根据添加时间查询最新的
            user = User.objects.get(username=username)
            zj.write_user_id = user.id
            zj.save()

            editandcheckid = zj.id
            editandcheckadd = EditAndCheck.objects.get(id=int(editandcheckid))  # 获取用例

            # 如果增加附带
            if is_with_relevance == 1:
                print("处理附带内容")
                # 处理新增数据场景依赖的文本输入框
                inputtapinputtext_old_all = InputTapInputText.objects.filter(
                    editandcheck_id=editandcheck_id).order_by("id")
                inputtapinputtext_old_all_count = inputtapinputtext_old_all.count()
                if inputtapinputtext_old_all_count != 0:
                    for inputtapinputtext_old in inputtapinputtext_old_all:
                        inputtapinputtext_new = InputTapInputText()
                        inputtapinputtext_new.editandcheck_id = zj.id
                        inputtapinputtext_new.input_ele_find = inputtapinputtext_old.input_ele_find
                        inputtapinputtext_new.input_ele_find_value = inputtapinputtext_old.input_ele_find_value
                        inputtapinputtext_new.is_auto_input = inputtapinputtext_old.is_auto_input
                        inputtapinputtext_new.auto_input_type = inputtapinputtext_old.auto_input_type
                        inputtapinputtext_new.auto_input_long = inputtapinputtext_old.auto_input_long
                        inputtapinputtext_new.input_text = inputtapinputtext_old.input_text
                        inputtapinputtext_new.is_with_time = inputtapinputtext_old.is_with_time

                        inputtapinputtext_new.is_click_clear_icon = inputtapinputtext_old.is_click_clear_icon
                        inputtapinputtext_new.clear_icon_find = inputtapinputtext_old.clear_icon_find
                        inputtapinputtext_new.clear_icon_find_value = inputtapinputtext_old.clear_icon_find_value


                        inputtapinputtext_new.is_check = inputtapinputtext_old.is_check
                        inputtapinputtext_new.save()

                # 处理新增数据场景依赖的文件输入框
                inputtapinputfile_old_all = InputTapInputFile.objects.filter(
                    editandcheck_id=editandcheck_id).order_by("id")
                inputtapinputfile_old_all_count = inputtapinputfile_old_all.count()
                if inputtapinputfile_old_all_count != 0:
                    for inputtapinputfile_old in inputtapinputfile_old_all:
                        inputtapinputfile_new = InputTapInputFile()
                        inputtapinputfile_new.editandcheck_id = zj.id
                        inputtapinputfile_new.input_ele_find = inputtapinputfile_old.input_ele_find
                        inputtapinputfile_new.input_ele_find_value = inputtapinputfile_old.input_ele_find_value
                        inputtapinputfile_new.input_file = inputtapinputfile_old.input_file
                        inputtapinputfile_new.input_class_name = inputtapinputfile_old.input_class_name
                        inputtapinputfile_new.save()

                # 处理新增数据场景依赖的时间输入框
                inputtapinputdatetime_old_all = InputTapInputDateTime.objects.filter(
                    editandcheck_id=editandcheck_id).order_by("id")
                inputtapinputdatetime_old_all_count = inputtapinputdatetime_old_all.count()
                if inputtapinputdatetime_old_all_count != 0:
                    for inputtapinputdatetime_old in inputtapinputdatetime_old_all:
                        inputtapinputdatetime_new = InputTapInputDateTime()
                        inputtapinputdatetime_new.editandcheck_id = zj.id
                        inputtapinputdatetime_new.input_ele_find = inputtapinputdatetime_old.input_ele_find
                        inputtapinputdatetime_new.input_ele_find_value = inputtapinputdatetime_old.input_ele_find_value
                        inputtapinputdatetime_new.date_ele_find = inputtapinputdatetime_old.date_ele_find
                        inputtapinputdatetime_new.date_ele_find_value = inputtapinputdatetime_old.date_ele_find_value
                        inputtapinputdatetime_new.last_month_ele_find = inputtapinputdatetime_old.last_month_ele_find
                        inputtapinputdatetime_new.last_month_ele_find_value = inputtapinputdatetime_old.last_month_ele_find_value
                        inputtapinputdatetime_new.click_last_month_counts = inputtapinputdatetime_old.click_last_month_counts
                        inputtapinputdatetime_new.next_month_ele_find = inputtapinputdatetime_old.next_month_ele_find
                        inputtapinputdatetime_new.next_month_ele_find_value = inputtapinputdatetime_old.next_month_ele_find_value
                        inputtapinputdatetime_new.click_next_month_counts = inputtapinputdatetime_old.click_next_month_counts
                        inputtapinputdatetime_new.last_year_ele_find = inputtapinputdatetime_old.last_year_ele_find
                        inputtapinputdatetime_new.last_year_ele_find_value = inputtapinputdatetime_old.last_year_ele_find_value
                        inputtapinputdatetime_new.click_last_year_counts = inputtapinputdatetime_old.click_last_year_counts
                        inputtapinputdatetime_new.next_year_ele_find = inputtapinputdatetime_old.next_year_ele_find
                        inputtapinputdatetime_new.next_year_ele_find_value = inputtapinputdatetime_old.next_year_ele_find_value
                        inputtapinputdatetime_new.click_next_year_counts = inputtapinputdatetime_old.click_next_year_counts
                        inputtapinputdatetime_new.save()

                # 处理新增数据场景依赖的单选项和复选项
                radioandreelectionlabel_old_all = RadioAndReelectionLabel.objects.filter(
                    editandcheck_id=editandcheck_id).order_by("id")
                radioandreelectionlabel_old_all_count = radioandreelectionlabel_old_all.count()
                if radioandreelectionlabel_old_all_count != 0:
                    for radioandreelectionlabel_old in radioandreelectionlabel_old_all:
                        radioandreelectionlabel_new = RadioAndReelectionLabel()
                        radioandreelectionlabel_new.editandcheck_id = zj.id
                        radioandreelectionlabel_new.label_ele_find = radioandreelectionlabel_old.label_ele_find
                        radioandreelectionlabel_new.label_ele_find_value = radioandreelectionlabel_old.label_ele_find_value
                        radioandreelectionlabel_new.is_check = radioandreelectionlabel_old.is_check
                        radioandreelectionlabel_new.checked_add_attribute = radioandreelectionlabel_old.checked_add_attribute
                        radioandreelectionlabel_new.checked_add_attribute_value = radioandreelectionlabel_old.checked_add_attribute_value
                        radioandreelectionlabel_new.save()

                # 处理新增数据场景依赖的选项框
                selecttapselectoption_old_all = SelectTapSelectOption.objects.filter(
                    editandcheck_id=editandcheck_id).order_by("id")
                selecttapselectoption_old_all_count = selecttapselectoption_old_all.count()
                if selecttapselectoption_old_all_count != 0:
                    for selecttapselectoption_old in selecttapselectoption_old_all:
                        selecttapselectoption_new = SelectTapSelectOption()
                        selecttapselectoption_new.editandcheck_id = zj.id
                        selecttapselectoption_new.select_ele_find = selecttapselectoption_old.select_ele_find
                        selecttapselectoption_new.select_ele_find_value = selecttapselectoption_old.select_ele_find_value
                        selecttapselectoption_new.select_option_ele_find = selecttapselectoption_old.select_option_ele_find
                        selecttapselectoption_new.select_option_ele_find_value = selecttapselectoption_old.select_option_ele_find_value

                        selecttapselectoption_new.is_click_clear_icon = selecttapselectoption_old.is_click_clear_icon
                        selecttapselectoption_new.clear_icon_find = selecttapselectoption_old.clear_icon_find
                        selecttapselectoption_new.clear_icon_find_value = selecttapselectoption_old.clear_icon_find_value

                        selecttapselectoption_new.save()

                # 处理新增数据场景依赖的验证元素
                asserttiptext_old_all = AssertTipText.objects.filter(editandcheck_id=editandcheck_id).order_by("id")
                asserttiptext_old_all_count = asserttiptext_old_all.count()
                if asserttiptext_old_all_count != 0:
                    for asserttiptext_old in asserttiptext_old_all:
                        asserttiptext_new = AssertTipText()
                        asserttiptext_new.editandcheck_id = zj.id
                        asserttiptext_new.tip_ele_find = asserttiptext_old.tip_ele_find
                        asserttiptext_new.tip_ele_find_value = asserttiptext_old.tip_ele_find_value
                        asserttiptext_new.tip_text = asserttiptext_old.tip_text
                        asserttiptext_new.save()

                # 处理新增数据场景依赖的富文本输入框
                iframebodyinputtext_old_all = IframeBodyInputText.objects.filter(
                    editandcheck_id=editandcheck_id).order_by("id")
                iframebodyinputtext_old_all_count = iframebodyinputtext_old_all.count()
                if iframebodyinputtext_old_all_count != 0:
                    for iframebodyinputtext_old in iframebodyinputtext_old_all:
                        iframebodyinputtext_new = IframeBodyInputText()
                        iframebodyinputtext_new.editandcheck_id = zj.id
                        iframebodyinputtext_new.iframe_ele_find = iframebodyinputtext_old.iframe_ele_find
                        iframebodyinputtext_new.iframe_ele_find_value = iframebodyinputtext_old.iframe_ele_find_value
                        iframebodyinputtext_new.input_ele_find = iframebodyinputtext_old.input_ele_find
                        iframebodyinputtext_new.input_ele_find_value = iframebodyinputtext_old.input_ele_find_value
                        iframebodyinputtext_new.is_auto_input = iframebodyinputtext_old.is_auto_input
                        iframebodyinputtext_new.auto_input_type = iframebodyinputtext_old.auto_input_type
                        iframebodyinputtext_new.auto_input_long = iframebodyinputtext_old.auto_input_long
                        iframebodyinputtext_new.input_text = iframebodyinputtext_old.input_text
                        iframebodyinputtext_new.is_with_time = iframebodyinputtext_old.is_with_time
                        iframebodyinputtext_new.is_check = iframebodyinputtext_old.is_check
                        iframebodyinputtext_new.save()

            return render(request, "editandcheck/editAndCheck.html", {
                "editandcheck": editandcheckadd,
                "clickandback_all": clickandback_all,
                "sumsg": u"添加测试用例---【{}】---成功,请继续添加".format(editandcheckadd.test_case_title),
                "django_server_yuming": DJANGO_SERVER_YUMING,
                "is_withRelevance": is_with_relevance,
            })
        else:
            return render(request, 'editandcheck/editAndCheckForm.html', {
                "editandcheck":editandcheck,
                "clickandback_all": clickandback_all,
                "editandcheckform": editandcheck_form,
                "errmsg": u"添加失败，请重新添加，添加时请检查各个字段是否填写",
                "django_server_yuming": DJANGO_SERVER_YUMING,
                "is_withRelevance": is_with_relevance,
            })  # 返回页面，回填信息