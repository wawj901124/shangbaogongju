import xml
import xml.etree.ElementTree as ET

"""
实现从xml文件中读取数据
"""
# 全局唯一标识
unique_id = 1

class ReadXml(object):
    def __init__(self):
        self.unique_id = 1


    # 遍历所有的节点
    def walkData(self,root_node, level, result_list):
        temp_list = [self.unique_id, level, root_node.tag, root_node.attrib]
        result_list.append(temp_list)
        self.unique_id += 1

        # 遍历每个子节点
        children_node = root_node.getchildren()
        if len(children_node) == 0:
            return
        for child in children_node:
            self.walkData(child, level + 1, result_list)
        return


    def getXmlData(self,file_name):
        level = 1  # 节点的深度从1开始
        result_list = []
        root = ET.parse(file_name).getroot()
        self.walkData(root, level, result_list)
        return result_list


if __name__ == '__main__':
    # 'd:\\fenlei2.xml'
    file_name = 'instr_1972_N.dev'
    R = ReadXml()
    result_list = R.getXmlData(file_name)
    for x in result_list:
        print(x)
        pass