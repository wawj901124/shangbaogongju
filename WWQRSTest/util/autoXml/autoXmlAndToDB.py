# ----------------------------------------------------------------------
import os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wanwenyc.settings")
django.setup()
# ----------------------------------------------------------------------
# 独运行某一个py文件时会出现如下错误：django.core.exceptions.AppRegistryNotReady: Apps aren't loaded yet.，以上内容可以解决此问题,加载django中的App

from xml.dom.minidom import parse
from xml.etree import ElementTree as ET
from xml.dom import minidom
import json

from shucaiyidate.modelsdev import TagContent, TagAttrib


#解析文件并自动入库
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


class SaveToMySql(object):
    def __init__(self,data_list,config_project,root_name):
        self.data_list = data_list
        self.config_project = config_project
        self.root_name = root_name
        self.is_exist_root = False
        self.db_root_id = self.saveRootDataAndReturnRootId()

    #先保存根目录数据
    def saveRootDataAndReturnRootId(self):
        #先查找是否有数据
        tagcontent_root = TagContent.objects.filter(config_project=self.config_project,tag_name=self.root_name)
        tagcontent_root_count = tagcontent_root.count()
        print(tagcontent_root_count)
        if tagcontent_root_count == 0:    #如果没有筛选到项目名和根目录名字,则保存根目录
            new_tagcontent = TagContent()
            new_tagcontent.config_project = self.config_project
            new_tagcontent.tag_level="1"
            new_tagcontent.tag_name=self.root_name
            new_tagcontent.is_root=True
            new_tagcontent.tag_text=""
            new_tagcontent.save()
            print("保存根目录数据成功")
            self.is_exist_root = True
        else:
            print("已经存在根目录数据")
            self.is_exist_root=False

        #筛选出根目录的ID号
        tagcontent_root = TagContent.objects.filter(config_project=self.config_project,tag_name=self.root_name)
        for tagcontent_one in tagcontent_root:
            root_id = tagcontent_one.id
            break
        print("在数据库中的ID值为：%s" % root_id )
        return root_id

    #保存获取的datalist(字典形式的列表数据)
    def saveDataListFromDictToMySql(self,depend_id,data_list):
        #遍历字典并保存
        mydata_list = data_list
        childElement_list = []
        # 为根元素添加添加子元素
        for mydate_one_dict in mydata_list:
            #获取tag_name
            tag_name = mydate_one_dict["TagName"]
            print("tag_name:")
            print(tag_name)

            # 获取tag_text
            tag_text = mydate_one_dict["TagText"]
            print("tag_text:")
            print(tag_text)
            if tag_text != None:
                tag_text = tag_text
            else:
                tag_text=''

            #获取属性
            tag_attrib_dict = mydate_one_dict["TagAttrib"]
            print("tag_attrib_dict:")
            print(tag_attrib_dict)


            #新建模型
            from shucaiyidate.modelsdev import TagContent,TagAttrib
            new_tagcontent = TagContent()
            #config_project入库
            new_tagcontent.config_project = self.config_project
            #tag_name入库
            new_tagcontent.tag_name = tag_name
            if tag_text != None:
                # tag_text入库
                new_tagcontent.tag_text = tag_text
            #依赖入库
            new_tagcontent.tag_father_id = depend_id
            #是否根节点入库
            new_tagcontent.is_root = False

            #根据节点名字保存节点级别
            if tag_name == "version" or \
                    tag_name == "deviceModel" \
                    or tag_name == "collectCmds" \
                    or tag_name == "controlCmds":
                new_tagcontent.tag_level = "2"
            elif tag_name == "cmd":
                new_tagcontent.tag_level = "3"
            elif tag_name == "pollutantFactor" or tag_name == "stateFactor":
                new_tagcontent.tag_level = "4"
            elif tag_name == "factor":
                new_tagcontent.tag_level = "5"
            elif tag_name == "section":
                new_tagcontent.tag_level = "6"
            elif tag_name == "convertRule":
                new_tagcontent.tag_level = "7"
            else:
                print("标签[%s]没有预期节点级别，需要添加，请添加，目前暂时为空处理。")
                new_tagcontent.tag_level = ""
            new_tagcontent.save()  #保存入库


            #保存后再根据保存的ID保存属性
            zj = TagContent.objects.all().order_by('-add_time')[:1][0]  # 根据添加时间查询最新的
            new_add_id = zj.id
            # 获取属性内容
            if tag_attrib_dict != {}:
                for key, value in tag_attrib_dict.items():
                    # 入库
                    new_tagattrib = TagAttrib()
                    new_tagattrib.tagcontent_id =  new_add_id
                    new_tagattrib.tag_value_name=key
                    new_tagattrib.tag_value_text=value
                    new_tagattrib.save()  #属性值入库


            #获取子集
            child_list = mydate_one_dict["TagChildren"]
            print("child_list:")
            print(child_list)
            if child_list != []:  #如果不为空，则说明需要将子集插入到当前
                print("进入到自查询中：")
                child_childElement_list = self.saveDataListFromDictToMySql(depend_id=new_add_id,data_list=child_list)
            else:
                child_childElement_list=[]
        print("入库循环完成。")


    def runSaveDateListToMySql(self):
        if self.is_exist_root:
            print("数据库中不存在工程【%s】根目录数据，开始插入数据到数据库..."% self.config_project)
            data_list = self.data_list
            depend_id = self.db_root_id
            self.saveDataListFromDictToMySql(depend_id=depend_id,data_list=data_list)
            print("插入数据完成。")
        else:
            print("数据库中存在工程【%s】根目录数据，根目录数据ID为：%s." % (self.config_project,self.db_root_id))
            print("请检查相应工程配置文件："
                  "\n\t如果需要重新插入，请删除原有数据，以免重复插入数据；"
                  "\n\t如果只是小改动，则请手动添加、删除、修改相应数据。")


#从数据库中读取数据，生成字典字符串
class GetDataDictFromMySql(object):
    def __init__(self,db_root_id):
        self.db_root_id = db_root_id
        pass

    #自循环根据id，返回list
    def GetChildListFromFatherDuiGuiToDict(self,father_id):
        father_list = []
        from shucaiyidate.modelsdev import TagContent, TagAttrib
        child_data_all = TagContent.objects.filter(tag_father_id=father_id)
        child_data_all_count = child_data_all.count()
        print(child_data_all_count)
        if child_data_all_count==0:
            father_list=father_list
        else:
            for child in child_data_all:
                child_one_dict = {}
                child_one_dict["TagID"] =child.id
                child_one_dict["TagLevel"]=child.tag_level
                child_one_dict["TagName"] = child.tag_name
                child_one_dict["TagText"] = child.tag_text

                #读取节点属性
                #读取one_level_data_one.tag_father，保存属性值为dict
                tagattrib_all = TagAttrib.objects.filter(tagcontent_id=child.id)
                tagattrib_all_count = tagattrib_all.count()
                child_attrib_dict = {}
                if tagattrib_all_count==0:
                    child_attrib_dict = child_attrib_dict
                else:
                    for tagattrib_one in tagattrib_all:
                        if tagattrib_one.tag_value_text == None:
                            tagattrib_one_tag_value_text = ""
                        else:
                            tagattrib_one_tag_value_text = tagattrib_one.tag_value_text
                        child_attrib_dict[tagattrib_one.tag_value_name]=tagattrib_one_tag_value_text
                print("child_attrib_dict:")
                print(child_attrib_dict)
                child_one_dict["TagAttrib"] = child_attrib_dict

                #查看是否有子节点

                child_child_data_all = TagContent.objects.filter(tag_father_id=child.id)
                child_child_data_all_count = child_child_data_all.count()
                if child_child_data_all_count == 0:  #如果没有找到，则说明没有子节点，子集为空
                    child_one_children_list = []
                else:
                    #否则子集就是自循环的父集
                    child_one_children_list = self.GetChildListFromFatherDuiGuiToDict(child.id)
                # 如果子节点长度为0，即没有子节点
                child_one_dict["TagChildren"] = child_one_children_list
                print("child_one_dict:")
                print(child_one_dict)
                father_list.append(child_one_dict)
        print("father_list:")
        print(father_list)
        return father_list

    #树形结构查看数据
    def treeCheck(self):
        data_list= self.GetChildListFromFatherDuiGuiToDict(self.db_root_id)

        tree_list = json.dumps(data_list, indent=1)  # 树形结构
        print("树形结构：")
        print("**********************************************************************")
        print(tree_list)
        print("**********************************************************************")
        return data_list



if __name__ == '__main__':
    #读取dev文件数据
    filename = "instr_1972_N.dev"
    ax=AutoXml(filename)
    data_list = ax.redXml()

    #把数据导入到数据库
    config_project = "instr_1972_N"
    root_name = "root"
    stms = SaveToMySql(data_list=data_list,config_project=config_project,root_name=root_name)
    stms.runSaveDateListToMySql()

    # #从数据库导出内容
    # db_root_id = "22"
    # gddl = GetDataDictFromMySql(db_root_id)
    # data_list = gddl.treeCheck()
    #
    # # 将数据写入文件
    # file_name = 'test1972.dev'
    # wx = WriteXml(data_list=data_list,file_name=file_name)
    # wx.generateXml()




