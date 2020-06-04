from django.shortcuts import render
from django.views.generic import View   #导入View
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from wanwenyc.settings import DJANGO_SERVER_YUMING,MEDIA_ROOT


from .modelsdev import TagContent,User,TagAttrib
from .models import XieyiConfigDate,FtpUploadFile,CloseXieYiCommand,RestartXieYiCommand
from .modelsnewdev import NodeConfig,ConfigCollectSendCmd,ConfigCollectFactor,\
    ConfigCollectReceivePors,ConfigCollectReceivePorsSection,ConfigCollectReceivePorsConvertrule,\
    ConfigControlSendCmd,ConfigControlSendParamid,ConfigControlSendPorsSection,ConfigControlSendPorsConvertrule


from .forms import TagContentForm
from .forms import XieyiConfigDateForm


#节点配置View
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


#协议测试用例View
class XieyiConfigDateView(View):
    """
    节点配置复制编写页面处理
    """

    def get(self, request, xieyiconfigdate_id):
        if request.user.username == 'check':
            return render(request, "canNotAddclickAndBack.html", {
                "django_server_yuming": DJANGO_SERVER_YUMING
            })
        elif request.user.is_active:
            xieyiconfigdate = XieyiConfigDate.objects.get(id=int(xieyiconfigdate_id))  # 获取数据
            is_with_relevance = 1

            return render(request, "xieyiconfigdate/xieyiConfigDate.html",
                          {"xieyiconfigdate": xieyiconfigdate,
                           "django_server_yuming": DJANGO_SERVER_YUMING,
                           "is_withRelevance": is_with_relevance,
                           })
        else:
            return render(request, "addContentError.html", {
                "django_server_yuming": DJANGO_SERVER_YUMING
            })

    def post(self, request,xieyiconfigdate_id):
        username = request.user.username

        xieyiconfigdate_form = XieyiConfigDateForm(request.POST)  # 实例化NewAddAndCheckForm()
        xieyiconfigdate = XieyiConfigDate.objects.get(id=int(xieyiconfigdate_id))  # 获取内容

        # 处理附带复制内容
        is_with_relevance = request.POST.get('is_withRelevance', '')
        print("is_withRelevance:%s" % is_with_relevance)
        print("is_withRelevance类型:%s" % type(is_with_relevance))
        is_with_relevance =int(is_with_relevance)
        print("is_withRelevance:%s" % is_with_relevance)
        print("is_withRelevance类型:%s" % type(is_with_relevance))
        # 结束处理

        if xieyiconfigdate_form.is_valid():  # is_valid()判断是否有错

            xieyiconfigdate_form.save(commit=True)  # 将信息保存到数据库中

            zj = XieyiConfigDate.objects.all().order_by('-add_time')[:1][0]  # 根据添加时间查询最新的
            user = User.objects.get(username=username)
            zj.write_user_id = user.id
            zj.save()

            xieyiconfigdateid = zj.id
            xieyiconfigdateadd = XieyiConfigDate.objects.get(id=int(xieyiconfigdateid))  # 获取用例

            # 如果增加附带
            if is_with_relevance == 1:
                print("处理附带内容")
                #处理FTP上传文件
                ftpuploadfile_old_all = FtpUploadFile.objects.filter(
                    xieyiconfigdate_id=xieyiconfigdate_id).order_by("id")
                ftpuploadfile_old_all_count = ftpuploadfile_old_all.count()
                if ftpuploadfile_old_all_count != 0:
                    for ftpuploadfile_old in ftpuploadfile_old_all:
                        ftpuploadfile_new = FtpUploadFile()
                        ftpuploadfile_new.xieyiconfigdate_id = zj.id
                        ftpuploadfile_new.up_remote_file = ftpuploadfile_old.up_remote_file
                        ftpuploadfile_new.up_local_file = ftpuploadfile_old.up_local_file
                        ftpuploadfile_new.save()

                # 处理关闭协议命令
                closexieyicommand_old_all = CloseXieYiCommand.objects.filter(
                    xieyiconfigdate_id=xieyiconfigdate_id).order_by("id")
                closexieyicommand_old_all_count = closexieyicommand_old_all.count()
                if closexieyicommand_old_all_count != 0:
                    for closexieyicommand_old in closexieyicommand_old_all:
                        closexieyicommand_new = CloseXieYiCommand()
                        closexieyicommand_new.xieyiconfigdate_id = zj.id
                        closexieyicommand_new.close_command = closexieyicommand_old.close_command
                        closexieyicommand_new.save()

                # 处理重启协议命令
                restartxieyicommand_old_all =  RestartXieYiCommand.objects.filter(
                    xieyiconfigdate_id=xieyiconfigdate_id).order_by("id")
                restartxieyicommand_old_all_count =  restartxieyicommand_old_all.count()
                if  restartxieyicommand_old_all_count != 0:
                    for  restartxieyicommand_old in  restartxieyicommand_old_all:
                         restartxieyicommand_new =  RestartXieYiCommand()
                         restartxieyicommand_new.xieyiconfigdate_id = zj.id
                         restartxieyicommand_new.restart_command =  restartxieyicommand_old.restart_command
                         restartxieyicommand_new.save()



            return render(request, "xieyiconfigdate/xieyiConfigDate.html", {
                "xieyiconfigdate": xieyiconfigdateadd,
                "sumsg":u"添加数据---【{}】---成功,请继续添加".format(xieyiconfigdateadd.test_case_title),
                "django_server_yuming": DJANGO_SERVER_YUMING,
            })
        else:
            return render(request, 'xieyiconfigdate/xieyiConfigDateForm.html', {
                "xieyiconfigdate": xieyiconfigdate,
                "xieyiconfigdateform": xieyiconfigdate_form ,
                "errmsg":u"添加失败，请重新添加，添加时请检查各个字段是否填写",
                "django_server_yuming": DJANGO_SERVER_YUMING,
            })  # 返回页面，回填信息

#根据数据库内容s生成dev文件
def NodeConfigMakeDevRequest(request, nodeconfig_id, trackback=None):
    nodeconfig = NodeConfig.objects.get(id=int(nodeconfig_id))  # 获取用例
    from depend.shucaiyi.modelsnewdevdepend.nodeConfigDependClass import MakeNodeConfig
    caseId  = nodeconfig.id
    mnc = MakeNodeConfig(caseId=caseId)
    file_name = nodeconfig.config_project + ".dev"
    file_content = mnc.makeAllXml()
    # import chardet
    # res = chardet.detect(file_content)
    # print("文件内容编码：")
    # print(res["encoding"])

    #将文件内容编码修改为utf8


    #判断文件是否存在，如果存在，则删除原有文件
    import os

    from wanwenyc.settings import MEDIA_ROOT
    from .modelsnewdev import upload_dev_file_path
    u_p = upload_dev_file_path(nodeconfig,file_name)
    print("上传文件路径：")
    print(u_p)
    print("MEDIA_ROOT:")
    print(MEDIA_ROOT)

    file_name_full_path = "{}/{}".format(MEDIA_ROOT,u_p)
    print("上传文件全路径：")
    print(file_name_full_path)
    is_exist = os.path.exists(file_name_full_path)
    if is_exist:  #如果存在，则删除文件
        os.remove(file_name_full_path)
        print("删除文件")

    from django.core.files import File   #导入File
    from django.core.files.base import ContentFile  #导入ContentFile
    #使用ContentFile保存内容
    nodeconfig.dev_file.save(name=file_name,content=ContentFile(file_content))   #使用ContentFile保存  #学习网址：https://www.jianshu.com/p/5c05eb437e08

    # #将文件编码从ISO-8859-1修改为utf-8
    # with open(file_name_full_path, "r",encoding='iso8859-1') as f:
    #     data = f.read()
    #
    # new_data = data.encode("iso-8859-1").decode('gbk')   #将内容以iso-8859-1编码，再以gbk解码
    #将内容再次以utf-8的形式保存
    with open(file_name_full_path, "w",encoding='utf-8') as f:  #保存到文件中，以utf-8编码
        f.write(file_content)

    # #使用File保存内容
    # f = open('/path/to/file')
    # nodeconfig.dev_file.save(name=file_name,content= File(f))
    print("重定向返回'/shucaiyidate/nodeconfig/'")
    return HttpResponseRedirect('/shucaiyidate/nodeconfig/')  #重定向到该页面

#根据已有内容复制一条数据
def NodeConfigCopyRequest(request, nodeconfig_id, trackback=None):
    nodeconfig_old = NodeConfig.objects.get(id=int(nodeconfig_id))  # 获取用例
    new_nodeconfig = NodeConfig()
    new_nodeconfig.config_project = nodeconfig_old.config_project
    new_nodeconfig.config_version = nodeconfig_old.config_version
    new_nodeconfig.config_device = nodeconfig_old.config_device
    new_nodeconfig.config_collect_packet_len = nodeconfig_old.config_collect_packet_len
    new_nodeconfig.save()  #保存

    #获取最新的的数据
    zx_nodeconfig = NodeConfig.objects.all().order_by('-add_time')[:1][0]  # 根据添加时间查询最新的

    #复制 采集指令_下发指令
    configcollectsendcmd_old_all = ConfigCollectSendCmd.objects.filter(nodeconfig_id=nodeconfig_old.id).order_by("id")
    configcollectsendcmd_old_all_count = configcollectsendcmd_old_all.count()
    if configcollectsendcmd_old_all_count == 0:
        pass
    else:
        for configcollectsendcmd_old_one in configcollectsendcmd_old_all:
            new_configcollectsendcmd =  ConfigCollectSendCmd()
            new_configcollectsendcmd.nodeconfig_id = zx_nodeconfig.id
            new_configcollectsendcmd.config_collect_send_id = configcollectsendcmd_old_one.config_collect_send_id
            new_configcollectsendcmd.config_collect_send_format = configcollectsendcmd_old_one.config_collect_send_format
            new_configcollectsendcmd.config_collect_send_cmd = configcollectsendcmd_old_one.config_collect_send_cmd
            new_configcollectsendcmd.config_collect_send_acktype = configcollectsendcmd_old_one.config_collect_send_acktype
            new_configcollectsendcmd.config_collect_send_ackhead = configcollectsendcmd_old_one.config_collect_send_ackhead
            new_configcollectsendcmd.config_collect_send_acktail = configcollectsendcmd_old_one.config_collect_send_acktail
            new_configcollectsendcmd.config_collect_send_acklen = configcollectsendcmd_old_one.config_collect_send_acklen
            new_configcollectsendcmd.config_collect_send_ackgap = configcollectsendcmd_old_one.config_collect_send_ackgap
            new_configcollectsendcmd.config_collect_send_ackcheckmode = configcollectsendcmd_old_one.config_collect_send_ackcheckmode
            new_configcollectsendcmd.config_collect_send_ackcheckarg = configcollectsendcmd_old_one.config_collect_send_ackcheckarg
            new_configcollectsendcmd.save()

            zx_configcollectsendcmd = ConfigCollectSendCmd.objects.all().order_by('-add_time')[:1][0]  # 根据添加时间查询最新的
            #复制 采集指令_监测因子
            configcollectfactor_old_all = ConfigCollectFactor.objects.filter(configcollectsendcmd_id=configcollectsendcmd_old_one.id).order_by("id")
            configcollectfactor_old_all_count = configcollectfactor_old_all.count()
            if configcollectfactor_old_all_count == 0:
                pass
            else:
                for configcollectfactor_old_one in configcollectfactor_old_all:
                    new_configcollectfactor = ConfigCollectFactor()
                    new_configcollectfactor.nodeconfig_id = zx_nodeconfig.id
                    new_configcollectfactor.configcollectsendcmd_id = zx_configcollectsendcmd.id
                    new_configcollectfactor.config_collect_factor_factorcode = configcollectfactor_old_one.config_collect_factor_factorcode
                    new_configcollectfactor.config_collect_factor_findmode = configcollectfactor_old_one.config_collect_factor_findmode
                    new_configcollectfactor.config_collect_factor_offset = configcollectfactor_old_one.config_collect_factor_offset
                    new_configcollectfactor.config_collect_factor_mark = configcollectfactor_old_one.config_collect_factor_mark
                    new_configcollectfactor.config_collect_factor_len = configcollectfactor_old_one.config_collect_factor_len
                    new_configcollectfactor.config_collect_factor_decodetype = configcollectfactor_old_one.config_collect_factor_decodetype
                    new_configcollectfactor.config_collect_factor_operator = configcollectfactor_old_one.config_collect_factor_operator
                    new_configcollectfactor.config_collect_factor_operand = configcollectfactor_old_one.config_collect_factor_operand
                    new_configcollectfactor.save() #保存

            #复制 采集指令_回复指令中的参数或状态
            configcollectreceivepors_old_all = ConfigCollectReceivePors.objects.filter(configcollectsendcmd_id=configcollectsendcmd_old_one.id).order_by("id")
            configcollectreceivepors_old_all_count = configcollectreceivepors_old_all.count()
            if configcollectreceivepors_old_all_count == 0:
                pass
            else:
                for configcollectreceivepors_old_one in configcollectreceivepors_old_all:
                    new_configcollectreceivepors = ConfigCollectReceivePors()
                    new_configcollectreceivepors.nodeconfig_id = zx_nodeconfig.id
                    new_configcollectreceivepors.configcollectsendcmd_id = zx_configcollectsendcmd.id
                    new_configcollectreceivepors.config_collect_receive_pors_factorcode =  configcollectreceivepors_old_one.config_collect_receive_pors_factorcode
                    new_configcollectreceivepors.config_collect_receive_pors_factortype = configcollectreceivepors_old_one.config_collect_receive_pors_factortype
                    new_configcollectreceivepors.save()  #保存

                    zx_configcollectreceivepors = ConfigCollectReceivePors.objects.all().order_by('-add_time')[:1][0]  # 根据添加时间查询最新的

                    #复制 采集指令_回复指令中的参数或状态_数据解析配置
                    configcollectreceiveporssection_old_all = ConfigCollectReceivePorsSection.objects.filter(configcollectreceivepors_id=configcollectreceivepors_old_one.id).order_by("id")
                    configcollectreceiveporssection_old_all_count = configcollectreceiveporssection_old_all.count()
                    if configcollectreceiveporssection_old_all_count == 0:
                        pass
                    else:
                        for configcollectreceiveporssection_old_one in configcollectreceiveporssection_old_all:
                            new_configcollectreceiveporssection = ConfigCollectReceivePorsSection()
                            new_configcollectreceiveporssection.nodeconfig_id = zx_nodeconfig.id
                            new_configcollectreceiveporssection.configcollectreceivepors_id = zx_configcollectreceivepors.id
                            new_configcollectreceiveporssection.config_collect_receive_pors_section_datatype = configcollectreceiveporssection_old_one.config_collect_receive_pors_section_datatype
                            new_configcollectreceiveporssection.config_collect_receive_pors_section_strformat = configcollectreceiveporssection_old_one.config_collect_receive_pors_section_strformat
                            new_configcollectreceiveporssection.config_collect_receive_pors_section_findmode = configcollectreceiveporssection_old_one.config_collect_receive_pors_section_findmode
                            new_configcollectreceiveporssection.config_collect_receive_pors_section_offset = configcollectreceiveporssection_old_one.config_collect_receive_pors_section_offset
                            new_configcollectreceiveporssection.config_collect_receive_pors_section_mark = configcollectreceiveporssection_old_one.config_collect_receive_pors_section_mark
                            new_configcollectreceiveporssection.config_collect_receive_pors_section_len = configcollectreceiveporssection_old_one.config_collect_receive_pors_section_len
                            new_configcollectreceiveporssection.config_collect_receive_pors_section_decodetype = configcollectreceiveporssection_old_one.config_collect_receive_pors_section_decodetype
                            new_configcollectreceiveporssection.config_collect_receive_pors_section_operator = configcollectreceiveporssection_old_one.config_collect_receive_pors_section_operator
                            new_configcollectreceiveporssection.config_collect_receive_pors_section_operand = configcollectreceiveporssection_old_one.config_collect_receive_pors_section_operand
                            new_configcollectreceiveporssection.save()

                            zx_configcollectreceiveporssection = ConfigCollectReceivePorsSection.objects.all().order_by('-add_time')[:1][0]  # 根据添加时间查询最新的

                            #复制 采集指令_回复指令中的参数或状态_数据解析配置_特殊规则
                            configcollectreceiveporsconvertrule_old_all = ConfigCollectReceivePorsConvertrule.objects.filter(configcollectreceiveporssection_id=configcollectreceiveporssection_old_one.id).order_by("id")
                            configcollectreceiveporsconvertrule_old_all_count = configcollectreceiveporsconvertrule_old_all.count()
                            if configcollectreceiveporsconvertrule_old_all_count == 0:
                                pass
                            else:
                                for configcollectreceiveporsconvertrule_old_one in configcollectreceiveporsconvertrule_old_all:
                                    new_configcollectreceiveporsconvertrule = ConfigCollectReceivePorsConvertrule()
                                    new_configcollectreceiveporsconvertrule.nodeconfig_id = zx_nodeconfig.id
                                    new_configcollectreceiveporsconvertrule.configcollectreceiveporssection_id = zx_configcollectreceiveporssection.id
                                    new_configcollectreceiveporsconvertrule.config_collect_receive_pors_convertrule_ruletype = configcollectreceiveporsconvertrule_old_one.config_collect_receive_pors_convertrule_ruletype
                                    new_configcollectreceiveporsconvertrule.config_collect_receive_pors_convertrule_enumvalue = configcollectreceiveporsconvertrule_old_one.config_collect_receive_pors_convertrule_enumvalue
                                    new_configcollectreceiveporsconvertrule.config_collect_receive_pors_convertrule_minvalue = configcollectreceiveporsconvertrule_old_one.config_collect_receive_pors_convertrule_minvalue
                                    new_configcollectreceiveporsconvertrule.config_collect_receive_pors_convertrule_maxvalue = configcollectreceiveporsconvertrule_old_one.config_collect_receive_pors_convertrule_maxvalue
                                    new_configcollectreceiveporsconvertrule.config_collect_receive_pors_convertrule_resultvalue = configcollectreceiveporsconvertrule_old_one.config_collect_receive_pors_convertrule_resultvalue
                                    new_configcollectreceiveporsconvertrule.save()


    #复制 反控指令_下发指令
    configcontrolsendcmd_old_all = ConfigControlSendCmd.objects.filter(nodeconfig_id=nodeconfig_old.id).order_by("id")
    configcontrolsendcmd_old_all_count = configcontrolsendcmd_old_all.count()
    if configcontrolsendcmd_old_all_count == 0:
        pass
    else:
        for configcontrolsendcmd_old_one in configcontrolsendcmd_old_all:
            new_configcontrolsendcmd = ConfigControlSendCmd()
            new_configcontrolsendcmd.nodeconfig_id = zx_nodeconfig.id
            new_configcontrolsendcmd.config_control_send_id = configcontrolsendcmd_old_one.config_control_send_id
            new_configcontrolsendcmd.config_control_send_format = configcontrolsendcmd_old_one.config_control_send_format
            new_configcontrolsendcmd.config_control_send_cmd = configcontrolsendcmd_old_one.config_control_send_cmd
            new_configcontrolsendcmd.config_control_send_acktype = configcontrolsendcmd_old_one.config_control_send_acktype
            new_configcontrolsendcmd.config_control_send_ackhead = configcontrolsendcmd_old_one.config_control_send_ackhead
            new_configcontrolsendcmd.config_control_send_acktail = configcontrolsendcmd_old_one.config_control_send_acktail
            new_configcontrolsendcmd.config_control_send_acklen = configcontrolsendcmd_old_one.config_control_send_acklen
            new_configcontrolsendcmd.config_control_send_ackgap = configcontrolsendcmd_old_one.config_control_send_ackgap
            new_configcontrolsendcmd.config_control_send_ackcheckmode = configcontrolsendcmd_old_one.config_control_send_ackcheckmode
            new_configcontrolsendcmd.config_control_send_ackcheckarg = configcontrolsendcmd_old_one.config_control_send_ackcheckarg
            new_configcontrolsendcmd.save()

            zx_configcontrolsendcmd = ConfigControlSendCmd.objects.all().order_by('-add_time')[:1][0]  # 根据添加时间查询最新的

            #复制 反控指令_下发指令_参数
            configcontrolsendparamid_old_all = ConfigControlSendParamid.objects.filter(configcontrolsendcmd_id=configcontrolsendcmd_old_one.id).order_by("id")
            configcontrolsendparamid_old_all_count = configcontrolsendparamid_old_all.count()
            if configcontrolsendparamid_old_all_count == 0:
                pass
            else:
                for configcontrolsendparamid_old_one in configcontrolsendparamid_old_all:
                    new_configcontrolsendparamid = ConfigControlSendParamid()
                    new_configcontrolsendparamid.nodeconfig_id = zx_nodeconfig.id
                    new_configcontrolsendparamid.configcontrolsendcmd_id = zx_configcontrolsendcmd.id
                    new_configcontrolsendparamid.config_control_send_paramid = configcontrolsendparamid_old_one.config_control_send_paramid
                    new_configcontrolsendparamid.save()

                    zx_configcontrolsendparamid = ConfigControlSendParamid.objects.all().order_by('-add_time')[:1][0]  # 根据添加时间查询最新的

                    #复制 反控指令_下发指令_参数_配置
                    configcontrolsendporssection_old_all = ConfigControlSendPorsSection.objects.filter(configcontrolsendparamid_id=configcontrolsendparamid_old_one.id).order_by("id")
                    configcontrolsendporssection_old_all_count = configcontrolsendporssection_old_all.count()
                    if configcontrolsendporssection_old_all_count == 0:
                        pass
                    else:
                        for configcontrolsendporssection_old_one in configcontrolsendporssection_old_all:
                            new_configcontrolsendporssection = ConfigControlSendPorsSection()
                            new_configcontrolsendporssection.nodeconfig_id = zx_nodeconfig.id
                            new_configcontrolsendporssection.configcontrolsendparamid_id = zx_configcontrolsendparamid.id
                            new_configcontrolsendporssection.config_control_send_pors_section_datatype = configcontrolsendporssection_old_one.config_control_send_pors_section_datatype
                            new_configcontrolsendporssection.config_control_send_pors_section_strformat = configcontrolsendporssection_old_one.config_control_send_pors_section_strformat
                            new_configcontrolsendporssection.config_control_send_pors_section_findmode = configcontrolsendporssection_old_one.config_control_send_pors_section_findmode
                            new_configcontrolsendporssection.config_control_send_pors_section_offset = configcontrolsendporssection_old_one.config_control_send_pors_section_offset
                            new_configcontrolsendporssection.config_control_send_pors_section_mark = configcontrolsendporssection_old_one.config_control_send_pors_section_mark
                            new_configcontrolsendporssection.config_control_send_pors_section_len = configcontrolsendporssection_old_one.config_control_send_pors_section_len
                            new_configcontrolsendporssection.config_control_send_pors_section_decodetype = configcontrolsendporssection_old_one.config_control_send_pors_section_decodetype
                            new_configcontrolsendporssection.config_control_send_pors_section_operator = configcontrolsendporssection_old_one.config_control_send_pors_section_operator
                            new_configcontrolsendporssection.config_control_send_pors_section_operand = configcontrolsendporssection_old_one.config_control_send_pors_section_operand
                            new_configcontrolsendporssection.save()

                            zx_configcontrolsendporssection = ConfigControlSendPorsSection.objects.all().order_by('-add_time')[:1][0]  # 根据添加时间查询最新的

                            #复制 反控指令_下发指令_参数_配置_特殊规则
                            configcontrolsendporsconvertrule_old_all  = ConfigControlSendPorsConvertrule.objects.filter(configcontrolsendporssection_id=configcontrolsendporssection_old_one.id).order_by("id")
                            configcontrolsendporsconvertrule_old_all_count = configcontrolsendporsconvertrule_old_all.count()
                            if configcontrolsendporsconvertrule_old_all_count == 0:
                                pass
                            else:
                                for configcontrolsendporsconvertrule_old_one in configcontrolsendporsconvertrule_old_all:
                                    new_configcontrolsendporsconvertrule=ConfigControlSendPorsConvertrule()
                                    new_configcontrolsendporsconvertrule.nodeconfig_id = zx_nodeconfig.id
                                    new_configcontrolsendporsconvertrule.configcontrolsendporssection_id = zx_configcontrolsendporssection.id
                                    new_configcontrolsendporsconvertrule.config_control_send_pors_convertrule_ruletype = configcontrolsendporsconvertrule_old_one.config_control_send_pors_convertrule_ruletype
                                    new_configcontrolsendporsconvertrule.config_control_send_pors_convertrule_enumvalue = configcontrolsendporsconvertrule_old_one.config_control_send_pors_convertrule_enumvalue
                                    new_configcontrolsendporsconvertrule.config_control_send_pors_convertrule_minvalue = configcontrolsendporsconvertrule_old_one.config_control_send_pors_convertrule_minvalue
                                    new_configcontrolsendporsconvertrule.config_control_send_pors_convertrule_maxvalue = configcontrolsendporsconvertrule_old_one.config_control_send_pors_convertrule_maxvalue
                                    new_configcontrolsendporsconvertrule.config_control_send_pors_convertrule_resultvalue = configcontrolsendporsconvertrule_old_one.config_control_send_pors_convertrule_resultvalue
                                    new_configcontrolsendporsconvertrule.save()  #保存

    print("重定向返回'/shucaiyidate/nodeconfig/'")
    return HttpResponseRedirect('/shucaiyidate/nodeconfig/')  #重定向到该页面

#解析上传的原有的Dev文件，并将其入库
def NodeConfigReadAndSaveRequest(request, nodeconfig_id, trackback=None):
    from depend.shucaiyi.modelsnewdevdepend.nodeConfigDependClass import  ReadNodeConfig
    nodeconfig = NodeConfig.objects.get(id=int(nodeconfig_id))   #获取用例

    if nodeconfig.local_file:  #如果local_file上传有文件，则对文件进行解析
        file_path = str(nodeconfig.local_file)
        print("上传文件：")
        print(file_path)

        file_full_path = MEDIA_ROOT + "/" + file_path
        print("上传文件绝对路径：")
        print(file_full_path)
        try:
            filePath = file_full_path
            caseId = nodeconfig_id
            rn = ReadNodeConfig(filePath,caseId)
            rn.runMain()
        except  Exception as e:
            print("没有入库成功，原因：【%s】" % e)

    else:  #否则，不做任何处理
        pass

    print("重定向返回'/shucaiyidate/nodeconfig/'")
    return HttpResponseRedirect('/shucaiyidate/nodeconfig/')  #重定向到该页面

