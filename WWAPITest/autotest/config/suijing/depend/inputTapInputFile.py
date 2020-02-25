
class InputTapInputFile(object):
    def inputtapinputfile(self,activebrowser,newaddid):

        from testdatas.models import InputTapInputFile
        inputtapinputfiles = InputTapInputFile.objects.filter(newaddandcheck_id=int(newaddid))
        if str(inputtapinputfiles) != "<QuerySet []>":
            activebrowser.outPutMyLog("找到依赖数据")
            for inputtapinputfile in inputtapinputfiles:
                activebrowser.findEleAndUploadFile(0,inputtapinputfile.input_ele_find,
                                                   inputtapinputfile.input_ele_find_value,
                                                   inputtapinputfile.input_file,
                                                   inputtapinputfile.input_class_name)
        else:
            activebrowser.outPutErrorMyLog("没有找到依赖id[%s]对应的数据！" % newaddid)



inputtapinputfile = InputTapInputFile()