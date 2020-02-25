
class AssertTipText(object):
    def assertiptext(self,activebrowser,newaddid):

        asserttext_list_all = []
        from testdatas.models import AssertTipText
        asserttiptexts = AssertTipText.objects.filter(newaddandcheck_id=int(newaddid))
        if str(asserttiptexts) != "<QuerySet []>":
            activebrowser.outPutMyLog("找到依赖数据")
            for asserttiptext in asserttiptexts:
                asserttext_list = []
                pretiptext = asserttiptext.tip_text
                asserttext_list.append(pretiptext)
                tiptext = activebrowser.findEleAndReturnText(0,asserttiptext.tip_ele_find,
                                                             asserttiptext.tip_ele_find_value)
                asserttext_list.append(tiptext)
                asserttext_list_all.append(asserttext_list)

        else:
            activebrowser.outPutErrorMyLog("没有找到依赖id[%s]对应的数据！" % newaddid)

        activebrowser.outPutMyLog("asserttext_list_all:%s" % asserttext_list_all)
        return asserttext_list_all




asserttiptext = AssertTipText()