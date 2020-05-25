from pywinauto.application import Application
import time

app = Application(backend='win32').connect(process = 11660)
time.sleep(1)
app[' Xshell 6 '].print_control_identifiers()
# app[' Xshell 6 '].menu_select("文件(F) -> 打开(O)")
# app[' Xshell 6 ']['菜单栏Toolbar'].print_control_identifiers()
# mylist = ['ReBar', '链接栏Toolbar', 'Toolbar', '链接栏', 'Toolbar0', 'Toolbar1', 'Toolbar2', '地址栏', '地址栏Toolbar', 'ComboBox', 'Edit', '标准按钮', 'Toolbar3', '标准按钮Toolbar', '菜单栏', 'Toolbar4', '菜单栏Toolbar', 'Afx:DockPane:cd0000:8:10003:10', 'NsMultiPaneCtrl', 'TabCtrl:cd0000:8:10003:0:0', 'Xshell6::CoreApp', 'Xshell', 'XshellXshell6::CoreApp', 'Afx:DockPane:400000:8:10003:10', 'AfxFrameOrView110u', 'Afx:00400000:0', 'CURSOR', 'CURSORAfx:00400000:0']

# a = app[' Xshell 6 ']['关闭会话Button'].texts()
# print(a)
# time.sleep(1)
# app[' Xshell 6 ']['关闭会话Button'].click()
# for i in mylist:
#     myone = app[' Xshell 6 '][i]
#     myone.draw_outline(colour ='green')
#     time.sleep(1)
#     print(i)
#
# my_scy = app[' Xshell 6 '].child_window(class_name="Afx:DockPane:cd0000:8:10003:10")
# my_scy.draw_outline(colour ='green')
