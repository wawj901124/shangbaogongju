from WWTest.base.activeBrowser import ActiveBrowser
ab = ActiveBrowser()

print("【手动】1.将电脑与 MCU 的网口 1 设置在同一网口，将电脑网口用交叉网线连接 MCU 的网口 1")
print("【手动】2.设备上电")
print("【自动】3.电脑地址栏输入：http://10.0.0.111 回车 进入登陆界面")
ab.getUrl("http://10.0.0.111")
print("【自动】4.输入用户名 test、密码 test 登陆")
print("【手动】5.test 登入数采仪后，数采仪屏幕会黑屏，观察 8 分钟左右后，数采仪是否会正常重 启，重启则看门狗功能正常")
while True:
    isreboot = input("数采仪是否重启,请填写‘是’或‘否’")
    if isreboot == '是':
        print("测试通过")
        assert True
        break
    elif isreboot == '否':
        print("测试失败，数采仪应该重启,而实际没有")
        assert False
        break
    else:
        continue