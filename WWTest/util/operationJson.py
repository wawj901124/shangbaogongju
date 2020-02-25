import json
import os

class OperationJson:

    def __init__(self,file_path=None):#构造函数
        if file_path == None:   #如果file_path为空，则self.file_path为默认写死的路径
            self.file_path = '%s/myJsonFile/logincookies.json' % str(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        else:   #如果传递了file_path，则使用传递的file_path
            self.file_path = file_path

        self.data = self.read_data()  # 获取json文件

    #读取json文件
    def read_data(self):
        with open(self.file_path) as fp:   #使用with，用完文件后会自动关闭文件，不需要fp.close()来关闭文件
            data = json.load(fp)
            return data

    #根据关键字获取数据
    def get_data(self,id):
        print("关键字：",id)
        return self.data[id]

    #获取文件里全部数据
    def get_all_data(self):
        return self.data

    # 写json
    def write_data(self, data):
        with open(self.file_path, 'w') as fp:
            fp.write(json.dumps(data))



if __name__ == '__main__':
    opjson = OperationJson(file_path=r'/root/PycharmProjects/wanwenyc/WWTest/myJsonFile/wanwenlogincookie.json')   #实例化
    # opjson = OperationJson()  # 实例化
    # print(opjson.write_data("0"))
    print(opjson.read_data())