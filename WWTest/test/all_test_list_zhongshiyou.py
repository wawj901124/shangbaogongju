from WWTest.autotest.test.zhongshiyou.AutoTestNewAdd import TestNewAddClass
from WWTest.autotest.test.zhongshiyou.AutoTestSearch import TestSearchClass
from WWTest.autotest.test.zhongshiyou.AutoTestEdit import TestEditClass
from WWTest.autotest.test.zhongshiyou.AutoTestDelete import TestDeleteClass
from WWTest.autotest.test.zhongshiyou.AutoTestLogin_baseAddNew import TestLoginClass
from WWTest.autotest.test.zhongshiyou.AutoTestLogin import TestLoginClass
def caselist():
    alltestnames = [
        "WWTest.autotest.test.zhongshiyou.AutoTestNewAdd.TestNewAddClass",
        "WWTest.autotest.test.zhongshiyou.AutoTestSearch.TestSearchClass",
        "WWTest.autotest.test.zhongshiyou.AutoTestEdit.TestEditClass",
        "WWTest.autotest.test.zhongshiyou.AutoTestDelete.TestDeleteClass",

        "WWTest.autotest.test.zhongshiyou.AutoTestLogin_baseAddNew.TestLoginClass",
        "WWTest.autotest.test.zhongshiyou.AutoTestLogin.TestLoginClass",




    ]
    print ('suite read case list success!! ')
    return alltestnames