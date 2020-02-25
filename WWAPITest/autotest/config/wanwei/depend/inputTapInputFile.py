
class InputTapInputFile(object):
    def inputtapinputfile(self,activebrowser,newaddid):

        from testdatas.models import InputTapInputFile
        inputtapinputfiles = InputTapInputFile.objects.filter(newaddandcheck_id=int(newaddid))
        if str(inputtapinputfiles) != "<QuerySet []>":
            activebrowser.outPutMyLog("找到依赖数据")
            for inputtapinputfile in inputtapinputfiles:
                input_file_list = inputtapinputfile.input_file.split(",")  #将文件名字以半角逗号分隔
                input_file_list_long = len(input_file_list)
                for i in range(0,input_file_list_long):
                    try:
                        #如果上传文件成功，就终止循环
                        activebrowser.findEleAndUploadFile(0,inputtapinputfile.input_ele_find,
                                                           inputtapinputfile.input_ele_find_value,
                                                           input_file_list[i],
                                                           inputtapinputfile.input_class_name)
                        break
                    except:
                        #否则，继续试用下一个文件名
                        continue
        else:
            activebrowser.outPutErrorMyLog("没有找到依赖id[%s]对应的数据！" % newaddid)



inputtapinputfile = InputTapInputFile()