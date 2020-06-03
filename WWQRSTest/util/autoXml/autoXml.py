from xml.dom.minidom import parse
from xml.etree import ElementTree as ET
from xml.dom import minidom
import json

class AutoXml(object):
    def __init__(self,filename):
        self.file_name = filename
        self.paser_root_node = self.paserGetRootNode()
        self.et_xml_tree = self.etGetXmlTree()
        self.et_xml_root = self.etGetXmlRoot()

    def paserGetRootNode(self):
        #获取根节点
        domTree = parse(self.file_name)
        rootNode = domTree.documentElement
        print("节点名称：")
        print(rootNode.nodeName)
        print("节点属性值：")
        print(rootNode.nodeValue)
        print("节点类型：")
        print(rootNode.nodeType)
        print("内容：")
        print(rootNode.firstChild.data)
        return rootNode

    #通过标签名获取
    def paserGetTagList(self,tagName):
        rootNode=self.paser_root_node
        tag_list = rootNode.getElementsByTagName(tagName)
        return tag_list

    #根据元素列表获取元素节点名和文本信息
    def paserGetTextFromTaglist(self,tag_list):
        # tag_list = self.paserGetTagList(tagName)
        tag_data_list = []
        for tag_one in tag_list:
            tag_one_dict = {}
            tag_one_node_name = tag_one.nodeName
            print(tag_one_node_name)
            tag_one_node_value = tag_one.nodeValue
            print(tag_one_node_value)
            tag_one_node_type = tag_one.nodeType
            print(tag_one_node_type)
            tag_one_first_child_data = tag_one.firstChild.data
            print(tag_one_first_child_data)
            tag_one_dict[tag_one_node_name]=tag_one_first_child_data
            tag_data_list.append(tag_one_dict)
        print(tag_data_list)
        return tag_data_list

    #根据元素列表获取元素节点名和文本信息
    def paserGetAttbibuteFromTaglist(self,tagName,attributenamelist):
        tag_list = self.paserGetTagList(tagName)
        tag_data_list = []
        for tag_one in tag_list:
            tag_one_dict = {}
            tag_one_node_name = tag_one.nodeName
            print(tag_one_node_name)
            tag_one_node_value = tag_one.nodeValue
            print(tag_one_node_value)
            tag_one_node_type = tag_one.nodeType
            print(tag_one_node_type)
            tag_one_first_child_data = tag_one.firstChild.data
            print(tag_one_first_child_data)
            tag_one_dict[tag_one_node_name]=tag_one_first_child_data

            attribute_name_list = attributenamelist
            attribute_dict = {}
            for attribute_name in attribute_name_list:
                attribute_name_value = tag_one.getAttribute(attribute_name)
                attribute_dict[attribute_name] = attribute_name_value

            print(attribute_dict)

            tag_data_list.append(tag_one_dict)
        print(tag_data_list)
        return tag_data_list



    def etGetXmlTree(self):
        xml_tree = ET.parse(self.file_name)
        print(xml_tree)
        return xml_tree

    def etGetXmlRoot(self):
        xml_tree = self.et_xml_tree
        xml_root = xml_tree.getroot()
        print("xml_root.tag:")
        print(xml_root.tag)
        print("xml_root.attrib:")
        print(xml_root.attrib)
        return xml_root

    def etGetChildFromFatherDiGui(self, fatherele):
        fatherele = fatherele
        father_list = []
        for child in fatherele:
            child_one_list = []
            child_tag = child.tag
            print("子集Tag:")
            print(child_tag)
            child_text = child.text
            print("子集的text:")
            print(child_text)
            child_attrib_dict=child.attrib
            print("子集的attrib:")
            print(child_attrib_dict)
            child_one_list.append(child_tag)
            child_one_list.append(child_text)
            child_one_list.append(child_attrib_dict)
            children_node = child.getchildren()   #获取子节点
            children_node_len = len(children_node)
            if children_node_len == 0:
                child_one_children_list = []
            else:
                child_one_children_list = self.etGetChildFromFatherDiGui(child)
            #如果子节点长度为0，即没有子节点
            child_one_list.append(child_one_children_list)
            father_list.append(child_one_list)

        print(father_list)
        return father_list


    def etGetChildFromFatherDiGuiToDict(self, fatherele):
        fatherele = fatherele
        father_list = []
        for child in fatherele:
            child_one_dict = {}
            child_tag = child.tag
            print("子集Tag:")
            print(child_tag)
            child_text = child.text
            print("子集的text:")
            print(child_text)
            child_attrib_dict=child.attrib
            print("子集的attrib:")
            print(child_attrib_dict)
            child_one_dict["TagName"] = child_tag
            child_one_dict["TagText"] = child_text
            child_one_dict["TagAttrib"] = child_attrib_dict
            children_node = child.getchildren()   #获取子节点
            children_node_len = len(children_node)
            if children_node_len == 0:
                child_one_children_list = []
            else:
                child_one_children_list = self.etGetChildFromFatherDiGuiToDict(child)
            #如果子节点长度为0，即没有子节点
            child_one_dict["TagChildren"] = child_one_children_list
            father_list.append(child_one_dict)

        print(father_list)
        return father_list


    def etJixiDiGuiFatherList(self,father_list):
        print(type(father_list))
        print("树形结构：")
        tree_list = json.dumps(father_list,indent=1)  #树形结构
        print(tree_list)
        print(type(tree_list))
        return father_list

    def redXml(self):
        fatherele = self.et_xml_root
        father_list = self.etGetChildFromFatherDiGuiToDict(fatherele)
        # father_list = self.etGetChildFromFatherDiGui(fatherele)
        father_list = self.etJixiDiGuiFatherList(father_list)
        return father_list


class WriteXml(object):
    def __init__(self, data_list,file_name):
        self.doc = self.createDoc()
        self.root_element = self.createRootElement()
        self.data_list = data_list
        self.write_file_name = file_name
        pass

    def createDoc(self):
        impl = minidom.getDOMImplementation()
        # 创建一个xml dom
        # 三个参数分别对应为 ：namespaceURI, qualifiedName, doctype
        doc = impl.createDocument(None, None, None)
        return doc

    def createRootElement(self):
        rootElement = self.doc.createElement('root')
        return rootElement

    #写入内容
    def writeXmlFromListContainDict(self,data_list):
        mydata_list = data_list
        childElement_list = []
        # 为根元素添加添加子元素
        for mydate_one_dict in mydata_list:
            tag_name = mydate_one_dict["TagName"]
            print("tag_name:")
            print(tag_name)
            # 创建子元素
            childElement = self.doc.createElement(tag_name)

            # 创建子元素的节点文本内容
            tag_text = mydate_one_dict["TagText"]
            print("tag_text:")
            print(tag_text)
            if tag_text != None:
                childElementText = self.doc.createTextNode(tag_text)
                childElement.appendChild(childElementText)

            tag_attrib_dict = mydate_one_dict["TagAttrib"]
            print("tag_attrib_dict:")
            print(tag_attrib_dict)
            if tag_attrib_dict != {}:
                for key, value in tag_attrib_dict.items():
                    # 为子元素添加id属性
                    childElement.setAttribute(key, value)

            child_list = mydate_one_dict["TagChildren"]
            print("child_list:")
            print(child_list)
            if child_list != []:  #如果不为空，则说明需要将子集插入到当前
                print("进入到自查询中：")
                child_childElement_list = self.writeXmlFromListContainDict(child_list)
            else:
                child_childElement_list=[]

            print("自查询子集集合")
            print(childElement_list)

            #把子集元素插入到当前元素中
            for child_childElement_one in child_childElement_list:
                childElement.appendChild(child_childElement_one)

            childElement_list.append(childElement)
        print(childElement_list)
        return childElement_list

    #写入内容
    def writeXmlFromListContainList(self,data_list):
        mydata_list = data_list
        childElement_list = []
        # 为根元素添加添加子元素
        for mydate_one_list in mydata_list:
            tag_name = mydate_one_list[0]
            print("tag_name:")
            print(tag_name)
            # 创建子元素
            childElement = self.doc.createElement(tag_name)

            # 创建子元素的节点文本内容
            tag_text = mydate_one_list[1]
            print("tag_text:")
            print(tag_text)
            if tag_text != None:
                childElementText = self.doc.createTextNode(tag_text)
                childElement.appendChild(childElementText)

            tag_attrib_dict = mydate_one_list[2]
            print("tag_attrib_dict:")
            print(tag_attrib_dict)
            if tag_attrib_dict != {}:
                for key, value in tag_attrib_dict.items():
                    # 为子元素添加id属性
                    childElement.setAttribute(key, value)

            child_list = mydate_one_list[3]
            print("child_list:")
            print(child_list)
            if child_list != []:  #如果不为空，则说明需要将子集插入到当前
                print("进入到自查询中：")
                child_childElement_list = self.writeXmlFromListContainList(child_list)
            else:
                child_childElement_list=[]

            print("自查询子集集合")
            print(childElement_list)

            #把子集元素插入到当前元素中
            for child_childElement_one in child_childElement_list:
                childElement.appendChild(child_childElement_one)

            childElement_list.append(childElement)
        print(childElement_list)
        return childElement_list


    # 生成XML文件方式
    def generateXml(self):
        # 创建根元素
        rootElement = self.root_element
        doc = self.doc
        rootElement = rootElement
        data_list = self.data_list

        childElement_list = self.writeXmlFromListContainDict(data_list)
        # childElement_list = self.writeXmlFromListContainList(data_list)

        for childElement in childElement_list:
            # 将子元素追加到根元素中
            rootElement.appendChild(childElement)
            # print(childElement.firstChild.data)
            # 将拼接好的根元素追加到dom对象
            doc.appendChild(rootElement)
        print("*******************************")
        print(doc)
        print("*******************************")

        # 打开test.xml文件 准备写入
        f = open(self.write_file_name, 'w', encoding='utf-8')
        # 写入文件
        self.doc.writexml(f, addindent=' ', newl='\n')
        # 关闭
        f.close()


if __name__ == '__main__':
    filename = "D:\pycharmproject\shangbaogongju\media/Dev/2_哈希分析仪/哈希分析仪.dev"
    # filename = "instr_1972_N.dev"
    # filename = "test.dev"
    ax=AutoXml(filename)
    data_list = ax.redXml()
    # file_name = 'new_project.dev'
    # wx = WriteXml(data_list=data_list,file_name=file_name)
    # wx.generateXml()

    # fatherele = ax.et_xml_root
    # count = 1
    # father_list = ax.etGetChildFromFatherDiGui(fatherele)
    # print("文件内容：")
    # # print(father_list)
    # ax.etJixiDiGuiFatherList(father_list)
    # father_list_len = len(father_list)
    # for i in range(0,father_list_len):
    #     print("\t" + str(father_list[i]))
    #     ziji = father_list[i][3]
    #     if ziji != []:
    #         print("\t\t" + str(ziji))



    # ax.paserGetOneTagList("version")
    # ax.paserGetOneTagList("deviceModel")
    # ax.paserGetOneTagList("collectCmds")
    # tagName = "cmd"
    # attributenamelist = ['id','format','cmd','ackType','ackHead','ackTail','ackLen','ackGap','ackCheckMode','ackCheckArg']
    # ax.paserGetAttbibuteFromTaglist(tagName,attributenamelist)
    # # ax.etGetNodeContentByPath('./collectCmds/cmd/stateFactor')

