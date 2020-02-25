
class InputTapInputDateTime(object):
    def inputtapinputdatetime(self,activebrowser,editid):

        from testdatas.models import InputTapInputDateTime
        inputtapinputdatetimes = InputTapInputDateTime.objects.filter(editandcheck_id=int(editid))
        if str(inputtapinputdatetimes) != "<QuerySet []>":
            activebrowser.outPutMyLog("找到依赖数据")
            for inputtapinputdatetime in inputtapinputdatetimes:
                #点击时间输入框
                activebrowser.findEleAndClick(0,inputtapinputdatetime.input_ele_find,
                                                 inputtapinputdatetime.input_ele_find_value)
                activebrowser.delayTime(3)

                #如果有点击上个月按钮的次数，就按照次数循环点击
                if inputtapinputdatetime.click_last_month_counts !=None:
                    for i in range(0,int(inputtapinputdatetime.click_last_month_counts)):
                        activebrowser.findEleAndClick(0, inputtapinputdatetime.last_month_ele_find,
                                                      inputtapinputdatetime.last_month_ele_find_value)
                else:
                    if inputtapinputdatetime.last_month_ele_find !=None and inputtapinputdatetime.last_month_ele_find_value!=None:
                        activebrowser.findEleAndClick(0, inputtapinputdatetime.last_month_ele_find,
                                                      inputtapinputdatetime.last_month_ele_find_value)


                #如果有点击下个月按钮的次数，就按照次数循环点击
                if inputtapinputdatetime.click_next_month_counts !=None:
                    for i in range(0,int(inputtapinputdatetime.click_next_month_counts)):
                        activebrowser.findEleAndClick(0, inputtapinputdatetime.next_month_ele_find,
                                                      inputtapinputdatetime.next_month_ele_find_value)
                else:
                    if inputtapinputdatetime.next_month_ele_find !=None and inputtapinputdatetime.next_month_ele_find_value!=None:
                        activebrowser.findEleAndClick(0, inputtapinputdatetime.next_month_ele_find,
                                                      inputtapinputdatetime.next_month_ele_find_value)


                #如果有点击上年按钮的次数，就按照次数循环点击
                if inputtapinputdatetime.click_last_year_counts !=None:
                    for i in range(0,int(inputtapinputdatetime.click_last_year_counts)):
                        activebrowser.findEleAndClick(0, inputtapinputdatetime.last_year_ele_find,
                                                      inputtapinputdatetime.last_year_ele_find_value)
                else:
                    if inputtapinputdatetime.last_year_ele_find !=None and inputtapinputdatetime.last_year_ele_find_value!=None:
                        activebrowser.findEleAndClick(0, inputtapinputdatetime.last_year_ele_find,
                                                      inputtapinputdatetime.last_year_ele_find_value)


                #如果有点击下年按钮的次数，就按照次数循环点击
                if inputtapinputdatetime.click_next_year_counts !=None:
                    for i in range(0,int(inputtapinputdatetime.click_next_year_counts)):
                        activebrowser.findEleAndClick(0, inputtapinputdatetime.next_year_ele_find,
                                                      inputtapinputdatetime.next_year_ele_find_value)
                else:
                    if inputtapinputdatetime.next_year_ele_find !=None and inputtapinputdatetime.next_year_ele_find_value!=None:
                        activebrowser.findEleAndClick(0, inputtapinputdatetime.next_year_ele_find,
                                                      inputtapinputdatetime.next_year_ele_find_value)


                #点击日期元素
                activebrowser.findEleAndClick(0,inputtapinputdatetime.date_ele_find,
                                                 inputtapinputdatetime.date_ele_find_value)


        else:
            activebrowser.outPutErrorMyLog("没有找到依赖id[%s]对应的数据！" % editid)




inputtapinputdatetime = InputTapInputDateTime()