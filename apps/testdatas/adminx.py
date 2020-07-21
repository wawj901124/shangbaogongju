import xadmin

from .models import ClickAndBack,User,NewAddAndCheck,SearchAndCheck,DeleteAndCheck,EditAndCheck
from .models import InputTapInputText,InputTapInputFile,InputTapInputDateTime,SelectTapSelectOption,AssertTipText
from .models import IframeBodyInputText
from .models import RadioAndReelectionLabel
from .models import SearchInputTapInputText,SearchSelectTapSelectOption
from .models import LoginAndCheck


class LoginAndCheckXadmin(object):
    all_zi_duan = ["id", "test_project", "test_module", "test_page",
                   "case_priority",
                   "test_case_title", "is_run_case",
                   "login_url",
                   "is_auto_input_code","code_image_xpath",
                   "code_type","code_input_ele_find",
                   "code_input_ele_find_value",
                   "login_button_ele_find",
                   "login_button_ele_find_value","click_login_button_delay_time",
                   "case_counts",  "write_user",
                   "add_time", "update_time"]
    list_display = ["test_project", "test_module", "test_page",
                    "case_priority",
                    "test_case_title", "is_run_case",
                    "login_url",
                    "is_auto_input_code", "code_image_xpath",
                    "code_type", "code_input_ele_find",
                    "code_input_ele_find_value",

                    "login_button_ele_find",
                    "login_button_ele_find_value", "click_login_button_delay_time",

                    "case_counts",
                    "go_to"]  # 定义显示的字段
    list_filter = ["test_project", "test_module", "test_page",
                   "test_case_title", "is_run_case",
                   "write_user"]  # 定义筛选的字段
    search_fields = ["test_project", "test_module", "test_page",
                   "test_case_title"]   # 定义搜索字段
    model_icon = "fa fa-file-text"  # 定义图标显示
    ordering = ["-add_time"]  # 添加默认排序规则显示排序，根据添加时间倒序排序
    readonly_fields = ["write_user", "add_time",
                       "update_time"]  # 设置某些字段为只为可读  #设置了readonly_fields，再设置exclude，exclude对该字段无效，

    # exclude = ['case_step']  # 设置某些字段为不显示，即隐藏  #readonly_fields和exclude设置会有冲突
    # inlines = [TestCaseInline]  # inlines配和TestCaseInline使用，可以直接在项目页面添加测试用例#只能做一层嵌套，不能进行两层嵌套

    list_editable = all_zi_duan  # 可以在列表页对字段进行编辑
    refresh_times = [3, 5]  # 对列表页进行定时刷新,配置了3秒和5秒，可以从中选择一个
    list_per_page = 50  # 每页设置50条数据，默认每页展示100条数据
    # fk_fields = ['test_project_id',]  #设置显示外键字段，未生效
    list_display_links = ["test_case_title", ]  # 设置点击链接进入编辑页面的字段
    # date_hierarchy = 'add_time'   #详细时间分层筛选，未生效
    show_detail_fields = ["test_project", ]  # 显示数据详情

    list_export = ('xls',)  # 控制列表页导出数据的可选格式
    show_bookmarks = True  # 控制是否显示书签功能

    # 设置是否加入导入插件
    import_excel = True  # True表示显示使用插件，False表示不显示使用插件，该import_excel变量会覆盖插件中的变量

    #设置内联
    class InputTapInputTextInline(object):
        model = InputTapInputText
        exclude = ["add_time","update_time","newaddandcheck","editandcheck","loginandcheck"]
        extra = 1
        style = 'tab'    #以标签形式展示

    #设置内联
    class AssertTipTextInline(object):
        model = AssertTipText
        exclude = ["add_time","update_time","newaddandcheck","editandcheck","loginandcheck"]
        extra = 1
        style = 'tab'    #以标签形式展示


    inlines = [InputTapInputTextInline,AssertTipTextInline,]


    def save_models(self):  # 重载save_models的方法，可以在做了某个动作后，动态重新加载
        obj = self.new_obj  # 取得当前用例的实例
        if self.request.user.is_superuser:  # 超级用户则不对编写人做修改
            obj.save()  # 保存当前用例
        else:  # 非超级用户会自动保存编写人
            user = User.objects.get(username=self.request.user)
            obj.write_user_id = user.id  # 保存当前的write_user为用户登录的user
            obj.save()  # 保存当前用例

    def queryset(self):  # 重载queryset方法，用来做到不同的admin取出的数据不同
        qs = super(LoginAndCheckXadmin, self).queryset()  # 调用父类
        if self.request.user.is_superuser:  # 超级用户可查看所有数据
            return qs
        else:
            qs = qs.filter(write_user=self.request.user)  # 否则只显示本用户数据
            return qs  # 返回qs

    def post(self, request, *args, **kwargs):  # 重载post函数，用于判断导入的逻辑
        if 'excel' in request.FILES:  # 如果excel在request.FILES中
            excel_file = request.FILES.get('excel', '')

            import xlrd  # 导入xlrd
            # 常用的Excel文件有.xls和.xls两种，.xls文件读取时需要设置formatting_info = True
            # data = xlrd.open_workbook(filename=None, file_contents=excel_file.read())  # xlsx文件

            exceldata = xlrd.open_workbook(filename=None, file_contents=excel_file.read(),
                                           formatting_info=True)  # xls文件

            from .analyzexls import Analyzexls
            analyzexls = Analyzexls()
            # 将获取的数据循环导入数据库中
            all_list_1 = analyzexls.get_sheets_mg(exceldata, 0)
            i = 0
            if len(all_list_1[0]) == 17:
                while i < len(all_list_1):
                    newaddandcheck = NewAddAndCheck()  # 数据库的对象等于ClickAndBack,实例化
                    newaddandcheck.test_project = all_list_1[i][0]  # 填写项目all_list_1[i][j]
                    newaddandcheck.test_module = all_list_1[i][1]  # 填写模块
                    newaddandcheck.test_page = all_list_1[i][2]  # 填写测试页

                    if all_list_1[i][3] == u"冒烟用例":
                        newaddandcheck.case_priority = "P0" # 填写用例优先级
                    elif all_list_1[i][3] == u"系统的重要功能用例":
                        newaddandcheck.case_priority = "P1"  # 填写用例优先级
                    elif all_list_1[i][3] == u"系统的一般功能用例":
                        newaddandcheck.case_priority = "P2"  # 填写用例优先级
                    elif all_list_1[i][3] == u"极低级别的用例":
                        newaddandcheck.case_priority = "P3"  # 填写用例优先级


                    newaddandcheck.test_case_title = all_list_1[i][4]  # 填写测试内容的名称
                    newaddandcheck.is_run_case =all_list_1[i][5]  # 填写是否运行

                    newaddandcheck.login_url = all_list_1[i][6]  # 填写登录页的url

                    newaddandcheck.is_auto_input_code = all_list_1[i][7]  # 填写是否自动输入验证码
                    newaddandcheck.code_image_xpath =all_list_1[i][8]  # 填写验证码xpath路径

                    newaddandcheck.code_type = all_list_1[i][9]  # 填写验证码类型
                    newaddandcheck.code_input_ele_find =all_list_1[i][10]  # 填写验证码输入框查找风格
                    newaddandcheck.code_input_ele_find_value = all_list_1[i][11]  # 填写验证码输入框查找风格的确切值

                    newaddandcheck.login_button_ele_find = all_list_1[i][12]  # 填写确定按钮查找风格的确切值
                    newaddandcheck.login_button_ele_find_value = all_list_1[i][13] # 填写是否点击取消按钮
                    newaddandcheck.click_login_button_delay_time = all_list_1[i][14]  # 填写取消按钮查找风格

                    newaddandcheck.case_counts = all_list_1[i][15]  # 填写case_counts
                    if all_list_1[i][16] != None:  # 如果编写人列有数据则填写编写人
                        users = User.objects.all()
                        for user in users:
                            if user.username == all_list_1[i][16]:
                                newaddandcheck.write_user_id = user.id  # 填写编写人
                    newaddandcheck.save()  # 保存到数据库

                    i = i + 1
            pass
        return super(LoginAndCheckXadmin,self).post(request,*args,**kwargs)  # 必须调用clickandbackAdmin父类，再调用post方法，否则会报错
        # 一定不要忘记，否则整个ClickAndBackXAdmin保存都会出错


class ClickAndBackXAdmin(object):
    all_zi_duan = ["id","test_project","test_module","test_page",
                   "test_case_title","is_run_case",
                   "is_static_load_page_time",
                   "current_page_click_ele_find","current_page_click_ele_find_value",
                   "is_new",
                   "next_page_check_ele_find","next_page_check_ele_find_value",
                   "case_counts","depend_case","write_user",
                   "add_time","update_time"]
    list_display =  ["test_project","test_module","test_page",
                   "test_case_title","is_run_case",
                    "is_static_load_page_time",
                     "current_page_click_ele_find","current_page_click_ele_find_value",
                    "is_new",
                   "next_page_check_ele_find","next_page_check_ele_find_value",
                   "case_counts","depend_case",
                    "go_to"]   #定义显示的字段
    list_filter =  ["test_project","test_module","test_page",
                   "test_case_title","is_run_case","is_new",
                    "write_user"] #定义筛选的字段
    search_fields = ["test_project", "test_module", "test_page",
                   "test_case_title"]    #定义搜索字段
    model_icon = "fa fa-file-text" # 定义图标显示
    ordering = ["-add_time"]  # 添加默认排序规则显示排序，根据添加时间倒序排序
    readonly_fields = ["write_user","add_time","update_time"]  # 设置某些字段为只为可读  #设置了readonly_fields，再设置exclude，exclude对该字段无效，

    # exclude = ['case_step']  # 设置某些字段为不显示，即隐藏  #readonly_fields和exclude设置会有冲突
    # inlines = [TestCaseInline]  # inlines配和TestCaseInline使用，可以直接在项目页面添加测试用例#只能做一层嵌套，不能进行两层嵌套

    list_editable = all_zi_duan   # 可以在列表页对字段进行编辑
    refresh_times = [3, 5]  # 对列表页进行定时刷新,配置了3秒和5秒，可以从中选择一个
    list_per_page = 50   #每页设置50条数据，默认每页展示100条数据
    # fk_fields = ['test_project_id',]  #设置显示外键字段，未生效
    list_display_links = ["test_case_title",]   #设置点击链接进入编辑页面的字段
    # date_hierarchy = 'add_time'   #详细时间分层筛选，未生效
    show_detail_fields = ["test_project",]   #显示数据详情

    list_export = ('xls',)  #控制列表页导出数据的可选格式
    show_bookmarks = True   #控制是否显示书签功能

    #设置是否加入导入插件
    import_excel = True   #True表示显示使用插件，False表示不显示使用插件，该import_excel变量会覆盖插件中的变量

    #重载get_context方法，只显示本用户添加的点击场景的用例
    def get_context(self):
        context = super(ClickAndBackXAdmin, self).get_context()   #调用父类

        if 'form' in context:   #固定写法
            if self.request.user.is_superuser:  # 超级用户则返回所有
                context['form'].fields['depend_case'].queryset = ClickAndBack.objects.all()
            else:  # 非超级用户则只返回本用户添加的点击场景的用例
                context['form'].fields['depend_case'].queryset = ClickAndBack.objects.filter(write_user=self.request.user)   #取form中的depend_click_case（与model中的字段相同），只取当前用户填写的数据
        return context

    def save_models(self):   #重载save_models的方法，可以在做了某个动作后，动态重新加载
        obj = self.new_obj   #取得当前用例的实例
        if self.request.user.is_superuser:  # 超级用户则不对编写人做修改
            obj.save()  # 保存当前用例
        else:    #非超级用户会自动保存编写人
            user = User.objects.get(username=self.request.user)
            obj.write_user_id = user.id  #保存当前的write_user为用户登录的user
            obj.save()   #保存当前用例


    def queryset(self):   #重载queryset方法，用来做到不同的admin取出的数据不同
        qs = super(ClickAndBackXAdmin, self).queryset()   #调用父类
        if self.request.user.is_superuser:   #超级用户可查看所有数据
            return qs
        else:
            qs = qs.filter(write_user=self.request.user)  #否则只显示本用户数据
            return qs   #返回qs

    def post(self,request, *args,**kwargs):   #重载post函数，用于判断导入的逻辑
        if 'excel' in request.FILES:  #如果excel在request.FILES中
            excel_file = request.FILES.get('excel', '')

            import xlrd   #导入xlrd
            #常用的Excel文件有.xls和.xls两种，.xls文件读取时需要设置formatting_info = True
            # data = xlrd.open_workbook(filename=None, file_contents=excel_file.read())  # xlsx文件

            exceldata = xlrd.open_workbook(filename=None, file_contents=excel_file.read(), formatting_info=True)  # xls文件

            from .analyzexls import Analyzexls
            analyzexls = Analyzexls()
            #将获取的数据循环导入数据库中
            all_list_1 = analyzexls.get_sheets_mg(exceldata, 0)
            i = 0
            if len(all_list_1[0]) == 14:
                while i < len(all_list_1):
                    clickandback = ClickAndBack()  # 数据库的对象等于ClickAndBack,实例化
                    clickandback.test_project = all_list_1[i][0]  # 填写项目all_list_1[i][j]
                    clickandback.test_module = all_list_1[i][1]  # 填写模块
                    clickandback.test_page = all_list_1[i][2]  # 填写测试页
                    clickandback.test_case_title = all_list_1[i][3]  # 填写测试内容的名称
                    clickandback.is_run_case = all_list_1[i][4]  # 填写是否运行
                    clickandback.is_static_load_page_time = all_list_1[i][5]  # 填写是否统计页面加载时间
                    # if all_list_1[i][4] == "TRUE":
                    #     clickandback.is_run_case = 1 # 填写是否运行
                    # elif all_list_1[i][4] == "FALSE":
                    #     clickandback.is_run_case = 0  # 填写是否运行

                    clickandback.current_page_click_ele_find = all_list_1[i][6]  # 填写当前页面要点击元素查找风格
                    clickandback.current_page_click_ele_find_value = all_list_1[i][7]  # 填写当前页面要点击元素查找风格的确切值
                    clickandback.is_new = all_list_1[i][8]  # 填写是否新窗口
                    # if all_list_1[i][7] == "TRUE":
                    #     clickandback.is_new = 1  # 填写是否新窗口
                    # elif all_list_1[i][7] == "FALSE":
                    #     clickandback.is_new = 0  # 填写是否新窗口
                    clickandback.next_page_check_ele_find = all_list_1[i][8]  # 填写next_page_check_ele_find
                    clickandback.next_page_check_ele_find_value = all_list_1[i][10]  # 填写next_page_check_ele_find_value
                    clickandback.case_counts = all_list_1[i][11] # 填写case_counts

                    if all_list_1[i][12] != None:  #如果依赖列有内容且内容存在数据库中，则保存依赖内容
                        depend = all_list_1[i][12]
                        depend_contents = ClickAndBack.objects.filter(test_case_title=depend)
                        depend_count = depend_contents.count()
                        if depend_count == 1:
                            for depend_content in depend_contents:
                                clickandback.depend_case_id = depend_content.id

                    if all_list_1[i][13] != None:  # 如果编写人列有数据则填写编写人
                        users = User.objects.all()
                        for user in users:
                            if user.username == all_list_1[i][13]:
                                clickandback.write_user_id = user.id   # 填写编写人
                    clickandback.save()  # 保存到数据库

                    i = i+1
            pass
        return super(ClickAndBackXAdmin,self).post(request,*args,**kwargs)   #必须调用clickandbackAdmin父类，再调用post方法，否则会报错
                                                                      #一定不要忘记，否则整个ClickAndBackXAdmin保存都会出错


class NewAddAndCheckXadmin(object):
    all_zi_duan = ["id", "test_project", "test_module", "test_page",
                   "case_priority",
                   "test_case_title", "is_run_case",
                   # "depend_new_add_and_check_case",
                   "depend_click_case","confirm_ele_find",
                   "confirm_ele_find_value",
                   "click_confirm_delay_time",
                   "is_click_cancel",
                   "cancel_ele_find","cancel_ele_find_value",
                   "is_submit_success",
                   "is_signel_page","page_number_xpath",
                   "result_table_ele_find","result_table_ele_find_value",
                   "table_colnum_counts",
                   "case_counts",  "write_user",
                   "add_time", "update_time"]
    list_display = ["test_project", "test_module", "test_page",
                    "case_priority",
                    "test_case_title", "is_run_case",
                    # "depend_new_add_and_check_case",
                    "depend_click_case", "confirm_ele_find",
                    "confirm_ele_find_value",
                    "click_confirm_delay_time",
                    "is_click_cancel",
                    "cancel_ele_find", "cancel_ele_find_value",
                    "is_submit_success",
                    "is_signel_page", "page_number_xpath",
                    "result_table_ele_find", "result_table_ele_find_value",
                    "table_colnum_counts",
                    "case_counts",
                    "go_to_with_relevance"]  # 定义显示的字段
    list_filter = ["test_project", "test_module", "test_page",
                   "test_case_title", "is_run_case",
                   "write_user"]  # 定义筛选的字段
    search_fields = ["test_project", "test_module", "test_page",
                   "test_case_title"]   # 定义搜索字段
    model_icon = "fa fa-file-text"  # 定义图标显示
    ordering = ["-add_time"]  # 添加默认排序规则显示排序，根据添加时间倒序排序
    readonly_fields = ["write_user", "add_time",
                       "update_time"]  # 设置某些字段为只为可读  #设置了readonly_fields，再设置exclude，exclude对该字段无效，

    # exclude = ['case_step']  # 设置某些字段为不显示，即隐藏  #readonly_fields和exclude设置会有冲突
    # inlines = [TestCaseInline]  # inlines配和TestCaseInline使用，可以直接在项目页面添加测试用例#只能做一层嵌套，不能进行两层嵌套

    list_editable = all_zi_duan  # 可以在列表页对字段进行编辑
    refresh_times = [3, 5]  # 对列表页进行定时刷新,配置了3秒和5秒，可以从中选择一个
    list_per_page = 50  # 每页设置50条数据，默认每页展示100条数据
    # fk_fields = ['test_project_id',]  #设置显示外键字段，未生效
    list_display_links = ["test_case_title", ]  # 设置点击链接进入编辑页面的字段
    # date_hierarchy = 'add_time'   #详细时间分层筛选，未生效
    show_detail_fields = ["test_project", ]  # 显示数据详情

    list_export = ('xls',)  # 控制列表页导出数据的可选格式
    show_bookmarks = True  # 控制是否显示书签功能

    # 设置是否加入导入插件
    import_excel = True  # True表示显示使用插件，False表示不显示使用插件，该import_excel变量会覆盖插件中的变量

    #设置内联
    class InputTapInputTextInline(object):
        model = InputTapInputText
        exclude = ["add_time","update_time","newaddandcheck","editandcheck","loginandcheck"]
        extra = 1
        style = 'tab'    #以标签形式展示

    #设置内联
    class InputTapInputFileInline(object):
        model = InputTapInputFile
        exclude = ["add_time","update_time","newaddandcheck","editandcheck",]
        extra = 1
        style = 'tab'    #以标签形式展示

    #设置内联
    class InputTapInputDateTimeInline(object):
        model = InputTapInputDateTime
        exclude = ["add_time","update_time","newaddandcheck","editandcheck",]
        extra = 1
        style = 'tab'    #以标签形式展示

    # 设置内联
    class RadioAndReelectionLabelInline(object):
        model = RadioAndReelectionLabel
        exclude = ["add_time", "update_time","newaddandcheck","editandcheck",]
        extra = 1
        style = 'tab'  # 以标签形式展示

    #设置内联
    class SelectTapSelectOptionInline(object):
        model = SelectTapSelectOption
        exclude = ["add_time","update_time","newaddandcheck","editandcheck",]
        extra = 1
        style = 'tab'    #以标签形式展示

    #设置内联
    class AssertTipTextInline(object):
        model = AssertTipText
        exclude = ["add_time","update_time","newaddandcheck","editandcheck","loginandcheck"]
        extra = 1
        style = 'tab'    #以标签形式展示

    #设置内联
    class IframeBodyInputTextInline(object):
        model = IframeBodyInputText
        exclude = ["add_time","update_time","newaddandcheck","editandcheck",]
        extra = 1
        style = 'tab'    #以标签形式展示

    inlines = [InputTapInputTextInline,InputTapInputFileInline,InputTapInputDateTimeInline,
               RadioAndReelectionLabelInline,
               SelectTapSelectOptionInline,AssertTipTextInline,
               IframeBodyInputTextInline,]

    #重载get_context方法，只显示本用户添加的点击场景的用例
    def get_context(self):
        context = super(NewAddAndCheckXadmin, self).get_context()   #调用父类

        if 'form' in context:   #固定写法
            if self.request.user.is_superuser:  # 超级用户则返回所有
                context['form'].fields['depend_click_case'].queryset = ClickAndBack.objects.all()
            else:  # 非超级用户则只返回本用户添加的点击场景的用例
                context['form'].fields['depend_click_case'].queryset = ClickAndBack.objects.filter(write_user=self.request.user)   #取form中的depend_click_case（与model中的字段相同），只取当前用户填写的数据
        return context

    def save_models(self):  # 重载save_models的方法，可以在做了某个动作后，动态重新加载
        obj = self.new_obj  # 取得当前用例的实例
        if self.request.user.is_superuser:  # 超级用户则不对编写人做修改
            obj.save()  # 保存当前用例
        else:  # 非超级用户会自动保存编写人
            user = User.objects.get(username=self.request.user)
            obj.write_user_id = user.id  # 保存当前的write_user为用户登录的user
            obj.save()  # 保存当前用例

    def queryset(self):  # 重载queryset方法，用来做到不同的admin取出的数据不同
        qs = super(NewAddAndCheckXadmin, self).queryset()  # 调用父类
        if self.request.user.is_superuser:  # 超级用户可查看所有数据
            return qs
        else:
            qs = qs.filter(write_user=self.request.user)  # 否则只显示本用户数据
            return qs  # 返回qs

    def post(self, request, *args, **kwargs):  # 重载post函数，用于判断导入的逻辑
        if 'excel' in request.FILES:  # 如果excel在request.FILES中
            excel_file = request.FILES.get('excel', '')

            import xlrd  # 导入xlrd
            # 常用的Excel文件有.xls和.xls两种，.xls文件读取时需要设置formatting_info = True
            # data = xlrd.open_workbook(filename=None, file_contents=excel_file.read())  # xlsx文件

            exceldata = xlrd.open_workbook(filename=None, file_contents=excel_file.read(),
                                           formatting_info=True)  # xls文件

            from .analyzexls import Analyzexls
            analyzexls = Analyzexls()
            # 将获取的数据循环导入数据库中
            all_list_1 = analyzexls.get_sheets_mg(exceldata, 0)
            i = 0
            if len(all_list_1[0]) == 20:
                while i < len(all_list_1):
                    newaddandcheck = NewAddAndCheck()  # 数据库的对象等于ClickAndBack,实例化
                    newaddandcheck.test_project = all_list_1[i][0]  # 填写项目all_list_1[i][j]
                    newaddandcheck.test_module = all_list_1[i][1]  # 填写模块
                    newaddandcheck.test_page = all_list_1[i][2]  # 填写测试页

                    if all_list_1[i][3] == u"冒烟用例":
                        newaddandcheck.case_priority = "P0" # 填写用例优先级
                    elif all_list_1[i][3] == u"系统的重要功能用例":
                        newaddandcheck.case_priority = "P1"  # 填写用例优先级
                    elif all_list_1[i][3] == u"系统的一般功能用例":
                        newaddandcheck.case_priority = "P2"  # 填写用例优先级
                    elif all_list_1[i][3] == u"极低级别的用例":
                        newaddandcheck.case_priority = "P3"  # 填写用例优先级


                    newaddandcheck.test_case_title = all_list_1[i][4]  # 填写测试内容的名称
                    newaddandcheck.is_run_case =all_list_1[i][5]  # 填写是否运行
                    if all_list_1[i][6] != None:  # 如果依赖列有内容且内容存在数据库中，则保存依赖内容
                        depend = all_list_1[i][6]
                        depend_contents = ClickAndBack.objects.filter(test_case_title=depend)
                        depend_count = depend_contents.count()
                        if depend_count == 1:
                            for depend_content in depend_contents:
                                newaddandcheck.depend_click_case_id = depend_content.id

                    newaddandcheck.confirm_ele_find = all_list_1[i][7]  # 填写确定按钮查找风格
                    newaddandcheck.confirm_ele_find_value = all_list_1[i][8]  # 填写确定按钮查找风格的确切值
                    newaddandcheck.is_click_cancel = all_list_1[i][9] # 填写是否点击取消按钮
                    newaddandcheck.cancel_ele_find = all_list_1[i][10]  # 填写取消按钮查找风格
                    newaddandcheck.cancel_ele_find_value = all_list_1[i][11]  # 填写取消按钮查找风格的确切值
                    newaddandcheck.is_submit_success = all_list_1[i][12] # 填写是否添加成功
                    newaddandcheck.is_signel_page = all_list_1[i][13]  # 填写是否单页面

                    newaddandcheck.page_number_xpath = all_list_1[i][14]  # 填写页数层xpath路径值
                    newaddandcheck.result_table_ele_find = all_list_1[i][15]  # 填写结果表格查找风格
                    newaddandcheck.result_table_ele_find_value = all_list_1[i][16] # 填写结果表格查找风格的确切值
                    newaddandcheck.table_colnum_counts = all_list_1[i][17]  # 填写结果表格总列数

                    newaddandcheck.case_counts = all_list_1[i][18]  # 填写case_counts
                    if all_list_1[i][19] != None:  # 如果编写人列有数据则填写编写人
                        users = User.objects.all()
                        for user in users:
                            if user.username == all_list_1[i][19]:
                                newaddandcheck.write_user_id = user.id  # 填写编写人
                    newaddandcheck.save()  # 保存到数据库

                    i = i + 1
            pass
        return super(NewAddAndCheckXadmin,self).post(request,*args,**kwargs)  # 必须调用clickandbackAdmin父类，再调用post方法，否则会报错
        # 一定不要忘记，否则整个ClickAndBackXAdmin保存都会出错


class SearchAndCheckXadmin(object):
    all_zi_duan = ["id", "test_project", "test_module", "test_page",
                   "case_priority",
                   "test_case_title", "is_run_case",
                   "search_ele_find",
                   "search_ele_find_value",
                   "is_with_date",
                   "result_table_ele_find","result_table_ele_find_value",
                   "case_counts", "depend_click_case",
                   "write_user",
                   "add_time", "update_time"]
    list_display = ["test_project", "test_module", "test_page",
                    "case_priority",
                    "test_case_title", "is_run_case",
                    "search_ele_find",
                    "search_ele_find_value",
                    "is_with_date",
                    "result_table_ele_find", "result_table_ele_find_value",
                    "case_counts","depend_click_case",
                    "go_to_with_relevance"]  # 定义显示的字段
    list_filter = ["test_project", "test_module", "test_page",
                   "test_case_title", "is_run_case",
                   "write_user"]  # 定义筛选的字段
    search_fields = ["test_project", "test_module", "test_page",
                   "test_case_title"]   # 定义搜索字段
    model_icon = "fa fa-file-text"  # 定义图标显示
    ordering = ["-add_time"]  # 添加默认排序规则显示排序，根据添加时间倒序排序
    readonly_fields = ["write_user", "add_time",
                       "update_time"]  # 设置某些字段为只为可读  #设置了readonly_fields，再设置exclude，exclude对该字段无效，

    # exclude = ['case_step']  # 设置某些字段为不显示，即隐藏  #readonly_fields和exclude设置会有冲突
    # inlines = [TestCaseInline]  # inlines配和TestCaseInline使用，可以直接在项目页面添加测试用例#只能做一层嵌套，不能进行两层嵌套

    list_editable = all_zi_duan  # 可以在列表页对字段进行编辑
    refresh_times = [3, 5]  # 对列表页进行定时刷新,配置了3秒和5秒，可以从中选择一个
    list_per_page = 50  # 每页设置50条数据，默认每页展示100条数据
    # fk_fields = ['test_project_id',]  #设置显示外键字段，未生效
    list_display_links = ["test_case_title", ]  # 设置点击链接进入编辑页面的字段
    # date_hierarchy = 'add_time'   #详细时间分层筛选，未生效
    show_detail_fields = ["test_project", ]  # 显示数据详情

    list_export = ('xls',)  # 控制列表页导出数据的可选格式
    show_bookmarks = True  # 控制是否显示书签功能

    # 设置是否加入导入插件
    import_excel = True  # True表示显示使用插件，False表示不显示使用插件，该import_excel变量会覆盖插件中的变量

    #设置内联
    class SearchInputTapInputTextInline(object):
        model = SearchInputTapInputText
        exclude = ["add_time","update_time"]
        extra = 1
        style = 'tab'    #以标签形式展示

    #设置内联
    class SearchSelectTapSelectOptionInline(object):
        model = SearchSelectTapSelectOption
        exclude = ["add_time","update_time"]
        extra = 1
        style = 'tab'    #以标签形式展示


    inlines = [SearchInputTapInputTextInline,SearchSelectTapSelectOptionInline]

    #重载get_context方法，只显示本用户添加的点击场景的用例
    def get_context(self):
        context = super(SearchAndCheckXadmin, self).get_context()   #调用父类

        if 'form' in context:   #固定写法
            if self.request.user.is_superuser:  # 超级用户则返回所有
                context['form'].fields['depend_click_case'].queryset = ClickAndBack.objects.all()
            else:  # 非超级用户则只返回本用户添加的点击场景的用例
                context['form'].fields['depend_click_case'].queryset = ClickAndBack.objects.filter(write_user=self.request.user)   #取form中的depend_click_case（与model中的字段相同），只取当前用户填写的数据
        return context

    def save_models(self):  # 重载save_models的方法，可以在做了某个动作后，动态重新加载
        obj = self.new_obj  # 取得当前用例的实例
        if self.request.user.is_superuser:  # 超级用户则不对编写人做修改
            obj.save()  # 保存当前用例
        else:  # 非超级用户会自动保存编写人
            user = User.objects.get(username=self.request.user)
            obj.write_user_id = user.id  # 保存当前的write_user为用户登录的user
            obj.save()  # 保存当前用例

    def queryset(self):  # 重载queryset方法，用来做到不同的admin取出的数据不同
        qs = super(SearchAndCheckXadmin, self).queryset()  # 调用父类
        if self.request.user.is_superuser:  # 超级用户可查看所有数据
            return qs
        else:
            qs = qs.filter(write_user=self.request.user)  # 否则只显示本用户数据
            return qs  # 返回qs

    def post(self, request, *args, **kwargs):  # 重载post函数，用于判断导入的逻辑
        if 'excel' in request.FILES:  # 如果excel在request.FILES中
            excel_file = request.FILES.get('excel', '')

            import xlrd  # 导入xlrd
            # 常用的Excel文件有.xls和.xls两种，.xls文件读取时需要设置formatting_info = True
            # data = xlrd.open_workbook(filename=None, file_contents=excel_file.read())  # xlsx文件

            exceldata = xlrd.open_workbook(filename=None, file_contents=excel_file.read(),
                                           formatting_info=True)  # xls文件

            from .analyzexls import Analyzexls
            analyzexls = Analyzexls()
            # 将获取的数据循环导入数据库中
            all_list_1 = analyzexls.get_sheets_mg(exceldata, 0)
            i = 0
            if len(all_list_1[0]) == 14:
                while i < len(all_list_1):
                    searchandcheck = SearchAndCheck()  # 数据库的对象等于SearchAndCheck,实例化
                    searchandcheck.test_project = all_list_1[i][0]  # 填写项目all_list_1[i][j]
                    searchandcheck.test_module = all_list_1[i][1]  # 填写模块
                    searchandcheck.test_page = all_list_1[i][2]  # 填写测试页
                    if all_list_1[i][3] == u"冒烟用例":
                        searchandcheck.case_priority = "P0" # 填写用例优先级
                    elif all_list_1[i][3] == u"系统的重要功能用例":
                        searchandcheck.case_priority = "P1"  # 填写用例优先级
                    elif all_list_1[i][3] == u"系统的一般功能用例":
                        searchandcheck.case_priority = "P2"  # 填写用例优先级
                    elif all_list_1[i][3] == u"极低级别的用例":
                        searchandcheck.case_priority = "P3"  # 填写用例优先级

                    searchandcheck.test_case_title = all_list_1[i][4]  # 填写测试内容的名称
                    searchandcheck.is_run_case = all_list_1[i][5]  # 填写是否运行
                    # if all_list_1[i][4] == "TRUE":
                    #     searchandcheck.is_run_case = 1  # 填写是否运行
                    # elif all_list_1[i][4] == "FALSE":
                    #     searchandcheck.is_run_case = 0  # 填写是否运行

                    searchandcheck.search_ele_find = all_list_1[i][6]  # 填写查询按钮查找风格
                    searchandcheck.search_ele_find_value = all_list_1[i][7]  # 填写查询按钮查找风格的确切值
                    searchandcheck.is_with_date = all_list_1[i][8]  # 填写是否查询到数据
                    # if all_list_1[i][7] == "TRUE":
                    #     searchandcheck.is_with_date = "1"  # 填写是否查询到数据
                    # elif all_list_1[i][7] == "FALSE":
                    #     searchandcheck.is_with_date = "0"  # 填写是否查询到数据
                    searchandcheck.result_table_ele_find = all_list_1[i][9]  # 填写结果表格查找风格
                    searchandcheck.result_table_ele_find_value = all_list_1[i][10]  # 填写结果表格查找风格的确切值
                    searchandcheck.case_counts = all_list_1[i][11]  # 填写case_counts

                    if all_list_1[i][12] != None:  # 如果依赖列有内容且内容存在数据库中，则保存依赖内容
                        depend = all_list_1[i][12]
                        depend_contents = ClickAndBack.objects.filter(test_case_title=depend)
                        depend_count = depend_contents.count()
                        if depend_count == 1:
                            for depend_content in depend_contents:
                                searchandcheck.depend_click_case_id = depend_content.id

                    if all_list_1[i][13] != None:  # 如果编写人列有数据则填写编写人
                        users = User.objects.all()
                        for user in users:
                            if user.username == all_list_1[i][13]:
                                searchandcheck.write_user_id = user.id  # 填写编写人
                    searchandcheck.save()  # 保存到数据库

                    i = i + 1
            pass
        return super(SearchAndCheckXadmin, self).post(request,*args,**kwargs)  # 必须调用SearchAndCheckXadmin父类，再调用post方法，否则会报错
        # 一定不要忘记，否则整个ClickAndBackXAdmin保存都会出错


class DeleteAndCheckXadmin(object):
    all_zi_duan = ["id", "test_project", "test_module", "test_page",
                   "case_priority",
                   "test_case_title", "is_run_case",
                   "depend_click_case",

                   "delete_ele_find","delete_ele_find_value",
                   "delete_button_find", "delete_button_find_value",

                   "confirm_ele_find",
                   "confirm_ele_find_value",
                   "click_confirm_delay_time",
                   "is_click_cancel",
                   "cancel_ele_find","cancel_ele_find_value",
                   "is_submit_success",
                   "popup_ele_find","popup_ele_find_value","popup_text",

                   "is_signel_page","page_number_xpath",
                   "result_table_ele_find","result_table_ele_find_value",
                   "table_colnum_counts",
                   "case_counts",  "write_user",
                   "add_time", "update_time"]
    list_display = ["test_project", "test_module", "test_page",
                    "case_priority",
                    "test_case_title", "is_run_case","depend_click_case",
                    "delete_ele_find", "delete_ele_find_value",
                    "delete_button_find", "delete_button_find_value",
                    "confirm_ele_find",
                    "confirm_ele_find_value",
                    "click_confirm_delay_time",
                    "is_click_cancel",
                    "cancel_ele_find", "cancel_ele_find_value",
                    "is_submit_success",
                    "popup_ele_find", "popup_ele_find_value", "popup_text",
                    "is_signel_page", "page_number_xpath",
                    "result_table_ele_find", "result_table_ele_find_value",
                    "table_colnum_counts",
                    "case_counts",
                    "go_to"]  # 定义显示的字段
    list_filter = ["test_project", "test_module", "test_page",
                   "test_case_title", "is_run_case",
                   "write_user"]  # 定义筛选的字段
    search_fields = ["test_project", "test_module", "test_page",
                   "test_case_title"]   # 定义搜索字段
    model_icon = "fa fa-file-text"  # 定义图标显示
    ordering = ["-add_time"]  # 添加默认排序规则显示排序，根据添加时间倒序排序
    readonly_fields = ["write_user", "add_time",
                       "update_time"]  # 设置某些字段为只为可读  #设置了readonly_fields，再设置exclude，exclude对该字段无效，

    # exclude = ['case_step']  # 设置某些字段为不显示，即隐藏  #readonly_fields和exclude设置会有冲突
    # inlines = [TestCaseInline]  # inlines配和TestCaseInline使用，可以直接在项目页面添加测试用例#只能做一层嵌套，不能进行两层嵌套

    list_editable = all_zi_duan  # 可以在列表页对字段进行编辑
    refresh_times = [3, 5]  # 对列表页进行定时刷新,配置了3秒和5秒，可以从中选择一个
    list_per_page = 50  # 每页设置50条数据，默认每页展示100条数据
    # fk_fields = ['test_project_id',]  #设置显示外键字段，未生效
    list_display_links = ["test_case_title", ]  # 设置点击链接进入编辑页面的字段
    # date_hierarchy = 'add_time'   #详细时间分层筛选，未生效
    show_detail_fields = ["test_project", ]  # 显示数据详情

    list_export = ('xls',)  # 控制列表页导出数据的可选格式
    show_bookmarks = True  # 控制是否显示书签功能

    # 设置是否加入导入插件
    import_excel = True  # True表示显示使用插件，False表示不显示使用插件，该import_excel变量会覆盖插件中的变量



    #重载get_context方法，只显示本用户添加的点击场景的用例
    def get_context(self):
        context = super(DeleteAndCheckXadmin, self).get_context()   #调用父类

        if 'form' in context:   #固定写法
            if self.request.user.is_superuser:  # 超级用户则返回所有
                context['form'].fields['depend_click_case'].queryset = ClickAndBack.objects.all()
            else:  # 非超级用户则只返回本用户添加的点击场景的用例
                context['form'].fields['depend_click_case'].queryset = ClickAndBack.objects.filter(write_user=self.request.user)   #取form中的depend_click_case（与model中的字段相同），只取当前用户填写的数据
        return context

    def save_models(self):  # 重载save_models的方法，可以在做了某个动作后，动态重新加载
        obj = self.new_obj  # 取得当前用例的实例
        if self.request.user.is_superuser:  # 超级用户则不对编写人做修改
            obj.save()  # 保存当前用例
        else:  # 非超级用户会自动保存编写人
            user = User.objects.get(username=self.request.user)
            obj.write_user_id = user.id  # 保存当前的write_user为用户登录的user
            obj.save()  # 保存当前用例

    def queryset(self):  # 重载queryset方法，用来做到不同的admin取出的数据不同
        qs = super(DeleteAndCheckXadmin, self).queryset()  # 调用父类
        if self.request.user.is_superuser:  # 超级用户可查看所有数据
            return qs
        else:
            qs = qs.filter(write_user=self.request.user)  # 否则只显示本用户数据
            return qs  # 返回qs

    def post(self, request, *args, **kwargs):  # 重载post函数，用于判断导入的逻辑
        if 'excel' in request.FILES:  # 如果excel在request.FILES中
            excel_file = request.FILES.get('excel', '')

            import xlrd  # 导入xlrd
            # 常用的Excel文件有.xls和.xls两种，.xls文件读取时需要设置formatting_info = True
            # data = xlrd.open_workbook(filename=None, file_contents=excel_file.read())  # xlsx文件

            exceldata = xlrd.open_workbook(filename=None, file_contents=excel_file.read(),
                                           formatting_info=True)  # xls文件

            from .analyzexls import Analyzexls
            analyzexls = Analyzexls()
            # 将获取的数据循环导入数据库中
            all_list_1 = analyzexls.get_sheets_mg(exceldata, 0)
            i = 0
            if len(all_list_1[0]) == 28:
                while i < len(all_list_1):
                    deleteandcheck = DeleteAndCheck()  # 数据库的对象等于ClickAndBack,实例化
                    deleteandcheck.test_project = all_list_1[i][0]  # 填写项目all_list_1[i][j]
                    deleteandcheck.test_module = all_list_1[i][1]  # 填写模块
                    deleteandcheck.test_page = all_list_1[i][2]  # 填写测试页

                    if all_list_1[i][3] == u"冒烟用例":
                        deleteandcheck.case_priority = "P0" # 填写用例优先级
                    elif all_list_1[i][3] == u"系统的重要功能用例":
                        deleteandcheck.case_priority = "P1"  # 填写用例优先级
                    elif all_list_1[i][3] == u"系统的一般功能用例":
                        deleteandcheck.case_priority = "P2"  # 填写用例优先级
                    elif all_list_1[i][3] == u"极低级别的用例":
                        deleteandcheck.case_priority = "P3"  # 填写用例优先级


                    deleteandcheck.test_case_title = all_list_1[i][4]  # 填写测试内容的名称
                    deleteandcheck.is_run_case =all_list_1[i][5]  # 填写是否运行
                    if all_list_1[i][6] != None:  # 如果依赖列有内容且内容存在数据库中，则保存依赖内容
                        depend = all_list_1[i][6]
                        depend_contents = ClickAndBack.objects.filter(test_case_title=depend)
                        depend_count = depend_contents.count()
                        if depend_count == 1:
                            for depend_content in depend_contents:
                                deleteandcheck.depend_click_case_id = depend_content.id

                    deleteandcheck.delete_ele_find = all_list_1[i][7]  # 填写被删除元素查找风格
                    deleteandcheck.delete_ele_find_value = all_list_1[i][8]  # 填写被删除元素查找风格的确切值
                    deleteandcheck.delete_button_find = all_list_1[i][9]  # 填写删除按钮查找风格
                    deleteandcheck.delete_button_find_value = all_list_1[i][10]  # 填写删除按钮查找风格的确切值

                    deleteandcheck.confirm_ele_find = all_list_1[i][11]  # 填写确定按钮查找风格
                    deleteandcheck.confirm_ele_find_value = all_list_1[i][12]  # 填写确定按钮查找风格的确切值
                    deleteandcheck.click_confirm_delay_time = all_list_1[i][13]  # 填写点击确定按钮后的延时时长（单位秒）
                    deleteandcheck.is_click_cancel = all_list_1[i][14] # 填写是否点击取消按钮
                    deleteandcheck.cancel_ele_find = all_list_1[i][15]  # 填写取消按钮查找风格
                    deleteandcheck.cancel_ele_find_value = all_list_1[i][16]  # 填写取消按钮查找风格的确切值
                    deleteandcheck.is_submit_success = all_list_1[i][17] # 填写是否添加成功

                    deleteandcheck.popup_ele_find = all_list_1[i][18]  # 填写删除成功弹框中的某个元素查找风格
                    deleteandcheck.popup_ele_find_value = all_list_1[i][19]  # 填写删除成功弹框中的某个元素查找风格的确切值
                    deleteandcheck.popup_text = all_list_1[i][20]  # 填写删除成功弹框中的某个元素文本信息内容



                    deleteandcheck.is_signel_page = all_list_1[i][21]  # 填写是否单页面

                    deleteandcheck.page_number_xpath = all_list_1[i][22]  # 填写页数层xpath路径值
                    deleteandcheck.result_table_ele_find = all_list_1[i][23]  # 填写结果表格查找风格
                    deleteandcheck.result_table_ele_find_value = all_list_1[i][24] # 填写结果表格查找风格的确切值
                    deleteandcheck.table_colnum_counts = all_list_1[i][25]  # 填写结果表格总列数

                    deleteandcheck.case_counts = all_list_1[i][26]  # 填写case_counts
                    if all_list_1[i][27] != None:  # 如果编写人列有数据则填写编写人
                        users = User.objects.all()
                        for user in users:
                            if user.username == all_list_1[i][27]:
                                deleteandcheck.write_user_id = user.id  # 填写编写人
                    deleteandcheck.save()  # 保存到数据库

                    i = i + 1
            pass
        return super(DeleteAndCheckXadmin,self).post(request,*args,**kwargs)  # 必须调用clickandbackAdmin父类，再调用post方法，否则会报错
        # 一定不要忘记，否则整个ClickAndBackXAdmin保存都会出错


class EditAndCheckXadmin(object):
    all_zi_duan = ["id", "test_project", "test_module", "test_page",
                   "case_priority",
                   "test_case_title", "is_run_case",
                   # "depend_new_add_and_check_case",
                   "depend_click_case",
                   "edit_ele_find","edit_ele_find_value","edit_button_find","edit_button_find_value",

                   "confirm_ele_find",
                   "confirm_ele_find_value",
                   "click_confirm_delay_time",
                   "is_click_cancel",
                   "cancel_ele_find","cancel_ele_find_value",
                   "is_submit_success",
                   "is_signel_page","page_number_xpath",
                   "result_table_ele_find","result_table_ele_find_value",
                   "table_colnum_counts",
                   "case_counts",  "write_user",
                   "add_time", "update_time"]
    list_display = ["test_project", "test_module", "test_page",
                    "case_priority",
                    "test_case_title", "is_run_case",
                    # "depend_new_add_and_check_case",
                    "depend_click_case",
                    "edit_ele_find", "edit_ele_find_value", "edit_button_find", "edit_button_find_value",
                    "confirm_ele_find",
                    "confirm_ele_find_value",
                    "click_confirm_delay_time",
                    "is_click_cancel",
                    "cancel_ele_find", "cancel_ele_find_value",
                    "is_submit_success",
                    "is_signel_page", "page_number_xpath",
                    "result_table_ele_find", "result_table_ele_find_value",
                    "table_colnum_counts",
                    "case_counts",
                    "go_to"]  # 定义显示的字段
    list_filter = ["test_project", "test_module", "test_page",
                   "test_case_title", "is_run_case",
                   "write_user"]  # 定义筛选的字段
    search_fields = ["test_project", "test_module", "test_page",
                   "test_case_title"]   # 定义搜索字段
    model_icon = "fa fa-file-text"  # 定义图标显示
    ordering = ["-add_time"]  # 添加默认排序规则显示排序，根据添加时间倒序排序
    readonly_fields = ["write_user", "add_time",
                       "update_time"]  # 设置某些字段为只为可读  #设置了readonly_fields，再设置exclude，exclude对该字段无效，

    # exclude = ['case_step']  # 设置某些字段为不显示，即隐藏  #readonly_fields和exclude设置会有冲突
    # inlines = [TestCaseInline]  # inlines配和TestCaseInline使用，可以直接在项目页面添加测试用例#只能做一层嵌套，不能进行两层嵌套

    list_editable = all_zi_duan  # 可以在列表页对字段进行编辑
    refresh_times = [3, 5]  # 对列表页进行定时刷新,配置了3秒和5秒，可以从中选择一个
    list_per_page = 50  # 每页设置50条数据，默认每页展示100条数据
    # fk_fields = ['test_project_id',]  #设置显示外键字段，未生效
    list_display_links = ["test_case_title", ]  # 设置点击链接进入编辑页面的字段
    # date_hierarchy = 'add_time'   #详细时间分层筛选，未生效
    show_detail_fields = ["test_project", ]  # 显示数据详情

    list_export = ('xls',)  # 控制列表页导出数据的可选格式
    show_bookmarks = True  # 控制是否显示书签功能

    # 设置是否加入导入插件
    import_excel = True  # True表示显示使用插件，False表示不显示使用插件，该import_excel变量会覆盖插件中的变量

    #设置内联
    class InputTapInputTextInline(object):
        model = InputTapInputText
        exclude = ["add_time","update_time","newaddandcheck","editandcheck","loginandcheck"]
        extra = 1
        style = 'tab'    #以标签形式展示

    #设置内联
    class InputTapInputFileInline(object):
        model = InputTapInputFile
        exclude = ["add_time","update_time","newaddandcheck","editandcheck"]
        extra = 1
        style = 'tab'    #以标签形式展示

    #设置内联
    class InputTapInputDateTimeInline(object):
        model = InputTapInputDateTime
        exclude = ["add_time","update_time","newaddandcheck","editandcheck"]
        extra = 1
        style = 'tab'    #以标签形式展示

    # 设置内联
    class RadioAndReelectionLabelInline(object):
        model = RadioAndReelectionLabel
        exclude = ["add_time", "update_time","newaddandcheck","editandcheck"]
        extra = 1
        style = 'tab'  # 以标签形式展示

    #设置内联
    class SelectTapSelectOptionInline(object):
        model = SelectTapSelectOption
        exclude = ["add_time","update_time","newaddandcheck","editandcheck"]
        extra = 1
        style = 'tab'    #以标签形式展示

    #设置内联
    class AssertTipTextInline(object):
        model = AssertTipText
        exclude = ["add_time","update_time","newaddandcheck","editandcheck","loginandcheck"]
        extra = 1
        style = 'tab'    #以标签形式展示

    #设置内联
    class IframeBodyInputTextInline(object):
        model = IframeBodyInputText
        exclude = ["add_time","update_time","newaddandcheck","editandcheck"]
        extra = 1
        style = 'tab'    #以标签形式展示

    inlines = [InputTapInputTextInline,InputTapInputFileInline,InputTapInputDateTimeInline,
               RadioAndReelectionLabelInline,
               SelectTapSelectOptionInline,AssertTipTextInline,
               IframeBodyInputTextInline,]

    #重载get_context方法，只显示本用户添加的点击场景的用例
    def get_context(self):
        context = super(EditAndCheckXadmin, self).get_context()   #调用父类

        if 'form' in context:   #固定写法
            if self.request.user.is_superuser:  # 超级用户则返回所有
                context['form'].fields['depend_click_case'].queryset = ClickAndBack.objects.all()
            else:  # 非超级用户则只返回本用户添加的点击场景的用例
                context['form'].fields['depend_click_case'].queryset = ClickAndBack.objects.filter(write_user=self.request.user)   #取form中的depend_click_case（与model中的字段相同），只取当前用户填写的数据
        return context

    def save_models(self):  # 重载save_models的方法，可以在做了某个动作后，动态重新加载
        obj = self.new_obj  # 取得当前用例的实例
        if self.request.user.is_superuser:  # 超级用户则不对编写人做修改
            obj.save()  # 保存当前用例
        else:  # 非超级用户会自动保存编写人
            user = User.objects.get(username=self.request.user)
            obj.write_user_id = user.id  # 保存当前的write_user为用户登录的user
            obj.save()  # 保存当前用例

    def queryset(self):  # 重载queryset方法，用来做到不同的admin取出的数据不同
        qs = super(EditAndCheckXadmin, self).queryset()  # 调用父类
        if self.request.user.is_superuser:  # 超级用户可查看所有数据
            return qs
        else:
            qs = qs.filter(write_user=self.request.user)  # 否则只显示本用户数据
            return qs  # 返回qs

    def post(self, request, *args, **kwargs):  # 重载post函数，用于判断导入的逻辑
        if 'excel' in request.FILES:  # 如果excel在request.FILES中
            excel_file = request.FILES.get('excel', '')

            import xlrd  # 导入xlrd
            # 常用的Excel文件有.xls和.xls两种，.xls文件读取时需要设置formatting_info = True
            # data = xlrd.open_workbook(filename=None, file_contents=excel_file.read())  # xlsx文件

            exceldata = xlrd.open_workbook(filename=None, file_contents=excel_file.read(),
                                           formatting_info=True)  # xls文件

            from .analyzexls import Analyzexls
            analyzexls = Analyzexls()
            # 将获取的数据循环导入数据库中
            all_list_1 = analyzexls.get_sheets_mg(exceldata, 0)
            i = 0
            if len(all_list_1[0]) == 25:
                while i < len(all_list_1):
                    editandcheck = EditAndCheck()  # 数据库的对象等于EditAndCheck,实例化
                    editandcheck.test_project = all_list_1[i][0]  # 填写项目all_list_1[i][j]
                    editandcheck.test_module = all_list_1[i][1]  # 填写模块
                    editandcheck.test_page = all_list_1[i][2]  # 填写测试页

                    if all_list_1[i][3] == u"冒烟用例":
                        editandcheck.case_priority = "P0" # 填写用例优先级
                    elif all_list_1[i][3] == u"系统的重要功能用例":
                        editandcheck.case_priority = "P1"  # 填写用例优先级
                    elif all_list_1[i][3] == u"系统的一般功能用例":
                        editandcheck.case_priority = "P2"  # 填写用例优先级
                    elif all_list_1[i][3] == u"极低级别的用例":
                        editandcheck.case_priority = "P3"  # 填写用例优先级


                    editandcheck.test_case_title = all_list_1[i][4]  # 填写测试内容的名称
                    editandcheck.is_run_case =all_list_1[i][5]  # 填写是否运行
                    if all_list_1[i][6] != None:  # 如果依赖列有内容且内容存在数据库中，则保存依赖内容
                        depend = all_list_1[i][6]
                        depend_contents = ClickAndBack.objects.filter(test_case_title=depend)
                        depend_count = depend_contents.count()
                        if depend_count == 1:
                            for depend_content in depend_contents:
                                editandcheck.depend_click_case_id = depend_content.id

                    editandcheck.edit_ele_find = all_list_1[i][7]  # 填写被修改元素查找风格
                    editandcheck.edit_ele_find_value = all_list_1[i][8]  # 填写被修改元素查找风格的确切值
                    editandcheck.edit_button_find = all_list_1[i][9] # 填写修改按钮查找风格
                    editandcheck.edit_button_find_value = all_list_1[i][10]  # 填写修改按钮查找风格的确切值

                    editandcheck.confirm_ele_find = all_list_1[i][11]  # 填写确定按钮查找风格
                    editandcheck.confirm_ele_find_value = all_list_1[i][12]  # 填写确定按钮查找风格的确切值
                    editandcheck.click_confirm_delay_time = all_list_1[i][13]  # 填写点击确定按钮后的延时时长（单位秒）
                    editandcheck.is_click_cancel = all_list_1[i][14] # 填写是否点击取消按钮
                    editandcheck.cancel_ele_find = all_list_1[i][15]  # 填写取消按钮查找风格
                    editandcheck.cancel_ele_find_value = all_list_1[i][16]  # 填写取消按钮查找风格的确切值
                    editandcheck.is_submit_success = all_list_1[i][17] # 填写是否添加成功
                    editandcheck.is_signel_page = all_list_1[i][18]  # 填写是否单页面

                    editandcheck.page_number_xpath = all_list_1[i][19]  # 填写页数层xpath路径值
                    editandcheck.result_table_ele_find = all_list_1[i][20]  # 填写结果表格查找风格
                    editandcheck.result_table_ele_find_value = all_list_1[i][21] # 填写结果表格查找风格的确切值
                    editandcheck.table_colnum_counts = all_list_1[i][22]  # 填写结果表格总列数

                    editandcheck.case_counts = all_list_1[i][23]  # 填写case_counts
                    if all_list_1[i][24] != None:  # 如果编写人列有数据则填写编写人
                        users = User.objects.all()
                        for user in users:
                            if user.username == all_list_1[i][24]:
                                editandcheck.write_user_id = user.id  # 填写编写人
                    editandcheck.save()  # 保存到数据库

                    i = i + 1
            pass

        return super(EditAndCheckXadmin,self).post(request,*args,**kwargs)  # 必须调用clickandbackAdmin父类，再调用post方法，否则会报错
        # 一定不要忘记，否则整个ClickAndBackXAdmin保存都会出错

# xadmin.site.register(LoginAndCheck,LoginAndCheckXadmin) #在xadmin中注册LoginAndCheckXAdmin

# xadmin.site.register(ClickAndBack, ClickAndBackXAdmin) #在xadmin中注册ClickAndBackXAdmin
# xadmin.site.register(NewAddAndCheck,NewAddAndCheckXadmin)  #在xadmin中注册NewAddAndCheckXadmin
# xadmin.site.register(SearchAndCheck,SearchAndCheckXadmin) #在xadmin中注册SearchAndCheckXadmin
# xadmin.site.register(DeleteAndCheck,DeleteAndCheckXadmin) #在xadmin中注册DeleteAndCheckXadmin
# xadmin.site.register(EditAndCheck,EditAndCheckXadmin) #在xadmin中注册DeleteAndCheckXadmin



