from pywinauto import Application  #导包
import time
from pywinauto.keyboard import send_keys #对键盘操作



class AutoXshell(object):

    def __init__(self):
        self.IS_RESTART = True
        self.EXE_NAME = "Xshell.exe"
        self.CHENGXU_NAME = "串口调试软件4.5"
        self.SELECT_COM_NUM = "COM3"
        # self.auto_common = AutoCommon()
        self.SELECT_CONTROL_NAME = "ComboBox1"
        self.APP = self.start_app()
        # self.APP_WINDOWS = self.get_app_windows()

    # 打开程序
    def start_app(self):
        if self.IS_RESTART:
            app = Application().start(self.EXE_NAME)  # 打开程序
        else:
            app = Application().connect(path= self.EXE_NAME)
        return app

    # 打开程序窗口
    def get_app_windows(self,windows_name):
        app_windows = self.APP[windows_name]
        return app_windows

    #打印窗口子组件
    def get_app_windows_control(self,windows_name):
        app_windows = self.get_app_windows(windows_name)
        get_app_windows_control = app_windows.print_control_identifiers()
        print(get_app_windows_control)
        return get_app_windows_control

    # # 打开程序窗口
    # def get_app_windows(self):
    #     app_windows = self.APP[self.CHENGXU_NAME]
    #     return app_windows

    def time_delay(self,delaytime):
        delaytime_int = int(delaytime)
        time.sleep(delaytime_int)
        print("等待%s" % delaytime)

    #处理COM选择
    def handle_select_com(self):
        select_com = self.APP_WINDOWS[self.SELECT_CONTROL_NAME]
        select_com_text = self.auto_common.get_Control_Text(select_com,"'",1)
        print(select_com_text)
        now_select_com_num = select_com_text.split("M")[1]  # 工具当前选择的端口
        print(now_select_com_num)
        pre_select_com_num = self.SELECT_COM_NUM.split("M")[1]  # 想要选择的端口
        print(pre_select_com_num)

        now_select_com_num_int = int(now_select_com_num)
        pre_select_com_num_int = int(pre_select_com_num)

        if now_select_com_num_int == pre_select_com_num_int:  # 如果相等则不进行操作
            select_com_text_hou =  self.auto_common.get_Control_Text(select_com,"'",1)
            print("选择的端口为：%s"%select_com_text_hou)
        elif pre_select_com_num_int > now_select_com_num_int:  # 如果预期比实际大，则点击后上一动然后按enter键
            cha = pre_select_com_num_int - now_select_com_num_int
            print(cha)
            print("即将点击")
            select_com.click()
            # select_com.texts
            print("已经点击")
            self.auto_common.cha_click(cha, "{VK_DOWN}")  # 按向下键
            # 再次获取控件文本
            select_com_text_hou =  self.auto_common.get_Control_Text(select_com,"'",1)
            print("选择的端口为：%s"%select_com_text_hou)
            assert select_com_text_hou == self.SELECT_COM_NUM
        else:
            cha = now_select_com_num_int - pre_select_com_num_int
            print(cha)
            print("即将点击")
            select_com.click()
            # select_com.texts
            print("已经点击")
            self.auto_common.cha_click(cha,"{VK_UP}")  # 按向上键
            # 再次获取控件文本
            select_com_text_hou =  self.auto_common.get_Control_Text(select_com,"'",1)
            print("选择的端口为：%s"%select_com_text_hou)
            assert select_com_text_hou == self.SELECT_COM_NUM


    def run_man(self):
        self.handle_select_com()


if __name__ == "__main__":

    # 获取控制台打印的东西
    class TextArea(object):
        def __init__(self):
            self.buffer = []

        def write(self, *args, **kwargs):
            self.buffer.append(args)
    # autos = AutoXshell()
    # huiha = autos.get_app_windows_control('Xshell 6(未激活)')
    # app = Application(backend='uia').start(r'D:\xshell\Xshell\Xshell.exe')
    # app['Xshell 6'].print_control_identifiers()
    # app = Application().start(r'D:\xshell\Xshell\Xshell.exe')
    # app['Xshell 6 (未激活)'].print_control_identifiers()
    # from pywinauto.application import Application
    # app = Application().start(r'D:\xshell\Xshell\Xshell.exe')
    #     # b= app.backend
    #     # print(b)
    import time
    import sys
    from pywinauto.application import Application
    app = Application().start('Xshell.exe')
    app_xshell = app['Xshell 6']
    print("11111111111111111111111111111111111111111111111111111111111111111111111111")
    app_xshell.print_control_identifiers()
    print("11111111111111111111111111111111111111111111111111111111111111111111111111")

    app_xshell.menu_select("选项卡(B) -> 新选项卡组(G) -> 右(R)")


    # time.sleep(5)
    # app_xshell['确定'].click()
    # for i in range(0,5):
    #     print("第%s-----------------"%i)
    #     win = 'Edit%s' % i
    #     edit_control = app_xshell[win]
    #     edit_control.draw_outline(colour ='red')
    #     edit_control.print_control_identifiers()
    #     time.sleep(5)
    # win = 'Edit'
    # edit_control = app_xshell[win]
    # edit_control.draw_outline(colour='red',rect = None)
    # # edit_control.child_window().print_control_identifiers()
    # stdout = sys.stdout
    # sys.stdout = TextArea()  # 申请的空间
    # edit_control.print_control_identifiers()
    # text_area, sys.stdout = sys.stdout, stdout  # 获取控件信息
    # print(text_area.buffer)
    # time.sleep(5)

    # win_yiji = 'Edit'
    # app_xshell_yiji = app_xshell[win_yiji].draw_outline(colour ='red')

    # edit_control = app_xshell[win_yiji]
    # app_xshell_yiji.print_control_identifiers()
    # time.sleep(5)

    # win_erji = 'Button'
    # app_xshell_erji = app_xshell_yiji[win_erji]
    # app_xshell_erji.print_control_identifiers()
    # app_xshell_erji.click()
    # print("点击")


    # dlg_spec = app.window(title=u'无标题 - 记事本')
    # a = dlg_spec.wrapper_object().minimize()  # 在调试时
    # print(a)




