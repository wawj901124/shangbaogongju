import unittest
# ----------------------------------------------------------------------
import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wanwenyc.settings")
django.setup()
# ----------------------------------------------------------------------
#独运行某一个py文件时会出现如下错误：django.core.exceptions.AppRegistryNotReady: Apps aren't loaded yet.，以上内容可以解决此问题,加载django中的App


from WWDBTest.util.getTimeStr import GetTimeStr
from WWDBTest.util.operationMyDB import OperationMyDB


class TestDeleteDBClass(unittest.TestCase):  # 创建测试类

    @classmethod  # 类方法，只执行一次，但必须要加注解@classmethod,且名字固定为setUpClass
    def setUpClass(cls):
        pass

    @classmethod  # 类方法，只执行一次，但必须要加注解@classmethod,且名字固定为tearDownClass
    def tearDownClass(cls):
        pass




    def setUp(self):  # 每条用例执行测试之前都要执行此方法
        pass

    def tearDown(self):  # 每条用例执行测试之后都要执行此方法
        pass



    #定义点击返回函数
    def definedeletedbdata(self,db_host,db_port,db_user,db_password,db_database,db_charset,
                  db_biao, db_ziduan, db_xiugaiqiandezhi, db_xiugaihoudezhi,
                  db_tiaojianziduan, db_tiaojianzhi):

        opdb = OperationMyDB(db_host=db_host,db_port = db_port, db_user = db_user, db_password =db_password, db_database = db_database, db_charset = db_charset,
        db_biao = db_biao, db_ziduan = db_ziduan, db_xiugaiqiandezhi = db_xiugaiqiandezhi, db_xiugaihoudezhi = db_xiugaihoudezhi,
        db_tiaojianziduan =db_tiaojianziduan, db_tiaojianzhi = db_tiaojianzhi)
        opdb.connectMyDBAndDelete()
        opdb.closeCursorAndConnect()


    # def test001(self):
    #     print("第一条测试用例")
    #     self.definedepend(self.dependid)

    @staticmethod    #根据不同的参数生成测试用例
    def getTestFunc(db_host,db_port,db_user,db_password,db_database,db_charset,
                  db_biao, db_ziduan, db_xiugaiqiandezhi, db_xiugaihoudezhi,
                  db_tiaojianziduan, db_tiaojianzhi):

        def func(self):
            self.definedeletedbdata(db_host,db_port,db_user,db_password,db_database,db_charset,
                  db_biao, db_ziduan, db_xiugaiqiandezhi, db_xiugaihoudezhi,
                  db_tiaojianziduan, db_tiaojianzhi)
        return func

def __generateTestCases():
    from testupdatadb.models import UpdateDbData

    updatedbdatatestcase_all = UpdateDbData.objects.filter(id=7).order_by('id')

    for updatedbdatatestcase in updatedbdatatestcase_all:
        forcount = updatedbdatatestcase.case_counts
        starttime = GetTimeStr().getTimeStr()
        if len(str(updatedbdatatestcase.id)) == 1:
            updatedbdatatestcaseid = '0000%s' % updatedbdatatestcase.id
        elif len(str(updatedbdatatestcase.id)) == 2:
            updatedbdatatestcaseid = '000%s' % updatedbdatatestcase.id
        elif len(str(updatedbdatatestcase.id)) == 3:
            updatedbdatatestcaseid = '00%s' % updatedbdatatestcase.id
        elif len(str(updatedbdatatestcase.id)) == 4:
            updatedbdatatestcaseid = '0%s' % updatedbdatatestcase.id
        elif len(str(updatedbdatatestcase.id)) == 5:
            updatedbdatatestcaseid = '%s' % updatedbdatatestcase.id
        else:
            updatedbdatatestcaseid = 'Id已经超过5位数，请重新定义'

        for i in range(1, forcount + 1):  # 循环，从1开始
            if len(str(i)) == 1:
                forcount_i = '0000%s' % i
            elif len(str(i)) == 2:
                forcount_i = '000%s' % i
            elif len(str(i)) == 3:
                forcount_i = '00%s' % i
            elif len(str(i)) == 4:
                forcount_i = '0%s' % i
            elif len(str(i)) == 5:
                forcount_i = '%s' % i
            else:
                forcount_i = 'Id已经超过5位数，请重新定义'

            #对表进行分离从操作
            db_biao_content = updatedbdatatestcase.db_biao
            db_biao_list = db_biao_content.split(',')
            print(db_biao_list)
            db_biao_list_len = len(db_biao_list)
            print("db_biao_list_len:%s"% db_biao_list_len)
            for j in range(1,db_biao_list_len+1):
                print("表:%s" % db_biao_list[j-1])
                if len(str(j)) == 1:
                    db_biao_j = '0000%s' % j
                elif len(str(j)) == 2:
                    db_biao_j = '000%s' % j
                elif len(str(j)) == 3:
                    db_biao_j = '00%s' % j
                elif len(str(j)) == 4:
                    db_biao_j = '0%s' % j
                elif len(str(j)) == 5:
                    db_biao_j = '%s' % j
                else:
                    db_biao_j = 'Id已经超过5位数，请重新定义'

                #对字段进行分离
                db_ziduan_content = updatedbdatatestcase.db_ziduan
                db_ziduan_list = db_ziduan_content.split(',')
                db_ziduan_list_len = len(db_ziduan_list)
                for k in range(1, db_ziduan_list_len + 1):
                    print("字段:%s" % db_ziduan_list[k-1])
                    if len(str(k)) == 1:
                        db_ziduan_k = '0000%s' % k
                    elif len(str(k)) == 2:
                        db_ziduan_k = '000%s' % k
                    elif len(str(k)) == 3:
                        db_ziduan_k = '00%s' % k
                    elif len(str(k)) == 4:
                        db_ziduan_k = '0%s' % k
                    elif len(str(k)) == 5:
                        db_ziduan_k = '%s' % k
                    else:
                        db_ziduan_k = 'Id已经超过5位数，请重新定义'


                    #对条件字段进行分离
                    db_tiaojianziduan_content = updatedbdatatestcase.db_tiaojianziduan
                    db_tiaojianziduan_list = db_tiaojianziduan_content.split(',')
                    db_tiaojianziduan_list_len = len(db_tiaojianziduan_list)
                    for h in range(1, db_tiaojianziduan_list_len + 1):
                        print("字段:%s" % db_tiaojianziduan_list[h-1])
                        if len(str(h)) == 1:
                            db_tiaojianziduan_h = '0000%s' % h
                        elif len(str(h)) == 2:
                            db_tiaojianziduan_h = '000%s' % h
                        elif len(str(h)) == 3:
                            db_tiaojianziduan_h = '00%s' % h
                        elif len(str(h)) == 4:
                            db_tiaojianziduan_h = '0%s' % h
                        elif len(str(h)) == 5:
                            db_tiaojianziduan_h = '%s' % h
                        else:
                            db_tiaojianziduan_h = 'Id已经超过5位数，请重新定义'

                        # 对条件字段的值进行分离
                        db_tiaojianzhi_content = updatedbdatatestcase.db_tiaojianzhi
                        db_tiaojianzhi_list = db_tiaojianzhi_content.split(',')
                        db_tiaojianzhi_list_len = len(db_tiaojianzhi_list)
                        for f in range(1, db_tiaojianzhi_list_len + 1):
                            print("字段:%s" % db_tiaojianzhi_list[f-1])
                            if len(str(f)) == 1:
                                db_tiaojianzhi_f = '0000%s' % f
                            elif len(str(f)) == 2:
                                db_tiaojianzhi_f = '000%s' % f
                            elif len(str(f)) == 3:
                                db_tiaojianzhi_f = '00%s' % f
                            elif len(str(f)) == 4:
                                db_tiaojianzhi_f = '0%s' % f
                            elif len(str(f)) == 5:
                                db_tiaojianzhi_f = '%s' % f
                            else:
                                db_tiaojianzhi_f = 'Id已经超过5位数，请重新定义'

                            args = []
                            args.append(updatedbdatatestcase.db_host)
                            args.append(updatedbdatatestcase.db_port)
                            args.append(updatedbdatatestcase.db_user)
                            args.append(updatedbdatatestcase.db_password)
                            args.append(updatedbdatatestcase.db_database)
                            args.append(updatedbdatatestcase.db_charset)
                            args.append(db_biao_list[j-1])
                            args.append(db_ziduan_list[k-1])
                            args.append(updatedbdatatestcase.db_xiugaiqiandezhi)
                            args.append(updatedbdatatestcase.db_xiugaihoudezhi)
                            args.append(db_tiaojianziduan_list[h-1])
                            args.append(db_tiaojianzhi_list[f-1])
                            setattr(TestDeleteDBClass,
                                    'test_func_%s_%s_%s_%s_%s_%s_%s_%s_%s_%s_%s' % (updatedbdatatestcaseid, updatedbdatatestcase.test_case_title, forcount_i,
                                                                                    db_biao_list[j-1],db_biao_j,
                                                                                    db_ziduan_list[k-1],db_ziduan_k,
                                                                                    db_tiaojianziduan_list[h-1],db_tiaojianziduan_h,
                                                                                    db_tiaojianzhi_list[f - 1],db_tiaojianzhi_f
                                                                                    ),
                                    TestDeleteDBClass.getTestFunc(*args))  # 通过setattr自动为TestCase类添加成员方法，方法以“test_func_”开头


__generateTestCases()

if __name__ == '__main__':
    print("hello world")
    unittest.main()












