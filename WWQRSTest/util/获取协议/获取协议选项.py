from selenium import webdriver   #导入驱动
import  os
import time
from selenium.webdriver.support.select import Select   #导入Select

path = r"%s/driver/chromedriver" % str(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))  # 配置驱动路径
print("path:%s" % path)

chromedriver = webdriver.Chrome(executable_path=path)  # 需要把驱动所在路径配置到系统环境变量里
chromedriver.get("http://192.168.101.104/")
account_ele = chromedriver.find_element_by_xpath("/html/body/div/div/div/form/table/tbody/tr[2]/td[2]/input")
account_ele.send_keys("config")
password_ele = chromedriver.find_element_by_xpath("/html/body/div/div/div/form/table/tbody/tr[3]/td[2]/input")
password_ele.send_keys("config")

login_ele = chromedriver.find_element_by_xpath("/html/body/div/div/div/form/table/tbody/tr[4]/td/input[1]")
login_ele.click()
time.sleep(6)

#
frame_ele = chromedriver.find_element_by_xpath("/html/frameset/frameset/frame[1]")
chromedriver.switch_to.frame(frame_ele)
chuankoucanshupeizhi_ele = chromedriver.find_element_by_xpath("/html/body/div/ul[1]/li[2]/a")
chuankoucanshupeizhi_ele.click()
time.sleep(3)

chromedriver.switch_to.default_content()  #退出frame

right_frame_ele = chromedriver.find_element_by_xpath("/html/frameset/frameset/frame[2]")
chromedriver.switch_to.frame(right_frame_ele)

chuankoucanshupeizhi_ele = chromedriver.find_element_by_xpath("/html/body/form/div/div[2]/table/tbody/tr[5]/td[8]/select")

select_ele = Select(chuankoucanshupeizhi_ele)

optionlist = []
w_list=[]
all_options = select_ele.options
from WWQRSTest.util.handleTxt import HandleTxt
file_name='select_option.txt'
ht = HandleTxt(file_name)
for option in all_options:
    optionlist.append(option.text)
    print(option.text)
    ht.add_content(option.text)


print('获取的选项所有内容：%s'% optionlist)



