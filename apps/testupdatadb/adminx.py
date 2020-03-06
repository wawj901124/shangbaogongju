import xadmin

from .models import UpdateDbData,User



class UpdateDbDataXadmin(object):
    all_zi_duan = ["id", "test_project", "test_module", "test_page",
                   "case_priority",
                   "test_case_title", "is_run_case",

                   "db_host", "db_port","db_user","db_password","db_database","db_charset",
                   "db_biao", "db_ziduan","db_xiugaiqiandezhi","db_xiugaihoudezhi","db_tiaojianziduan",
                   "db_tiaojianzhi",

                   "case_counts",  "write_user",
                   "add_time", "update_time"]
    list_display = ["test_project", "test_module", "test_page",
                    "case_priority",
                    "test_case_title", "is_run_case",

                    "db_host", "db_port", "db_user", "db_password", "db_database", "db_charset",
                    "db_biao", "db_ziduan", "db_xiugaiqiandezhi", "db_xiugaihoudezhi", "db_tiaojianziduan",
                    "db_tiaojianzhi",

                    "case_counts","go_to"]  # 定义显示的字段
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

    #批量复制
    def patch_copy(self,request,querset):  #此处的querset为选中的数据
        querset = querset.order_by('id')  #按照id顺序排序
        for qs_one in querset:
            #新建实体并复制选中的内容
            new_udd = UpdateDbData()
            new_udd.test_project = qs_one.test_project
            new_udd.test_module = qs_one.test_module
            new_udd.test_page = qs_one.test_page
            new_udd.case_priority = qs_one.case_priority
            new_udd.test_case_title = qs_one.test_case_title
            new_udd.is_run_case = qs_one.is_run_case
            new_udd.depend_case_id = qs_one.depend_case_id
            new_udd.db_host = qs_one.db_host
            new_udd.db_port = qs_one.db_port
            new_udd.db_user = qs_one.db_user
            new_udd.db_password = qs_one.db_password
            new_udd.db_database = qs_one.db_database
            new_udd.db_charset = qs_one.db_charset
            new_udd.db_biao = qs_one.db_biao
            new_udd.db_ziduan = qs_one.db_ziduan
            new_udd.db_xiugaiqiandezhi = qs_one.db_xiugaiqiandezhi
            new_udd.db_xiugaihoudezhi = qs_one.db_xiugaihoudezhi
            new_udd.db_tiaojianziduan = qs_one.db_tiaojianziduan
            new_udd.db_tiaojianzhi = qs_one.db_tiaojianzhi
            new_udd.db_paixuziduan = qs_one.db_paixuziduan
            new_udd.is_daoxu = qs_one.is_daoxu
            new_udd.db_qianjiwei = qs_one.db_qianjiwei
            new_udd.case_counts = qs_one.case_counts

            if self.request.user.is_superuser:  # 超级用户则不保存user
                pass
            else: #否则保存user为当前用户
                new_udd.write_user = self.request.user
            new_udd.save()      #保存数据

    #批量删除
    def patch_delete(self,request,querset):
        for qs_one in querset:
            qs_one.depend_case_id = ""
            #再删除本体
            qs_one.delete()

    patch_copy.short_description = "批量复制"
    patch_delete.short_description = "批量删除"
    actions=[patch_copy,patch_delete,]

    #重载get_context方法，只显示本用户添加的用例
    def get_context(self):
        context = super(UpdateDbDataXadmin, self).get_context()   #调用父类

        if 'form' in context:   #固定写法
            if self.request.user.is_superuser:  # 超级用户则返回所有
                context['form'].fields['depend_case'].queryset = UpdateDbData.objects.all()
            else:  # 非超级用户则只返回本用户添加的点击场景的用例
                context['form'].fields['depend_case'].queryset = UpdateDbData.objects.filter(write_user=self.request.user)   #取form中的depend_click_case（与model中的字段相同），只取当前用户填写的数据
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
        qs = super(UpdateDbDataXadmin, self).queryset()  # 调用父类
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
                    updatedbdata = UpdateDbData()  # 数据库的对象等于ClickAndBack,实例化
                    updatedbdata.test_project = all_list_1[i][0]  # 填写项目all_list_1[i][j]
                    updatedbdata.test_module = all_list_1[i][1]  # 填写模块
                    updatedbdata.test_page = all_list_1[i][2]  # 填写测试页

                    if all_list_1[i][3] == u"冒烟用例":
                        updatedbdata.case_priority = "P0" # 填写用例优先级
                    elif all_list_1[i][3] == u"系统的重要功能用例":
                        updatedbdata.case_priority = "P1"  # 填写用例优先级
                    elif all_list_1[i][3] == u"系统的一般功能用例":
                        updatedbdata.case_priority = "P2"  # 填写用例优先级
                    elif all_list_1[i][3] == u"极低级别的用例":
                        updatedbdata.case_priority = "P3"  # 填写用例优先级


                    updatedbdata.test_case_title = all_list_1[i][4]  # 填写测试内容的名称
                    updatedbdata.is_run_case =all_list_1[i][5]  # 填写是否运行


                    updatedbdata.db_host = all_list_1[i][6]  # 填写数据库IP
                    updatedbdata.db_port = all_list_1[i][7]  # 填写数据库端口
                    updatedbdata.db_user =all_list_1[i][8]  # 填写数据库用户名
                    updatedbdata.db_password = all_list_1[i][9]  # 填写数据库密码
                    updatedbdata.db_database = all_list_1[i][10]  # 填写数据库库名
                    updatedbdata.db_charset =all_list_1[i][11]  # 填写数据库编码格式
                    updatedbdata.db_biao = all_list_1[i][12]  # 填写数据库中的表
                    updatedbdata.db_ziduan =all_list_1[i][13]  # 填写数据库中的表的字段名
                    updatedbdata.db_xiugaiqiandezhi = all_list_1[i][14]  # 填写数据库中的表的字段替换前的值
                    updatedbdata.db_xiugaihoudezhi = all_list_1[i][15]  # 填写数据库中的表的字段替换后的值
                    updatedbdata.db_tiaojianziduan = all_list_1[i][16] # 填写where条件字段名
                    updatedbdata.db_tiaojianzhi = all_list_1[i][17]  # 填写where条件字段值

                    updatedbdata.case_counts = all_list_1[i][18]  # 填写case_counts
                    if all_list_1[i][19] != None:  # 如果编写人列有数据则填写编写人
                        users = User.objects.all()
                        for user in users:
                            if user.username == all_list_1[i][19]:
                                updatedbdata.write_user_id = user.id  # 填写编写人
                    updatedbdata.save()  # 保存到数据库

                    i = i + 1
            pass
        return super(UpdateDbDataXadmin,self).post(request,*args,**kwargs)  # 必须调用clickandbackAdmin父类，再调用post方法，否则会报错
        # 一定不要忘记，否则整个ClickAndBackXAdmin保存都会出错




xadmin.site.register(UpdateDbData,UpdateDbDataXadmin) #在xadmin中注册DeleteAndCheckXadmin



