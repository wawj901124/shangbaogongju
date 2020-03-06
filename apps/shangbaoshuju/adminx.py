import xadmin

from .models import ShangBaoShuJu,ShuJuYinZi
from .models import StoreSBShuJu



class ShangBaoShuJuAdmin(object):
    ziduan = ['id','test_project','test_module',
              'test_page','test_case_title',
              'forcount',


              'add_time','update_time']

    list_display =['test_project','test_module',
                   'test_page',
                   'test_case_title',
                   'forcount',



                   'add_time','update_time']#定义显示的字段
    search_fields =  ['test_project','test_module',
                   'test_case_title',]   #定义搜索字段
    list_filter =  ['test_project','test_module',
                   'test_case_title',] #定义筛选的字段
    model_icon = 'fa fa-bars '  # 定义图标显示
    ordering = ['-add_time']  # 添加默认排序规则显示排序，根据添加时间倒序排序
    # readonly_fields = ziduan  # 设置某些字段为只为可读  #设置了readonly_fields，再设置exclude，exclude对该字段无效，
    # exclude = ['case_step']  # 设置某些字段为不显示，即隐藏  #readonly_fields和exclude设置会有冲突
    # inlines = [TestCaseInline]  # inlines配和TestCaseInline使用，可以直接在项目页面添加测试用例#只能做一层嵌套，不能进行两层嵌套
    # list_editable = ziduan   # 可以在列表页对字段进行编辑
    refresh_times = [3, 5]  # 对列表页进行定时刷新,配置了3秒和5秒，可以从中选择一个
    list_per_page = 50   #每页设置50条数据，默认每页展示100条数据
    # fk_fields = ['test_project_id',]  #设置显示外键字段，未生效
    list_display_links = []   #设置点击链接进入编辑页面的字段
    # date_hierarchy = 'add_time'   #详细时间分层筛选，未生效
    # show_detail_fields = []   #显示数据详情
    # data_charts = {   #使用网址：https://xadmin.readthedocs.io/en/latest/_modules/xadmin/plugins/chart.html
    #                   # 插件介绍网址：http://www.mamicode.com/info-detail-2403646.html
    #                   #使用网址：https://www.jianshu.com/p/6201e1e9133c
    #     "user_count": {'title': u"页面加载时间", "x-field": "forcount", "y-field": ( 'page_load_time_no_catch', 'dom_load_time_no_catch',),
    #                    "order": ('id',)},
    # }

    # fields=['test_project',]   #添加页的字段显示


    #设置内联
    class ShuJuYinZiInline(object):
        model = ShuJuYinZi
        exclude = ["add_time","update_time","write_user"]
        extra = 1
        style = 'tab'    #以标签形式展示

    inlines = [ShuJuYinZiInline, ]

    #批量处理命令
    def patch_copy(self,request,querset):  #此处的querset为选中的数据
        querset = querset.order_by('id')  #按照id顺序排序
        for qs_one in querset:
            #新建实体并复制选中的内容
            new_sbsj = ShangBaoShuJu()
            new_sbsj.test_project = qs_one.test_project
            new_sbsj.test_module = qs_one.test_module
            new_sbsj.test_page = qs_one.test_page
            new_sbsj.test_case_title = qs_one.test_case_title
            new_sbsj.forcount = qs_one.forcount
            new_sbsj.time_delay = qs_one.time_delay
            new_sbsj.is_check_crc = qs_one.is_check_crc
            new_sbsj.shujuduan_st = qs_one.shujuduan_st
            new_sbsj.shujuduan_cn = qs_one.shujuduan_cn
            new_sbsj.shujuduan_pw = qs_one.shujuduan_pw
            new_sbsj.mn_type = qs_one.mn_type
            new_sbsj.shujuduan_mn = qs_one.shujuduan_mn
            new_sbsj.mn_sql = qs_one.mn_sql
            new_sbsj.mn_auto_make_base = qs_one.mn_auto_make_base
            new_sbsj.mn_auto_make_down = qs_one.mn_auto_make_down
            new_sbsj.mn_auto_make_up = qs_one.mn_auto_make_up
            new_sbsj.mn_auto_make_interval = qs_one.mn_auto_make_interval
            new_sbsj.shujuduan_flag = qs_one.shujuduan_flag
            new_sbsj.shujuduan_cp_datatime_type = qs_one.shujuduan_cp_datatime_type
            new_sbsj.actual_data_sql = qs_one.actual_data_sql
            new_sbsj.dele_zidian = qs_one.dele_zidian
            if self.request.user.is_superuser:  # 超级用户则不保存user
                pass
            else: #否则保存user为当前用户
                new_sbsj.write_user = self.request.user
            new_sbsj.save()      #保存数据
            #获取刚保存的数据的id
            newadd = ShangBaoShuJu.objects.filter(test_case_title = qs_one.test_case_title).order_by('-add_time')
            for new_last in newadd:
                newaddid = new_last.id
                break

            #获取ShuJuYinZi中相应的内容
            old_sjyzs = ShuJuYinZi.objects.filter(shangbaoshuju_id=qs_one.id).order_by('add_time')
            for old_sjyz_one in old_sjyzs:
                new_sjyz = ShuJuYinZi()
                new_sjyz.shangbaoshuju_id = newaddid
                new_sjyz.yinzi_code = old_sjyz_one.yinzi_code
                new_sjyz.yinzi_rtd_up = old_sjyz_one.yinzi_rtd_up
                new_sjyz.yinzi_rtd_down = old_sjyz_one.yinzi_rtd_down
                new_sjyz.yinzi_rtd_xiaoshuwei = old_sjyz_one.yinzi_rtd_xiaoshuwei
                new_sjyz.yinzi_rtd_count = old_sjyz_one.yinzi_rtd_count
                new_sjyz.yinzi_flag = old_sjyz_one.yinzi_flag
                if self.request.user.is_superuser:  # 超级用户则不保存user
                    pass
                else:  # 否则保存user为当前用户
                    new_sjyz.write_user = self.request.user
                new_sjyz.save()   #保存数据库


    #批量删除
    def patch_delete(self,request,querset):
        for qs_one in querset:
            #先删除关联
            old_sjyzs = ShuJuYinZi.objects.filter(shangbaoshuju_id=qs_one.id)
            for old_sjyz_one in old_sjyzs:
                old_sjyz_one.delete()
            #再删除本体
            qs_one.delete()

    # #批量设置用户名
    # def patch_set_user(self,request,querset):
    #     for qs_one in querset:
    #         #先设置关联用户名
    #         old_sjyzs = ShuJuYinZi.objects.filter(shangbaoshuju_id=qs_one.id)
    #         for old_sjyz_one in old_sjyzs:
    #             old_sjyz_one.w
    #         #再删除本体
    #         qs_one.delete()


    patch_copy.short_description = "批量复制"
    patch_delete.short_description = "批量删除"
    actions=[patch_copy,patch_delete,]




    def queryset(self):   #重载queryset方法，用来做到不同的admin取出的数据不同
        qs = super(ShangBaoShuJuAdmin, self).queryset()   #调用父类
        if self.request.user.is_superuser:   #超级用户可查看所有数据
            return qs
        else:
            qs = qs.filter(write_user=self.request.user)  #否则只显示本用户数据
            return qs   #返回qs

class StoreSBShuJuAdmin(object):
    ziduan = ['id','test_project','test_module',
              'test_page','test_case_title',
              'test_start_time','forcount',


              'add_time','update_time']

    list_display =['test_project','test_module',
                   'test_page',
                   'test_case_title','test_start_time',
                   'forcount',
                   'shujuduan_mn',
                   'sb_yinzi','sb_shuju','sb_ret',


                   'add_time','update_time']#定义显示的字段
    search_fields =  ['test_project','test_module',
                   'test_case_title','test_start_time',]   #定义搜索字段
    list_filter =  ['test_project','test_module',
                   'test_case_title','test_start_time',] #定义筛选的字段
    model_icon = 'fa fa-bars '  # 定义图标显示
    ordering = ['-add_time']  # 添加默认排序规则显示排序，根据添加时间倒序排序
    # readonly_fields = ziduan  # 设置某些字段为只为可读  #设置了readonly_fields，再设置exclude，exclude对该字段无效，
    # exclude = ['case_step']  # 设置某些字段为不显示，即隐藏  #readonly_fields和exclude设置会有冲突
    # inlines = [TestCaseInline]  # inlines配和TestCaseInline使用，可以直接在项目页面添加测试用例#只能做一层嵌套，不能进行两层嵌套
    # list_editable = ziduan   # 可以在列表页对字段进行编辑
    refresh_times = [3, 5]  # 对列表页进行定时刷新,配置了3秒和5秒，可以从中选择一个
    list_per_page = 50   #每页设置50条数据，默认每页展示100条数据
    # fk_fields = ['test_project_id',]  #设置显示外键字段，未生效
    list_display_links = []   #设置点击链接进入编辑页面的字段
    # date_hierarchy = 'add_time'   #详细时间分层筛选，未生效
    # show_detail_fields = []   #显示数据详情
    # data_charts = {   #使用网址：https://xadmin.readthedocs.io/en/latest/_modules/xadmin/plugins/chart.html
    #                   # 插件介绍网址：http://www.mamicode.com/info-detail-2403646.html
    #                   #使用网址：https://www.jianshu.com/p/6201e1e9133c
    #     "user_count": {'title': u"页面加载时间", "x-field": "forcount", "y-field": ( 'page_load_time_no_catch', 'dom_load_time_no_catch',),
    #                    "order": ('id',)},
    # }



    def queryset(self):   #重载queryset方法，用来做到不同的admin取出的数据不同
        qs = super(StoreSBShuJuAdmin, self).queryset()   #调用父类
        if self.request.user.is_superuser:   #超级用户可查看所有数据
            return qs
        else:
            qs = qs.filter(write_user=self.request.user)  #否则只显示本用户数据
            return qs   #返回qs

xadmin.site.register(ShangBaoShuJu, ShangBaoShuJuAdmin) #在xadmin中注册ShangBaoShuJu
xadmin.site.register(StoreSBShuJu, StoreSBShuJuAdmin) #在xadmin中注册StoreSBShuJu
