

class TiHuanDenpend(object):
    def __init__(self,modeltxt,modelname,table_html_file_name,table_html_form_file_name):
        self.modeltxt = modeltxt
        self.modelname = modelname.lower()  #转为小写
        self.table_html_file_name = table_html_file_name
        self.table_html_form_file_name = table_html_form_file_name
        self.tihuan_list = self.get_tihuan_list()
        self.table_html = self.get_table_html()


    #从modeltxt中获取到字段名和字段类型
    def get_tihuan_list(self):
        with open(self.modeltxt , 'r', encoding='utf-8') as f:  # 打开文件
            yuan_txt_list = f.readlines()  # 把文件内容读到列表中
        print(yuan_txt_list)
        tihuan_list = []
        for yuan_txt_one in yuan_txt_list:
            tihuan_one_list = []
            yuan_txt_one_list = yuan_txt_one.split("=")
            ziduan_name = yuan_txt_one_list[0].strip()
            ziduan_type_pre = yuan_txt_one_list[1].strip()
            ziduan_type_pre_list = ziduan_type_pre.split("(")
            print("ziduan_type_pre_list:")
            print(ziduan_type_pre_list)
            ziduan_type_pre_list_one = ziduan_type_pre_list[0].strip()
            ziduan_type_pre_list_one_list = ziduan_type_pre_list_one.split(".")
            ziduan_type_pre_list_one_list_two = ziduan_type_pre_list_one_list[1].strip()
            ziduan_type = ziduan_type_pre_list_one_list_two

            #获取字段描述
            yuan_txt_des_list = yuan_txt_one.split("verbose_name")
            print("yuan_txt_des_list:")
            print(yuan_txt_des_list)
            yuan_txt_des_list_two = yuan_txt_des_list[1]
            yuan_txt_des_list_two = yuan_txt_des_list_two.strip()  #去掉前后空格
            if '"' in yuan_txt_des_list_two:  #如果双引号在里面，则以双引号隔开：
                yuan_txt_des_list_two_list = yuan_txt_des_list_two.split('"')  #以双引号隔开
            elif "'" in yuan_txt_des_list_two: #如果单引号在其中，则以单引号隔开
                yuan_txt_des_list_two_list = yuan_txt_des_list_two.split('"')  # 以双引号隔开
            else:
                print("既没有找到单引号，也没有找到双引号，只能返回全部内容")
                yuan_txt_des_list_two_list = [0,yuan_txt_des_list_two]
            print("yuan_txt_des_list_two_list:")
            print(yuan_txt_des_list_two_list)
            ziduan_des = yuan_txt_des_list_two_list[1].strip()

            print("ziduan_name:")
            print(ziduan_name)
            print("ziduan_type:")
            print(ziduan_type)
            tihuan_one_list.append(ziduan_name)
            tihuan_one_list.append(ziduan_type)
            tihuan_one_list.append(ziduan_des)
            tihuan_list.append(tihuan_one_list)

        print("tihuan_list:")
        print(tihuan_list)
        return tihuan_list

    #根据替换内容和替换类型生产table表单
    def get_table_html(self):
        tihuan_list = self.tihuan_list
        table_html_tou = """    <table cellpadding="0" cellspacing="0">"""+"\n"
        table_html_wei = """    </table>"""+"\n"
        table_html_content = ""
        for tihuan_one in tihuan_list:
            ziduan_name = tihuan_one[0]
            ziduan_type = tihuan_one[1]
            ziduan_des = tihuan_one[2]

            if ziduan_type == 'CharField':  #对应input text
                content_one_ziduan = """        <tr>
            <td>
                <label>%s:</label>
            </td>
            <td>
                <input id="%s" name="%s" type="text" value="{{ %s.%s|default:"" }}"/>
            </td>
        </tr>"""%(str(ziduan_des),str(ziduan_name),str(ziduan_name),str(self.modelname),str(ziduan_name))
                table_html_content = table_html_content+content_one_ziduan + "\n"
            elif ziduan_type == 'ForeignKey':  #对应select 及option,%号要用%号进行转义，不然识别会出错
                content_one_ziduan = """        <tr>
            <td>
                <label>%s:</label>
            </td>
            <td>
                <select id="%s" name="%s">
                    <option value=""
                            {%% if %s.%s_id == None %%}
                                selected="selected"
                            {%% endif %%}>
                            ---请选择
                    </option>
                    {%%for cab in %s_all%%}
                        <option
                                value={{cab.id}}
                                        {%% if cab.id == %s.%s_id %%}
                                            selected="selected"
                                        {%% endif %%}>
                            [{{ cab.test_project }}]-[{{ cab.test_module }}]-[{{ cab.test_page }}]_{{cab.test_case_title }}]
                        </option>
                    {%%endfor%%}
                </select>
            </td>
        </tr>""" % (str(ziduan_des), str(ziduan_name), str(ziduan_name), str(self.modelname), str(ziduan_name),str(ziduan_name),str(self.modelname),str(ziduan_name))
                table_html_content = table_html_content + content_one_ziduan + "\n"


        table_html = table_html_tou+table_html_content+table_html_wei
        print("table_html:")
        print(table_html)
        return table_html

    #将html写入table_html.txt中
    def write_table_html_to_file(self):
        import os
        table_html = self.table_html
        new_file_name =self.table_html_file_name
        if os.path.exists(new_file_name):
            os.remove(new_file_name)
        with open(new_file_name, "w", encoding='utf-8') as f:
                f.write(table_html)

    #读取table_html.txt中的内容，替换modelname为modelnameform
    def get_table_html_form(self):
        self.write_table_html_to_file()
        # 打开需要替换的文件
        with open("table_html.txt", 'r', encoding='utf-8') as ca:  # 打开文件
            wc = ca.readlines()  # 把文件内容读到列表中

        tihuan_list = self.tihuan_list
        for tihuan_one in tihuan_list:
            ziduan_name = tihuan_one[0]
            tihuanqian_old = "%s.%s"%(self.modelname,ziduan_name)
            tihuanhou_new = "%sform.%s.value" % (self.modelname,ziduan_name)

            #遍历内容进行替换
            wc_len = len(wc)
            for i in range(0, wc_len):
                if tihuanqian_old in wc[i]:
                    wc[i] = wc[i].replace(tihuanqian_old, tihuanhou_new)
        print("替换后内容列表：")
        print(wc)
        return wc

    def write_table_html_form_to_file(self):
        table_html_form_list = self.get_table_html_form()
        import os
        new_file_name = self.table_html_form_file_name
        if os.path.exists(new_file_name):
            os.remove(new_file_name)
        with open(new_file_name, "w", encoding='utf-8') as f:
            for one in table_html_form_list:
                f.write(one)

    def run(self):
        self. write_table_html_form_to_file()










if __name__ == '__main__':
    modeltxt = "model.txt"
    modelname = "RecriminatDataOrder"
    table_html_file_name = "table_html.txt"
    table_html_form_file_name = "table_form_html.txt"

    thd = TiHuanDenpend(modeltxt=modeltxt,modelname=modelname,
                        table_html_file_name=table_html_file_name,
                        table_html_form_file_name=table_html_form_file_name)
    thd.run()