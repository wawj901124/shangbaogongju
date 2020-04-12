class HandleTxt(object):
    def __init__(self,file_name):
        self.file_name = file_name

    #追加写入文件
    def add_content(self,addContent):
        with open(self.file_name,"a+") as f:
            all_content = self.read_content_all()
            all_content_list = all_content.split("\n")
            if addContent not in all_content_list:  #如果不存在在文件中则写入，否则不写入
                f.write(addContent)
                f.write("\n")
                print("已经添加【%s】到【%s】文件中"%(addContent,self.file_name))
            else:
                print("【%s】在【%s】文件中已存在" % (addContent, self.file_name))

    #读取文件,并一行一行返回
    def read_content_one(self):
        with open(self.file_name,"r") as f:
             yield f.readline()

    #读取文件,并返回所有内容
    def read_content_all(self):
        with open(self.file_name,"r") as f:
             return f.read()


if __name__ == "__main__":
    import os
    file_name ="%s\\CONFIG\\ONE\\ONEWEBURL"% str(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) )  #配置驱动路径
    print("path:%s" % file_name)
    ht = HandleTxt(file_name)
    ht.add_content("series")
    ht.read_content_all()


