
class RadioAndReelectionLabel(object):
    def radioandreelectionlabel(self,activebrowser,editid):
        from testdatas.models import RadioAndReelectionLabel
        radioandreelectionlabels = RadioAndReelectionLabel.objects.filter(editandcheck_id=int(editid))
        if str(radioandreelectionlabels) != "<QuerySet []>":
            activebrowser.outPutMyLog("找到依赖数据")
            for radioandreelectionlabel in radioandreelectionlabels:
                if radioandreelectionlabel.is_check:
                    #获取属性值
                    if radioandreelectionlabel.checked_add_attribute ==  None:
                        add_attribute = "aria-checked"
                    else:
                        add_attribute = radioandreelectionlabel.checked_add_attribute
                    aria_checked = activebrowser.findEleAndReturnValueNum(0,radioandreelectionlabel.label_ele_find,
                                                 radioandreelectionlabel.label_ele_find_value,add_attribute)

                    #对比获取到的属性值与预期值结果
                    if radioandreelectionlabel.checked_add_attribute_value == None:
                        add_attribute_value = "true"
                    else:
                        add_attribute_value = radioandreelectionlabel.checked_add_attribute_value
                    if aria_checked != add_attribute_value:   #如果元素的属性"aria-checked"的值不等于"true"即元素未被选中，则点击该元素
                        activebrowser.findEleAndClick(0,radioandreelectionlabel.label_ele_find,
                                                 radioandreelectionlabel.label_ele_find_value)
                else:
                    #获取属性值
                    if radioandreelectionlabel.checked_add_attribute ==  None:
                        add_attribute = "aria-checked"
                    else:
                        add_attribute = radioandreelectionlabel.checked_add_attribute
                    aria_checked = activebrowser.findEleAndReturnValueNum(0,radioandreelectionlabel.label_ele_find,
                                                 radioandreelectionlabel.label_ele_find_value,add_attribute)

                    #对比获取到的属性值与预期值结果
                    if radioandreelectionlabel.checked_add_attribute_value == None:
                        add_attribute_value = "true"
                    else:
                        add_attribute_value = radioandreelectionlabel.checked_add_attribute_value
                    if aria_checked == add_attribute_value:   #如果元素的属性"aria-checked"的值不等于"true"即元素未被选中，则点击该元素
                        activebrowser.findEleAndClick(0,radioandreelectionlabel.label_ele_find,
                                                 radioandreelectionlabel.label_ele_find_value)


        else:
            activebrowser.outPutErrorMyLog("没有找到依赖id[%s]对应的数据！" % editid)




radioandreelectionlabel = RadioAndReelectionLabel()