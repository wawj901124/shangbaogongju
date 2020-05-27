from pywinauto.application import Application
import time

app = Application().start('notepad.exe')
time.sleep(1)
app[' 无标题 - 记事本 '].print_control_identifiers()
app[' 无标题 - 记事本 '].menu_select("编辑(E) -> 替换(R)..")
time.sleep(1)
# app['替换'].取消.click()