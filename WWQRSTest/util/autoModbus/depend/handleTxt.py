import os


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

    #读取文件,并一行一行返回
    def read_all_content_list(self):
        with open(self.file_name,"r") as f:
            all_content = f.readlines()
            return all_content

    #读取文件,并返回所有内容
    def read_content_all(self):
        with open(self.file_name,"r") as f:
             return f.read()

    #删除一个文件
    def delete_file(self):
        if os.path.exists(self.file_name):  # 如果文件存在
            # 删除文件，可使用以下两种方法。
            os.remove(self.file_name)  # 则删除
            print("已经删除文件：%s" % self.file_name)
            # os.unlink(my_file)
        else:
            print('目前没有文件【%s】,无需删除' % self.file_name)


if __name__ == "__main__":
    import os
    file_name ="%s\\CONFIG\\ONE\\ONEWEBURL"% str(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) )  #配置驱动路径
    print("path:%s" % file_name)
    ht = HandleTxt(file_name)
    ht.add_content("series")
    ht.read_content_all()


