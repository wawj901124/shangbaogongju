from django.contrib import admin

# Register your models here.

from .modelsnewdev import NodeConfig,ConfigCollectSendCmd,ConfigCollectFactor

# #自定义管理页面
# class NodeConfigAdmin(admin.ModelAdmin):
#     list_display = ["id",
#                     "config_project",
#                     "config_file_name",
#                     "go_to"]  # 定义显示的字段
#
# admin.site.register(NodeConfig,NodeConfigAdmin)  #自定义注册

class ConfigCollectSendCmdInline(admin.TabularInline):
    model = ConfigCollectSendCmd
    extra = 0

class ConfigCollectFactorInline(admin.TabularInline):
    model = ConfigCollectFactor
    extra = 0
    # formset = ConfigCollectFactorInlineFormSet




#使用装饰器注册
@admin.register(NodeConfig)
class NodeConfigAdmin(admin.ModelAdmin):
    list_display = ["id",
                    "config_project",
                    "config_file_name",
                    "go_to"]  # 定义显示的字段
    fieldsets = [
        (None,    {'fields': ['config_project',"config_file_name",]}),
    ]
    inlines = [ConfigCollectSendCmdInline,ConfigCollectFactorInline]







# admin.site.register(NodeConfig)   #直接注册
# admin.site.register(ConfigCollectSendCmd)
# admin.site.register(ConfigCollectFactor)