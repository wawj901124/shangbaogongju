class SelectTapSelectText(object):
    def selecttapselecttext(self,activebrowser,newaddid):
        from testdatas.models import SelectTapSelectText

        selecttapselecttexts =  SelectTapSelectText.objects.filter(newaddandcheck_id=int(newaddid))
        if str(selecttapselecttexts) != "<QuerySet []>":
            activebrowser.outPutMyLog("找到依赖数据")
            for selecttapselecttext in selecttapselecttexts:
                activebrowser.findEleAndReturnOptions(0,selecttapselecttext.select_ele_find,
                                                      selecttapselecttext.select_ele_find_value,
                                                      selecttapselecttext.select_option_text)

        else:
            activebrowser.outPutErrorMyLog("没有找到依赖id[%s]对应的数据！" % newaddid)


selecttapselecttext = SelectTapSelectText()