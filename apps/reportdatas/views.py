from django.shortcuts import render
from django.views.generic import View   #导入View
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from wanwenyc.settings import DJANGO_SERVER_YUMING,MEDIA_ROOT
from .models import RdmAutoStatic,RdmStatic
# Create your views here.

#根据数据库内容s生成dev文件
def RdmAutoStaticRequest(request, rdmautostatic_id, trackback=None):
    rdmautostatic = RdmAutoStatic.objects.get(id=int(rdmautostatic_id))  # 获取用例
    people_name = rdmautostatic.people_name
    start_date = str(rdmautostatic.start_date)
    end_date = str(rdmautostatic.end_date)
    print(people_name)
    print(start_date)
    print(end_date)
    from django.db.models import Q
    # s使用Q来筛选不等于'<span style="margin-left: 19px;color: gray;">无</span>'的项
    mubiao_data_list = RdmStatic.objects.filter(~Q(day_task_name='[]')).\
        filter(~Q(week_task_deck='<span style="margin-left: 19px;color: gray;">无</span>')).\
        filter(people_name=people_name).filter(is_week=False).order_by('-id')  #筛选出有效的相应人员的日记录,按照id倒序排列

    all_task_name_list = []
    all_task_desc_list = []
    all_task_quse_list = []

    for mubiao_data_one in mubiao_data_list:
        day_date = mubiao_data_one.day_date
        new_day_date_list = []
        for one_char in day_date:
            if one_char in "0123456789-":
                new_day_date_list.append(one_char)
        new_day_date = "".join(new_day_date_list)
        #获取到各项的日期
        print("各项的日期为：%s"% new_day_date)
        if start_date <= new_day_date and new_day_date<=end_date:
            print("在时间范围内的日期：%s" % new_day_date)
            #统计在时间范围内的数据
            #统计所有的任务名称
            day_task_name = mubiao_data_one.day_task_name
            print(day_task_name)
            print(type(day_task_name))
            day_task_name_list = eval(day_task_name)   #eval()函数将列表样式的字符串自动转为列表
            print("day_task_name_list:")
            print(day_task_name_list)
            print(type(day_task_name_list))
            for day_task_name_one in day_task_name_list:
                if day_task_name_one not in all_task_name_list:
                    all_task_name_list.append(day_task_name_one)

            #统计所有任务详情
            day_task_desc = mubiao_data_one.day_task_desc
            if day_task_desc not in all_task_desc_list:
                all_task_desc_list.append(day_task_desc)

            #统计所有问题详情
            day_task_quse =  mubiao_data_one.day_task_quse
            if day_task_quse not in all_task_quse_list:
                all_task_quse_list.append(day_task_quse)



    print("所有任务名称：")
    print(all_task_name_list)
    print("所有任务详情：")
    print(all_task_desc_list)
    print("所有问题详情：")
    print(all_task_quse_list)
    rdmautostatic.all_task_name = all_task_name_list
    rdmautostatic.all_task_desc = all_task_desc_list
    rdmautostatic.all_task_quse = all_task_quse_list
    rdmautostatic.save()  #保存入库
    print("重定向返回'/reportdatas/rdmautostatic/'")
    return HttpResponseRedirect('/reportdatas/rdmautostatic/')  #重定向到该页面