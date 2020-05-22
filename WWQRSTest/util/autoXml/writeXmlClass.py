
from xml.dom import minidom
from WWQRSTest.util.autoXml.autoXml import AutoXml
filename = "instr_1972_N.dev"
ax = AutoXml(filename)
mydata_list = ax.redXml()
print("+++++++++++++++++++++++++已经获取数据++++++++++++++++++++++++++++++++++++")

class WriteXml(object):
    def __init__(self):
        self.doc = self.createDoc()
        self.root_element = self.createRootElement()
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
        data_list = mydata_list

        # childElement_list = self.writeXmlFromListContainDict(data_list)
        childElement_list = self.writeXmlFromListContainList(data_list)

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
        f = open('test.dev', 'w', encoding='utf-8')
        # 写入文件
        self.doc.writexml(f, addindent=' ', newl='\n')
        # 关闭
        f.close()

if __name__ == '__main__':
    wx = WriteXml()
    wx.generateXml()

