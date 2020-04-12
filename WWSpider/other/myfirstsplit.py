# import requests
# import json
#
# url = "http://fpie1.com/#/play-details/78"
# rese = requests.get(url)
# retext = rese.text
# print(retext)
# html = json.loads(retext)
# print(html)
url = "https://www.busdmm.one/HUNT-001"
from requests_html import HTMLSession

session = HTMLSession()

rese = session.get(url)
retext = rese.text
# print(retext)
rl= rese.html.absolute_links
# print(rese.html.links)
# print(rese.html.absolute_links)
# for i in rl:
#     print(i)

#获取图片地址和视频标题
img = rese.html.find("a.bigImage img",first=True)  #获取类名为bigImage的a标签下的img标签 ，返回符合条件的第一项，如果first=False，则返回所有符合的集合
# img = rese.html.xpath("//div[6]/div[1]/div[1]/a/img",first=True)  #获取列表中的第一个
print(img.attrs["src"])  #获取元素属性中的src键的值
print(img.attrs["title"])#获取元素属性中的title键的值

# prenums = rese.html.find("div.col-md-3 p span")  #获取类名包含有col-md-3的div标签下的p标签的元素
#
# detail_list = []
# for i in prenums:
#     # yaosu = i.html.find("span",first=True)
#     pre_text =i.text
#     print(pre_text)
#     # yuqi = pre_text.split(" ")
#     detail_list.append(pre_text)
#
# print(detail_list)

# prenums = rese.html.xpath("//div[@class='col-md-3 info']/p/a[1]")  #使用xpath的方法获取类名为col-md-3 info的div标签下的所有P标签的内容
# for prenum in prenums:
#     print(prenum.text)
#     print(prenum.attrs)
# detail_list = []
# for i in prenums:
#     print(i)
#     # yaosu = i.html.find("span",first=True)
#     pre_text =i.text
#     # print(pre_text)
#     P_span = i.html.xpath("span")
#     for j in P_span:
#         print(j.text)
#
#     # yuqi = pre_text.split(" ")
#     detail_list.append(pre_text)
#
# print(detail_list)









# from WWTest.base.activeBrowser import ActiveBrowser
#
# ab = ActiveBrowser()
# ab.getUrl(url)
# ab.delayTime(2)
# #定位到frame
# frame_xpath = "/html/body/div/div[2]/div[1]/div[2]/p[2]/iframe"
# frame_obj = ab.findELe("xpath",frame_xpath )
# video_url = frame_obj.get_attribute("src")
# print(video_url)
#
# down_load = ab.findEleAndReturnText(0,"xpath","/html/body/div/div[2]/div[1]/div[2]/p[4]/span")
# print(down_load)
#
#
# # ab.getUrl(video_url)
# front_cover_img = ab.getScreenshotAboutMySQL()
# # print(front_cover_img)
#
# ab.driver.switch_to.frame(frame_obj)
# print("切换到frame")
#
# front_cover_img = ab.findELe("xpath","/html/body/div/div/div[7]")
# video_url = front_cover_img.get_attribute("style").split('"')[1]
# print(video_url)
# import requests
# imagewe = requests.get(video_url)
# image_content = imagewe.content
# print(image_content)
# imageend = ab.saveSpiderImage()
# with open(imageend,'wb') as f:
#     f.write(image_content)
# print("封面图：%s"% imageend)
