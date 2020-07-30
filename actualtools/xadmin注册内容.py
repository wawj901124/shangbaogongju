import xadmin
from .modelsnewdev import NodeConfig,ConfigControlSendPorsSection,ConfigControlSendPorsConvertrule


#dev配置
class NodeConfigXadmin():
    all_zi_duan = ["id",
                   "config_project",
                   "add_time", "update_time"]
    list_display = ["config_project",
                    "config_file_name",
                    "config_xieyi_num",
                    "config_xieyi_type",
                    "config_version",
                    "config_device",
                    "go_to"]  # 定义显示的字段
    list_filter = ["config_project",
                   "config_file_name",
                   "config_xieyi_num",
                   "config_xieyi_type",
                   "config_version",
                   "config_device",
                   "write_user"]  # 定义筛选的字段
    search_fields = ["config_project",
                     "config_file_name",
                     "config_version",
                     "config_device",
                     "config_xieyi_num",]   # 定义搜索字段
    model_icon = "fa fa-file-text"  # 定义图标显示
    ordering = ["-add_time"]  # 添加默认排序规则显示排序，根据添加时间倒序排序
    # readonly_fields = ["write_user", "add_time",
    #                    "update_time"]  # 设置某些字段为只为可读  #设置了readonly_fields，再设置exclude，exclude对该字段无效，

    # exclude = ['case_step']  # 设置某些字段为不显示，即隐藏  #readonly_fields和exclude设置会有冲突
    # inlines = [TestCaseInline]  # inlines配和TestCaseInline使用，可以直接在项目页面添加测试用例#只能做一层嵌套，不能进行两层嵌套

    # list_editable = all_zi_duan  # 可以在列表页对字段进行编辑
    refresh_times = [3, 5]  # 对列表页进行定时刷新,配置了3秒和5秒，可以从中选择一个
    list_per_page = 50  # 每页设置50条数据，默认每页展示100条数据
    # fk_fields = ['test_project_id',]  #设置显示外键字段，未生效
    list_display_links = ["config_project", ]  # 设置点击链接进入编辑页面的字段
    # date_hierarchy = 'add_time'   #详细时间分层筛选，未生效
    show_detail_fields = ["config_project", ]  # 显示数据详情

    # 编辑页的字段显示
    fields=['config_project','config_xieyi_num','config_xieyi_type','config_version','config_device','config_collect_packet_len','local_file','write_user']   #添加页的字段显示

    list_export = ('xls',)  # 控制列表页导出数据的可选格式
    show_bookmarks = True  # 控制是否显示书签功能

    # 设置是否加入导入插件
    import_excel = False  # True表示显示使用插件，False表示不显示使用插件，该import_excel变量会覆盖插件中的变量


    #设置内联
    class ConfigCollectSendCmdInline(object):
        model = ConfigCollectSendCmd
        exclude = ["write_user","add_time","update_time"]
        extra = 1
        style = 'accordion'    #以标签形式展示 ，形式有：stacked，one，accordion（折叠），tab（标签），table（表格）


    # #设置内联
    # class ConfigCollectFactorInline(object):
    #     model = ConfigCollectFactor
    #     exclude = ["write_user","add_time","update_time"]
    #     extra = 1
    #     style = 'accordion'    #以标签形式展示 ，形式有：stacked，one，accordion（折叠），tab（标签），table（表格）
    #     # form = ConfigCollectFactorForm

    #设置内联
    class ConfigCollectReceivePorsInline(object):
        model =  ConfigCollectReceivePors
        exclude = ["write_user","add_time","update_time"]
        extra = 1
        style = 'accordion'    #以标签形式展示 ，形式有：stacked，one，accordion（折叠），tab（标签），table（表格）


    #设置内联
    class ConfigCollectReceivePorsSectionInline(object):
        model = ConfigCollectReceivePorsSection
        exclude = ["write_user","add_time","update_time"]
        extra = 1
        style = 'accordion'    #以标签形式展示 ，形式有：stacked，one，accordion（折叠），tab（标签），table（表格）


    #设置内联
    class ConfigCollectReceivePorsConvertruleInline(object):
        model = ConfigCollectReceivePorsConvertrule
        exclude = ["write_user","add_time","update_time"]
        extra = 1
        style = 'accordion'    #以标签形式展示 ，形式有：stacked，one，accordion（折叠），tab（标签），table（表格）

    #设置内联
    class ConfigControlSendCmdInline(object):
        model = ConfigControlSendCmd
        exclude = ["write_user","add_time","update_time"]
        extra = 1
        style = 'accordion'    #以标签形式展示 ，形式有：stacked，one，accordion（折叠），tab（标签），table（表格）

    #设置内联
    class ConfigControlSendParamidInline(object):
        model = ConfigControlSendParamid
        exclude = ["write_user","add_time","update_time"]
        extra = 1
        style = 'accordion'    #以标签形式展示 ，形式有：stacked，one，accordion（折叠），tab（标签），table（表格）

    #设置内联
    class ConfigControlSendPorsSectionInline(object):
        model = ConfigControlSendPorsSection
        exclude = ["write_user","add_time","update_time"]
        extra = 1
        style = 'accordion'    #以标签形式展示 ，形式有：stacked，one，accordion（折叠），tab（标签），table（表格）



    #设置内联
    class ConfigControlSendPorsConvertruleInline(object):
        model = ConfigControlSendPorsConvertrule
        fk_name = 'nodeconfig'
        form = ConfigControlSendPorsConvertruleForm
        # formset = ConfigControlSendPorsConvertruleFormset
        exclude = ["add_time","update_time"]
        extra = 1
        style = 'accordion'    #以标签形式展示 ，形式有：stacked，one，accordion（折叠），tab（标签），table（表格）

        # def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
        #     print("db_field.name:")
        #     print(db_field.name)
        #
        #     if db_field.name == 'configcontrolsendporssection':
        #         kwargs['queryset'] = ConfigControlSendPorsSection.objects.filter(write_user=request.user)
        #     else:
        #         pass
        #
        #     return super(ConfigControlSendPorsConvertruleInline, self).formfield_for_foreignkey(db_field, request, **kwargs)


    inlines = [ConfigCollectSendCmdInline,
               ConfigCollectFactorInline,
               ConfigCollectReceivePorsInline,
               ConfigCollectReceivePorsSectionInline,
               ConfigCollectReceivePorsConvertruleInline,
               ConfigControlSendCmdInline,
               ConfigControlSendParamidInline,
               ConfigControlSendPorsSectionInline,
               ConfigControlSendPorsConvertruleInline,]

    # #内联过滤
    # def change_view(self, request, object_id, extra_context=None):
    #     def formfield_for_foreignkey(self, db_field, request, **kwargs):
    #         if db_field.name == 'configcontrolsendporssection':
    #             kwargs['queryset'] = ConfigControlSendPorsSection.objects.filter(write_user=request.user)
    #         return super(ItemInline, self).formfield_for_foreignkey(db_field, request, **kwargs)
    #
    #     ItemInline.formfield_for_foreignkey = formfield_for_foreignkey
    #
    #     self.inline_instances = [ItemInline(self.model, self.admin_site)]
    #
    #     return super(NodeConfigXadmin, self).change_view(request, object_id,
    #                                                 extra_context=extra_context)





    #批量处理命令
    # #批量复制
    # def patch_copy(self,request,querset):  #此处的querset为选中的数据
    #     querset = querset.order_by('id')  #按照id顺序排序
    #     for qs_one in querset:
    #         #新建实体并复制选中的内容
    #         new_tagcontent = TagContent()
    #         new_tagcontent.config_project = qs_one.config_project
    #         new_tagcontent.tag_name = qs_one.tag_name
    #         new_tagcontent.is_root = qs_one.is_root
    #         new_tagcontent.tag_level = qs_one.tag_level
    #         new_tagcontent.tag_text = qs_one.tag_text
    #         new_tagcontent.tag_father = qs_one.tag_father
    #         if self.request.user.is_superuser:  # 超级用户则不保存user
    #             pass
    #         else: #否则保存user为当前用户
    #             new_tagcontent.write_user = self.request.user
    #         new_tagcontent.save()      #保存数据
    #         #获取刚保存的数据的id
    #         newadd = TagContent.objects.filter(config_project = qs_one.config_project).order_by('-add_time')
    #         for new_last in newadd:
    #             newaddid = new_last.id
    #             break
    #
    #         #获取TagAttrib中相应的内容
    #         old_tagattrib_all =TagAttrib.objects.filter(tagcontent_id=qs_one.id).order_by('add_time')
    #         for old_tagattrib_one in old_tagattrib_all:
    #             new_tagattrib = TagAttrib()
    #             new_tagattrib.tagcontent_id = newaddid
    #             new_tagattrib.tag_value_name = old_tagattrib_one.tag_value_name
    #             new_tagattrib.tag_value_text = old_tagattrib_one.tag_value_text
    #             if self.request.user.is_superuser:  # 超级用户则不保存user
    #                 pass
    #             else:  # 否则保存user为当前用户
    #                 new_tagattrib.write_user = self.request.user
    #             new_tagattrib.save()   #保存数据库


    #批量删除
    def patch_delete(self,request,querset):
        for qs_one in querset:
            #先删除关联

            #关联之 ConfigCollectReceivePorsConvertrule 去掉依赖
            ConfigCollectReceivePorsConvertrule_all = ConfigCollectReceivePorsConvertrule.objects.filter(nodeconfig_id=qs_one.id)
            for ConfigCollectReceivePorsConvertrule_one in ConfigCollectReceivePorsConvertrule_all:
                ConfigCollectReceivePorsConvertrule_one.nodeconfig_id = ""  #置空依赖
                ConfigCollectReceivePorsConvertrule_one.configcollectreceiveporssection_id = ""  #置空依赖
                ConfigCollectReceivePorsConvertrule_one.delete()  #删除

            #关联之 ConfigCollectReceivePorsSection 去掉依赖
            ConfigCollectReceivePorsSection_all = ConfigCollectReceivePorsSection.objects.filter(nodeconfig_id=qs_one.id)
            for ConfigCollectReceivePorsSection_one in ConfigCollectReceivePorsSection_all:
                ConfigCollectReceivePorsSection_one.nodeconfig_id = ""  #置空依赖
                ConfigCollectReceivePorsSection_one.configcollectreceivepors_id = ""  # 置空依赖
                ConfigCollectReceivePorsSection_one.delete()  #删除

            #关联之 ConfigCollectReceivePors 去掉依赖
            ConfigCollectReceivePors_all = ConfigCollectReceivePors.objects.filter(nodeconfig_id=qs_one.id)
            for ConfigCollectReceivePors_one in ConfigCollectReceivePors_all:
                ConfigCollectReceivePors_one.nodeconfig_id = ""  #置空依赖
                ConfigCollectReceivePors_one.configcollectsendcmd_id = ""   #置空依赖
                ConfigCollectReceivePors_one.delete()  #删除

            #关联之 ConfigCollectFactor 去掉依赖
            ConfigCollectFactor_all = ConfigCollectFactor.objects.filter(nodeconfig_id=qs_one.id)
            for ConfigCollectFactor_one in ConfigCollectFactor_all:
                ConfigCollectFactor_one.nodeconfig_id = ""  #置空依赖
                ConfigCollectFactor_one.configcollectsendcmd_id = ""  # 置空依赖
                ConfigCollectFactor_one.delete()  #删除


            #关联之 ConfigCollectSendCmd 去掉依赖
            ConfigCollectSendCmd_all = ConfigCollectSendCmd.objects.filter(nodeconfig_id=qs_one.id)
            for ConfigCollectSendCmd_one in ConfigCollectSendCmd_all:
                ConfigCollectSendCmd_one.nodeconfig_id = ""  #置空依赖
                ConfigCollectSendCmd_one.delete()  #删除


            # 关联之 ConfigControlSendPorsConvertrule 去掉依赖
            ConfigControlSendPorsConvertrule_all = ConfigControlSendPorsConvertrule.objects.filter(nodeconfig_id=qs_one.id)
            for ConfigControlSendPorsConvertrule_one in ConfigControlSendPorsConvertrule_all:
                ConfigControlSendPorsConvertrule_one.nodeconfig_id = ""  #置空依赖
                ConfigControlSendPorsConvertrule_one.configcontrolsendporssection_id = ""  #置空依赖
                ConfigControlSendPorsConvertrule_one.delete()  #删除

            #关联之 ConfigControlSendPorsSection 去掉依赖
            ConfigControlSendPorsSection_all = ConfigControlSendPorsSection.objects.filter(nodeconfig_id=qs_one.id)
            for ConfigControlSendPorsSection_one in ConfigControlSendPorsSection_all:
                ConfigControlSendPorsSection_one.nodeconfig_id = ""  #置空依赖
                ConfigControlSendPorsSection_one.configcontrolsendparamid_id = ""  #置空依赖
                ConfigControlSendPorsSection_one.delete()  #删除

            #关联之 ConfigControlSendParamid 去掉依赖
            ConfigControlSendParamid_all = ConfigControlSendParamid.objects.filter(nodeconfig_id=qs_one.id)
            for ConfigControlSendParamid_one in ConfigControlSendParamid_all:
                ConfigControlSendParamid_one.nodeconfig_id = ""  #置空依赖
                ConfigControlSendParamid_one.configcontrolsendcmd_id = ""  #置空依赖
                ConfigControlSendParamid_one.delete()  #删除


            #关联之 ConfigControlSendCmd 去掉依赖
            ConfigControlSendCmd_all = ConfigControlSendCmd.objects.filter(nodeconfig_id=qs_one.id)
            for ConfigControlSendCmd_one in ConfigControlSendCmd_all:
                ConfigControlSendCmd_one.nodeconfig_id = ""
                ConfigControlSendCmd_one.delete()  #删除

            # 再删除本体
            qs_one.delete()

    # #批量设置用户名
    # def patch_set_user(self,request,querset):
    #     for qs_one in querset:
    #         #先设置关联用户名
    #         old_sjyzs = ShuJuYinZi.objects.filter(shangbaoshuju_id=qs_one.id)
    #         for old_tagattrib_one in old_sjyzs:
    #             old_tagattrib_one.w
    #         #再删除本体
    #         qs_one.delete()


    # patch_copy.short_description = "批量复制"
    patch_delete.short_description = "批量删除"

    actions=[patch_delete,]

    # #外键筛选
    # def render_change_form(self, request, context, add=False, change=False, form_url='', obj=None):
    #     # 新增 Post 时，相关联的 Blog 需要过滤，关键就在下面这句。
    #     context['adminform'].form.fields['blog'].queryset = Team.objects.filter(user=request.user)
    #     return super(NodeConfigXadmin, self).render_change_form(request, context, add, change, form_url, obj)

    def changelist_view(self, request, extra_context=None):   #根据用户权限不同显示不同数据
        user = request.user
        if user.is_superuser:
            self.list_display = ['', '']
        else:
            self.list_display = ['']
            return super(NodeConfigXadmin, self).changelist_view(request, extra_context=None)


    def instance_forms(self):  # 需要重写instance_forms方法，此方法作用是生成表单实例
        super().instance_forms()
        # 判断是否为新建操作，新建操作才会设置write_user的默认值
        if not self.org_obj:
            self.form_obj.initial['write_user'] = self.request.user.id


    def save_models(self):  # 重载save_models的方法，可以在做了某个动作后，动态重新加载
        obj = self.new_obj  # 取得当前用例的实例
        if self.request.user.is_superuser:  # 超级用户则不对编写人做修改
            obj.save()  # 保存当前用例
        else:  # 非超级用户会自动保存编写人
            user = User.objects.get(username=self.request.user)
            obj.write_user_id = user.id  # 保存当前的write_user为用户登录的user
            obj.save()  # 保存当前用例

    # #条件过滤
    # def queryset(self):  # 重载queryset方法，用来做到不同的admin取出的数据不同
    #     qs = super(NodeConfigXadmin, self).queryset()  # 调用父类
    #     if self.request.user.is_superuser:  # 超级用户可查看所有数据
    #         return qs
    #     else:
    #         qs = qs.filter(write_user=self.request.user)  # 否则只显示本用户数据
    #         return qs  # 返回qs

    #外键过滤
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if not request.user.is_superuser:
            if db_field.name == "nodeconfig":
                # shop = Shop.objects.get(username=request.user.username)
                kwargs["queryset"] = NodeConfig.objects.filter(write_user=request.user)
        else:
            kwargs["queryset"] = NodeConfig.objects.all()
        return super(NodeConfigXadmin, self).formfield_for_foreignkey(db_field, request, **kwargs)


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
            # if len(all_list_1[0]) == 17:
            #     while i < len(all_list_1):
            #         newaddandcheck = NewAddAndCheck()  # 数据库的对象等于ClickAndBack,实例化
            #         newaddandcheck.test_project = all_list_1[i][0]  # 填写项目all_list_1[i][j]
            #         newaddandcheck.test_module = all_list_1[i][1]  # 填写模块
            #         newaddandcheck.test_page = all_list_1[i][2]  # 填写测试页
            #
            #         if all_list_1[i][3] == u"冒烟用例":
            #             newaddandcheck.case_priority = "P0" # 填写用例优先级
            #         elif all_list_1[i][3] == u"系统的重要功能用例":
            #             newaddandcheck.case_priority = "P1"  # 填写用例优先级
            #         elif all_list_1[i][3] == u"系统的一般功能用例":
            #             newaddandcheck.case_priority = "P2"  # 填写用例优先级
            #         elif all_list_1[i][3] == u"极低级别的用例":
            #             newaddandcheck.case_priority = "P3"  # 填写用例优先级
            #
            #
            #         newaddandcheck.test_case_title = all_list_1[i][4]  # 填写测试内容的名称
            #         newaddandcheck.is_run_case =all_list_1[i][5]  # 填写是否运行
            #
            #         newaddandcheck.login_url = all_list_1[i][6]  # 填写登录页的url
            #
            #         newaddandcheck.is_auto_input_code = all_list_1[i][7]  # 填写是否自动输入验证码
            #         newaddandcheck.code_image_xpath =all_list_1[i][8]  # 填写验证码xpath路径
            #
            #         newaddandcheck.code_type = all_list_1[i][9]  # 填写验证码类型
            #         newaddandcheck.code_input_ele_find =all_list_1[i][10]  # 填写验证码输入框查找风格
            #         newaddandcheck.code_input_ele_find_value = all_list_1[i][11]  # 填写验证码输入框查找风格的确切值
            #
            #         newaddandcheck.login_button_ele_find = all_list_1[i][12]  # 填写确定按钮查找风格的确切值
            #         newaddandcheck.login_button_ele_find_value = all_list_1[i][13] # 填写是否点击取消按钮
            #         newaddandcheck.click_login_button_delay_time = all_list_1[i][14]  # 填写取消按钮查找风格
            #
            #         newaddandcheck.case_counts = all_list_1[i][15]  # 填写case_counts
            #         if all_list_1[i][16] != None:  # 如果编写人列有数据则填写编写人
            #             users = User.objects.all()
            #             for user in users:
            #                 if user.username == all_list_1[i][16]:
            #                     newaddandcheck.write_user_id = user.id  # 填写编写人
            #         newaddandcheck.save()  # 保存到数据库
            #
            #         i = i + 1
            pass
        return super(NodeConfigXadmin,self).post(request,*args,**kwargs)  # 必须调用clickandbackAdmin父类，再调用post方法，否则会报错
        # 一定不要忘记，否则整个ClickAndBackXAdmin保存都会出错


xadmin.site.register(NodeConfig, NodeConfigXadmin)  # 在xadmin中注册NodeConfig