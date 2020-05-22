from selenium import webdriver   #导入驱动
import  os
import time
from selenium.webdriver.support.select import Select   #导入Select

class AutoModbus(object):
    def __init__(self):
        self.chromedriver = webdriver.Chrome()

    def write_device(self):
        try:
            #登录web后台config
            self.chromedriver.get("http://192.168.101.104/")
            account_ele = self.chromedriver.find_element_by_xpath("/html/body/div/div/div/form/table/tbody/tr[2]/td[2]/input")
            account_ele.send_keys("config")
            password_ele = self.chromedriver.find_element_by_xpath("/html/body/div/div/div/form/table/tbody/tr[3]/td[2]/input")
            password_ele.send_keys("config")
            login_ele = self.chromedriver.find_element_by_xpath("/html/body/div/div/div/form/table/tbody/tr[4]/td/input[1]")
            login_ele.click()
            time.sleep(6)

            #配置串口

            #点击写入设备
            frame_ele = self.chromedriver.find_element_by_xpath("/html/frameset/frameset/frame[1]")
            self.chromedriver.switch_to.frame(frame_ele)
            chuankoucanshupeizhi_ele = self.chromedriver.find_element_by_xpath("/html/body/div/div[4]/input")
            chuankoucanshupeizhi_ele.click()
            time.sleep(3)
            self.chromedriver.switch_to.default_content()  # 退出frame

            #获取js弹窗
            alert = self.chromedriver.switch_to.alert
            # print(alert.text)
            # alert.accept()
        except Exception as e:
            print("问题：")
            print(e)


if __name__ == '__main__':
    a = AutoModbus()
    a.write_device()