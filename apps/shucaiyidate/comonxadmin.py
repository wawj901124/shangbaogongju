#自定义的一些xadmin的通用函数

class CommonXadmin(object):

    #根据model获取经过过滤列表过滤后所得到的字段列表
    def sql_model_filter_field_name_list_and_return(self,sql_model_name,filter_name_list=None):
        """sql_model_name 为数据库模块
           filter_name_list 为需要过滤的字段列表，即不需要保存的字段，一般固定为['id','add_time', 'update_time']"""
        fields_data = sql_model_name._meta.fields
        l_model_name_list = list(key.name for key in fields_data)
        print("model所有字段列表：")
        print(l_model_name_list)
        l_model_name_list.remove('id')  #删除id一项
        l_model_name_list.remove('write_user')  # 删除write_user一项
        l_model_name_list.remove('add_time')  # 删除add_time一项
        l_model_name_list.remove('update_time')  # 删除update_time一项
        print("model所有字段列表（去掉id、write_user、add_time、update_time字段）：")
        print(l_model_name_list)

        if filter_name_list==None:
            filter_name_list = ['id','write_user','add_time', 'update_time']
        else:
            filter_name_list = filter_name_list

        l_model_name_filter_list = []  # model字段列表过滤掉不用的字段后的字段
        for l_model_name_one in l_model_name_list:
            if l_model_name_one not in filter_name_list:  #如果不存在在过滤列表里，则保存到新名字列表
                l_model_name_filter_list.append(l_model_name_one)
        print("经过过滤后的字段列表：")
        print(l_model_name_filter_list)
        return l_model_name_filter_list

    #复制新加某个模块的内容,复制一个对象数据
    def sql_model_copy_one(self,sql_model_name,old_object,filter_name_list=None):
        """sql_model_name 为数据库模块
           old_object为旧的数据的实例化对象
           filter_name_list 为需要过滤的字段列表，即不需要保存的字段，一般固定为['id','add_time', 'update_time']"""
        l_model_name_filter_list = self.sql_model_filter_field_name_list_and_return(sql_model_name=sql_model_name,
                                                                                    filter_name_list=filter_name_list)
        #旧模块内容保存到新模块内容
        new_object = sql_model_name()
        for l_model_name_filter_one in l_model_name_filter_list:
            bianliang = "new_object.%s = old_object.%s" % (l_model_name_filter_one,l_model_name_filter_one)
            exec(bianliang) #就值赋值给新模块 ,exec将字符串作为脚本运行
            print(bianliang)

        new_object.save()  #保存数据

    #复制新加某个模块的内容,复制一个对象数据,一个内嵌数据，
    def sql_model_copy_one_neiqian(self,sql_model_name,old_object,neiqianwaijian_name,neiqian_new_id,filter_name_list=None):
        """sql_model_name 为数据库模块
           old_object为旧的数据的实例化对象
           filter_name_list 为需要过滤的字段列表，即不需要保存的字段，一般固定为['id','add_time', 'update_time']"""
        l_model_name_filter_list = self.sql_model_filter_field_name_list_and_return(sql_model_name=sql_model_name,
                                                                                    filter_name_list=filter_name_list)
        #旧模块内容保存到新模块内容
        new_object = sql_model_name()
        for l_model_name_filter_one in l_model_name_filter_list:
            if l_model_name_filter_one == neiqianwaijian_name:
                new_neiqian_ziduan_id = neiqianwaijian_name+"_id"
                bianliang = "new_object.%s = %d" % (new_neiqian_ziduan_id, int(neiqian_new_id))
                exec(bianliang)  # 就值赋值给新模块 ,exec将字符串作为脚本运行
                print(bianliang)
                # new_object[new_neiqian_ziduan_id] = int(neiqian_new_id)   #保存内嵌模块外键为最新生成的数据
            else:
                bianliang = "new_object.%s = old_object.%s" % (l_model_name_filter_one, l_model_name_filter_one)
                exec(bianliang)  # 就值赋值给新模块 ,exec将字符串作为脚本运行
                print(bianliang)
                # new_object[l_model_name_filter_one] = old_object[l_model_name_filter_one]  #就值赋值给新模块
        new_object.save()  #保存数据


    #复制某个模块内容，并返回新的模块的id
    def sql_model_copy_old_and_return_new_id_common(self,sql_model_name,old_object,filter_name_list=None):
        """sql_model_name 为数据库模块
           old_object为旧的数据的实例化对象
           filter_name_list 为需要过滤的字段列表，即不需要保存的字段，一般固定为['id','add_time', 'update_time']"""
        #调用复制一条数据的函数
        self.sql_model_copy_one(sql_model_name=sql_model_name,old_object=old_object,filter_name_list=filter_name_list)
        newadd = sql_model_name.objects.all().order_by('-id')[:1][0]  # 根据id查询最新的 一条数据
        print("最新一条数据的ID：")
        print(newadd.id)
        return newadd.id

    #复制某个内嵌模块通用函数
    def sql_model_copy_common(self,sql_model_name,neiqianwaijian_name,neiqian_id,neiqian_new_id,filter_name_list=None):
        #sql_model_name 为内嵌数据库模块
        #neiqianwaijian_name 内嵌外键字段的名字
        #neiqian_id，内嵌外键依赖的id
        #filter_name_list 内嵌model需要过滤的字段列表，即不需要保存的字段
        guolu = {}
        g_key = neiqianwaijian_name+"_id"
        guolu[g_key]=neiqian_id
        print("guolu:")
        print(guolu)
        old_all = sql_model_name.objects.filter(**guolu).order_by('id')  #过滤且按照id正序排列
        for old_one in old_all:
            #调用复制一条数据的函数
            self.sql_model_copy_one_neiqian(sql_model_name=sql_model_name,
                                            old_object=old_one,
                                            neiqianwaijian_name=neiqianwaijian_name,
                                            neiqian_new_id=neiqian_new_id,
                                            filter_name_list=filter_name_list)



    #删除某个内嵌模块通用函数
    def sql_model_delete_common(self,sql_model_name,neiqianwaijian_name,neiqian_id):
        #sql_model_name 为内嵌数据库模块
        #neiqianwaijian_name 内嵌外键字段的名字
        #neiqian_id，内嵌外键依赖的id
        guolu = {}
        g_key = neiqianwaijian_name+"_id"
        guolu[g_key]=neiqian_id
        print("guolu:")
        print(guolu)
        old_all = sql_model_name.objects.filter(**guolu).order_by('id')  #过滤且按照id正序排列
        for old_one in old_all:
            old_one.delete()   #删除
            print("删除一条数据")



