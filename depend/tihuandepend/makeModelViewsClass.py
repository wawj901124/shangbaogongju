
class MakeModelViews(object):
    def __init__(self,modelname,is_with_relevance=False):
        self.modelname = modelname
        self.modelname_lower = modelname.lower()  #转为小写
        self.is_with_relevance = is_with_relevance

    def makeView(self):
        model_view_one = """class %sView(View):
    def get(self, request, %s_id):
        if request.user.username == 'check':
            return render(request, "canNotAddclickAndBack.html", {
                "django_server_yuming": DJANGO_SERVER_YUMING
            })
        elif request.user.is_active:
            %s = %s.objects.get(id=int(%s_id))  # 获取数据"""% (self.modelname,self.modelname_lower,
                                  self.modelname_lower,self.modelname,self.modelname_lower)

        model_view_two = """
            xieyitestcase_all = XieyiTestCase.objects.all().order_by("-id")   #dev配置依赖"""

        model_view_relevance_one = """"""
        if self.is_with_relevance:
            model_view_relevance_one = model_view_relevance_one+"""
            is_with_relevance = 1
            
            """


        model_view_three = """
            return render(request, "%s/%s.html",
                          {"%s":%s,
                           "django_server_yuming": DJANGO_SERVER_YUMING,""" % (self.modelname_lower,
                                  self.modelname_lower,self.modelname_lower,self.modelname_lower)
        model_view_four = """
                           "xieyitestcase_all":xieyitestcase_all,"""

        model_view_relevance_two = """"""
        if self.is_with_relevance:
            model_view_relevance_two = model_view_relevance_two +"""
                           "is_withRelevance": is_with_relevance,"""

        model_view_five = """
                           })
        else:
            return render(request, "addContentError.html", {
                "django_server_yuming": DJANGO_SERVER_YUMING
            })"""
        model_view_six ="""
        
    def post(self, request,%s_id):
        username = request.user.username

        %s_form = %sForm(request.POST)  # 实例化%sForm()
        %s = %s.objects.get(id=int(%s_id))  # 获取内容"""%(self.modelname_lower,self.modelname_lower,self.modelname,self.modelname,
                                                       self.modelname_lower,self.modelname,self.modelname_lower,)

        model_view_seven = """
        xieyitestcase_all = XieyiTestCase.objects.all().order_by("-id")  # 依赖"""

        model_view_relevance_three = """"""
        if self.is_with_relevance:
            model_view_relevance_three = model_view_relevance_three+"""
        # 处理附带复制内容
        is_with_relevance = request.POST.get('is_withRelevance', '')
        print("is_withRelevance:%s" % is_with_relevance)
        print("is_withRelevance类型:%s" % type(is_with_relevance))
        is_with_relevance =int(is_with_relevance)
        print("is_withRelevance:%s" % is_with_relevance)
        print("is_withRelevance类型:%s" % type(is_with_relevance))
        # 结束处理
        
        """

        model_view_eight = """

        if %s_form.is_valid():  # is_valid()判断是否有错

            %s_form.save(commit=True)  # 将信息保存到数据库中

            zj = %s.objects.all().order_by('-id')[:1][0]  # 根据添加时间查询最新的
            user = User.objects.get(username=username)
            zj.write_user_id = user.id
            zj.save()

            %saddid = zj.id
            %sadd = %s.objects.get(id=int(%saddid))  # 获取用例"""% (self.modelname_lower,self.modelname_lower,self.modelname,
                                                                    self.modelname_lower, self.modelname_lower,self.modelname,self.modelname_lower)
        model_view_relevance_four = """"""
        if self.is_with_relevance:
            model_view_relevance_four = model_view_relevance_four+ """            
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
                                         filter_name_list=filter_name_list)"""

        model_view_eight_two = """

            return render(request, "%s/%s.html", {
                "%s": %sadd,
                "sumsg":u"添加数据---【{}】---成功,请继续添加".format(%sadd.id),
                "django_server_yuming": DJANGO_SERVER_YUMING,""" % (self.modelname_lower, self.modelname_lower,
                                            self.modelname_lower, self.modelname_lower,
                                            self.modelname_lower)

        model_view_nine = """
                "nodeconfig_all": nodeconfig_all,"""

        model_view_relevance_five = """"""
        if self.is_with_relevance:
            model_view_relevance_five = model_view_relevance_five+"""
                "is_withRelevance": is_with_relevance,"""

        model_view_ten = """
            })
        else:
            return render(request, '%s/%sform.html', {
                "%s": %s,
                "%sform": %s_form ,
                "errmsg":u"添加失败，请重新添加，添加时请检查各个字段是否填写",
                "django_server_yuming": DJANGO_SERVER_YUMING, """ % ( self.modelname_lower, self.modelname_lower,
                                                                    self.modelname_lower, self.modelname_lower,
                                                                    self.modelname_lower,self.modelname_lower)

        model_view_ele ="""
                "nodeconfig_all": nodeconfig_all,"""

        model_view_relevance_six = """"""
        if self.is_with_relevance:
            model_view_relevance_six = model_view_relevance_six+"""
                "is_withRelevance": is_with_relevance,"""

        model_view_twe = """
            })  # 返回页面，回填信息"""



        model_view =  model_view_one+model_view_two+model_view_relevance_one+model_view_three\
                      +model_view_four+model_view_relevance_two+model_view_five+model_view_six\
                      +model_view_seven+model_view_relevance_three+model_view_eight+\
                      model_view_relevance_four+model_view_eight_two+model_view_nine+model_view_relevance_five\
                      +model_view_ten\
                      +model_view_ele+model_view_relevance_six+model_view_twe
        print("model_view:")
        print( model_view)
        return  model_view

    def write_view_to_file_name(self):
        import os
        modelview = self.makeView()
        new_file_name ="model_view.txt"
        if os.path.exists(new_file_name):
            os.remove(new_file_name)
        with open(new_file_name, "w", encoding='utf-8') as f:
                f.write(modelview)

    def run(self):
        self.write_view_to_file_name()

if __name__ == '__main__':
    modelname = "RecriminatDataOrder"
    is_with_relevance = False
    mmv = MakeModelViews(modelname=modelname,is_with_relevance=is_with_relevance)
    mmv.run()


