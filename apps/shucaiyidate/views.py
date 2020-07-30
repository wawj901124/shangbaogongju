from django.shortcuts import render
from django.views.generic import View   #导入View
from django.http import HttpResponse
from django.http import HttpResponseRedirect
import time

from wanwenyc.settings import DJANGO_SERVER_YUMING,MEDIA_ROOT


from .modelsdev import TagContent,User,TagAttrib
from .models import XieyiConfigDate,FtpUploadFile,CloseXieYiCommand,RestartXieYiCommand
from .modelsnewdev import NodeConfig,ConfigCollectSendCmd,ConfigCollectFactor,\
    ConfigCollectReceivePors,ConfigCollectReceivePorsSection,ConfigCollectReceivePorsConvertrule,\
    ConfigControlSendCmd,ConfigControlSendParamid,ConfigControlSendPorsSection,ConfigControlSendPorsConvertrule

from .modelsorder import XieyiConfigDateOrder,\
    XieyiTestCase,SenderHexDataOrder,RecriminatDataOrder,\
    FtpUploadFileOrder


from .forms import TagContentForm
from .forms import XieyiConfigDateForm
from .forms import XieyiTestCaseForm,XieyiConfigDateOrderForm,\
    SenderHexDataOrderForm,RecriminatDataOrderForm

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
                        time.sleep(1)
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
                        time.sleep(1)
                        closexieyicommand_new = CloseXieYiCommand()
                        closexieyicommand_new.xieyiconfigdate_id = zj.id
                        closexieyicommand_new.close_command = closexieyicommand_old.close_command
                        closexieyicommand_new.save()

                # 处理重启协议命令
                restartxieyicommand_old_all =  RestartXieYiCommand.objects.filter(
                    xieyiconfigdate_id=xieyiconfigdate_id).order_by("id")
                restartxieyicommand_old_all_count =  restartxieyicommand_old_all.count()
                if  restartxieyicommand_old_all_count != 0:
                    for restartxieyicommand_old in restartxieyicommand_old_all:
                        time.sleep(1)
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
    from depend.shucaiyi.modelsnewdevdepend.nodeConfigDependClass import MakeNodeConfig
    mnc = MakeNodeConfig(caseId=nodeconfig_id)
    print("即将异步调用生成新的dev文件函数" )
    mnc.saveMakeAllXmlContentToDB()
    print("已经异步调起生成新的dev文件的函数，但程序什么时候完成未知，继续后续操作")

    print("重定向返回'/shucaiyidate/nodeconfig/'")
    return HttpResponseRedirect('/shucaiyidate/nodeconfig/')  #重定向到该页面

#根据已有内容复制一条数据
def NodeConfigCopyRequest(request, nodeconfig_id, trackback=None):
    from depend.shucaiyi.modelsnewdevdepend.nodeConfigDependClass import CopyNodeConfig
    cnc = CopyNodeConfig(caseId=nodeconfig_id)

    print("即将异步调用根据现有数据生成新数据函数" )
    cnc.saveCopy()
    print("已经异步调起根据现有数据生成新数据函数，但程序什么时候完成未知，继续后续操作")

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
            print("即将调用异步入库ID为【%s】数据"% str(caseId))
            rn.runMain()
            print("调用异步入库【%s】数据完成，但程序什么时候完成未知，继续后续操作"% str(caseId))
        except  Exception as e:
            print("没有入库成功，原因：【%s】" % e)

    else:  #否则，不做任何处理
        pass

    print("重定向返回'/shucaiyidate/nodeconfig/'")
    return HttpResponseRedirect('/shucaiyidate/nodeconfig/')  #重定向到该页面

#删除一条数据
def NodeConfigDeleteRequest(request, nodeconfig_id, trackback=None):
    from depend.shucaiyi.modelsnewdevdepend.nodeConfigDependClass import DeleteNodeConfig
    dnc = DeleteNodeConfig(caseId=nodeconfig_id)

    print("即将同步调用删除ID为【%s】的数据函数"% str(nodeconfig_id) )
    dnc.deleteDate()
    # print("已经异步调起删除ID为【%s】的数据函数，但程序什么时候完成未知，继续后续操作" % str(nodeconfig_id))

    print("重定向返回'/shucaiyidate/nodeconfig/'")
    return HttpResponseRedirect('/shucaiyidate/nodeconfig/')  #重定向到该页面


#协议测试用例View
class XieyiTestCaseView(View):
    """
    节点配置复制编写页面处理
    """

    def get(self, request, xieyitestcase_id):
        if request.user.username == 'check':
            return render(request, "canNotAddclickAndBack.html", {
                "django_server_yuming": DJANGO_SERVER_YUMING
            })
        elif request.user.is_active:
            xieyitestcase = XieyiTestCase.objects.get(id=int(xieyitestcase_id))  # 获取数据
            #获取配置所有内容
            xieyiconfigdateorder_all = XieyiConfigDateOrder.objects.order_by("-id")


            is_with_relevance = 1

            return render(request, "xieyitestcase/xieyiTestCase.html",
                          {"xieyitestcase":  xieyitestcase,
                           "xieyiconfigdateorder_all":xieyiconfigdateorder_all,
                           "django_server_yuming": DJANGO_SERVER_YUMING,
                           "is_withRelevance": is_with_relevance,
                           })
        else:
            return render(request, "addContentError.html", {
                "django_server_yuming": DJANGO_SERVER_YUMING
            })

    def post(self, request,xieyitestcase_id):
        username = request.user.username
        # 获取配置所有内容
        xieyiconfigdateorder_all = XieyiConfigDateOrder.objects.order_by("-id")
        xieyitestcase_form = XieyiTestCaseForm(request.POST)  # 实例化NewAddAndCheckForm()
        xieyitestcase = XieyiTestCase.objects.get(id=int(xieyitestcase_id))  # 获取内容


        # 处理附带复制内容
        is_with_relevance = request.POST.get('is_withRelevance', '')  #获取is_withRelevance属性的值
        print("is_withRelevance:%s" % is_with_relevance)
        print("is_withRelevance类型:%s" % type(is_with_relevance))
        is_with_relevance =int(is_with_relevance)
        print("is_withRelevance:%s" % is_with_relevance)
        print("is_withRelevance类型:%s" % type(is_with_relevance))
        # 结束处理

        if xieyitestcase_form.is_valid():  # is_valid()判断是否有错

            xieyitestcase_form.save(commit=True)  # 将信息保存到数据库中

            zj = XieyiTestCase.objects.all().order_by('-add_time')[:1][0]  # 根据添加时间查询最新的
            user = User.objects.get(username=username)
            zj.write_user_id = user.id
            zj.save()

            xieyitestcaseid = zj.id
            xieyitestcaseadd = XieyiTestCase.objects.get(id=int(xieyitestcaseid))  # 获取用例

            # 如果增加附带
            if is_with_relevance == 1:
                print("处理附带内容")
                #处理协议测试之测试数据，端口发送和接收数据
                senderhexdataorder_old_all = SenderHexDataOrder.objects.filter(
                    xieyitestcase_id=xieyitestcase_id).order_by("id")
                senderhexdataorder_old_all_count = senderhexdataorder_old_all.count()
                if senderhexdataorder_old_all_count != 0:
                    for senderhexdataorder_old in senderhexdataorder_old_all:
                        senderhexdataorder_new = SenderHexDataOrder()
                        senderhexdataorder_new.xieyitestcase_id = zj.id
                        senderhexdataorder_new.is_send_hex = senderhexdataorder_old.is_send_hex
                        senderhexdataorder_new.send_wait_time = senderhexdataorder_old.send_wait_time
                        senderhexdataorder_new.com_send_date = senderhexdataorder_old.com_send_date
                        senderhexdataorder_new.is_need_expect = senderhexdataorder_old.is_need_expect
                        senderhexdataorder_new.is_need_after_expect = senderhexdataorder_old.is_need_after_expect
                        senderhexdataorder_new.is_just_one = senderhexdataorder_old.is_just_one
                        senderhexdataorder_new.is_receive_hex = senderhexdataorder_old.is_receive_hex
                        senderhexdataorder_new.com_expect_date = senderhexdataorder_old.com_expect_date
                        senderhexdataorder_new.is_assert_expect = senderhexdataorder_old.is_assert_expect
                        senderhexdataorder_new.xieyi_jiexi_expect_result = senderhexdataorder_old.xieyi_jiexi_expect_result
                        senderhexdataorder_new.save()  #保存


                # 处理反控数据
                recriminatdataorder_old_all = RecriminatDataOrder.objects.filter(
                    xieyitestcase_id=xieyitestcase_id).order_by("id")
                recriminatdataorder_old_all_count = recriminatdataorder_old_all.count()
                if recriminatdataorder_old_all_count != 0:
                    for recriminatdataorder_old in recriminatdataorder_old_all:
                        recriminatdataorder_new = RecriminatDataOrder()
                        recriminatdataorder_new.xieyitestcase_id = zj.id
                        recriminatdataorder_new.send_wait_time = recriminatdataorder_old.send_wait_time
                        recriminatdataorder_new.com_send_date = recriminatdataorder_old.com_send_date
                        recriminatdataorder_new.com_expect_date = recriminatdataorder_old.com_expect_date
                        recriminatdataorder_new.save()




            return render(request, "xieyitestcase/xieyiTestCase.html", {
                "xieyitestcase": xieyitestcaseadd,
                "xieyiconfigdateorder_all": xieyiconfigdateorder_all,
                "sumsg":u"添加数据---【{}】---成功,请继续添加".format(xieyitestcaseadd.test_case_title),
                "django_server_yuming": DJANGO_SERVER_YUMING,
                "is_withRelevance": is_with_relevance,
            })
        else:
            return render(request, 'xieyitestcase/xieyiTestCaseForm.html', {
                "xieyitestcase": xieyitestcase,
                "xieyiconfigdateorder_all": xieyiconfigdateorder_all,
                "xieyitestcaseform": xieyitestcase_form ,
                "errmsg":u"添加失败，请重新添加，添加时请检查各个字段是否填写",
                "django_server_yuming": DJANGO_SERVER_YUMING,
                "is_withRelevance": is_with_relevance,
            })  # 返回页面，回填信息


#协议测试用例之配置View
class XieyiConfigDateOrderView(View):
    """
    节点配置复制编写页面处理
    """

    def get(self, request, xieyiconfigdateorder_id):
        if request.user.username == 'check':
            return render(request, "canNotAddclickAndBack.html", {
                "django_server_yuming": DJANGO_SERVER_YUMING
            })
        elif request.user.is_active:
            xieyiconfigdateorder = XieyiConfigDateOrder.objects.get(id=int(xieyiconfigdateorder_id))  # 获取数据
            nodeconfig_all = NodeConfig.objects.all().order_by("-id")   #dev配置依赖

            is_with_relevance = 1

            return render(request, "xieyiconfigdateorder/xieyiConfigDateOrder.html",
                          {"xieyiconfigdateorder": xieyiconfigdateorder,
                           "django_server_yuming": DJANGO_SERVER_YUMING,
                           "nodeconfig_all":nodeconfig_all,
                           "is_withRelevance": is_with_relevance,
                           })
        else:
            return render(request, "addContentError.html", {
                "django_server_yuming": DJANGO_SERVER_YUMING
            })

    def post(self, request,xieyiconfigdateorder_id):
        username = request.user.username

        xieyiconfigdateorder_form = XieyiConfigDateOrderForm(request.POST)  # 实例化NewAddAndCheckForm()
        xieyiconfigdateorder = XieyiConfigDateOrder.objects.get(id=int(xieyiconfigdateorder_id))  # 获取内容
        nodeconfig_all = NodeConfig.objects.all().order_by("-id")  # dev配置依赖

        # 处理附带复制内容
        is_with_relevance = request.POST.get('is_withRelevance', '')
        print("is_withRelevance:%s" % is_with_relevance)
        print("is_withRelevance类型:%s" % type(is_with_relevance))
        is_with_relevance =int(is_with_relevance)
        print("is_withRelevance:%s" % is_with_relevance)
        print("is_withRelevance类型:%s" % type(is_with_relevance))
        # 结束处理

        if xieyiconfigdateorder_form.is_valid():  # is_valid()判断是否有错

            xieyiconfigdateorder_form.save(commit=True)  # 将信息保存到数据库中

            zj = XieyiConfigDateOrder.objects.all().order_by('-add_time')[:1][0]  # 根据添加时间查询最新的
            user = User.objects.get(username=username)
            zj.write_user_id = user.id
            zj.save()

            xieyiconfigdateorderid = zj.id
            xieyiconfigdateorderadd = XieyiConfigDateOrder.objects.get(id=int(xieyiconfigdateorderid))  # 获取用例

            # 如果增加附带
            if is_with_relevance == 1:
                print("处理附带内容")
                #处理FTP上传文件
                from .comonxadmin import CommonXadmin
                cx = CommonXadmin()
                sql_model_name= FtpUploadFileOrder
                neiqianwaijian_name = "xieyiconfigdateorder"
                neiqian_id = xieyiconfigdateorder_id
                neiqian_new_id = zj.id
                filter_name_list = None
                cx.sql_model_copy_common(sql_model_name=sql_model_name,
                                         neiqianwaijian_name=neiqianwaijian_name,
                                         neiqian_id=neiqian_id,
                                         neiqian_new_id=neiqian_new_id,
                                         filter_name_list=filter_name_list)




            return render(request, "xieyiconfigdateorder/xieyiConfigDateOrder.html", {
                "xieyiconfigdateorder": xieyiconfigdateorderadd,
                "sumsg":u"添加数据---【{}】---成功,请继续添加".format(xieyiconfigdateorderadd.test_project),
                "django_server_yuming": DJANGO_SERVER_YUMING,
                "nodeconfig_all": nodeconfig_all,
                "is_withRelevance": is_with_relevance,
            })
        else:
            return render(request, 'xieyiconfigdateorder/xieyiConfigDateOrderForm.html', {
                "xieyiconfigdateorder": xieyiconfigdateorder,
                "xieyiconfigdateorderform": xieyiconfigdateorder_form ,
                "errmsg":u"添加失败，请重新添加，添加时请检查各个字段是否填写",
                "django_server_yuming": DJANGO_SERVER_YUMING,
                "nodeconfig_all": nodeconfig_all,
                "is_withRelevance": is_with_relevance,
            })  # 返回页面，回填信息


#协议测试用例之串口测试数据View
class SenderHexDataOrderView(View):
    """
    串口收发数据复制编写页面处理
    """

    def get(self, request, senderhexdataorder_id):
        if request.user.username == 'check':
            return render(request, "canNotAddclickAndBack.html", {
                "django_server_yuming": DJANGO_SERVER_YUMING
            })
        elif request.user.is_active:
            senderhexdataorder = SenderHexDataOrder.objects.get(id=int(senderhexdataorder_id))  # 获取数据
            xieyitestcase_all = XieyiTestCase.objects.all().order_by("-id")   #dev配置依赖


            return render(request, "senderhexdataorder/senderHexDataOrder.html",
                          {"senderhexdataorder": senderhexdataorder,
                           "django_server_yuming": DJANGO_SERVER_YUMING,
                           "xieyitestcase_all":xieyitestcase_all,
                           })
        else:
            return render(request, "addContentError.html", {
                "django_server_yuming": DJANGO_SERVER_YUMING
            })

    def post(self, request,senderhexdataorder_id):
        username = request.user.username

        senderhexdataorder_form = SenderHexDataOrderForm(request.POST)  # 实例化NewAddAndCheckForm()
        senderhexdataorder = SenderHexDataOrder.objects.get(id=int(senderhexdataorder_id))  # 获取内容
        xieyitestcase_all = XieyiTestCase.objects.all().order_by("-id")  # dev配置依赖



        if senderhexdataorder_form.is_valid():  # is_valid()判断是否有错

            senderhexdataorder_form.save(commit=True)  # 将信息保存到数据库中

            zj = SenderHexDataOrder.objects.all().order_by('-add_time')[:1][0]  # 根据添加时间查询最新的
            user = User.objects.get(username=username)
            zj.write_user_id = user.id
            zj.save()

            senderhexdataorderid = zj.id
            senderhexdataorderadd = SenderHexDataOrder.objects.get(id=int(senderhexdataorderid))  # 获取用例


            return render(request, "senderhexdataorder/senderHexDataOrder.html", {
                "senderhexdataorder": senderhexdataorderadd,
                "sumsg":u"添加数据---【{}】---成功,请继续添加".format(senderhexdataorderadd.com_send_date),
                "django_server_yuming": DJANGO_SERVER_YUMING,
                "xieyitestcase_all": xieyitestcase_all,
            })
        else:
            return render(request, 'senderhexdataorder/senderHexDataOrderForm.html', {
                "senderhexdataorder": senderhexdataorder,
                "senderhexdataorderform": senderhexdataorder_form ,
                "errmsg":u"添加失败，请重新添加，添加时请检查各个字段是否填写",
                "django_server_yuming": DJANGO_SERVER_YUMING,
                "xieyitestcase_all": xieyitestcase_all,
            })  # 返回页面，回填信息


#协议测试用例之反控测试数据View
class RecriminatDataOrderView(View):
    """
    串口收发数据复制编写页面处理
    """

    def get(self, request, recriminatdataorder_id):
        if request.user.username == 'check':
            return render(request, "canNotAddclickAndBack.html", {
                "django_server_yuming": DJANGO_SERVER_YUMING
            })
        elif request.user.is_active:
            recriminatdataorder = RecriminatDataOrder.objects.get(id=int(recriminatdataorder_id))  # 获取数据
            xieyitestcase_all = XieyiTestCase.objects.all().order_by("-id")   #dev配置依赖


            return render(request, "recriminatdataorder/recriminatDataOrder.html",
                          {"recriminatdataorder": recriminatdataorder,
                           "django_server_yuming": DJANGO_SERVER_YUMING,
                           "xieyitestcase_all":xieyitestcase_all,
                           })
        else:
            return render(request, "addContentError.html", {
                "django_server_yuming": DJANGO_SERVER_YUMING
            })

    def post(self, request,recriminatdataorder_id):
        username = request.user.username

        recriminatdataorder_form = RecriminatDataOrderForm(request.POST)  # 实例化RecriminatDataOrderForm()
        recriminatdataorder = RecriminatDataOrder.objects.get(id=int(recriminatdataorder_id))  # 获取内容
        xieyitestcase_all = XieyiTestCase.objects.all().order_by("-id")  # dev配置依赖



        if recriminatdataorder_form.is_valid():  # is_valid()判断是否有错

            recriminatdataorder_form.save(commit=True)  # 将信息保存到数据库中

            zj = RecriminatDataOrder.objects.all().order_by('-id')[:1][0]  # 根据添加时间查询最新的
            user = User.objects.get(username=username)
            zj.write_user_id = user.id
            zj.save()

            recriminatdataorderid = zj.id
            recriminatdataorderadd = RecriminatDataOrder.objects.get(id=int(recriminatdataorderid))  # 获取用例


            return render(request, "recriminatdataorder/recriminatDataOrder.html", {
                "recriminatdataorder": recriminatdataorderadd,
                "sumsg":u"添加数据---【{}】---成功,请继续添加".format(recriminatdataorderadd.com_send_date),
                "django_server_yuming": DJANGO_SERVER_YUMING,
                "xieyitestcase_all": xieyitestcase_all,
            })
        else:
            return render(request, 'recriminatdataorder/recriminatDataOrderForm.html', {
                "recriminatdataorder": recriminatdataorder,
                "recriminatdataorderform": recriminatdataorder_form ,
                "errmsg":u"添加失败，请重新添加，添加时请检查各个字段是否填写",
                "django_server_yuming": DJANGO_SERVER_YUMING,
                "xieyitestcase_all": xieyitestcase_all,
            })  # 返回页面，回填信息
