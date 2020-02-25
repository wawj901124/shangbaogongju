from WWTest.autotest.test.wanwei.AutoTestNewAdd import TestNewAddClass
from WWTest.autotest.test.wanwei.AutoTestSearch import TestSearchClass
def caselist():
    alltestnames = [
        "WWTest.autotest.test.wanwei.AutoTestNewAdd.TestNewAddClass",
        "WWTest.autotest.test.wanwei.AutoTestSearch.TestSearchClass",

    ]
    print ('suite read case list success!! ')
    return alltestnames